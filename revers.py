word = input("Enter word: ")
reverse = []
index = len(word)
while  index > 0:
    reverse += word [index - 1]
    index = index - 1
    reverse= ''.join(list(reverse))
print(reverse)

