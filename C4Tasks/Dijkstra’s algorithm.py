G = {
    'Admiralteystaya' : {'Sadovaya' : 4},
    'Sadovaya' : {'Admiralteystaya' : 4, 'Spasskaya' : 3, 'Sennaya Ploschad' : 4, 'Zvenigorodskaya' : 5},
    'Spasskaya' : {'Sadovaya' : 3, 'Sennaya Ploschad' : 4, 'Dostoyevskaya' : 6},
    'Sennaya Ploschad' : {'Sadovaya' : 4, 'Spasskaya' : 4},
    'Dostoyevskaya' : {'Spasskaya' : 6, 'Vladimirskaya' : 3},
    'Vladimirskaya' : {'Dostoyevskaya' : 3, 'Pushkinskaya' : 4},
    'Pushkinskaya' : {'Vladimirskaya' : 4, 'Zvenigorodskaya' : 3},
    'Zvenigorodskaya' : {'Pushkinskaya' : 3, 'Sadovaya' : 5},
}

D = {k : 100 for k in G.keys()}
start_k = 'Admiralteystaya'    #start
D[start_k] = 0
U = {k : False  for k in G.keys()}
P = {k : None for k in G.keys()}

for _ in range(len(D)):
    min_k = min([k for k in U.keys() if not U[k]], key = lambda x : D[x])

    for v in G[min_k].keys():
        if D[v] > D[min_k] + G[min_k][v]:
            D[v] = min(D[v], D[min_k] + G[min_k][v])
            P[v] = min_k
    U[min_k] = True

print(D)

pointer = 'Vladimirskaya'
while pointer is not None:
        print(pointer)
        pointer = P[pointer]