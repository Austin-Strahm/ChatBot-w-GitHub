chatClasses = []

def chatClassAdd(chatFunction):
  chatClasses.append(chatFunction)

class ChatClassBase:
  def chat(self, txt):
    return None

  def help(self):
    return []