
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QStackedWidget, QMessageBox
from download_videoHandle import DownloadHandle
from Upload_videoHandle import UploadHandle

import sys

class UI(QMainWindow):
    def __init__(self):
        
        # single

        self.downloadUi=QMainWindow()
        self.download_videoHandle=DownloadHandle(self.downloadUi)
        self.download_videoHandle.btnUpload_video.clicked.connect(lambda: self.loadUploadForm(0))
        self.download_videoHandle.btnDownload_video.clicked.connect(lambda: self.loadDownloadForm(0))
      
        # list
        self.UploadUi=QMainWindow()
        self.download_listHandle=UploadHandle(self.UploadUi)    
        self.download_listHandle.btnDownload_video.clicked.connect(lambda: self.loadDownloadForm(0))
        self.download_listHandle.btnUpload_video.clicked.connect(lambda: self.loadUploadForm(0))
        self.downloadUi.show()
    def loadDownloadForm(self, data):
        self.UploadUi.hide()
       
        self.downloadUi.show()
 
    def loadUploadForm(self, data):
        self.downloadUi.hide()
     
        self.UploadUi.show()   
        
if __name__ == "__main__":
    app = QApplication([])
    ui = UI()
    app.exec_()