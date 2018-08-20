b = int(input("digite a largura: "))
a = int(input("digite a altura: "))

i, j = 0, 0

while i < a:
    while j < b:
        print("#", end = "")
        j+=1
    print()
    j = 0
    i+=1