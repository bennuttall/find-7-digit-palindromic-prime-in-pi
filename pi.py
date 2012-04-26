def isprime(n):
    n*=1.0
    if n%2==0 and n!=2 or n%3==0 and n!=3:
        return False
    for b in range(1,int((n**0.5+1)/6.0+1)):
        if n%(6*b-1)==0:
            return False
        if n %(6*b+1)==0:
           return False
    return True

f = open('pi.txt','r')

d = f.readline(7)

while 1:
	n = f.readline(1)
	if len(n):
		d = d[1:7] + n
		if d == d[::-1]:
			if isprime(int(d)):
				print d
	else:
		break