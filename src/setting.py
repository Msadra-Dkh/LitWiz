# Start

# LibrarZzz! / FileZzz!
#-----------------------------------------------------------------------------------#
import json
from PySide6.QtCore import (
    QMetaObject,
    Qt,Q_ARG
)

import keyboard, app_obj, converter
import constants

#-----------------------------------------------------------------------------------#

# ClasseZzz!
#-----------------------------------------------------------------------------------#
class Setting :
    @staticmethod
    def load() :
        if not constants.JSON_SETTING_PATH.exists() :
            default_setting = {
                            "hotkeys": {
                                "HK1": "F7"
                            },
                            "sound": True,
                            "notification": True
                        }
            Setting.save(default_setting)

        with open(constants.JSON_SETTING_PATH, "r", encoding="utf-8") as setting_file:
            return json.load(setting_file)

    @staticmethod
    def save(data) :
        with open(constants.JSON_SETTING_PATH, "w", encoding="utf-8") as setting_file:
            json.dump(data, setting_file, indent=4)
    
    @staticmethod
    def delete(slot) :
        QMetaObject.invokeMethod(
            app_obj.sound,
            "play",
            Qt.QueuedConnection,
            Q_ARG(str, str(constants.correct_path("assets/sound/Deletehotkey.wav"))))
        
        QMetaObject.invokeMethod(
            app_obj.notif,
            "show_image_notification",
            Qt.QueuedConnection,
            Q_ARG(str, str(constants.correct_path("assets/notification/Deletehotkey.png"))))

        setting = Setting.load()
        setting["hotkeys"][slot] = ""
        
        Setting.save(setting)
        HotkeyManager.reload()
    
    @staticmethod
    def newhotkey(hotkey) :
            
        data = Setting.load()
        slot = Setting.get_empty_slot()

        if slot is None :
            QMetaObject.invokeMethod(
                app_obj.sound,
                "play",
                Qt.QueuedConnection,
                Q_ARG(str, str(constants.correct_path("assets/sound/Fullhotkey.wav"))))

            QMetaObject.invokeMethod(
                app_obj.notif,
                "show_image_notification",
                Qt.QueuedConnection,
                Q_ARG(str, str(constants.correct_path("assets/notification/nomorespace.png"))))
            return False
        
        else :
            QMetaObject.invokeMethod(
                app_obj.sound,
                "play",
                Qt.QueuedConnection,
                Q_ARG(str, str(constants.correct_path("assets/sound/Addhotkey.wav"))))

            QMetaObject.invokeMethod(
                app_obj.notif,
                "show_image_notification",
                Qt.QueuedConnection,
                Q_ARG(str, str(constants.correct_path("assets/notification/Newhotkey.png"))))
        
            data["hotkeys"][slot] = hotkey
            Setting.save(data)
            HotkeyManager.reload()
            
            return True


    @staticmethod    
    def get_empty_slot():
        data = Setting.load()
        hotkeys = data["hotkeys"]

        for slot , hotkey in hotkeys.items() :
            if hotkey == "" :
                return slot
            
        return None
            
    @staticmethod
    def soundset(check) :
        setting = Setting.load()
        setting["sound"] = check

        Setting.save(setting)

    @staticmethod    
    def notifset(check) :
        setting = Setting.load()
        setting["notification"] = check

        Setting.save(setting)

#-----------------------------------------------------------------------------------#
class HotkeyManager:
    initial = False

    @staticmethod
    def reload():
        if HotkeyManager.initial :
            keyboard.clear_all_hotkeys()

        setting = Setting.load()
        for hotkey in setting["hotkeys"].values() :
            if hotkey :
                                
                keyboard.add_hotkey(hotkey.lower(), converter.convert_the_text)
        
        HotkeyManager.initial = True

#-----------------------------------------------------------------------------------#

# the END
