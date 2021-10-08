from baseChat import BaseChat,addChatObject


class AustinChat(BaseChat):
  def chat(self, txt):

    import re
    responses1 = ["time", "times", "clock", "today"]
    responses2 = ["im"]
    responses22 = ["i", "we", "am", "are"]
    punctuation = [",", ".", "?", "!", "`", ";", ":", "(", ")", "-", "_", "'"]
    favorites = {"dog":"golden doodle", "food":"food for thought", "class":"computer science with Dr. McCurdy", "color":"navy blue", "movie":"Die Hard", "show":"Lost", "number":"23"}
    favoritesPlural = {"colors":"navy blue and green", "numbers":"4 8 15 16 23 42"}
    teachers = {"odegard":"Mr. Odegard teaches mathematics at SET High", "mccurdy":"Dr. McCurdy is the principle and computer science teacher at SET High", "putaro":"Mr. Putaro teaches mathematics and music prodution at SET High", "ryan":"Ms. Ryan is an academic coach at SET High", "cozik":"Ms. Cozik is a special education teacher at SET High", "ashe":"Mr. Ashe teaches earth science, physics, and chemistry at SET High", "burge":"Ms. Burge is a special education and english teacher at SET High", "montello":"Mr. Montello teaches robotics classes and clubs at SET High", "Heath":"Ms. Heath is the office manager at SET High", "heid":"Mr. Heid teaches the art, stocks, and youtube classes at SET High", "walsall":"Mr. Walsall teaches the biology, forensics, and space science classes at SET High", "mc":"MC is the assistant principle at SET High", "mcclendon":"MC is the assistant principle at SET High", "romero":"Ms. Romero is the lead of special education, runs the IGNITE club, and is the school phsycologist at SET High", "lennon":"Ms. Lennon teaches english at SET High", "j":"Ms. Jokanovic teaches history at SET High", "jokanovic":"Ms. Jokanovic teaches history at SET High", "bush":"Ms. Bush is a special education teacher at SET High", "geis":"Ms. Geis is the physical education and leadership teacher at SET High", "maldonado":"Mr. Maldonado teaches guitar at SET High", "hines":"Ms. Hines is the counselor at SET High", "castro":"Ms. Castro works at the main office and manages attendence", "farias":"Ms. Farias teaches spanish at SET High", "marquez":"Ms. Marquezth is an academic coach at SET High", "apalategui":"Mr. Apalategui teaches history classes at SET High"}

    import time
    timeNumbers = time.time()
    timeNumbers = timeNumbers-25200
    currentTime = time.ctime(timeNumbers)
    dadBotValue = 0
    iamValue = 0


    for punc in punctuation:
      txt = txt.replace(punc, "")
    
    txtLower = txt.lower()
    
    txtWords = txt.split(" ")

    favoriteUnfiltered = re.search("(.*)what((s)|([\s]+is)|([\s]+are))[\s]+((your)|(youre))[\s]+favorite[\s]+(\S+)(.*)", txtLower)
    if favoriteUnfiltered:
      favoriteFiltered = favoriteUnfiltered.group(9)

      if favoriteFiltered in favorites:
        print("My favorite {} is {}".format(favoriteFiltered, favorites[favoriteFiltered]))
      elif favoriteFiltered in favoritesPlural:
        print("My favorite {} are {}".format(favoriteFiltered, favoritesPlural[favoriteFiltered]))

    teachersUnfiltered = re.search("(.*)((dr)|(mr)|(ms)|(mrs))((\s)|(\W*))+(\w+)+(.*)", txtLower)
    if teachersUnfiltered:
      teachersFiltered = teachersUnfiltered.group(10)

      if teachersFiltered in teachers:
        return (teachers[teachersFiltered])

    for word in txtWords:
      if word.lower() in responses1:
        return ("The current time is {}".format(currentTime))

    for word1 in txtWords:
      if word1 in teachers:
        return (teachers[word1])

    for word in txtWords:

      if dadBotValue == 1:
        return ("Hi {}, I'm CoreBot and you've activated DadBot Mode!".format(word))

      if iamValue == 2:
        return ("Hi {}, I'm CoreBot and you've activated DadBot Mode!".format(word))

      if word.lower() in responses2:
        dadBotValue = 1

      if word.lower() in responses22:
        iamValue = iamValue+1
      else:
        iamValue = 0

    return None
  
  def help(self):
    return ["time", "(teacher name or question)", "i'm (any word)"]

chatObject = AustinChat()
addChatObject(chatObject)