d = dict(weather = "clima", earth = "terra", rain = "chuva")

def vocabulary(word):
    #return d.get(word, "We couldn't find that word!")

    try:
        return d[word]
    except KeyError:
        return "That word does not exist."


word = input("Enter word: ")
print(vocabulary(word))