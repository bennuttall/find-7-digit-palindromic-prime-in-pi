def isprime(n):
    n *= 1.0
    if n %2 == 0 and n != 2 or n % 3 == 0 and n != 3:
        return False
    for b in range(1, int((n ** 0.5 + 1) / 6.0 + 1)):
        if n % (6 * b - 1) == 0:
            return False
        if n % (6 * b + 1) == 0:
           return False
    return True

def main():
    f = open('pi.txt', 'r')
    d = f.readline(7)
    
    while True:
        n = f.readline(1)
        if len(n):
            d = d[1:7] + n
            if d == d[::-1]:
                if isprime(int(d)):
                    print d
                    break  # remove this break to see more solutions
        else:
            break

if __name__ == '__main__':
    main()
