from Tkinter import *
from gtts import gTTS
import os
from translate import Translator

root = Tk()
root.title("The Ultimate Translator")
var2 = StringVar(root)
var2.set("Choose Language")
drop_menu=OptionMenu(root,var2,'Afrikaans', 'Albanian', 'Arabic', 'Armenian', 'Bengali', 'Catalan', 'Chinese', 'Chinese ﴾Mandarin/China﴿', 'Chinese ﴾Mandarin/Taiwan﴿', 'Chinese ﴾Cantonese﴿', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'English ﴾Australia﴿', 'English ﴾United Kingdom﴿', 'English ﴾United States﴿', 'Esperanto', 'Finnish', 'French', 'German', 'Greek', 'Hindi', 'Hungarian', 'Icelandic', 'Indonesian', 'Italian', 'Japanese', 'Korean', 'Latin', 'Latvian', 'Macedonian', 'Norwegian', 'Polish', 'Portuguese', 'Portuguese ﴾Brazil﴿', 'Romanian', 'Russian', 'Serbian', 'Slovak', 'Spanish' , 'Spanish ﴾Spain﴿', 'Spanish ﴾United States﴿', 'Swahili', 'Swedish', 'Tamil', 'Thai', 'Turkish', 'Vietnamese', 'Welsh')
drop_menu.grid(row=1,column=1, pady=15, padx=15)

translation_lang_code='en'
def translate():
    translation_lang= var2.get()
    lang=['Afrikaans', 'Albanian', 'Arabic', 'Armenian', 'Bengali', 'Catalan', 'Chinese', 'Chinese ﴾Mandarin/China﴿', 'Chinese ﴾Mandarin/Taiwan﴿', 'Chinese ﴾Cantonese﴿', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'English ﴾Australia﴿', 'English ﴾United Kingdom﴿', 'English ﴾United States﴿', 'Esperanto', 'Finnish', 'French', 'German', 'Greek', 'Hindi', 'Hungarian', 'Icelandic', 'Indonesian', 'Italian', 'Japanese', 'Korean', 'Latin', 'Latvian', 'Macedonian', 'Norwegian', 'Polish', 'Portuguese', 'Portuguese ﴾Brazil﴿', 'Romanian', 'Russian', 'Serbian', 'Slovak', 'Spanish' , 'Spanish ﴾Spain﴿', 'Spanish ﴾United States﴿', 'Swahili', 'Swedish', 'Tamil', 'Thai', 'Turkish', 'Vietnamese', 'Welsh']
    code=['af', 'sq', 'ar', 'hy', 'bn', 'ca', 'zh', 'zh‐cn', 'zh‐tw', 'zh‐yue', 'hr', 'cs', 'da', 'nl', 'en', 'en‐au', 'en‐uk', 'en‐us', 'eo', 'fi', 'fr', 'de', 'el', 'hi', 'hu', 'is', 'id', 'it', 'ja', 'ko', 'la', 'lv', 'mk', 'no', 'pl', 'pt', 'pt‐br', 'ro', 'ru', 'sr', 'sk', 'es', 'es‐es', 'es‐us', 'sw', 'sv', 'ta', 'th', 'tr', 'vi', 'cy']
    for i in range(51):
        if translation_lang==lang[i]:
            translation_lang_code=code[i]
    text=e1.get()
    translator= Translator(to_lang=translation_lang)
    translation = translator.translate(text)
    return translation
