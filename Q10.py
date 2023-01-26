vowel = 0
consonant = 0
upper = 0
lower = 0
string = input("Enter a string: ")
for i in string:
    if i.isupper():
        upper += 1
    if i.lower():
        lower += 1
    if i in "aeiouAEIOU":
        vowel += 1
    else:
        consonant += 1
print("""Number of upper case letters: {}
Number of lower case letters: {}
Number of vowels: {}
Number of consonants: {}""".format(upper, lower, vowel, consonant))
