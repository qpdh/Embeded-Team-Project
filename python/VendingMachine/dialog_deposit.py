from PyQt5.QtWidgets import *
from PyQt5 import uic
import threading
import time

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

        self.startContolThread()

    def deposit(self, value):
        self.wallet += value
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
    def checkControl(self):
        while self.controlFlag:
            print('test deposit')
            time.sleep(1)
