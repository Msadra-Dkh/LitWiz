# Start

# LibrarZzz! / FileZzz!
#-----------------------------------------------------------------------------------#
from PySide6.QtCore import QObject, Slot, QUrl
from PySide6.QtMultimedia import QSoundEffect
import json, constants

#-----------------------------------------------------------------------------------#

# ClasseZzz!
#-----------------------------------------------------------------------------------#
class SoundPlayer(QObject) :
    def __init__(self) :
        super().__init__()
        self.sound = QSoundEffect(self)

    @Slot(str)
    def play(self, path) :
        with open(constants.JSON_SETTING_PATH, "r", encoding="utf-8") as setting_file:
            soundset = json.load(setting_file)
        
        if not soundset["sound"] : return

        self.sound.setSource(QUrl.fromLocalFile(path))
        self.sound.setVolume(1.0)

        self.sound.play()
#-----------------------------------------------------------------------------------#

# the END
