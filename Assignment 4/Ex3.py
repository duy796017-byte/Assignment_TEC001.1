import re
text=input("enter text:")
def sum(text):
    N = re.findall(r'[0-9]+', text)
    total = 0
    for num in N:
        total += int(num)
    return total
print(sum(text))
