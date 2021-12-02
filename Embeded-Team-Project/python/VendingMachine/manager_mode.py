import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from Module.DrinkDBManagement import DrinkDBManagement
from IO_Modules.all import *
import threading
import time

import pyautogui
# import resources_rc

# VendingMachine 파일 연결
# 단, UI파일은 Python코드 파일과 같은 디렉토리에 위치해야 한다.
from_class = uic.loadUiType('./ui/manager_mode.ui')[0]


# 화면을 띄우는데 사용되는 class 선언
class ManagerDialog(QDialog, from_class):

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

        # 잔고 리스트

        self.initUI()

    def initUI(self):
        # 640*480 크기 고정
        self.setFixedSize(640, 480)
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

        

        self.pushButton_fill.clicked.connect(self.fillDrink)
        
        self.pushButton_quit.clicked.connect(self.myclose)

        self.pushButtonList[0].click()
        
        self.startContolThread()

        start_step_motor()
        
    # 제품 버튼 리스너
    def setOnClickedListener(self, i):
        drinkInfo = self.drinkManagement.print_drink(i)

        write_led(self.drinkLEDValueList[i-1])
        write_text_lcd(drinkInfo["name"],"stock "+str(drinkInfo["stock"])+" cost "+str(drinkInfo["cost"]))
        write_dot(int(drinkInfo["stock"]))

    def fillDrink(self):
        for i in range(len(self.pushButtonList)):
            if self.pushButtonList[i].isChecked():
                print(i, 'checked')
                drinkInfo = self.drinkManagement.fill_drink(i + 1)
                print(i, 'checked end')
                
                self.setOnClickedListener(i+1)
                self.mqtt('sensor/name', str(drinkInfo["name"]))
                self.mqtt('sensor/stock', '9_남음')
                self.mqtt('sensor/system', '재고가_추가되었습니다')
                

    def bringName_Cost(self, drinkNameList, drinkCostList):
        drinksInfo = self.drinkManagement.print_all_drink()

        # todo drinkInfo & drinkNameList & drinkCostList 길이가 같아야 함
        for i in range(len(drinksInfo)):
            name = drinksInfo[i]["name"]
            cost = drinksInfo[i]["cost"]
            drinkNameList[i].setText(name)
            drinkCostList[i].setText(str(cost))

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
        #   1
        # 3   5
        #   7
        while self.controlFlag:
            data = read_push_switch()
            for i in range(len(data)):
                if data[i] == 1:
                    if i == 1:
                        pyautogui.hotkey('up')
                        break
                    elif i == 3:
                        pyautogui.hotkey('left')
                        break
                    elif i == 5:
                        pyautogui.hotkey('right')
                        break
                    elif i == 7:
                        pyautogui.hotkey('down')
                        break
                    elif i == 4:                       
                        self.pushButton_fill.click()
                        break
                    elif i == 2:
                        self.pushButton_quit.click()
                        break
            time.sleep(0.3)
            
            
    def showModal(self):
        return super().exec_()
    
    def myclose(self):
        stop_step_motor()
        self.stopControlThread()
        self.close()
        
    def mqtt(self, topic, data):
        command = 'mosquitto_pub -d -t ' + topic + ' -m ' + data
        os.system(command)
#
# if __name__ == "__main__":
#     # QApplication 프로그램을 실행시켜주는 클래스
#     app = QApplication(sys.argv)
#
#     # WindowClass의 인스턴스생성
#     myWindow = ManagerDialog()
#
#     # 프로그램 화면을 보여주는 코드
#     myWindow.show()
#
#     # 프로그램을 이벤트 루프토 진입시키는(프로그램을 작동시키는)코드
#     app.exec()
