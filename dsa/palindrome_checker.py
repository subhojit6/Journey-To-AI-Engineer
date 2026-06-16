word = input("Enter the word to check: ")
reverse = word[::-1]

if word == reverse:
    print(f"{word} is a Palindrome")
else:
    print(f"{word} is not a Palindrome")

# count = 0
# while count < 5:
#     print("hello world")
#     count += 1