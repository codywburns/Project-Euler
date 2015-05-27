def sieve(n):
    x = [1] *n
    x[1] = 0
    for i in range(2,n/2):
        j = 2 * long(i)
        while j < n:
                x[j] = 0
                j = j+i
    return x

def prime(x,n):
    i = 1
    j = 1
    while j <= n:
        if x[i] == 1:
            j += 1
        i += 1
    print n
    return i-1
x = sieve(200000) #should be bigger than number of primes(nop), 
nop = 10001  # which prime to return

print prime(x,nop)
