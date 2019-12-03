alphabet = "abcdefghigklmnopqrstuvwxyzabcdefghigklmnopqrstuvwxyzабвгдеєжзиіїйклмнопрстуфхцчшщьюяабвгдеєжзиіїйклмнопрстуфхцчшщьюя12345678901234567890"

encrypt = input("Enter a clear message: ")
key = 1
encrypt = encrypt.lower()
encrypted = ""
for letter in encrypt:
    position = alphabet.find(letter)
    newPosition = position + key
    if letter in alphabet:
        encrypted = encrypted + alphabet[newPosition]
    else: 
        encrypted = encrypted + letter
print ("Your ciper is: ", encrypted)
