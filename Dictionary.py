import json
from difflib import get_close_matches

x = "y"
while x == "y":
    data = json.load(open("data.json"))

    def translate(word):
        word = word.lower()
        if word in data:
            return data[word]

        elif word.title() in data:
            return data[word.title()]

        elif word.upper() in data:
            return data[word.upper()]

        elif len(get_close_matches(word, data.key())) > 0:
            print("Did you mean %s instead \n" %get_close_matches(word, data.keys())[0] )
            decide = input("Press y for Yes and n for No")
            if decide == "y":
                return data[get_close_matches(word, data.key())[0]]
            elif decide == "n":
                return("You have entered a wrong word. Please check it again.\n")
            else:
                return("You have entered a wrong input. Please press y or n.\n")

        else:
            print("You have entered a wrong word. Please check it again.\n")

    word = input("Enter the word you want to search\n")

    output = translate(word)

    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)

    print(output)

x = input("\n\n\n\nPress y to search again")
