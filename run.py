
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QStackedWidget, QMessageBox
from download_videoHandle import DownloadHandle
from Upload_videoHandle import UploadHandle
from download_historyHandle import HistoryHandle
from Info_videoHandle import InfoHandle
import sys

class UI(QMainWindow):
    def __init__(self):
        
        # single

        self.downloadUi=QMainWindow()
        self.download_videoHandle=DownloadHandle(self.downloadUi)
        self.download_videoHandle.btnUpload_video.clicked.connect(lambda: self.loadUploadForm(0))
        self.download_videoHandle.btnDownload_video.clicked.connect(lambda: self.loadDownloadForm(0))
        self.download_videoHandle.btnDownload_history.clicked.connect(lambda: self.loadHistoryForm(0))
        # list
        self.UploadUi=QMainWindow()
        self.download_listHandle=UploadHandle(self.UploadUi)    
        self.download_listHandle.btnDownload_video.clicked.connect(lambda: self.loadDownloadForm(0))
        self.download_listHandle.btnUpload_video.clicked.connect(lambda: self.loadUploadForm(0))
        self.download_listHandle.btnDownload_history.clicked.connect(lambda: self.loadHistoryForm(0))
        #history
        self.historyUi=QMainWindow()
        self.download_historyHandle= HistoryHandle(self.historyUi) 
        self.download_historyHandle.btnDownload_video.clicked.connect(lambda: self.loadDownloadForm(0))
        self.download_historyHandle.btnUpload_video.clicked.connect(lambda: self.loadUploadForm(0))
        self.download_historyHandle.btnDownload_history.clicked.connect(lambda: self.loadHistoryForm(0))
        # info
        self.infoVideoUi = QMainWindow()
        self.Info_videoHandle= InfoHandle(self.infoVideoUi)
        self.downloadUi.show()
    def loadDownloadForm(self, data):
        self.UploadUi.hide()
        self.historyUi.hide()
        self.infoVideoUi.hide()
        self.downloadUi.show()
        
        
    def loadHistoryForm(self, data):
        self.UploadUi.hide()
        self.downloadUi.hide()
        self.historyUi.show()

        
    
    def loadUploadForm(self, data):
        self.downloadUi.hide()
        self.historyUi.hide()
        self.UploadUi.show()   
if __name__ == "__main__":
    app = QApplication([])
    ui = UI()
    app.exec_()