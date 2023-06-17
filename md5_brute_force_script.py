import hashlib

# Replace md5 hash flag and salt as needed
hash = "f88d03fc794cedfccb18409126bcc819"
salt = "2cc92255bcde"
count = 0

# using a list of words with 7 letters
with open('word-list-7-letters.txt') as word_list:
    for word in word_list:
        temp = hashlib.md5((word.strip() + salt).encode()).hexdigest()

        if temp == hash:
            print(word)
            break
    else:
        print("No word found.")