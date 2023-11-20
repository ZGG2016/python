import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog

from basic.qt.resources.wiki import Ui_MainWindow


class WikiWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.params = {}
        self.setupUi(self)
        self.no_button.setChecked(True)  # 设置默认选中“否”
        self.inputfile_button.clicked.connect(self.get_input_dir)
        self.buttonBox.accepted.connect(self.submit)
        self.buttonBox.rejected.connect(self.clear)

    def get_input_dir(self):
        input_dir = QFileDialog.getExistingDirectory(self, "选择输入文件目录")
        self.inputfile_dir.setText(input_dir)

    def submit(self):
        if self.username.text() == "" or self.password.text() == "" or self.inputfile_dir.text == "":
            self.notice.setText("所有项都需要填写，请检查是否有漏填项！")
            return

        self.params = {
            "username": self.username.text(),
            "password": self.password.text(),
            "inputfile_dir": self.inputfile_dir.text(),
            "is_overwrite": not self.no_button.isChecked()
        }
        self.notice.setText("请到输入目录下查看结果！")
        print("submit:", self.params)

    def clear(self):
        """
        恢复到默认状态，即文本框都是为空，单选框选到“否”
        :return:
        """
        self.username.clear()
        self.password.clear()
        self.inputfile_dir.clear()
        self.yes_button.setChecked(False)
        self.no_button.setChecked(True)
        self.notice.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WikiWindow()
    win.show()
    sys.exit(app.exec_())
