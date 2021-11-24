import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from DrinkDBManagement import DrinkDBManagement
# import resources_rc

# UI 파일 연결
# 단, UI파일은 Python코드 파일과 같은 디렉토리에 위치해야 한다.
from_class = uic.loadUiType('manager_mode.ui')[0]


# 화면을 띄우는데 사용되는 class 선언
class ManagerDialog(QDialog, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

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

    def initUI(self):
        # 640*420 크기 고정
        self.setFixedSize(700, 500)
        self.bringName_Cost()


    def bringName_Cost(self, drinkNameList, drinkCostList):
        drinksInfo = self.drinkManagement.print_all_drink()

        # todo drinkInfo & drinkNameList & drinkCostList 길이가 같아야 함
        for i in range(len(drinksInfo)):
            name = drinksInfo[i]["name"]
            cost = drinksInfo[i]["cost"]
            drinkNameList[i].setText(name)
            drinkCostList[i].setText(str(cost))

    def showModal(self):
        return super().exec_()

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
