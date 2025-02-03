words = input('введите слова:')
words = words.split()

for word in words:
    if word == word[::-1]:
        print(word)
