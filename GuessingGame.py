
import nltk
from nltk import word_tokenize
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import random
import sys


stopWords = set(stopwords.words('english'))#setting stop words


if len(sys.argv)<2:#checking for sysarg
	print("No file name provided")
	exit()

fileName = sys.argv[1]


f = open(fileName)#open and read file
yourList = f.read()

xx = word_tokenize(yourList)#tokenize
y = len(set(xx))#how many unique strings
z = len(xx)#how many tokens
g = y/z#calc lexical diversity
g= round(g,2)#round lexical diversity to two digits
print("Lexical diversity is %d", g)

def preprocessing(x):#preprocessing method
	lemmatizer = WordNetLemmatizer()
	zz = []
	for t in x:#make new list zz with lowercase, alpha, in stopwords, and length<5
		if t.isalpha() and t.islower() and t not in stopWords and len(t)>5:
			tt = lemmatizer.lemmatize(t)#lemmatize words whichc fit the criteria
			zz.append(tt)
	kk = list(set(zz))#only unique words
	acount = len(kk)#how many unique words
	kk = nltk.pos_tag(kk)#pos tag the unique words and get only the nouns
	#print(kk[0:20])
	Nlist = []
	hList = ["NN","NNS","NNP","NNPS"]
	for x in kk:
		if x[1] in hList:
			Nlist.append(x)
	dcount = len(Nlist)#how many nounds
	
	superList = []
	for x in Nlist:
		superList.append(x[0])#elimate pos, and only keep word

	print("Number of tokens from step A is "+ str(acount) + " and nouns from step D is " + str(dcount))
	return((zz,superList))#return as tuple
(a,b) = preprocessing(xx) #call preprocessing and unpack tuple 

fdist = FreqDist(a)# find the frequency of the nouns
dicty = {}
for one, two in fdist.items():
	if one in b:
		dicty[one] = two#dict with keys being the unique nouns, and the values being the frequency
sorted_values = sorted(dicty.values())#sort and reverse the dict
sorted_values = sorted_values[::-1]
sorted_dicty = {}
for i in sorted_values:
    for k in dicty.keys():
        if dicty[k] == i:
            sorted_dicty[k] = dicty[k]
keys = sorted_dicty.keys()
keys = list(keys)
dictList = []
x = 0
while x<50:#print top 50 nouns
	dictList.append(keys[x])
	print(str(x+1) + ". " + str(keys[x]) + ": " + str(dicty[keys[x]]))
	x+=1



actualWord = random.choice(dictList)#get random word from top 50
placeholder = len(actualWord)*'_'#set placeholder with underscores

score = 5
guess = ""

while score > 0 and guess != "!" and "_" in placeholder:
	print(placeholder + ", score: " + str(score))#print status
	guess = input("Enter your guess: \n")
	hit = 0 #toggle to see if guess was sucessfull
	if guess != "!":#if they made a valid guess
		for x in range(len(actualWord)):#if the guess is correct, then replace all instances of that letter in the placeholder
			if guess == actualWord[x]:
				s = list(placeholder)
				s[x] = guess
				placeholder = "".join(s)
				hit = 1
	else:#messages to player after each round
		print("Game exited")
	if hit == 0:
		print("Sorry, guess again")
		score = score-1
	else:
		print("Right!!")
		score = score+1

print("Word was " + actualWord + ", score: " + str(score))


