HF = input("Enter color code:")
def hexadecimal(HF):
    if len(HF)!= 7:
        return False
    for i in range(1):
        if not HF[i]=="#":
            return False
    for i in range(1, 8):
        if HF[i] not in "0123456789ABCDEFabcdef":
            return False
    return True
print(hexadecimal(HF))
