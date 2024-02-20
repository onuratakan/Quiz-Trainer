import sys
import json
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self, questions):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.questions = questions
        self.current_number = str(next(iter(self.questions)))
        self.browser.setUrl(QUrl(self.questions.get(self.current_number)))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        self.addToolBar(navbar)

        previous_btn = QAction("Previous", self)
        previous_btn.triggered.connect(self.previous_question)
        navbar.addAction(previous_btn)

        next_btn = QAction("Next", self)
        next_btn.triggered.connect(self.next_question)
        navbar.addAction(next_btn)

        find_btn = QAction("Find", self)
        find_btn.triggered.connect(self.find_question)
        navbar.addAction(find_btn)

        self.url_bar = QLineEdit()
        self.url_bar.setText(self.current_number)
        self.url_bar.returnPressed.connect(self.find_question)
        navbar.addWidget(self.url_bar)

    def find_question(self):
        question_num = self.url_bar.text()
        if not question_num == self.current_number:
            question_url = self.questions.get(question_num)
            if question_url:
                self.browser.setUrl(QUrl(question_url))
                self.url_bar.setText(question_num)
                self.current_number = question_num
            else:
                QMessageBox.warning(
                    self,
                    "Question",
                    "Question Not Found. Please only enter an existing question number.",
                )
                self.url_bar.setText(self.current_number)

    def previous_question(self):
        if not self.current_number == "1":
            question_num = str((int(self.current_number) - 1))
            question_url = self.questions.get(question_num)
            if question_url:
                self.browser.setUrl(QUrl(question_url))
                self.url_bar.setText(question_num)
                self.current_number = question_num
        else:
            QMessageBox.warning(self, "Question", "There is no previous question.")
            self.url_bar.setText(self.current_number)

    def next_question(self):
        question_num = str((int(self.current_number) + 1))
        question_url = self.questions.get(question_num)
        if question_url:
            self.browser.setUrl(QUrl(question_url))
            self.url_bar.setText(question_num)
            self.current_number = question_num
        else:
            QMessageBox.warning(self, "Question", "There is no next question.")
            self.url_bar.setText(self.current_number)


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <json_file_path>")
        sys.exit(1)

    json_file_path = sys.argv[1]
    questions = read_json_file(json_file_path)

    app = QApplication(sys.argv)
    QApplication.setApplicationName("Quiz Trainer")

    app_icon = QIcon("resources/icons/app_icon.png")
    app.setWindowIcon(app_icon)

    window = MainWindow(questions)
    app.exec_()


def read_json_file(file_path):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
    return data


if __name__ == "__main__":
    main()
