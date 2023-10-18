def readFile(name):
    with open(name, "r", errors="ignore") as file:  
        return file.read()

def wordCount(text):
  palabras_totales = len(text.split())
  return palabras_totales

def uniqueWordCount(text):
  # return count
  return 0

def findContent(text, word):
  # return count
  return 0