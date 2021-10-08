import austin
from baseChat import CHAT_OBJECTS

def answer(txt):
  punctuation = [",", ".", "?", "!", "`", ";", ":", "(", ")", "-", "_", "'"]
  for punc in punctuation:
    txtPunc = txt.replace(punc, "")
  txtLower = txtPunc.lower()
  
  if txtLower == "help":
    helpStrings = []
    for chatFunction in CHAT_OBJECTS:
      helpStrings.extend(chatFunction.help())
    
    return "  >I can respond to:\n    •" + "\n    •".join(helpStrings)

  for function in CHAT_OBJECTS:
    response = function.chat(txt)
    
    if response:
      return "    >{}".format(response)

  return "    >CoreBot cannot respond"

while(True):
  userInput = input("Input: ")
  print(answer(userInput))