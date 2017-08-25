import os
word = raw_input("Input key word: ")
print type(word)
dir = 'poems/' + word
os.mkdir(dir)
# os.mkdir('poems/33')
# os.chdir('poems')