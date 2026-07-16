# Start

# LibrarZzz! / FileZzz!
#-----------------------------------------------------------------------------------#
import time, pyperclip
from PySide6.QtCore import QTimer
from PySide6.QtCore import (
    QMetaObject,
    Qt,
    Q_ARG
)

import keyboard_layout, keyboardlangs, constants, app_obj, sender

#-----------------------------------------------------------------------------------#

#FunciZzz!
#----------------------------------------------------------------------------------#
def convert_the_text ():  
    '''
    about this function:
        This function saves the current clipboard content,
        copies the selected text, converts it between
        Persian and English keyboard layouts, pastes the
        result, and finally restores the original clipboard.

    variables:
        old_clipboard  : for saving the latest clipboards input
        text_input     : for getting selected string from user
        converted_text : this is the final string that is converted 'text_input'
        clean_input    : a clean version of 'text_input' with no whitespace
        convert_dic    : choosen dictionary for changing 'text_input'
        find_lang_char : a meaningful character of 'clean_input' for choosing the true dictionary
    '''
    

    # saving clipboard
    old_clipboard = pyperclip.paste()

    try:
        # update clipboard
        pyperclip.copy(str())
        sender.ctrl_c()
        time.sleep(0.2)

        # getting selected string from user
        text_input = pyperclip.paste()
        print(text_input)
        converted_text = ""

        clean_input = text_input.lstrip()

        if clean_input:
            convert_dic = None
        
            #find the true dic
            for find_lang_char in clean_input:

                # FA to EN
                if find_lang_char in constants.fa_to_en :
                    convert_dic = constants.fa_to_en
                    keyboard_layout.switch_layout(keyboardlangs.ENGLISH_LAYOUT)

                    break

                # EN to FA
                elif find_lang_char in constants.en_to_fa :
                    convert_dic = constants.en_to_fa
                    keyboard_layout.switch_layout(keyboardlangs.PERSIAN_LAYOUT)

                    break
            
            # converting the input and pasting / V0.1.0: Changing keyboard layout
            if convert_dic :
                converted_text = ''.join(
                    convert_dic.get(lit, lit) for lit in text_input
                    )

                pyperclip.copy(converted_text)
                sender.ctrl_v()
                time.sleep(0.1)

                QMetaObject.invokeMethod(
                    app_obj.sound,
                    "play",
                    Qt.QueuedConnection,
                    Q_ARG(str, str(constants.correct_path("assets/sound/Convert.wav"))))

                QMetaObject.invokeMethod(
                    app_obj.notif,
                    "show_image_notification",
                    Qt.QueuedConnection,
                    Q_ARG(str, str(constants.correct_path("assets/notification/Convert.png"))))

        else :
            QMetaObject.invokeMethod(
                app_obj.sound,
                "play",
                Qt.QueuedConnection,
                Q_ARG(str, str(constants.correct_path("assets/sound/Notextnotif.wav"))))
            
            QMetaObject.invokeMethod(
                app_obj.notif,
                "show_image_notification",
                Qt.QueuedConnection,
                Q_ARG(str, str(constants.correct_path("assets/notification/Notext.png"))))
        
    finally:
        # restore clipboard
        pyperclip.copy(old_clipboard)

#----------------------------------------------------------------------------------#

# the END
