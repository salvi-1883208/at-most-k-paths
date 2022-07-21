
def conta(i, j, t, d):
    if i < 0 or j < 0:              # n <= 0
        return 0

    if T[i][j][t] != -1:            # in caso abbia già calcolato la cella
        return T[i][j][t]

    if i == 0 and j == 0:           # in caso sia la prima cella
        T[i][j][t] = 1

    elif d == 0 and i == 0:         # se direzione orizzontale e prima riga
        T[i][j][t] = 1
    elif d == 1 and j == 0:         # se direzione verticale e prima colonna
        T[i][j][t] = 1
    elif t == 0:                    # zero svolte e non prima riga o prima colonna
        T[i][j][t] = 0

    elif d == 0:                    # se direzione orizzontale
        # sommo la cella di sinistra con qella di sopra con una svolta in meno e direzione diversa
        T[i][j][t] = conta(i, j - 1, t, 0) + conta(i - 1, j, t - 1, 1)

    elif d == 1:                    # se direzione verticale
        # sommo la cella di sopra con qella di sinistra con una svolta in meno e direzione diversa
        T[i][j][t] = conta(i - 1, j, t, 1) + conta(i, j - 1, t - 1, 0)
    return T[i][j][t]


def es(n, k):
    if n == 0:
        return 1
    return conta(n - 1, n, k, 1) * 2


tests = [(0, 0), (0, 1), (1, 0), (4, 2), (4, 3), (5, 2), (1000, 103)]

print("n\t|k\t|paths")
for el in tests:
    n = el[0]
    k = el[1]
    T = [[[-1 for _ in range(k+1)]
          for _ in range(n)]
         for _ in range(n)]
    result = es(n-1, k)
    print("{}\t| {}\t| {}".format(n, k, result))
