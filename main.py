from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QAction, QIcon


# import daum

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.createUI()
        self.createActions()
        #self.creatMenu()

    def createUI(self):
        # Create window
        self.setWindowTitle('Delete-News-Comment')
        self.resize(800, 500)
        self.setMinimumSize(500, 450)
        # Set Window Icon
        self.setWindowIcon(QIcon('eraser.png'))
        # Create central widget and layout
        self._centralWidget = QWidget()
        self._verticalLayout = QVBoxLayout()
        self._centralWidget.setLayout(self._verticalLayout)
        # Set central widget
        self.setCentralWidget(self._centralWidget)
        # Vertically center widgets
        # self._verticalLayout.addStretch(1)
        # Add lock image
        # self.addLockImage()
        self.addText()
        self.addInputText()
        self.createButton()
        # Vertically center widgets
        self._verticalLayout.addStretch(1)
        # Add Copyright
        #self.addCopyRight()

    def addLockImage(self):
        imageLabel = QLabel()
        pixmap = QPixmap('lock.png')
        imageLabel.setPixmap(pixmap)
        self._verticalLayout.addWidget(imageLabel, alignment=Qt.AlignmentFlag.AlignCenter)

    def addText(self):
        messageLabel = QLabel(
            'Hi there 👋\nEnter your ID and Password to continue.'
        )
        messageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        messageLabel.setFixedWidth(350)
        messageLabel.setMinimumHeight(100)
        messageLabel.setWordWrap(True)
        self._verticalLayout.addWidget(messageLabel, alignment=Qt.AlignmentFlag.AlignCenter)

    def addCopyRight(self):
        copyRight = QLabel(
            'Copyright © <a href="https://github.com/la1av1a">la1av1a</a> 2022')
        copyRight.setOpenExternalLinks(True)
        self._verticalLayout.addWidget(copyRight, alignment=Qt.AlignmentFlag.AlignCenter)

    def addInputText(self):
        groupBox = QGroupBox()
        groupBox.setFixedWidth(350)

        self.naverButton = QRadioButton('Naver', self)
        self.naverButton.setChecked(True)
        self.daumButton = QRadioButton('Daum(Kakao)', self)
        self.daumButton.setChecked(False)

        formLayout = QFormLayout()
        self.idLabel = QLabel('ID')
        self.idField = QLineEdit()
        self.idField.setTextMargins(3, 0, 3, 0)
        self.idField.setMinimumWidth(200)
        self.idField.setMaximumWidth(300)
        self.idField.setClearButtonEnabled(True)

        passwordLabel = QLabel('Password')
        self.passwordField = QLineEdit()
        self.passwordField.setTextMargins(3, 0, 3, 0)
        self.passwordField.setMinimumWidth(200)
        self.passwordField.setMaximumWidth(300)
        self.passwordField.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordField.setClearButtonEnabled(True)

        formLayout.addRow(self.naverButton, self.daumButton)
        formLayout.addRow(self.idLabel, self.idField)
        formLayout.addRow(passwordLabel, self.passwordField)
        # formLayout.addRow(submitLabel, submitField)

        groupBox.setLayout(formLayout)
        self._verticalLayout.addWidget(groupBox, alignment=Qt.AlignmentFlag.AlignCenter)
        self.idField.returnPressed.connect(self.btnRun_clicked)
        self.passwordField.returnPressed.connect(self.btnRun_clicked)
        self.naverButton.clicked.connect(self.radioBtn_clicked)
        self.daumButton.clicked.connect(self.radioBtn_clicked)

    def createButton(self):
        self.submitButton = QPushButton("Run", self)
        self.submitButton.move(425, 270)
        self.submitButton.resize(150, 50)
        self.submitButton.clicked.connect(self.btnRun_clicked)

    def radioBtn_clicked(self):
        if self.naverButton.isChecked():
            self.idLabel.setText("ID")
            return

        self.idLabel.setText("ID(Email)")
        return

    def btnRun_clicked(self):
        id = self.idField.text()
        pwField = self.passwordField
        pw = pwField.text()
        pwField.setText("")

        if len(id) == 0 or len(pw) == 0:
            QMessageBox.about(self, "Message", "ID 또는 Password는 공백이지 않아야 합니다.")
            return

        if self.naverButton.isChecked():
            import naver
            naver.main(id, pw)
            QMessageBox.about(self, "Message", "완료!")

        else:
            import daum
            daum.main(id, pw)
            QMessageBox.about(self,"Message","완료!")

    def creatMenu(self):
        # Create menu bar
        menuBar = self.menuBar()
        # Add menu items
        menuBar.setNativeMenuBar(False)
        # fileMenu = menuBar.addMenu('File')
        # editMenu = menuBar.addMenu('Edit')
        # accountMenu = menuBar.addMenu('Account')
        helpMenu = menuBar.addMenu('About')
        # Add sub-items under Help menu item
        #helpMenu.addAction(self.sendEmailAction)
        #helpMenu.addAction(self.visitWebsiteAction)
        #helpMenu.addAction(self.fileBugReportAction)
        # Add horizontal line
        helpMenu.addSeparator()
        # Add 'Follow Us' sub-item under Help menu item
        # Use addMenu method because it contains sub-items
        # followUs = helpMenu.addMenu('Follow Us')
        # followUs.addAction(self.twitterAction)
        # followUs.addAction(self.facebookAction)
        # followUs.addAction(self.githubAction)

    def createActions(self):
        # Help menu actions
        self.sendEmailAction = QAction('Email Us', self)
        self.visitWebsiteAction = QAction('Visit Our Website', self)
        self.fileBugReportAction = QAction('File a Bug Report', self)
        # Social media actions
        # self.twitterAction = QAction('Twitter', self)
        # self.facebookAction = QAction('Facebook', self)
        # self.githubAction = QAction('GitHub', self)

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

# https://mr-doosun.tistory.com/31
# https://life-of-panda.tistory.com/72
