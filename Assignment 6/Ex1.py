A = []

while True:
    N = input("Enter a random number (empty to quit): ")
    if N == "":
        break
    while True:
        try:
            B = float(N)
            A.append(B)
            break  
        except ValueError:
            N = input("Invalid input. Please enter a valid number: ")
A.sort(reverse=True)
print(A[:5])