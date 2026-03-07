def middle_characters(s):
    length = len(s)
    mid = length // 2

    if length % 2 == 0:
        return s[mid - 1:mid + 1]
    else:
        return s[mid]
text=str(input("Enter a string:"))
result = middle_characters(text)
print(result)