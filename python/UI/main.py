import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from DrinkDBManagement import *
from manager_mode import ManagerDialog
from dialog_deposit import DepositDialog
# UI 파일 연결
# 단, UI파일은 Python코드 파일과 같은 디렉토리에 위치해야 한다.
from_class = uic.loadUiType('main.ui')[0]

# 화면을 띄우는데 사용되는 class 선언
class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

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

    # 제품 버튼 리스너
    def setOnClickedListener(self, i):
        drinkInfo = self.drinkManagement.print_drink(i)
        self.label_name.setText(drinkInfo["name"])
        self.label_stock.setText(str(drinkInfo["stock"]))
        self.label_cost.setText(str(drinkInfo["cost"]))
        print(i, 'Button Clicked')

    # 구매 버튼 리스너
    def purchaseButtonListener(self):
        print('push button clicked')

    # 입금 버튼 리스너
    def insertButtonListener(self):
        win = DepositDialog()
        win.showModal()
        print('insert button clicked')

    # 잔돈 반환 버튼 리스너
    def returnButtonListener(self):
        print('return button clicked')

    # 관리자 모드 버튼 리스너
    def directorButtonListener(self):
        win = ManagerDialog()
        win.showModal()
        print('director button clicked')

    def bringName_Cost(self, drinkNameList, drinkCostList):
        drinksInfo = self.drinkManagement.print_all_drink()

        # todo drinkInfo & drinkNameList & drinkCostList 길이가 같아야 함
        for i in range(len(drinksInfo)):
            name = drinksInfo[i]["name"]
            cost = drinksInfo[i]["cost"]
            drinkNameList[i].setText(name)
            drinkCostList[i].setText(str(cost))


if __name__ == "__main__":
    # QApplication 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스생성
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트 루프토 진입시키는(프로그램을 작동시키는)코드
    app.exec_()
