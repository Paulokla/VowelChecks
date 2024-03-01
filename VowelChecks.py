vowel = ["vowels:"]
consonant = ["consonants:"]
user = input("enter name: ")
for i in user:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vowel.append(i)
        res = vowel.count(i)
        print(res)
    else:
        consonant.append(i)


print(vowel)
print(consonant)
