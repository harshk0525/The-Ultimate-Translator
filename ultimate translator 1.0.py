from Tkinter import *
from gtts import gTTS
import os
from translate import Translator

root = Tk()
root.title("The Ultimate Translator")

var1 = StringVar(root)
var1.set("Choose Language")
var2 = StringVar(root)
var2.set("Choose Language")
var3 = StringVar(root)
var3.set("Choose Accent")
drop_menu=OptionMenu(root,var1,'Arabic', 'Bengali', 'Catalan', 'Chinese',  'Czech', 'Danish', 'Dutch', 'English', 'Finnish', 'French', 'German', 'Greek', 'Hindi', 'Hungarian', 'Indonesian', 'Italian', 'Japanese', 'Korean', 'Latin', 'Latvian', 'Norwegian', 'Polish', 'Portuguese', 'Romanian', 'Russian' , 'Slovak', 'Spanish' , 'Swedish', 'Thai', 'Turkish', 'Vietnamese', 'Welsh')
drop_menu.grid(row=1,column=0, pady=15, padx=15)
drop_menu=OptionMenu(root,var2,'Arabic', 'Bengali', 'Catalan', 'Chinese',  'Czech', 'Danish', 'Dutch', 'English', 'Finnish', 'French', 'German', 'Greek', 'Hindi', 'Hungarian', 'Indonesian', 'Italian', 'Japanese', 'Korean', 'Latin', 'Latvian', 'Norwegian', 'Polish', 'Portuguese', 'Romanian', 'Russian' , 'Slovak', 'Spanish' , 'Swedish', 'Thai', 'Turkish', 'Vietnamese', 'Welsh')
drop_menu.grid(row=1,column=1, pady=15, padx=15)
drop_menu=OptionMenu(root,var3,'Arabic', 'Bengali', 'Catalan', 'Chinese',  'Czech', 'Danish', 'Dutch', 'English', 'Finnish', 'French', 'German', 'Greek', 'Hindi', 'Hungarian', 'Indonesian', 'Italian', 'Japanese', 'Korean', 'Latin', 'Latvian', 'Norwegian', 'Polish', 'Portuguese', 'Romanian', 'Russian' , 'Slovak', 'Spanish' , 'Swedish', 'Thai', 'Turkish', 'Vietnamese', 'Welsh')
drop_menu.grid(row=1,column=2, pady=15, padx=15)
translation_lang_code='en'
def translate():
    translation_lang= var2.get()
    lang=[ 'Arabic', 'Bengali', 'Catalan', 'Chinese',  'Czech', 'Danish', 'Dutch', 'English', 'Finnish', 'French', 'German', 'Greek', 'Hindi', 'Hungarian', 'Indonesian', 'Italian', 'Japanese', 'Korean', 'Latin', 'Latvian', 'Norwegian', 'Polish', 'Portuguese', 'Romanian', 'Russian' , 'Slovak', 'Spanish' , 'Swedish', 'Thai', 'Turkish', 'Vietnamese', 'Welsh']
    code=['ar', 'bn', 'ca', 'zh', 'cs', 'da', 'nl', 'en', 'fi', 'fr', 'de', 'el', 'hi', 'hu', 'id', 'it', 'ja', 'ko', 'la', 'lv', 'no', 'pl', 'pt', 'ro', 'ru', 'sk', 'es', 'sv', 'th', 'tr', 'vi', 'cy']
    for i in range(32):
        if translation_lang==lang[i]:
            translation_lang_code=code[i]
    text=e1.get()
    translator= Translator(to_lang=translation_lang)
    translation = translator.translate(text)
    print translation
def speak():
    translation_lang= var1.get()
    lang=[ 'Arabic', 'Bengali', 'Catalan', 'Chinese',  'Czech', 'Danish', 'Dutch', 'English', 'Finnish', 'French', 'German', 'Greek', 'Hindi', 'Hungarian', 'Indonesian', 'Italian', 'Japanese', 'Korean', 'Latin', 'Latvian', 'Norwegian', 'Polish', 'Portuguese', 'Romanian', 'Russian' , 'Slovak', 'Spanish' , 'Swedish', 'Thai', 'Turkish', 'Vietnamese', 'Welsh']
    code=['ar', 'bn', 'ca', 'zh', 'cs', 'da', 'nl', 'en', 'fi', 'fr', 'de', 'el', 'hi', 'hu', 'id', 'it', 'ja', 'ko', 'la', 'lv', 'no', 'pl', 'pt', 'ro', 'ru', 'sk', 'es', 'sv', 'th', 'tr', 'vi', 'cy']
    for i in range(32):
        if translation_lang==lang[i]:
            translation_lang_code=code[i]
    text=e1.get()
    translator= Translator(to_lang=translation_lang)
    translation = translator.translate(text)
    tts = gTTS(translation, lang=translation_lang_code)
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")
    os.startfile('good.mp3')
def accent():
    translation_lang= var3.get()
    lang=[ 'Arabic', 'Bengali', 'Catalan', 'Chinese',  'Czech', 'Danish', 'Dutch', 'English', 'Finnish', 'French', 'German', 'Greek', 'Hindi', 'Hungarian', 'Indonesian', 'Italian', 'Japanese', 'Korean', 'Latin', 'Latvian', 'Norwegian', 'Polish', 'Portuguese', 'Romanian', 'Russian' , 'Slovak', 'Spanish' , 'Swedish', 'Thai', 'Turkish', 'Vietnamese', 'Welsh']
    code=['ar', 'bn', 'ca', 'zh', 'cs', 'da', 'nl', 'en', 'fi', 'fr', 'de', 'el', 'hi', 'hu', 'id', 'it', 'ja', 'ko', 'la', 'lv', 'no', 'pl', 'pt', 'ro', 'ru', 'sk', 'es', 'sv', 'th', 'tr', 'vi', 'cy']
    for i in range(32):
        if translation_lang==lang[i]:
            translation_lang_code=code[i]
    text=e1.get()
    tts = gTTS(text, lang=translation_lang_code)
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")
    os.startfile('good.mp3')

    
Label(root, text="Enter Text in English").grid(row=0)

e1 = Entry(root, width=34, bg="green")
e1.grid(row=0, column=1, pady=15, padx=15 , columnspan = 20)
Button(root, text='Speak in Language', command=speak).grid(row=3, column=0, pady=15, padx=15)
Button(root, text='Translate', command=translate).grid(row=3, column=1, pady=15, padx=15)
Button(root, text='Speak in Accent', command=accent).grid(row=3, column=2, pady=15, padx=15)
Label(root, text="Translated Text:"). grid(row=5, column=0, pady=15, padx=15)

root.mainloop()
