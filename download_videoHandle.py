from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel,QVBoxLayout,QPushButton,QDialog,QFileDialog,QMessageBox
from download_video import Ui_MainWindow
from PyQt5.QtCore import QTimer,QObject
import sys
import yt_dlp
class DownloadHandle(Ui_MainWindow,QObject):
    def __init__(self,mainwindow):
        super().__init__()
        self.setupUi(mainwindow)
        self.btnSearch.clicked.connect(self.search_clicked)
        self.btnDownload.clicked.connect(self.download_clicked)
        self.btnDelete.clicked.connect(self.Delete_clicked)
        self.btnFile.clicked.connect(self.File_clicked)
        self.btnPercent.setValue(0)
        self.timer = QTimer(self)  # Sử dụng self làm đối số cho QTimer
        self.timer.timeout.connect(QApplication.processEvents)  # Kết nối timeout với processEvents
        self.timer.start(100)

    def File_clicked(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setViewMode(QFileDialog.Detail)
        if file_dialog.exec_():
            file_paths = file_dialog.selectedFiles()
            if file_paths:
                file_path = file_paths[0]
                self.txtFile.setText(file_path)
    
    def download_video(self, url, quantity, file):
        def progress_hook(d):
            if d['status'] == 'downloading':
                if d.get('total_bytes') and d.get('downloaded_bytes'):
                    percent = int(d['downloaded_bytes'] * 100 / d['total_bytes'])
                    self.btnPercent.setValue(percent)  
                    QApplication.processEvents()
        
        ydl_opts = {
            'format': 'bestvideo[height<='+quantity+']+bestaudio/best[height<='+quantity+']',
            'outtmpl': file,
            'progress_hooks': [progress_hook]
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    def load_quality_options(self):
        link = self.txtSearch.text()
        allowed_qualities = ['2160p', '1440p', '1080p', '720p', '480p', '360p', '240p', '144p']
        added_qualities = set()
        with yt_dlp.YoutubeDL() as ydl:
            info = ydl.extract_info(link, download=False)
            formats = info.get('formats', [])
            for format in formats:
                quality = format.get('format_note', '')
                if quality in allowed_qualities and quality not in added_qualities:
                    self.cbQuality.addItem(quality, format['format_id'])
                    added_qualities.add(quality)
    def search_clicked(self):
         self.cbQuality.clear()
         self.load_quality_options()
    def Delete_clicked(self):
        self.txtSearch.clear()
        self.txtFile.clear()
    def download_clicked(self):
        self.btnPercent.setValue(0)
        link = self.txtSearch.text()
        file = self.txtFile.text()
        quantity = self.cbQuality.currentText()
        # print(file)
        # print(quantity)
       
        self.download_video(link,quantity,file)
    
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    # ui = SingleHandle(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())