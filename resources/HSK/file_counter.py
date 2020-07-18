import sys

file_path = sys.argv[1]
file = open(file_path,"r")
Lines = file.readlines()

all_counter = 0

for line in Lines:
    curr_counter = 0

    for dict_path in ["HSK1.md", "HSK2.md", "HSK3.md", "HSK4.md", "HSK5.md", "HSK6.md"]:
        # dict_path = "HSK1.md"
        # for word in dictSet:
  
        print(dict_path)
  
        for line in open(dict_path):
            curLine = line.strip()
            words = curLine.split('|')
            word = words[1]
            word = word.strip()
            if (word in line):
                print(curLine)    
                curr_counter += 1
        
        print("\n")
    
    all_counter += curr_counter;

print(all_counter)
