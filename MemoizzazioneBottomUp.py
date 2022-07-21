def es(n, k):
    if n <= 0 or k < 0:  # vincoli
        return 0
    if n == 1:
        return 1

    T = [[[[-1 for _ in range(2)]  # inizializzazione della matrice
           for _ in range(k+1)]
          for _ in range(n)]
         for _ in range(n)]

    # casi base
    for i in range(n):
        for j in range(n):
            for d in range(2):
                T[i][j][0][d] = 0  # se il numero di svolte è 0 i percorsi sono 0

    for t in range(k+1):
        for d in range(2):
            T[0][0][t][d] = 1       # il numero di svolte per la prima cella è 1

    for i in range(n):
        for t in range(k+1):
            for d in range(2):
                if d == 0:
                    T[0][i][t][0] = 1       # prima riga se direzione orizzontale
                else:
                    T[i][0][t][1] = 1       # prima colonna se direzione verticale

    # calcolo
    for i in range(n):
        for j in range(n):
            for t in range(1, k+1):
                for d in range(2):
                    # se ho già calcolato la cella
                    if T[i][j][t][d] != -1:
                        continue
                    north = 0       # utilizzo una variabile per considerare i casi in cui andrei fuori dalla matrice
                    west = 0
                    if d == 0:      # se direzione orizzontale
                        if i >= 1:  # se non sto calcolando una cella nella prima riga
                            north = T[i-1][j][t-1][1]
                        if j >= 1:  # se non sto calcolando una cella nella prima colonna
                            west = T[i][j-1][t][0]
                    else:			# se direzione verticale
                        if i >= 1:  # se non sto calcolando una cella nella prima riga
                            north = T[i-1][j][t][1]
                        if j >= 1:  # se non sto calcolando una cella nella prima colonna
                            west = T[i][j-1][t-1][0]
                    T[i][j][t][d] = north + west

    for i in range(n):
        for j in range(n):
            print(T[i][j], end='\n' if j == n-1 else '\t')

    return T[n-2][n-1][k][1] + T[n-1][n-2][k][0]


tests = [(0, 0), (0, 1), (1, 0), (4, 2), (4, 3), (5, 2), (1000, 400)]

print("n\t|k\t|paths")
for el in tests:
    n = el[0]
    k = el[1]
    result = es(n, k)
    print("{}\t| {}\t| {}".format(n, k, result))
