import logging
import serial
import time


class DeviceReader:

    MPPT1Data   = {}
    MPPT2Data   = {}
    BMVData     = {}

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
        fields = {}
        try:
            ser = serial.Serial(port=serialport,
                                baudrate=baudrate,
                                parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                bytesize=serial.EIGHTBITS,
                                timeout=1)
            time.sleep(0.1)

        except (serial.SerialException, FileNotFoundError) as ex:
            logging.warning("Cannot connect to MPPT1, continuing without it!")
            return
        except Exception as ex:
            logging.error("Ran into an unhandled error!" + str(ex))
            return

        while True:
            try:
                data = ser.readline()

            except (serial.SerialException, FileNotFoundError) as ex:
                logging.warning("Cannot connect to MPPT1, continuing without it!")
                return
                if ser:
                    data = ser.readline()
                else:
                    logging.warning("Cannot connect to MPPT1, continuing without it!")
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

    def MPPTHandler_2(self, serialport, baudrate=19200, debug=False):
        fields = {}
        try:
            ser = serial.Serial(port=serialport,
                                baudrate=baudrate,
                                parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                bytesize=serial.EIGHTBITS,
                                timeout=1)
            time.sleep(0.1)

        except (serial.SerialException, FileNotFoundError) as ex:
            logging.warning("Cannot connect to MPPT2, continuing without it!")
            return

        except Exception as ex:
            logging.error("Ran into an unhandled error!" + str(ex))
            return

        while True:
            try:
                data = ser.readline()


            except (serial.SerialException, FileNotFoundError) as ex:
                logging.warning("Cannot connect to MPPT2, continuing without it!")
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