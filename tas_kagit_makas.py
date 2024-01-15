import itertools
num = int(i) if (i:=input('kacta bitsin? (default: 3)')) else 1

score_comp = 0
score_secim = 0
while num != score_comp or num != score_secim:
 
    import random
    oyun = ['tas', 'kagit', 'makas', 'spock', 'lizard']
    
    secim = input('tas, kagit, makas, spock, lizard ?')
    secim = oyun.index(secim)

    comp = random.randint(0,4)
    winner = (comp-secim)%5
    
    if winner == 0:
        print(f"Berabere. Senin secimin: {oyun[secim]}, Bilgisayarin secimi: {oyun[comp]}")
    elif winner == 1 or winner == 3:
        print(f"Bilgisayar kazandi.Senin secimin: {oyun[secim]}, Bilgisayarin secimi: {oyun[comp]}")
        score_comp += 1
    else:
        print(f"Sen kazandin.Senin secimin: {oyun[secim]}, Bilgisayarin secimi: {oyun[comp]}")
        score_secim += 1

if score_secim == num:
    print(f"""  Sen: {score_secim}
            Bilgisayar:{score_comp}
            Sen kazandin.""")
elif score_comp == num:
    print(f"""  Sen: {score_secim}
        Bilgisayar:{score_comp}
        Bilgisayar kazandi.""")
