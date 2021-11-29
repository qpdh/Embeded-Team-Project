import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from python.VendingMachine.Module.DrinkDBManagement import *
from manager_mode import ManagerDialog
from dialog_deposit import DepositDialog

import time

import threading

# from IO_Modules.led_write import *
# from IO_Modules.text_lcd_write import *
# from IO_Modules.dip_switch_read import *
# from IO_Modules.dot_write import *

# VendingMachine 파일 연결
# 단, UI파일은 Python코드 파일과 같은 디렉토리에 위치해야 한다.
from_class = uic.loadUiType('./ui/main.ui')[0]


# 화면을 띄우는데 사용되는 class 선언
class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 쓰레드 선언
        self.controlThread = None
        # control Flag 선언
        self.controlFlag = False

        # DB 연결 클래스 호출
        self.drinkManagement = DrinkDBManagement()

        # pushButton 리스트
        self.pushButtonList = [self.pushButton_drink0, self.pushButton_drink1, self.pushButton_drink2,
                               self.pushButton_drink3,
                               self.pushButton_drink4, self.pushButton_drink5, self.pushButton_drink6,
                               self.pushButton_drink7]
        # 음료수 명 리스트
        self.drinkNameList = [self.label_name0, self.label_name1, self.label_name2, self.label_name3,
                              self.label_name4, self.label_name5, self.label_name6, self.label_name7]

        # 음료수 가격 리스트
        self.drinkCostList = [self.label_cost0, self.label_cost1, self.label_cost2, self.label_cost3,
                              self.label_cost4, self.label_cost5, self.label_cost6, self.label_cost7]

        # 선택 음료수 LED 값 리스트
        self.drinkLEDValueList = [128, 64, 32, 16, 8, 4, 2, 1]

        self.initUI()

    def initUI(self):
        # 900*500 크기 고정
        self.setFixedSize(900, 500)

        self.bringName_Cost(self.drinkNameList, self.drinkCostList)
        # 버튼에 기능을 연결하는 코드
        self.pushButtonList[0].clicked.connect(lambda: self.setOnClickedListener(1))
        self.pushButtonList[1].clicked.connect(lambda: self.setOnClickedListener(2))
        self.pushButtonList[2].clicked.connect(lambda: self.setOnClickedListener(3))
        self.pushButtonList[3].clicked.connect(lambda: self.setOnClickedListener(4))
        self.pushButtonList[4].clicked.connect(lambda: self.setOnClickedListener(5))
        self.pushButtonList[5].clicked.connect(lambda: self.setOnClickedListener(6))
        self.pushButtonList[6].clicked.connect(lambda: self.setOnClickedListener(7))
        self.pushButtonList[7].clicked.connect(lambda: self.setOnClickedListener(8))

        # 구입
        self.pushButton_purchase.clicked.connect(self.purchaseButtonListener)
        # 입금
        self.pushButton_insert.clicked.connect(self.insertButtonListener)
        # 잔돈 반환
        self.pushButton_return.clicked.connect(self.returnButtonListener)
        # 관리자 모드
        self.pushButton_director.clicked.connect(self.directorButtonListener)

        self.pushButtonList[0].click()
        self.pushButtonList[0].setFocus()

        # 쓰레드 시작
        self.startContolThread()

    # 쓰레드 동작
    def checkControl(self):
        while self.controlFlag:
            print('test')
            time.sleep(1)

    # 제품 버튼 리스너
    def setOnClickedListener(self, i):
        drinkInfo = self.drinkManagement.print_drink(i)
        self.label_name.setText(drinkInfo["name"])
        self.label_stock.setText(str(drinkInfo["stock"]))
        self.label_cost.setText(str(drinkInfo["cost"]))
        print(i, 'Button Clicked')
        # write_led(self.drinkLEDValueList[i-1])
        # write_text_lcd(drinkInfo["name"],"stock "+str(drinkInfo["stock"])+" cost "+str(drinkInfo["cost"]))
        # write_dot(drinkInfo["stock"])

    # 구매 버튼 리스너
    def purchaseButtonListener(self):
        print('push button clicked')
        for i in range(len(self.pushButtonList)):
            if self.pushButtonList[i].isChecked():
                drinkInfo = self.drinkManagement.print_drink(i + 1)
                self.mqtt('sensor/name', str(drinkInfo["name"]) + '_sold')
                self.mqtt('sensor/stock', str(drinkInfo["stock"]) + '_remain')

                wallet = int(self.label_wallet.text())
                stock = int(self.label_stock.text())
                money = int(self.label_cost.text())
                # 살 수 없는 경우
                # 1. 잔고가 부족할 때
                if wallet < money:
                    self.textEdit_system.append('돈이 부족합니다.\n')
                    return
                # 2. 재고가 없을 때
                if stock == 0:
                    self.textEdit_system.append('해당 품목의 재고가 없습니다.\n')
                    return
                # 살 수 있는 경우

                wallet -= money
                stock -= 1
                self.changedWallet(wallet)
                self.drinkManagement.purchase_drink(i + 1)
                self.label_stock.setText(str(stock))
                self.textEdit_system.append('맛있게 드십시오.\n')

                break

    # 입금 버튼 리스너
    def insertButtonListener(self):
        self.stopControlThread()
        win = DepositDialog(int(self.label_wallet.text()))
        win.showModal()

        self.startContolThread()
        self.label_wallet.setText(str(win.wallet))

        self.pushButtonList[0].click()
        self.pushButtonList[0].setFocus()
        print('insert button clicked')

    # 잔고 값이 바뀌면 호출하는 함수
    # TODO FND에 반영할 것
    def changedWallet(self, money):
        self.label_wallet.setText(str(money))
        pass

    # 잔돈 반환 버튼 리스너
    def returnButtonListener(self):
        myMoney = int(self.label_wallet.text())
        if myMoney == 0:
            self.textEdit_system.append('반환할 돈이 존재하지 않습니다.\n')
        else:
            self.changedWallet(0)
            self.textEdit_system.append('잔돈이 반환되었습니다.\n')

        print('return button clicked')

    def stopControlThread(self):
        self.controlFlag = False
        self.controlThread.join()
        time.sleep(1)

    def startContolThread(self):
        self.controlFlag = True
        self.controlThread = threading.Thread(target=self.checkControl)
        self.controlThread.daemon = True
        self.controlThread.start()

    # 관리자 모드 버튼 리스너
    def directorButtonListener(self):
        # password = read_dip_switch()
        password = 170
        if password == 170:
            self.stopControlThread()
            win = ManagerDialog()
            win.showModal()
            self.pushButtonList[0].click()
            self.pushButtonList[0].setFocus()
            self.startContolThread()
            print('director button clicked')

        else:
            self.textEdit_system.append('비밀번호가 일치하지 않습니다.\n')
            print('password error')

    def bringName_Cost(self, drinkNameList, drinkCostList):
        drinksInfo = self.drinkManagement.print_all_drink()

        # todo drinkInfo & drinkNameList & drinkCostList 길이가 같아야 함
        for i in range(len(drinksInfo)):
            name = drinksInfo[i]["name"]
            cost = drinksInfo[i]["cost"]
            drinkNameList[i].setText(name)
            drinkCostList[i].setText(str(cost))

    def mqtt(self, topic, data):
        command = 'mosquitto_pub -d -t ' + topic + ' -m ' + data
        print(command)
    # os.system(command)


if __name__ == "__main__":
    # QApplication 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스생성
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트 루프토 진입시키는(프로그램을 작동시키는)코드
    app.exec_()
