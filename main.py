from austin import austinFunction

def answer(txt):
  answer = austinFunction(txt)

  if answer:
    return answer

  return "CoreBot cannot respond"

while(True):
  userInput = input("Input: ")
  print(answer(userInput))

#i added github
