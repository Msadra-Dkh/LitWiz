# START v0.3.0

# LibrarZzz! / FileZzz!
#-----------------------------------------------------------------------------------#
import sys,tray
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer
import traceback

from setting import HotkeyManager, Setting
from notifications import Notification
from sound import SoundPlayer
import app_obj, constants

#----------------------------------------------------------------------------------#

#FunciZzz!
#----------------------------------------------------------------------------------#
def main() :
    app = QApplication(sys.argv)

    Setting.load()

    notifsound = SoundPlayer()
    app_obj.sound = notifsound
    notifsound.play(str(constants.correct_path("assets/sound/Start.wav")))

    notif = Notification()
    app_obj.notif = notif
    notif.set_image(str(constants.correct_path("assets/notification/Start.png")))

    QTimer.singleShot(100, notif.show_notif)


    # HotKeyZzz!
    HotkeyManager.reload()

    Testtray = tray.SystemTray()

    app.setQuitOnLastWindowClosed(False)
    
    return app.exec()

#----------------------------------------------------------------------------------#

# Main_Idea
#----------------------------------------------------------------------------------#
try :
    sys.exit(main())

except Exception:
    with open("error.log", "w", encoding="utf-8") as f:
        f.write(traceback.format_exc())

#----------------------------------------------------------------------------------#

# the END