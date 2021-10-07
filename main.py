import austin
from baseChat import chatClasses

def answer(txt):
  punctuation = [",", ".", "?", "!", "`", ";", ":", "(", ")", "-", "_", "'"]
  for punc in punctuation:
    txtPunc = txt.replace(punc, "")
  txtLower = txtPunc.lower()
  
  if txtLower == "help":
    helpList = []
    for chatFunction in chatClasses:
      helpList.extend(chatFunction.help())
    
    return "I can respond to:\n  •" + "\n •".join(helpList)

  for function in chatClasses:
    response = function.chat(txt)
    
    if response:
      return "    >{}".format(response)

  return "CoreBot cannot respond"

while(True):
  userInput = input("Input: ")
  print(answer(userInput))