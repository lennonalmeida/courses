a = str(input("Digite um numero inteiro: "))
s = len(a)
i = 0
plus = 0 
while i < s:
	j = 1+i
	plus += int(a[i:j])
	i+=1
print(plus)
