n = int(input("Nhập số nguyên: "))
if n < 2:
    print("Không phải số nguyên tố")
else:
    prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            prime = False
            break
    if prime:
        print("Số nguyên tố")
    else:
        print("Không phải số nguyên tố")