def speak():
    translation_lang= var2.get()
    lang=['Afrikaans', 'Albanian', 'Arabic', 'Armenian', 'Bengali', 'Catalan', 'Chinese', 'Chinese ﴾Mandarin/China﴿', 'Chinese ﴾Mandarin/Taiwan﴿', 'Chinese ﴾Cantonese﴿', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'English ﴾Australia﴿', 'English ﴾United Kingdom﴿', 'English ﴾United States﴿', 'Esperanto', 'Finnish', 'French', 'German', 'Greek', 'Hindi', 'Hungarian', 'Icelandic', 'Indonesian', 'Italian', 'Japanese', 'Korean', 'Latin', 'Latvian', 'Macedonian', 'Norwegian', 'Polish', 'Portuguese', 'Portuguese ﴾Brazil﴿', 'Romanian', 'Russian', 'Serbian', 'Slovak', 'Spanish' , 'Spanish ﴾Spain﴿', 'Spanish ﴾United States﴿', 'Swahili', 'Swedish', 'Tamil', 'Thai', 'Turkish', 'Vietnamese', 'Welsh']
    code=['af', 'sq', 'ar', 'hy', 'bn', 'ca', 'zh', 'zh‐cn', 'zh‐tw', 'zh‐yue', 'hr', 'cs', 'da', 'nl', 'en', 'en‐au', 'en‐uk', 'en‐us', 'eo', 'fi', 'fr', 'de', 'el', 'hi', 'hu', 'is', 'id', 'it', 'ja', 'ko', 'la', 'lv', 'mk', 'no', 'pl', 'pt', 'pt‐br', 'ro', 'ru', 'sr', 'sk', 'es', 'es‐es', 'es‐us', 'sw', 'sv', 'ta', 'th', 'tr', 'vi', 'cy']
    for i in range(51):
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
    translation_lang= var2.get()
    lang=['Afrikaans', 'Albanian', 'Arabic', 'Armenian', 'Bengali', 'Catalan', 'Chinese', 'Chinese ﴾Mandarin/China﴿', 'Chinese ﴾Mandarin/Taiwan﴿', 'Chinese ﴾Cantonese﴿', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'English ﴾Australia﴿', 'English ﴾United Kingdom﴿', 'English ﴾United States﴿', 'Esperanto', 'Finnish', 'French', 'German', 'Greek', 'Hindi', 'Hungarian', 'Icelandic', 'Indonesian', 'Italian', 'Japanese', 'Korean', 'Latin', 'Latvian', 'Macedonian', 'Norwegian', 'Polish', 'Portuguese', 'Portuguese ﴾Brazil﴿', 'Romanian', 'Russian', 'Serbian', 'Slovak', 'Spanish' , 'Spanish ﴾Spain﴿', 'Spanish ﴾United States﴿', 'Swahili', 'Swedish', 'Tamil', 'Thai', 'Turkish', 'Vietnamese', 'Welsh']
    code=['af', 'sq', 'ar', 'hy', 'bn', 'ca', 'zh', 'zh‐cn', 'zh‐tw', 'zh‐yue', 'hr', 'cs', 'da', 'nl', 'en', 'en‐au', 'en‐uk', 'en‐us', 'eo', 'fi', 'fr', 'de', 'el', 'hi', 'hu', 'is', 'id', 'it', 'ja', 'ko', 'la', 'lv', 'mk', 'no', 'pl', 'pt', 'pt‐br', 'ro', 'ru', 'sr', 'sk', 'es', 'es‐es', 'es‐us', 'sw', 'sv', 'ta', 'th', 'tr', 'vi', 'cy']
    for i in range(51):
        if translation_lang==lang[i]:
            translation_lang_code=code[i]
    text=e1.get()
    tts = gTTS(text, lang=translation_lang_code)
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")
    os.startfile('good.mp3')

    
Label(root, text="Enter Text in English").grid(row=0)

e1 = Entry(root)
e1.grid(row=0, column=1, pady=15, padx=15)
Button(root, text='Speak in Language', command=speak).grid(row=3, column=0, pady=15, padx=15)
Button(root, text='Translate', command=translate).grid(row=3, column=1, pady=15, padx=15)
Button(root, text='Speak in Accent', command=accent).grid(row=3, column=2, pady=15, padx=15)
Label(root, text="Translated Text:  "+translate()). grid(row=5, column=0, pady=15, padx=15)

root.mainloop()
