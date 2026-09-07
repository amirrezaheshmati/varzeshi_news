from deep_translator import GoogleTranslator

def translate(text) :
  fa = GoogleTranslator(source="auto" , target="fa").translate(text)
  return fa