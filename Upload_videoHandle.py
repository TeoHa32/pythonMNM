
from upload_video import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel,QVBoxLayout,QPushButton,QDialog,QFileDialog,QMessageBox
from PyQt5.QtCore import QTimer,QObject
import sys
import re
import subprocess
class UploadHandle(Ui_MainWindow):
    def __init__(self,mainwindow):
        self.setupUi(mainwindow)
        self.btnFile.clicked.connect(self.File_clicked)
        self.btnUpload.clicked.connect(self.upload)
        
        
        
    def delete(self):
        self.txtTitle.text.clear()
        self.txtDes.text.clear()
        self.txtkey_word.text.clear()
        self.cbCategory.currentText.clear()
        self.cbStatus.currentText.clear()
    
    def File_clicked(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setViewMode(QFileDialog.Detail)
        if file_dialog.exec_():
            file_paths = file_dialog.selectedFiles()
            if file_paths:
                file_path = file_paths[0]
                self.txtFile.setText(file_path)
    def upload(self):
        if self.txtFile.text() != "":
            if (self.txtTitle.text() != "" and
            self.txtDes.text() != "" and
            self.txtkey_word.text() != "" and
            self.cbCategory.currentText() != "" and
            self.cbStatus.currentText() != ""):
                title = self.txtTitle.text()
                file_path = self.txtFile.text()
                file = file_path.replace("/","\\")
                des = self.txtDes.text()
                keywork = self.txtkey_word.text()
                CBcategory = self.cbCategory.currentText()
                category_list = re.findall(r'\d+', CBcategory)
                if category_list:
                    category = category_list[0]
                status = self.cbStatus.currentText()
                result = subprocess.run('python upload_video_api.py --file="'+file+'" --title="'+title+'" --description="'+des+'" --keywords="'+keywork+'" --category="'+category+'" --privacyStatus="'+status+'"', shell=True, capture_output=True)
                if result.returncode ==0 :
                    msg_box = QMessageBox()
                    msg_box.setIcon(QMessageBox.Warning)
                    msg_box.setWindowTitle("Thông báo")
                    msg_box.setText("Đăng video thành công.")
                    msg_box.exec_()
                else :
                    msg_box = QMessageBox()
                    msg_box.setIcon(QMessageBox.Warning)
                    msg_box.setWindowTitle("Thông báo")
                    msg_box.setText("Đăng video thất bại.")
                    msg_box.exec_()
            else:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setWindowTitle("Thông báo")
                msg_box.setText("Vui lòng nhập đủ thông tin.")
                msg_box.exec_()
        else:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setWindowTitle("Thông báo")
                msg_box.setText("Vui lòng chọn video cần đăng.")
                msg_box.exec_()