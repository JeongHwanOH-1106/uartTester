import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile, QThread, QCoreApplication
import traceback
import numpy
import struct
import time
import serial

from UartGCS_ui import Ui_MainWindow


class UartTerm(QMainWindow):
    def __init__(self):
        super(UartTerm, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.receiver = Receiver(self)
        self.ui.transmitter = Transmitter(self)
        self.ui.ser = serial.Serial('COM1', 115200, timeout=0) # 포트, 전송속도, 타임아웃 설정

        self.ui.serial_status = False

        self.ui.GCS_to_FC = bytearray(126)
        self.ui.packet_idx = int(1)
        
    def port_open(self):
        print("Open Button Clicked!")
        try:
            self.ui.ser.open()
            print("Port opening")
        except:
            print("Port already opend")

        self.ui.receiver.start()
        self.ui.transmitter.start()
        self.ui.serial_status = True
        

    def port_close(self):
        print("Close Button Clicked!")
        self.ui.serial_status = False
        self.ui.receiver.stop()
        self.ui.transmitter.stop()
        if self.ui.ser.isOpen():
            self.ui.ser.close()
            print("Port Closing")
        else:
            print("Port already closed")
             


    def serial_send(self):
        print("Send Button Clicked!")
        self.ui.label_3.setText("I have been clicked asdfjkalsdjfkiajsdk")
        self.ui.label_3.adjustSize()
        
class Transmitter(QThread):
    def __init__(self, parent=None):
        super(Transmitter, self).__init__(parent)
        self.UartTerm = parent
        self.is_running = False
        
    def run(self):
        self.is_running = True
        print("Transmitter run")
        
        while self.is_running:
            time.sleep(0.02)
            if self.UartTerm.ui.ser.isOpen():
                try:
                    ail = int(numpy.sin(self.UartTerm.ui.packet_idx * 0.01) * 500 + 1500)
                    ele = int(numpy.cos(self.UartTerm.ui.packet_idx * 0.01) * 500 + 1500)
                    rud = 1500
                    thr = 1900

                    self.UartTerm.ui.GCS_to_FC[0:1] = struct.pack('c', bytes('D', "utf-8"))
                    self.UartTerm.ui.GCS_to_FC[1:2] = struct.pack('c', bytes('n', "utf-8"))
                    self.UartTerm.ui.GCS_to_FC[2:8] = struct.pack('BBBBH', 116, self.UartTerm.ui.packet_idx, 1, 0, 2)

                    self.UartTerm.ui.GCS_to_FC[16:18] = struct.pack('h', ail)
                    self.UartTerm.ui.GCS_to_FC[18:20] = struct.pack('h', ele)
                    self.UartTerm.ui.GCS_to_FC[20:22] = struct.pack('h', rud)
                    self.UartTerm.ui.GCS_to_FC[22:24] = struct.pack('h', thr)

                    # self.UartTerm.ui.udp_socket_SV.sendto(self.UartTerm.ui.GCS_to_FC, ('127.0.0.1', int(32001)))
                    self.UartTerm.ui.ser.write(self.UartTerm.ui.GCS_to_FC)

                    if self.UartTerm.ui.packet_idx == 255:
                        self.UartTerm.ui.packet_idx = 0
                    else:
                        self.UartTerm.ui.packet_idx += 1
                    
                except BlockingIOError:
                    pass
                
                except:
                    err_msg_t = traceback.format_exc()
                    print(err_msg_t)
                    pass
    
    def stop(self):
        self.is_running = False
        self.quit()
        self.wait(1000)
            

class Receiver(QThread):
    def __init__(self, parent=None):
        super(Receiver, self).__init__(parent)
        self.UartTerm = parent

        self.is_running = False
    
    def run(self):
        self.is_running = True
        flag_recv = False
        print("Receiver run")
        packet_arr = bytearray(126)
        
        while self.is_running:
            if self.UartTerm.ui.ser.isOpen():
                try:
                    data = self.UartTerm.ui.ser.readline()
                    if data:
                        flag_recv = True
                        # print("받은 데이터 : ",data.decode("utf-8"))
                        # self.UartTerm.ui.textEdit.append("Rx >> " + str(data))

                        packet_arr = data[0:126]

                        cnt = struct.unpack('B', packet_arr[3:4])
                        phi_cmd = struct.unpack('h', packet_arr[72:74])
                        the_cmd = struct.unpack('h', packet_arr[74:76])
                        psi_cmd = struct.unpack('h', packet_arr[76:78])

                        self.UartTerm.ui.val_cnt.setText(str(cnt))
                        self.UartTerm.ui.val_Phi_cmd.setText(str(phi_cmd))
                        self.UartTerm.ui.val_The_cmd.setText(str(the_cmd))
                        self.UartTerm.ui.val_Psi_cmd.setText(str(psi_cmd))

                        # lon = struct.unpack('d', packet_arr[0:8])
                        # lat = struct.unpack('d', packet_arr[8:16])
                        # alt = struct.unpack('d', packet_arr[16:24])
                        # phi = struct.unpack('d', packet_arr[24:32])
                        # the = struct.unpack('d', packet_arr[32:40])
                        # psi = struct.unpack('d', packet_arr[40:48])

                        # self.UartTerm.ui.val_lon.setText(str(lon))
                        # self.UartTerm.ui.val_lat.setText(str(lat))
                        # self.UartTerm.ui.val_alt.setText(str(alt))
                        # self.UartTerm.ui.val_phi.setText(str(phi))
                        # self.UartTerm.ui.val_the.setText(str(the))
                        # self.UartTerm.ui.val_psi.setText(str(psi))
                        
                    
                except BlockingIOError:
                    pass
                
                except:
                    err_msg_t = traceback.format_exc()
                    print(err_msg_t)
                    pass
                
    def stop(self):
        self.is_running = False
        self.quit()
        self.wait(1000)
                
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = UartTerm()
    window.show()

    sys.exit(app.exec())