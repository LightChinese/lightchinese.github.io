import sys
sentence = sys.argv[1]

for dict_path in ["HSK1.md", "HSK2.md", "HSK3.md", "HSK4.md", "HSK5.md", "HSK6.md"]:
  # dict_path = "HSK1.md"
  # for word in dictSet:

  print(dict_path)

  for line in open(dict_path):
      curLine = line.strip()
      words = curLine.split('|')
      word = words[1]
      word = word.strip()
      #print(word)
      if (word in sentence):
          print(curLine)        
  
  print("\n")
