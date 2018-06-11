import math
def isPrimo(n):
	ret = False
	i = 3
	primo = 2
	MAX = math.ceil(n/2)
	while i<MAX:
		if n%i == 0:
			primo+=1
			if  primo > 2:
				i = MAX
		i+=2
	if primo == 2:
		ret = True
	return ret

def maior_primo(n):
	ret = 1
	if n%2 == 0:
		n-=1
	while n>0:
		if isPrimo(n):
			ret = n
			n = 0
		n-=2
	return ret

#main code
a = int(input())
print(maior_primo(a))
