def grab_vowels(string):
    string_literal = string.lower()
    VOWELS = "aeiou"

    vowels = list()
    for character in string_literal:
        if character in VOWELS:
            vowels.append(character)

    handleDelimeter = ""
    for vowel in vowels:
        if vowel not in handleDelimeter:
            handleDelimeter += vowel

    print("Vowels:", ", ".join(handleDelimeter))


grab_vowels("Umuzi")