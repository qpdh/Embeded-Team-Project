import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# import resources_rc

# UI 파일 연결
# 단, UI파일은 Python코드 파일과 같은 디렉토리에 위치해야 한다.
from_class = uic.loadUiType('manager_mode.ui')[0]


# 화면을 띄우는데 사용되는 class 선언
class ManagerDialog(QDialog, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 640*420 크기 고정
        self.setFixedSize(700, 500)

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
