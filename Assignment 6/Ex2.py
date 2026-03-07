S = ["winter", "spring", "summer", "autumn"]

M = int(input("enter number of month (1-12): "))

if M == 12 or M == 1 or M == 2:
    print(S[0])
elif M == 3 or M == 4 or M == 5:
    print(S[1])
elif M == 6 or M == 7 or M == 8:
    print(S[2])
elif M == 9 or M == 10 or M == 11:
    print(S[3])
else:
    print("invalid value")