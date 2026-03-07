def word_frequency(text):
    freq = {}

    words = text.split()

    for w in words:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1

    return freq
text = input("Enter text: ")

result = word_frequency(text)

for word in result:
    print(word, result[word])