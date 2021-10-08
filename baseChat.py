CHAT_OBJECTS = []

def addChatObject(chatObject):
  CHAT_OBJECTS.append(chatObject)

class BaseChat:
  def chat(self, text):
    return None

  def help(self):
    return []