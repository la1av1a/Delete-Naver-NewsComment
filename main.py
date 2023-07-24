from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QAction, QIcon

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.createUI()
        self.createActions()

    def createUI(self):
        self.setWindowTitle('뉴스 댓글 자동 삭제기')
        self.resize(800, 500)
        self.setMinimumSize(500, 450)
        self.setWindowIcon(QIcon('eraser.png'))
        self._centralWidget = QWidget()
        self._verticalLayout = QVBoxLayout()
        self._centralWidget.setLayout(self._verticalLayout)
        self.setCentralWidget(self._centralWidget)
        self.addText()
        self.addInputText()
        self.createButton()
        self._verticalLayout.addStretch(1)

    def addText(self):
        messageLabel = QLabel(
            '안녕하세요. 👋\n계속하려면 ID와 비밀번호를 입력하세요.'
        )
        messageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        messageLabel.setFixedWidth(350)
        messageLabel.setMinimumHeight(100)
        messageLabel.setWordWrap(True)
        self._verticalLayout.addWidget(messageLabel, alignment=Qt.AlignmentFlag.AlignCenter)

    def addInputText(self):
        groupBox = QGroupBox()
        groupBox.setFixedWidth(350)

        self.naverButton = QRadioButton('Naver', self)
        self.naverButton.setChecked(True)

        formLayout = QFormLayout()
        self.idLabel = QLabel('아이디')
        self.idField = QLineEdit()
        self.idField.setTextMargins(3, 0, 3, 0)
        self.idField.setMinimumWidth(200)
        self.idField.setMaximumWidth(300)
        self.idField.setClearButtonEnabled(True)

        passwordLabel = QLabel('비밀번호')
        self.passwordField = QLineEdit()
        self.passwordField.setTextMargins(3, 0, 3, 0)
        self.passwordField.setMinimumWidth(200)
        self.passwordField.setMaximumWidth(300)
        self.passwordField.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordField.setClearButtonEnabled(True)

        formLayout.addRow(self.naverButton)
        formLayout.addRow(self.idLabel, self.idField)
        formLayout.addRow(passwordLabel, self.passwordField)

        groupBox.setLayout(formLayout)
        self._verticalLayout.addWidget(groupBox, alignment=Qt.AlignmentFlag.AlignCenter)
        self.idField.returnPressed.connect(self.btnRun_clicked)
        self.passwordField.returnPressed.connect(self.btnRun_clicked)

    def createButton(self):
        self.submitButton = QPushButton("시작", self)
        self.submitButton.move(425, 270)
        self.submitButton.resize(150, 50)
        self.submitButton.clicked.connect(self.btnRun_clicked)

    def btnRun_clicked(self):
        id = self.idField.text()
        pwField = self.passwordField
        pw = pwField.text()
        pwField.setText("")

        if len(id) == 0 or len(pw) == 0:
            QMessageBox.about(self, "Message", "ID 또는 Password는 공백이지 않아야 합니다.")
            return

        import naver
        naver.main(id, pw)
        QMessageBox.about(self, "Message", "완료!")

    def createActions(self):
        self.sendEmailAction = QAction('Email Us', self)
        self.visitWebsiteAction = QAction('Visit Our Website', self)
        self.fileBugReportAction = QAction('File a Bug Report', self)

style = '''
QPushButton,QGroupBox{
background-color: white;
border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: rgb(58, 134, 255);
padding: 4px;
}
MainWindow,QMessageBox{
background-color: white;
border-style: outset;
border-width: 2px;
border-color: rgb(58, 134, 255);
}
QMenuBar{
background-color: white;
}
'''
if __name__ == '__main__':
    application = QApplication([])
    application.setStyleSheet(style)
    mainWindow = MainWindow()
    mainWindow.show()
    application.exec()
