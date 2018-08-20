#Nim Game to coursera's python course for Lennon

def computador_escolhe_jogada(a, b):
    n, m = a, b
    if n <= m:
        ret = n
    else:
        ret = n-(m+1)
        while True:
            x = n-ret
            if (ret <= m) and ((x % (m + 1)) == 0):
                break
            ret -= 1
            if ret == 0:
                 ret = m
                 break

    if ret == 1:
        print("O computador tirou uma peça!")
    else:
        print("O computador tirou "+str(ret)+" peças!")
    return ret

def usuario_escolhe_jogada(a, b):
    n, m = a, b
    while 1:
        c = int(input("Quantas peças você vai tirar? "))
        if 0 < c <= m and 0 < c <= n:
            ret = c
            break
        else:
            print("\nOops! Jogada inválida! Tente de novo.\n")

    if ret == 1:
        print("\nVocê tirou uma peça.")
    else:
        print("\nVocê tirou "+str(ret)+" peças.")

    return ret



def partida():
    value_cpu, value_usr = False, False
    i, j = -1, -1
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if ((n % (m + 1)) == 0):
        print("\nVocê começa!\n")
        test = True
    else:
        print("\nComputador começa!\n")
        test = False
    while True:
        if test:
            i = usuario_escolhe_jogada(n, m)
            n -= i
            value_usr = True
            if n != 0:
                value_usr = False
                if n == 1:
                    print("Agora resta uma peça no tabuleiro!\n")
                else:
                    print("Agora restam "+str(n)+" peças no tabuleiro!\n")

            test = False
        else:
            j = computador_escolhe_jogada(n, m)
            n -= j
            value_cpu = True
            if n != 0:
                value_cpu = False
                if n == 1:
                    print("Agora resta uma peça no tabuleiro!\n")
                else:
                    print("Agora restam "+str(n)+" peças no tabuleiro\n")

            test = True

        if value_usr:
            print("Fim de jogo! Você ganhou!")
            break
        elif value_cpu:
            print("Fim de jogo! O computador ganhou!")
            break

    return value_usr, value_cpu


def campeonato():
    i = 1
    j, k = 0, 0
    while i<4:
        print("\n**** Rodada "+str(i)+" ****\n")
        a, b = partida()
        if a:
            j+=1
        elif b:
            k+=1

        i+=1
    print("\n**** Fim do campeonato! ****\n")
    print("Você "+str(j)+" X "+str(k)+" Computador")

if __name__ == "__main__":
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print()
    a = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))

    if a == 1:
        j, k = partida()
    elif a == 2:
        print("\nVocê escolheu um campeonato!")
        campeonato()
