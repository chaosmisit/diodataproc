f = open('livro2.txt')
data = f.read()
wordlist = data.split()
wordfreq = [wordlist.count(w) for w in wordlist]
#print("String\n" + data +"\n")
#print("List\n" + str(wordlist) + "\n")
#print("Frequencies\n" + str(wordfreq) + "\n")
#print("Pairs\n" + str(list(zip(wordlist, wordfreq))))
#newfile = open('output.txt', 'w')
table = list(zip(wordlist, wordfreq))
table = sorted(table, key=lambda x: (x[1],x[1]), reverse=True)
table = list(dict.fromkeys(table))
ntable = ""
for x in table:
	line = str(x)
	line = line + "\n"
	ntable = ntable + line

with open('output.txt', 'w') as newfile:
	write_data = newfile.write(ntable)
print(ntable)
