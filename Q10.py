vowel = 0
consonant = 0
upper = 0
lower = 0
letter = 0
string = input("Enter a string: ")
for i in string:
    if not i.isspace():
        letter += 1
    if i.isupper():
        upper += 1
    if i.islower():
        lower += 1
    if i in "aeiouAEIOU":
        vowel += 1
    if i.isalpha() and i not in "aeiouAEIOU":
        consonant += 1
print("""Number of letters: {}
Number of upper case letters: {}
Number of lower case letters: {}
Number of vowels: {}
Number of consonants: {}""".format(letter, upper, lower, vowel, consonant))
