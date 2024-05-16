from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QStackedWidget, QMessageBox, QTabWidget
from info_video import Ui_MainWindow
import sys
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

class InfoHandle(QMainWindow, Ui_MainWindow):
    def __init__(self, mainwindow=None):
        super().__init__()
        self.setupUi(mainwindow)
        self.btnLike.clicked.connect(self.like)
        self.btnDisLike.clicked.connect(self.dislike)


    def like(self):
        flow = InstalledAppFlow.from_client_secrets_file(
        r'C:\file\pythonMNM\client_secrets.json', SCOPES)
        # Sử dụng run_local_server để lấy thông tin xác thực
        credentials = flow.run_local_server(port=0)

        # Xây dựng dịch vụ API YouTube
        youtube = build('youtube', 'v3', credentials=credentials)

        # ID của video mà bạn muốn like
        video_id = self.txtId.text()

        # Thực hiện hành động like
        youtube.videos().rate(
            id=video_id,
            rating='like'
        ).execute()
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("Thông báo")
        msg_box.setText("Like video thành công.")
        msg_box.exec_()
    def dislike(self):
        flow = InstalledAppFlow.from_client_secrets_file(
        r'C:\file\pythonMNM\client_secrets.json', SCOPES)
        # Sử dụng run_local_server để lấy thông tin xác thực
        credentials = flow.run_local_server(port=0)

        # Xây dựng dịch vụ API YouTube
        youtube = build('youtube', 'v3', credentials=credentials)

        # ID của video mà bạn muốn like
        video_id = self.txtId.text()

        # Thực hiện hành động like
        youtube.videos().rate(
            id=video_id,
            rating='like'
        ).execute()
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("Thông báo")
        msg_box.setText("dislike video thành công.")
        msg_box.exec_()    