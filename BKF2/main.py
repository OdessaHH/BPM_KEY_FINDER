import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QFileDialog
import key_estimator
import bpm_counter

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BPM Counter and Key Estimator")
        self.setGeometry(100, 100, 400, 200)

        # Create labels
        self.label_info = QLabel("This app estimates the key and counts the BPM of your chosen file.")
        self.label_file = QLabel("No audio file chosen.")
        self.label_key = QLabel("Key: ")
        self.label_bpm = QLabel("BPM: ")

        # Create buttons
        self.btn_choose_file = QPushButton("Choose File")
        self.btn_choose_file.clicked.connect(self.choose_file)

        self.btn_choose_another_file = QPushButton("Choose Another File")
        self.btn_choose_another_file.clicked.connect(self.choose_another_file)
        self.btn_choose_another_file.setEnabled(False)

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_info)
        layout.addWidget(self.btn_choose_file)
        layout.addWidget(self.label_file)
        layout.addWidget(self.label_key)
        layout.addWidget(self.label_bpm)
        layout.addWidget(self.btn_choose_another_file)

        # Create central widget and set layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Initialize audio_file as None
        self.audio_file = None

    def choose_file(self):
        file_dialog = QFileDialog()
        audio_file, _ = file_dialog.getOpenFileName(self, "Select Audio File", "/home/user/Music")
        if audio_file:
            self.audio_file = audio_file
            self.label_file.setText(f"Chosen File: {audio_file}")
            self.update_results()
            self.btn_choose_file.setEnabled(False)
            self.btn_choose_another_file.setEnabled(True)

    def choose_another_file(self):
        self.audio_file = None
        self.label_file.setText("No audio file chosen.")
        self.label_key.setText("Key: ")
        self.label_bpm.setText("BPM: ")
        self.btn_choose_file.setEnabled(True)
        self.btn_choose_another_file.setEnabled(False)

    def update_results(self):
        if self.audio_file:
            key, scale, key_strength = key_estimator.key_estimate(self.audio_file)
            bpm = bpm_counter.calculate_bpm(self.audio_file)
            bpm_rounded = round(bpm)

            # Convert key strength to percentage and round to two decimal places
            key_strength_percent = key_strength * 100
            key_strength_rounded = round(key_strength_percent, 2)

            self.label_key.setText(f"Key: {key} ({scale})")
            self.label_bpm.setText(f"BPM: {bpm_rounded}")
        else:
            self.label_key.setText("Key: ")
            self.label_bpm.setText("BPM: ")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
