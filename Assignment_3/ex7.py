def acronym(phrase):
    words = phrase.split()
    result = ""

    for word in words:
        result = result + word[0].upper()

    return result
text = input("Enter a phrase: ")
print(acronym(text))
