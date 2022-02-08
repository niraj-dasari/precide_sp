from googletrans import Translator

translator = Translator()
def trans(txt):
    text = txt
    translation = translator.translate(text)
    return translation.text


