import sys
dict_path = sys.argv[1]
file_path = sys.argv[2]

# dictSet = set(line.strip() for line in open(dict_path))

file = open(file_path,"r") 
file_contents = file.read() 

# for word in dictSet:
for line in open(dict_path):
    curLine = line.strip()
    words = curLine.split('|')
    word = words[1]
    word = word.strip()
    #print(word)
    if (word in file_contents):
        print(curLine)
        