#find duplicat resords
import collections
str="ramakant dixit ramakant ramakant sharam sunita dixit ramakant verma kanan dixit"
word_token=str.split()
word_count=collections.Counter(word_token)
dup=[]
for word,count in word_count.items():
    if count>1:
        dup.append(word)
print(dup)