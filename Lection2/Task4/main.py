#Introduction
print("Hello There, I am simple vowels extractor. Write me your text and I will extract wovels and display them!")

#gets user text
user_text = input("Write your text: ")

# list of vowels
vowels = "AEIOUaeiou"

# Initialize an empty string to store the vowels
user_vowels = []

#look text by character
for character in user_text:

    #finds vowels by comparing 
    if character in vowels: 
        user_vowels.append(character)

# write the extracted vowels
print(user_vowels)

