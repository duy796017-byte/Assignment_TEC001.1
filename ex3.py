M=None
m=None
while True:
    a=input("enter numbers:")
    if a=="":
        break
    a=float(a)
    if M is None or M < a :
        M=a
    if m is None or a < M:
        m=a
print("largest number:", M)
print("smallest number:", m)