import sys

hexagon = set()
info = sys.stdin.readline().strip()
center_letter = info[0]
for char in info:
    hexagon.add(char)

matching_words = []
num_words = int(sys.stdin.readline().strip())
for i in range(num_words):
    word = sys.stdin.readline().strip()
    if center_letter in word and len(word) >= 4:
        valid_word = True
        for letter in word:
            if letter not in hexagon:
                valid_word = False
                break
        if valid_word:
            matching_words.append(word)

[print(word) for word in matching_words]
