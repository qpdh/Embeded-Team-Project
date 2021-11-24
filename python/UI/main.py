import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from DrinkDBManagement import *

# UI 파일 연결
# 단, UI파일은 Python코드 파일과 같은 디렉토리에 위치해야 한다.
from_class = uic.loadUiType('main.ui')[0]


# 화면을 띄우는데 사용되는 class 선언
class WindowClass(QMainWindow, from_class):
    index = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 640*420 크기 고정
        self.setFixedSize(900, 500)

        # DB 연결 클래스 호출
        self.drinkManagement = DrinkDBManagement()

        self.drinks = [i for i in range(8)]
        
        # pushButton 리스트
        self.pushButtonList = [self.pushButton_drink0, self.pushButton_drink1, self.pushButton_drink2,
                               self.pushButton_drink3,
                               self.pushButton_drink4, self.pushButton_drink5, self.pushButton_drink6,
                               self.pushButton_drink7]
        
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

        # 잔돈 반환

        # 관리자 모드

        self.pushButtonList[0].click()


    def setOnClickedListener(self, i):
        drinkInfo = self.drinkManagement.print_drink(i)
        self.label_name.setText(drinkInfo["name"])
        self.label_stock.setText(str(drinkInfo["stock"]))
        self.label_cost.setText(str(drinkInfo["cost"]))
        print(i, 'Button Clicked')

    def purchaseButtonListener(self):
        print('push button clicked')


if __name__ == "__main__":
    # QApplication 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스생성
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트 루프토 진입시키는(프로그램을 작동시키는)코드
    app.exec_()
