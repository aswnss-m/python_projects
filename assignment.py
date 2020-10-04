f = open("/home/aswnss/Documents/data.txt","r")

data = dict()
text = f.read()

words= text.split()
for word in words:
	word = word.strip()
	for i in word:
		i = i.lower()
		i = i.replace(',','')
		i = i.replace('.','')
		i = i.replace('"','')
		i = i.replace('!','')
		data[i] = data.get(i,0)+1


max_value = max(data.values())


for i in data:
	print(i , ':' , data[i])

print('\n\n\n\n\n')
for i in data:
	if data[i] == max_value:
		print(i,data[i])
