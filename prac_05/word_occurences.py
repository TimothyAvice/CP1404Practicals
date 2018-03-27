"""
Counts each word in a string
"""

user_text = input("Text: ")
text = user_text.split(" ")

words = {}

for word in text:
    if word in words:
        words[word] += 1
    elif word not in words:
        words[word] = 1
for word in words:
    print("{}: {}".format(word, words[word]))