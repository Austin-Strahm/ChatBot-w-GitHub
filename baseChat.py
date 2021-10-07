chatClasses = []

def chatClassAdd(chatFunction):
  chatClasses.append(chatFunction)

class BaseClass:
  def chat(self, txt):
    return None

  def help(self):
    return []