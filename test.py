def create_prime(prime, n, total):
    gab = 2
    for i in range(7, n, gab):
        count = 1
        gab = 6-gab
        for j in range(0, i):
            if i%prime[j] == 0:
                count = 0
                break
        if count:
            prime[total] = i
            total+=1
    return prime

prime = [2,3,5]
n=100
total = 3
create_prime(prime,n,total)