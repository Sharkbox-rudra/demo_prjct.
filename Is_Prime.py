def is_prime2():
    n = int(input("Enter a number:"))
    if n == 2 or n == 3:
        return True
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True