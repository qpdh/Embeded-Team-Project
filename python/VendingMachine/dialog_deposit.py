from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QCoreApplication
import threading
import time
from IO_Modules.all import *

# import resources_rc

# VendingMachine 파일 연결
# 단, UI파일은 Python코드 파일과 같은 디렉토리에 위치해야 한다.
from_class = uic.loadUiType('./ui/dialog_deposit.ui')[0]


# 화면을 띄우는데 사용되는 class 선언
class DepositDialog(QDialog, from_class):
    def __init__(self, wallet):
        super().__init__()
        self.setupUi(self)


        # 쓰레드 선언
        self.controlThread = None
        # control Flag 선언
        
        self.controlFlag = False

        self.wallet = wallet

        self.initUI()

    def initUI(self):
        # 140*240 크기 고정
        self.setFixedSize(140, 240)

        self.pushButton_50.clicked.connect(lambda: self.deposit(50))
        self.pushButton_100.clicked.connect(lambda: self.deposit(100))
        self.pushButton_500.clicked.connect(lambda: self.deposit(500))

        
        self.pushButton_quit.clicked.connect(self.myclose)
        
        self.startContolThread()

    def deposit(self, value):
        self.wallet += value
        if self.wallet >= 10000:
            self.wallet -= value
        else:
            write_fnd(self.wallet)
        # TODO FND에 값 변경할 것

    def showModal(self):
        return super().exec_()

    def closeEvent(self, QCloseEvent):
        self.stopControlThread()
        QCloseEvent.accept()

    def stopControlThread(self):
        self.controlFlag = False
        self.controlThread.join()
        time.sleep(1)

    def startContolThread(self):
        self.controlFlag = True
        self.controlThread = threading.Thread(target=self.checkControl)
        self.controlThread.start()

    # 쓰레드 동작
    # 쓰레드 동작
    def checkControl(self):
        #   1  2
        #   4 
        #   7
        while self.controlFlag:
            data = read_push_switch()
            for i in range(len(data)):
                if data[i] == 1:
                    if i == 1:
                        self.pushButton_50.click()
                        break
                    elif i == 4:
                        self.pushButton_100.click()
                        break
                    elif i == 7:
                        self.pushButton_500.click()
                        break
                    elif i == 2:
                        self.pushButton_quit.click()
                        break
                        
            time.sleep(0.3)
            
    def myclose(self):
        self.stopControlThread()
        self.close()
