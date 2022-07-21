
def conta(i, j, t, d):

    if i < 0 or j < 0 or t < 0:     # n <= 0
        return 0

    if i == 0 and j == 0:           # in caso sia la prima cella
        return 1

    if d == 0 and i == 0:           # se direzione orizzontale e prima riga
        return 1
    if d == 1 and j == 0:           # se direzione verticale e prima colonna
        return 1
    if t == 0:                      # zero svolte e non prima riga o prima colonna
        return 0

    if d == 0:                      # se direzione orizzontale
        # sommo la cella di sinistra con qella di sopra con una svolta in meno e direzione diversa
        return conta(i, j - 1, t, 0) + conta(i - 1, j, t - 1, 1)

    # se direzione verticale
    # sommo la cella di sopra con qella di sinistra con una svolta in meno e direzione diversa
    return conta(i - 1, j, t, 1) + conta(i, j - 1, t - 1, 0)


def es(n, k):
    if n == 0:
        return 1
    return conta(n - 1, n, k, 1) + conta(n, n - 1, k, 0)


tests = [(0, 0), (0, 1), (1, 0), (4, 2), (4, 3), (5, 2), (5, 4)]
print("n\t| k\t|paths\t")
for el in tests:
    n = el[0]
    k = el[1]
    result = es(n-1, k)
    print("{}\t| {}\t| {}".format(n, k, result))
