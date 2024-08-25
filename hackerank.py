"""vowel = ["a", "e", "i", "o", "u", "y"]
count = 0
total = 0
num = int(input())
    

words = []
counts = [] 

for i in range(num):
    word = (str(input("")).rstrip("\n").lower())
    if len(word) <= 20:
        words.append(word)
    else:
        break

    for char in vowel:
        for chars in words[i]:
            if char in chars:
                count += 1
            else:
                count += 0
    
    if count % 2 == 0:
        count = 2
    else:
        count = 1
    total += count
    count = 0

separator = " "  # You can change the separator as needed
result = separator.join(words)
print(result)
print(total)
"""



vowel = ["a", "e", "i", "o", "u", "y"]
count = 0
total = 0

num = int(input("Enter the number of words: "))

# Get all words in a single line and split them into a list
words = input("Enter the words separated by space: ").split()

# Ensure the list length matches the specified number of words
if len(words) != num:
    print("Number of words entered does not match the specified number.")
else:
    for word in words:
        word = word.lower()
        if len(word) <= 20:
            # Count the number of vowels in the word
            for char in vowel:
                for chars in word:
                    if char in chars:
                        count += 1
                    else:
                        count += 0

            if count % 2 == 0:
                count = 2
            else:
                count = 1
            total += count
            count = 0
        else:
            print(f"Word '{word}' exceeds 20 characters, which is not allowed.")
            break

    separator = " "  # You can change the separator as needed
    result = separator.join(words)
    print(result)
    print(total)