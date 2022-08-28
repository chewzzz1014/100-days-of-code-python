def check_prime(n):
    is_prime = True

    if n==0 or n==1:
        is_prime = False
    else:
        for i in range(2, int(n/2)):
            if n%i == 0:
                is_prime = False
                break
    if is_prime:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")


check_prime(175)