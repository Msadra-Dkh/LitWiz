# Start

# LibrarZzz! / FileZzz!
#-----------------------------------------------------------------------------------#
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import (
    QDialog,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QSystemTrayIcon,
    QMenu,
    QApplication
)

from hotkeys import NewHotkeys
from setting import Setting, HotkeyManager
import app_obj , constants

# ClasseZzz!
#-----------------------------------------------------------------------------------#
class SystemTray :
    def __init__(self):
        
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(QIcon(str(constants.correct_path("assets/systemtray/trayicon.png"))))
        setting = Setting.load()

        self.menu = QMenu()
        self.new_hotkey = self.menu.addAction("🔮 Set a new Hotkey")
        self.delete_hotkey = self.menu.addAction("🗑️ Delete a Hotkey")
        self.menu.addSeparator()

        self.sound = self.menu.addAction("🔊 Sounds")
        self.sound.setCheckable(True)
        self.sound.setChecked(setting["sound"])
        self.notification = self.menu.addAction("🎭 Notifications")
        
        self.notification.setCheckable(True)
        self.notification.setChecked(setting["notification"])
        self.menu.addSeparator()

        self.about = self.menu.addAction("🧙 About LitWiz")
        self.close = self.menu.addAction("🚧 Close the spell book")
        
        self.tray.setContextMenu(self.menu)

        self.new_hotkey.triggered.connect(self.set_hotkey)
        self.delete_hotkey.triggered.connect(self.del_hotkey)

        self.sound.triggered.connect(self.sound_check)
        self.notification.triggered.connect(self.notifz)

        self.about.triggered.connect(self.show_about)
        self.close.triggered.connect(self.exit)

        self.tray.show()

    def set_hotkey(self) :
        hotkey = NewHotkeys()
        hotkey.exec()

    def del_hotkey(self) :
        del_tab = DeleteHotkey()
        del_tab.exec()

    def sound_check(self) :
        self.sound_enabled = self.sound.isChecked()

        if not self.sound_enabled :
            app_obj.notif.set_image(str(constants.correct_path("assets/notification/Mutenotif.png")))
            app_obj.notif.show_notif()

        Setting.soundset(self.sound_enabled)
        print("Sound:", self.sound_enabled)
    
    def notifz(self) :
        self.notif_enabled = self.notification.isChecked()
        Setting.notifset(self.notif_enabled)
        print("Notifications:", self.notif_enabled)


    def show_about(self) :
        app_obj.sound.play(str(constants.correct_path("assets/sound/About.wav")))

        app_obj.notif.set_image(str(constants.correct_path("assets/notification/about.png")))
        app_obj.notif.show_notif()

        about_box = AboutBox()
        about_box.exec()

    def exit(self) : 
        app_obj.sound.play(str(constants.correct_path("assets/sound/off.wav")))

        app_obj.notif.set_image(str(constants.correct_path("assets/notification/Close.png")))
        app_obj.notif.show_notif()

        QTimer.singleShot(3500, QApplication.instance().quit)

#-----------------------------------------------------------------------------------#
class AboutBox(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon(str(constants.correct_path("assets/systemtray/trayicon.png"))))
                           
        self.setWindowTitle(" About LitWiz ")
        self.setFixedSize(350, 220)

        box_layout = QVBoxLayout()
        title = QLabel("✨🔮 LitWiz 🔮✨")
        version = QLabel("Version: 0.3.0")
        seprator = QLabel("_______________________________")
        description = QLabel("✨ A Wizard with magical spells for text converting! ✨")
        implement = QLabel("👨‍💻 This is a test project by M.sadra.dkh (...Khaak...). 👨‍💻")
        github = QLabel('<a href="https://github.com/Msadra-Dkh/"> GitHub </a>')
        github.setOpenExternalLinks(True)
        close_button = QPushButton("Close")
        close_button.clicked.connect(self.accept)

        font = QFont()
        font.setPointSize(18)
        font.setBold(True)

        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(font)

        version.setAlignment(Qt.AlignmentFlag.AlignCenter)
        seprator.setAlignment(Qt.AlignmentFlag.AlignCenter)
        description.setAlignment(Qt.AlignmentFlag.AlignCenter)
        implement.setAlignment(Qt.AlignmentFlag.AlignCenter)
        github.setAlignment(Qt.AlignmentFlag.AlignCenter)


        box_layout.addWidget(title)
        box_layout.addWidget(version)
        box_layout.addWidget(seprator)
        box_layout.addWidget(description)
        box_layout.addWidget(implement)
        box_layout.addWidget(github)
        box_layout.addStretch()
        box_layout.addWidget(close_button)

        self.setLayout(box_layout)

#-----------------------------------------------------------------------------------#
class DeleteHotkey(QDialog):
        def __init__(self):
            super().__init__()

            self.setWindowIcon(QIcon(str(constants.correct_path("assets/systemtray/trayicon.png"))))
                           
            self.setWindowTitle(" Delete a Hotkey ")
            self.setFixedSize(350, 220)

            box_layout = QVBoxLayout()
            title = QLabel("🗑️ Erase Spells 🗑️")
            title_font = QFont()
            title_font.setBold(True)
            title_font.setPointSizeF(10)
            title.setFont(title_font)

            seprator = QFrame()
            seprator.setFrameShape(QFrame.Shape.HLine)
            seprator.setFrameShadow(QFrame.Shadow.Sunken)

            description = QLabel(" Which spell would you like to erase?")
            close_button = QPushButton("Close")
            close_button.clicked.connect(self.accept)

            title.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.seprator = QFrame()
            self.seprator.setFrameShape(QFrame.Shape.HLine)
            self.seprator.setFrameShadow(QFrame.Shadow.Sunken)

            description.setAlignment(Qt.AlignmentFlag.AlignCenter)

            row1 = QHBoxLayout()
            button1 = QPushButton("Erase")
            button1.clicked.connect(lambda: Setting.delete("HK1"))
            HotkeyManager.reload()
            button1.clicked.connect(self.accept)
            if Setting.load()["hotkeys"]["HK1"] == "" :
                text1 = "Empty"
                button1.setEnabled(bool(Setting.load()["hotkeys"]["HK1"]))
            else :
                text1 = Setting.load()["hotkeys"]["HK1"]

            hk1 = QLabel(f'🧿 {text1}')


            row2 = QHBoxLayout()
            button2 = QPushButton("Erase")
            button2.clicked.connect(lambda: Setting.delete("HK2"))
            HotkeyManager.reload()
            button2.clicked.connect(self.accept)
            #if Setting.load()["hotkeys"]["HK2"] == "" :
                #text2 = "Empty"
                #button2.setEnabled(bool(Setting.load()["hotkeys"]["HK2"]))
            #else :
                #text2 = Setting.load()["hotkeys"]["HK2"]
                
            #hk2 = QLabel(f'🧿 {text2}')

            box_layout.addWidget(title)
            box_layout.addWidget(seprator)
            box_layout.addWidget(description)
            box_layout.addSpacing(20)
            
            row1.addStretch()
            row1.addWidget(hk1)
            row1.addSpacing(10)
            row1.addWidget(button1)
            row1.addStretch()

            #row2.addStretch()
            #row2.addWidget(hk2)
            #row2.addSpacing(10)
            #row2.addWidget(button2)
            #row2.addStretch()

            box_layout.addLayout(row1)
            box_layout.addLayout(row2)
            box_layout.addStretch()
            box_layout.addWidget(close_button)

            self.setLayout(box_layout)

#-----------------------------------------------------------------------------------#

# the END
