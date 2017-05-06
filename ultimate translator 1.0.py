##The Ultimate Translator that supports 32 languages
##It uses Google Translator Engine to translate user input text into language of choice
##It uses Tkinter modules tkMessageBox and tkinter itself for the Graphical User Interface which makes this application interactive
##Created by Harsh Karamchandani,Abhishek Mishra (c){2017}

from Tkinter import *   ##Imports Tkinter modules we need. We need tkMessageBox, tkinter for our application.
from gtts import gTTS  ##To import google text to speech engine
import os
from translate import Translator

root = Tk()  ##Creates Window of our app by making an instance of class Tk
root.title("The Ultimate Translator") ##Title of the GUI Screen

var1 = StringVar(root)
var1.set("Choose Language") ##User gets an option to choose a language for translation of user-input text
var2 = StringVar(root)
var2.set("Choose Language")
var3 = StringVar(root)
var3.set("Choose Accent")
##The application supports 32 languages. So, user has an option of selecting one of these languages for translation
##Creating drop-down menu for user to make a selection from the list
drop_menu=OptionMenu(root,var1,'Arabic', 'Bengali', 'Catalan', 'Chinese',  'Czech', 'Danish', 'Dutch', 'English', 'Finnish', 'French', 'German', 'Greek', 'Hindi', 'Hungarian', 'Indonesian', 'Italian', 'Japanese', 'Korean', 'Latin', 'Latvian', 'Norwegian', 'Polish', 'Portuguese', 'Romanian', 'Russian' , 'Slovak', 'Spanish' , 'Swedish', 'Thai', 'Turkish', 'Vietnamese', 'Welsh')
drop_menu.grid(row=1,column=0, pady=15, padx=15)
drop_menu=OptionMenu(root,var2,'Arabic', 'Bengali', 'Catalan', 'Chinese',  'Czech', 'Danish', 'Dutch', 'English', 'Finnish', 'French', 'German', 'Greek', 'Hindi', 'Hungarian', 'Indonesian', 'Italian', 'Japanese', 'Korean', 'Latin', 'Latvian', 'Norwegian', 'Polish', 'Portuguese', 'Romanian', 'Russian' , 'Slovak', 'Spanish' , 'Swedish', 'Thai', 'Turkish', 'Vietnamese', 'Welsh')
drop_menu.grid(row=1,column=1, pady=15, padx=15)
drop_menu=OptionMenu(root,var3,'Arabic', 'Bengali', 'Catalan', 'Chinese',  'Czech', 'Danish', 'Dutch', 'English', 'Finnish', 'French', 'German', 'Greek', 'Hindi', 'Hungarian', 'Indonesian', 'Italian', 'Japanese', 'Korean', 'Latin', 'Latvian', 'Norwegian', 'Polish', 'Portuguese', 'Romanian', 'Russian' , 'Slovak', 'Spanish' , 'Swedish', 'Thai', 'Turkish', 'Vietnamese', 'Welsh')
drop_menu.grid(row=1,column=2, pady=15, padx=15)
translation_lang_code='en'
def translate(): ##This function translates the user input text into the language of choice
    translation_lang= var2.get()
    lang=[ 'Arabic', 'Bengali', 'Catalan', 'Chinese',  'Czech', 'Danish', 'Dutch', 'English', 'Finnish', 'French', 'German', 'Greek', 'Hindi', 'Hungarian', 'Indonesian', 'Italian', 'Japanese', 'Korean', 'Latin', 'Latvian', 'Norwegian', 'Polish', 'Portuguese', 'Romanian', 'Russian' , 'Slovak', 'Spanish' , 'Swedish', 'Thai', 'Turkish', 'Vietnamese', 'Welsh']
    ##Below are the codes of language supported by the application. The Google translator engine understands the selected language using these codes only
    code=['ar', 'bn', 'ca', 'zh', 'cs', 'da', 'nl', 'en', 'fi', 'fr', 'de', 'el', 'hi', 'hu', 'id', 'it', 'ja', 'ko', 'la', 'lv', 'no', 'pl', 'pt', 'ro', 'ru', 'sk', 'es', 'sv', 'th', 'tr', 'vi', 'cy']
    for i in range(32):
        if translation_lang==lang[i]:
            translation_lang_code=code[i]
    text=e1.get()
    translator= Translator(to_lang=translation_lang)
    translation = translator.translate(text)
    print translation
def speak(): ##This function speaks out the translated text
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
    tts.save("good.mp3")  ##The text to speech engine saves the file as "good.mp3"
    os.system("mpg321 good.mp3") ##Specifying the type of saved file in the last step for the OS
    os.startfile('good.mp3')  ##OS starts and plays the audio of translated text
def accent():  ##Function to speak out the translated text in the accent chosen by user
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
    
Label(root, text="Enter Text in English").grid(row=0)  ##This is to tell the user to enter the input in English language only. This can be changed using source code.

e1 = Entry(root, width=34, bg="green") ##The color of the textbox that accepts user input
e1.grid(row=0, column=1, pady=15, padx=15 , columnspan = 20)
Button(root, text='Speak in Language', command=speak).grid(row=3, column=0, pady=15, padx=15) ##Creating a button to allow user to command "Speak in language" task
Button(root, text='Translate', command=translate).grid(row=3, column=1, pady=15, padx=15)  ##Creating a button to allow user to command "Translate" task
Button(root, text='Speak in Accent', command=accent).grid(row=3, column=2, pady=15, padx=15)  ##Creating a button to allow user to command "Speak in Accent" task

root.mainloop()  ##Keeps the program running till user closes it
