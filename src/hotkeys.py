# Start

# LibrarZzz! / FileZzz!
#-----------------------------------------------------------------------------------#
from PySide6.QtGui import QIcon,QKeySequence,QFont
from PySide6.QtCore import Qt
from PySide6.QtWidgets import(
    QDialog,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QFrame
)

from setting import Setting
import constants

#-----------------------------------------------------------------------------------#

# ClasseZzz!
#-----------------------------------------------------------------------------------#
class NewHotkeys(QDialog):

    def __init__(self):
        super().__init__()

        self.selected_hotkey = None

        self.setWindowTitle("🔮 Set a New Hotkey")
        self.setFixedSize(350, 200)
        self.setWindowIcon(QIcon(str(constants.correct_path("assets/systemtray/trayicon.png"))))

        layout = QVBoxLayout()

        self.title = QLabel("Press your new hotkey...")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_font = QFont()
        title_font.setBold(True)
        title_font.setPointSizeF(10)
        self.title.setFont(title_font)

        self.seprator = QFrame()
        self.seprator.setFrameShape(QFrame.Shape.HLine)
        self.seprator.setFrameShadow(QFrame.Shadow.Sunken)

        self.label = QLabel("- ??? -")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.save_button = QPushButton("Learn spell")
        self.save_button.setEnabled(False)
        self.save_button.clicked.connect(self.save_hotkey)
        self.close_button = QPushButton("Cancel")
        self.close_button.clicked.connect(self.reject)


        layout.addWidget(self.title)
        layout.addWidget(self.seprator)
        layout.addWidget(self.label)
        layout.addStretch()
        layout.addWidget(self.save_button)
        layout.addWidget(self.close_button)


        self.setLayout(layout)
    
    def keyPressEvent(self, event) :

        if event.key() in (Qt.Key.Key_Control, Qt.Key.Key_Shift, Qt.Key.Key_Alt, Qt.Key.Key_Meta) : return
        self.save_button.setEnabled(True)
        sequence = QKeySequence(event.keyCombination())
        hotkey = sequence.toString()
        self.selected_hotkey = hotkey
        self.label.setText(hotkey)
    
    def save_hotkey(self) :
        if Setting.newhotkey(self.selected_hotkey) :
            self.accept()

        else :
            self.label.setText("🧙 Spell book is full!")

#-----------------------------------------------------------------------------------#

# the END
