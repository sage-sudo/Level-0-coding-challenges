def grab_vowels(string):
    string_literal = string.lower()
    vowels = "aeiou"

    _vowels = list()
    for character in string_literal:
        if character in vowels:
            _vowels.append(character)

    handle_delimeter = ""
    for vowel in _vowels:
        if vowel not in handle_delimeter:
            handle_delimeter += vowel

    print("Vowels:", ", ".join(handle_delimeter))


grab_vowels("Umuzi")
