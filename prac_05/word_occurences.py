user_text = input("Text: ")
text = user_text.split(" ")

WORDS = {}

for word in text:
    if word in WORDS:
        WORDS[word] += 1
    elif word not in WORDS:
        WORDS[word] = 1
for word in WORDS:
        print("{}: {}".format(word, WORDS[word]))