from googletrans import Translator
import sys
sys.stdout.reconfigure(encoding='utf-8')


def translate_Vi_En(viet_text):
    translator = Translator()
    translation = translator.translate(viet_text, src='vi', dest='en')
    return translation.text
