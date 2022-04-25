import json

file = open('wordsaaa.txt','w')

f = open('words.json')
read = json.load(f)

for elt in read :
    file.write(f"{elt['word']}\n")

file.close()