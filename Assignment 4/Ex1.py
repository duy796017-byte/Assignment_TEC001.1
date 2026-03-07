code = input("Enter code:")
def C(code):
    if len(code) != 6:
        return False
    for i in range(3):
        if not code[i].isalpha() or not code[i].isupper():
            return False
    for i in range(3, 7):
        if not code[i].isdigit():
            return False
    return True
print(C(code))
