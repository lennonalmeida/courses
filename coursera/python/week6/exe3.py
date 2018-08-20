def vogal(l):
	vogais = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
	if l in vogais:
		a = True
	else:
		a = False
	return a
aa = str(input())
print(vogal(aa))
