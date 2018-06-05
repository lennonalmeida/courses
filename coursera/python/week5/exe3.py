def vogal(l):
	vogais = ['a', 'e', 'i', 'o', 'u']
	if l in vogais:
		a = True
	else:
		a = False
	return a
aa = str(input())
print(vogal(aa))
