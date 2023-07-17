import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

"""Takes in text document and outputs a bar-chart 
of the frequencies of each alphabet character in the document."""

textDoc = input("Please provide file name. Ex. 'cat.txt': ")

f = open(textDoc, 'r')
fullDocument = f.read().lower()
f.close()

# creating the dataset
letterFreq = defaultdict(int)
lowerLetters = []

for i in range(26):
    letterChar = chr(i + 97)
    lowerLetters.append(letterChar)

for char in fullDocument:
    if char in lowerLetters:
        letterFreq[char] += 1

letters = list(letterFreq.keys())
frequency = list(letterFreq.values())

fig = plt.figure(figsize = (10, 5))

# creating the bar plot
plt.bar(letters, frequency, color ='green',
		width = 0.4)

plt.xlabel("Letter")
plt.ylabel("Frequency in Document")
plt.title("Freq. of Letters in Document")
plt.show()
