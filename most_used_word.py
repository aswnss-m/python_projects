import pandas as pd

#reading the data
df = pd.read_csv("REVIEW.csv")
#list of the reviews
Revs = list(df["Review"])

#dictionary of the words
words_dict = dict()
for review in Revs:
    review = review.lower()
    review = review.replace(".", " ")
    review = review.replace(",", " ")
    review = review.replace("  ", " ")
    words = review.split(" ")
    for word in words:        
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1

keys = words_dict.keys()
data = []

# All the words in the reviews
for key in keys:
    data.append(f"{key} : {words_dict[key]}")
# writing all of them into a file 'new'
with open('new.txt','w',encoding="utf-8") as f:
    f.write("\n".join(data))

# getting the word count of required words
with open('required.txt','r',encoding='utf-8') as r:
    required= r.read()
    required = required.split("\n")
    temp = ['review,count']
    for req in required:
        temp.append(f"{req.lower()},{words_dict[req.lower()]}")
    
    #writting that data into a new2 file
    with open('new2.csv','w',encoding='utf-8') as x:
        x.write("\n".join(temp))
