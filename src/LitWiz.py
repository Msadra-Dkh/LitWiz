# START V0.1.0

# LibrarZzz / FileZzz!
#----------------------------------------------------------------------------------#
import keyboard
import pyperclip
import time

import keyboard_layout
import keyboardlangs
#----------------------------------------------------------------------------------#

# CONSTANTZzz!
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#

# DicZzz!
#----------------------------------------------------------------------------------#
en_to_fa = {
    'q':'ض', 'w':'ص', 'e':'ث', 'r':'ق', 't':'ف', 'y':'غ', 'u':'ع',
    'i':'ه', 'o':'خ', 'p':'ح', '[':'ج', ']':'چ', '\\':'پ', 'a':'ش',
    's':'س', 'd':'ی', 'f':'ب', 'g':'ل', 'h':'ا', 'j':'ت', 'k':'ن',
    'l':'م', ';':'ک', "'":'گ', 'z':'ظ', 'x':'ط', 'c':'ز', 'v':'ر',
    'b':'ذ', 'n':'د', 'm':'ئ', ',':'و', '.':'.', '/':'/',

    '{':'ج', '}':'چ', '|':'پ', '<':'و', '>':'.', ':':'ک', '"':'گ',
    '?':'؟', ' ':' ',

    'Q':'ض', 'W':'ص', 'E':'ث', 'R':'ق', 'T':'ف', 'Y':'غ', 'U':'ع', 
    'I':'ه', 'O':'خ', 'P':'ح', 'A':'ش', 'S':'س', 'D':'ی', 'F':'ب',
    'G':'ل', 'H':'ا', 'J':'ت', 'K':'ن', 'L':'م', 'Z':'ظ', 'X':'ط',
    'C':'ز', 'V':'ر', 'B':'ذ', 'N':'د', 'M':'ئ'
}

fa_to_en = {
    'ض':'q', 'ص':'w', 'ث':'e', 'ق':'r', 'ف':'t', 'غ':'y', 'ع':'u',
    'ه':'i', 'خ':'o', 'ح':'p', 'ج':'[', 'چ':']', 'پ':'\\', 'ش':'a',
    'س':'s', 'ی':'d', 'ب':'f', 'ل':'g', 'ا':'h', 'ت':'j', 'ن':'k',
    'م':'l', 'ک':';', 'گ':"'", 'ظ':'z', 'ط':'x', 'ز':'c', 'ر':'v',
    'ذ':'b', 'د':'n', 'ئ':'m', 'و':',', '؟':'?',
    ' ':' '
}
#----------------------------------------------------------------------------------#



# FunciZzz!
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

    # update clipboard
    pyperclip.copy("")
    keyboard.press_and_release('ctrl+c')
    time.sleep(0.07)

    # getting selected string from user
    text_input = pyperclip.paste()

    converted_text = ""

    clean_input = text_input.lstrip()

    if clean_input :
        convert_dic = None
    
        #find the true dic
        for find_lang_char in clean_input:

            # FA to EN
            if find_lang_char in fa_to_en :
                convert_dic = fa_to_en
                keyboard_layout.switch_layout(keyboardlangs.ENGLISH_LAYOUT)

                break

            # EN to FA
            elif find_lang_char in en_to_fa :
                convert_dic = en_to_fa
                keyboard_layout.switch_layout(keyboardlangs.PERSIAN_LAYOUT)

                break
        
        # converting the input and pasting / V0.1.0: Changing keyboard layout
        if convert_dic :
            converted_text = ''.join(
                convert_dic.get(lit, lit) for lit in text_input
                )

            pyperclip.copy(converted_text)
            keyboard.press_and_release('ctrl+v')
            time.sleep(0.05)

    # restore clipboard
    pyperclip.copy(old_clipboard)
#----------------------------------------------------------------------------------#



# Main_Idea
#----------------------------------------------------------------------------------#
# HotKeyZzz!
keyboard.add_hotkey('f7' , convert_the_text)
keyboard.add_hotkey('f8' , convert_the_text)
keyboard.add_hotkey('ctrl+shift+w' , convert_the_text)
keyboard.wait()
#----------------------------------------------------------------------------------#

# the END