import logging
import serial
import time

import influxdb

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def handshake(ser):
    try:
        ser.write('ready?'.encode())
        logging.info("Initiating handshake with Arduino")
        time.sleep(0.1)
        data = ser.readline()
    except Exception as ex:
        logging.error("Ran into an unhandled error!" + str(ex))

    if data == b'ready!\r\n':
        logging.info("handshake succesfull")
        return True
    else:
        logging.info("Handshake failed!")
        return False


class DeviceReader:

    ArduinoData = {}
    MPPT1Data   = {}
    MPPT2Data   = {}
    BMVData     = {}


    def __init__(self, serverip, database, username, password):
        self.Serverip = serverip
        self.Database = database
        self.Username = username
        self.Password = password

    # noinspection PyUnusedLocal,PyUnusedLocal
    def DeviceReconnect(self, name, serialport, baudrate, starttime = 0.0):
        starttime = time.time()
        try:
            ser = serial.Serial(port=serialport,
                                baudrate=baudrate,
                                parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                bytesize=serial.EIGHTBITS,
                                timeout=1)
            time.sleep(0.01)

        # Recursive function
        except serial.SerialException as ex:
            time.sleep(5)
            logging.info("Attempting {} reconnect...".format(name))
            if time.time() - starttime < 600:
                self.DeviceReconnect(name, serialport, baudrate, starttime)
            else:
                logging.info("Reconnect timout, shutting down thread")
                return
        except Exception as ex:
            logging.error(str(ex))
        if ser:
            print("Succesfully reconnected with {}".format(name))
            return ser

    # noinspection PyUnusedLocal,PyUnusedLocal,PyUnusedLocal,PyUnusedLocal
    def ArduinoHandler(self, serialport, messages, baudrate=115200, DTR=True):

        succes = False
        try:

            ser = serial.Serial(port=serialport,
                                baudrate=baudrate,
                                parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                bytesize=serial.EIGHTBITS,
                                timeout=1)
            time.sleep(0.01)

        except (serial.SerialException, FileNotFoundError) as ex:
            logging.warning("Cannot connect to Arduino, continuing without it!")
            return
            # Reconnection protocol
            # ser = self.DeviceReconnect("Arduino", serialport, baudrate)
        except Exception as ex:
            logging.error("Ran into an unhandled error!" + str(ex))
            return
        time.sleep(.5)

        # if succes = true, the handshake is succesfull
        while succes != True:
            logging.info("Attempting Handshake...")
            succes = handshake(ser)
            time.sleep(.5)

        try:
            client = influxdb.InfluxDBClient(host=self.Serverip, port=8086, username=self.Username,
                                             password=self.Password, database=self.Database)
        except Exception as ex:
            logging.error("Ran into an unhandled error!" + str(ex))
            return

        # list where al the data ends up, gets reset every data loop
        datapoints = []
        fields = {}

        # Main loop
        while True:

            try:
                data = ser.readline()
                data = data.decode('utf-8')
                data = data.rstrip()
                # strip the /r/n ^^

            except serial.SerialException as ex:
                logging.warning("Cannot connect to Arduino, continuing without it!")
                # Reconnection protocol
                # ser = self.DeviceReconnect("Arduino", serialport, baudrate)
                if ser:
                    data = ser.readline()
                else:
                    return
            except Exception as ex:
                logging.error("Ran into an unhandled error!" + str(ex))

            if len(data) > 0:

                if data == 'start' and fields != {}:
                    self.ArduinoData = fields
                    # reset stuff
                    data = None

                elif data is not None:
                    Databuffer = str(data).split(" ", 1)

                    try:
                        key = str(Databuffer[0])
                        Val = float(Databuffer[1])

                        fields[key] = Val
                    # the checksum gives a indexerror so we pass it
                    except IndexError:
                        pass
                    except ValueError:
                        pass
                    except Exception as ex:
                        logging.error(str(Databuffer) + " " + str(ex))

    # noinspection PyUnusedLocal,PyUnusedLocal,PyUnusedLocal
    def BMVHandler(self, serialport, baudrate=19200):
        fields = {}
        try:
            ser = serial.Serial(port=serialport,
                                baudrate=baudrate,
                                parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                bytesize=serial.EIGHTBITS,
                                timeout=1)
            time.sleep(0.01)

        except (serial.SerialException, FileNotFoundError) as ex:
            logging.warning("Cannot connect to BMV, continuing without it!")
            return
            
        except Exception as ex:
            logging.error("Ran into an unhandled error!" + str(ex))
            return

        while True:
            try:
                data = ser.readline()

            except (serial.SerialException, FileNotFoundError) as ex:
                logging.warning("Cannot connect to BMV, continuing without it!")
                # Reconnection protocol
                # ser = self.DeviceReconnect("BMV", serialport, baudrate)
                if ser:
                    data = ser.readline()
                else:
                    return
            except Exception as ex:
                logging.error("Ran into an unhandled error!" + str(ex))
            try:
                data = data.decode('utf-8')
                data = data.rstrip()
                # strip the /r/n ^^

            except UnicodeDecodeError as ex:
                # passes the checksum, i don't use that shit.
                pass

            if data == "PID	0x203":  # start of dataloop
                if fields != {}:
                    self.BMVData = fields
                    # reset stuff
                    data = None
                    fields = {}

            elif data is not "":
                # split on a tab
                Databuffer = str(data).split("\t", 1)
                try:
                    key = str(Databuffer[0])
                    Val = float(Databuffer[1])

                    fields[key] = Val
                # the checksum gives a indexerror so we pass it
                except IndexError:
                    pass
                except ValueError:
                    pass
                except Exception as ex:
                    logging.error(str(Databuffer) + " " + str(ex))


    # noinspection PyUnusedLocal,PyUnusedLocal,PyUnusedLocal
    def MPPTHandler_1(self, serialport, baudrate=19200, debug=False):
        try:
            client = influxdb.InfluxDBClient(host=self.Serverip, port=8086, username=self.Username,
                                             password=self.Password, database=self.Database)
        except Exception as ex:
            logging.error(str(ex))
            return

        fields = {}

        try:

            ser = serial.Serial(port=serialport,
                                baudrate=baudrate,
                                parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                bytesize=serial.EIGHTBITS,
                                timeout=1)
            time.sleep(0.01)


        except (serial.SerialException, FileNotFoundError) as ex:
            logging.warning("Cannot connect to MPPT1, continuing without it!")
            return
            # Reconnection protocol
            # ser = self.DeviceReconnect("MPPT1", serialport, baudrate)
        except Exception as ex:
            logging.error("Ran into an unhandled error!" + str(ex))
            return

        time.sleep(.5)

        while True:
            try:
                data = ser.readline()

            except (serial.SerialException, FileNotFoundError) as ex:
                logging.warning("Cannot connect to MPPT1, continuing without it!")
                # Reconnection protocol
                # ser = self.DeviceReconnect("MPPT1", serialport, baudrate)
                if ser:
                    data = ser.readline()
                else:
                    return
            except Exception as ex:
                logging.error("Ran into an unhandled error!" + str(ex))
                return

            try:
                data = data.decode('utf-8')
                data = data.rstrip()
                # strip the /r/n ^^

            except UnicodeDecodeError as ex:
                # passes the checksum, i don't use that shit.
                pass

            if data == "PID	0xA042":  # start of dataloop
                if fields != {}:
                    self.MPPT1Data = fields
                    # reset stuff
                    data = None
                    fields = {}

            elif data is not "":
                # split on a tab
                Databuffer = str(data).split("\t", 1)
                try:
                    key = str(Databuffer[0])
                    Val = float(Databuffer[1])

                    fields[key] = Val
                # the checksum gives a indexerror so we pass it
                except IndexError:
                    pass
                except ValueError:
                    pass
                except Exception as ex:
                    logging.error(str(Databuffer) + " " + str(ex))

    # noinspection PyUnusedLocal,PyUnusedLocal,PyUnusedLocal
    def MPPTHandler_2(self, serialport, baudrate=19200, debug=False):
        try:
            client = influxdb.InfluxDBClient(host=self.Serverip, port=8086, username=self.Username,
                                             password=self.Password, database=self.Database)
        except Exception as ex:
            logging.error(ex.args)
            return

        datapoints = []
        fields = {}
        try:

            ser = serial.Serial(port=serialport,
                                baudrate=baudrate,
                                parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                bytesize=serial.EIGHTBITS,
                                timeout=1)
            time.sleep(0.01)

        except (serial.SerialException, FileNotFoundError) as ex:
            logging.warning("Cannot connect to MPPT2, continuing without it!")
            return
            # Reconnection protocol
            # ser = self.DeviceReconnect("MPPT2", serialport, baudrate)

        except Exception as ex:
            logging.error("Ran into an unhandled error!" + str(ex))
            return

        time.sleep(.5)

        while True:
            try:
                data = ser.readline()


            except (serial.SerialException, FileNotFoundError) as ex:
                logging.warning("Cannot connect to MPPT2, continuing without it!")
                # Reconnection protocol
                # ser = self.DeviceReconnect("MPPT2", serialport, baudrate)
                if ser:
                    data = ser.readline()
                else:
                    return
            except Exception as ex:
                logging.error("Ran into an unhandled error!" + str(ex))
                return

            try:
                data = data.decode('utf-8')
                data = data.rstrip()
                # strip the /r/n ^^

            except UnicodeDecodeError as ex:
                # passes the checksum, i don't use that shit.
                pass

            if debug:
                print(data)

            if data == "PID	0xA042":  # start of dataloop
                if fields != {}:
                    self.MPPT2Data = fields
                    # reset stuff
                    data = None
                    fields = {}

            elif data is not "":
                # split on a tab
                Databuffer = str(data).split("\t", 1)
                try:
                    key = str(Databuffer[0])
                    Val = float(Databuffer[1])

                    fields[key] = Val
                # the checksum gives a indexerror so we pass it
                except IndexError:
                    pass
                except ValueError:
                    pass
                except Exception as ex:
                    logging.error(str(Databuffer) + " " + str(ex))
