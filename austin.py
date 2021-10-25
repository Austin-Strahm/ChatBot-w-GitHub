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

    try:
      mult = re.match("(\d+)(\*)(\d+)", txt)
      multiplication = multiply(mult.group(1), mult.group(3))
      return multiplication
    except:
      nothing = 0

    return None
  
  def help(self):
    return ["time", "(teacher name or question)", "i'm (any word)", "multiplication (eg. 2*2)"]

import re

def multiply(leftInput, rightInput):
  leftNegativeValue = 0
  rightNegativeValue = 0
  leftListValue = -1
  integerAnswer = 0
  decimalValue = 0
  integerValue = 0
  leftInputNum = float(leftInput)
  rightInputNum = float(rightInput)
  # setting up values to exist prior to later use

  if leftInputNum == 0 or rightInputNum == 0:
    return "0"
  if leftInputNum < 0:
    leftNegativeValue = 1
  if rightInputNum < 0:
    rightNegativeValue = 1
  leftInputNum = abs(leftInputNum)
  rightInputNum = abs(rightInputNum)
  if type(leftInputNum) == int or type(leftInputNum) == float:
    integerValue = 0
  else:
    return "LeftInput is not a number"
  if type(rightInputNum) == int or type(rightInputNum) == float:
    integerValue = 0
  else:
    return "rightInput is not a number"
  # if either are 0, then the product is 0
  # if either are negative, we use values to ensure that later we can revert the product to either negative or positive
  # if either are not numbers, we return a string describing the lack of numbers

  leftInputFloat = re.match("(\d+)(\.)(\d+)", str(leftInput))
  rightInputFloat = re.match("(\d+)(\.)(\d+)", str(rightInput))
  # from the numbers, we try extracting numbers either side of a decimal point

  if leftInputFloat:
    leftIntegerStr = str(leftInputFloat.group(1))
    leftFloatStr = str(leftInputFloat.group(3))
    leftIntegerList = list(leftIntegerStr)
    leftFloatList = list(leftFloatStr)
    leftIntegerList.extend(leftFloatStr)
  else:
    leftIntegerList = list(str(leftInput))
    leftFloatList = range(0)

  if rightInputFloat:
    rightIntegerStr = str(rightInputFloat.group(1))
    rightFloatStr = str(rightInputFloat.group(3))
    rightIntegerList = list(rightIntegerStr)
    rightFloatList = list(rightFloatStr)
    rightIntegerList.extend(rightFloatStr)
  else:
    rightIntegerList = list(str(rightInput))
    rightFloatList = range(0)
  # if the system above worked, there would be 'leftInputFloat' and if so, this gets a list of:
  # 1) full number without the decimal point
  # 2) right side of the number after the decimal point
  # if the regular expression did not work, we just convert the numbers directly into lists


  for leftDigit in leftIntegerList:
    answer = 0
    rightListValue = -1

    for rightDigit in rightIntegerList:
      rightDigitList = range(int(rightIntegerList[rightListValue]))
      
      for item in rightDigitList:
        answer = answer + int(leftIntegerList[leftListValue])

      for zero1 in range(abs(leftListValue)-1):
        answer = "{}0".format(answer)
        answer = int(answer)

      for zero2 in range(abs(rightListValue)-1):
        answer = "{}0".format(answer)
        answer = int(answer)

      integerAnswer = integerAnswer+answer

      rightListValue = rightListValue-1
      answer = 0
    
    leftListValue = leftListValue-1
  # for each digit in the leftInput, we multiply this number with each digit in the rightInput
  # to make sure we get the correct digit placement, we start from right to left for each number list and as the list goes from side to side, we add a 0 at the end of the product between two digits.


  for item in leftIntegerList:
    integerValue = integerValue+1
  
  # for item in list(leftIntegerStr):
  #   decimalValue = decimalValue+1

  for item in leftFloatList:
    decimalValue = decimalValue-1

  for item in rightIntegerList:
    integerValue = integerValue+1

  # for item in list(rightIntegerStr):
  #   decimalValue = decimalValue+1

  for item in rightFloatList:
    decimalValue = decimalValue-1

  integerAnswer = round(integerAnswer,integerValue)
  # to ensure that the computer doesn't scuff the addition, we round the number at the end based on how many digits are in each number.

  if leftFloatList or rightFloatList:
    answerList = list(str(integerAnswer))
    answerList.insert(decimalValue,".")
    answerList = "".join(answerList)
  else:
    answerList = integerAnswer
  # to make sure we put the decimal back in after the multiplication, we count how many decimal digits there are and from there we can tell where the decimal goes.

  if leftNegativeValue == 1:
    answerList = -(float(answerList))
  if rightNegativeValue == 1:
    answerList = -(float(answerList))
  # correcting negative values

  integer = "{}".format(str(float(answerList)))
  return integer

chatObject = AustinChat()
addChatObject(chatObject)