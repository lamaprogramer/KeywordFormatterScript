import re;

string = """"""
string = re.sub(r"\s+", " ", string)
string = re.sub(r"[^\w\s]", "", string)
string = string.split(" ")

newString = ""

wordCount = 0
for i in string:
    newString += f"\"{i}\", "
    wordCount += 1
    if wordCount == 5:
        wordCount = 0
        newString += "\n"
    
print(newString)
