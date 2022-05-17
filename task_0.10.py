def grab_common_chars(string1, string2):
    string1 = str(string1).lower()
    string2 = str(string).lower()
    common_characters = list()

    for string in string2:
        if string in string1 and string not in common_characters:
            common_characters.append(string)

    print("Common letters:", ", ".join(common_characters))


grab_common_chars("house", "computers")
