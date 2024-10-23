def degraus_magicos(n):    
    degrau_atual = 0
    movimentos = 0  

    while movimentos < 10:
        print(f"Degrau atual: {degrau_atual}")
        k = int(input("Informe o valor de k: "))  

        if degrau_atual % 2 == 0:
            degrau_atual += k
        
        else:
            degrau_atual -= k
        
        if degrau_atual < 0:
            degrau_atual = 0
        
        movimentos += 1
        
        if degrau_atual == n:
            print(f"Você conseguiu alcançar o degrau {n} em {movimentos} movimentos!")
            return

    
    print(f"Você não conseguiu alcançar o degrau {n} em 10 movimentos.")

n = int(input("Informe o núme
