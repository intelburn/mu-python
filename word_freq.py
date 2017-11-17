import string
with open("gutenberg.txt") as Book:
	text=Book.readlines()
WordCount={}
for line in text:
	words=line.split(" ")
	for word in words:
		word=word.strip()
		word=word.strip("!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~")
		if word in WordCount.keys():
			WordCount[word]+=1
		else:
			WordCount[word]=1
SortedWords=[(word, WordCount[word]) for word in sorted(WordCount, key=WordCount.get, reverse=True)]
with open("freqs.txt", 'a') as output:
	for pair in SortedWords:
		output.write("{0} : {1}\n".format(pair[0], pair[1]))
print("Done")
