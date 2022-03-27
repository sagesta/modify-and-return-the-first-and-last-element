word = input('enter a word \n')
words = list(word)
#print (words,'\n')

def chop(t):
   return t[1:-1]

jump = chop(words)
print (jump)
