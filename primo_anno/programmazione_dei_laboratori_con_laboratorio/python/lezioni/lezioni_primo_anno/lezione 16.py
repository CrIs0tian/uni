"""
soluzione dell'esercizio 16
"""


def find_in_file(filename, k):
    # costo computazionale
    f = open(filename)  # O(1) ovvero costo costante
    lines = ()  # O(1)
    r = 1  # riga corrente
    for line in f:  # eseguito O(n)
        if k in line:  # se len(line) é O(1), O(1) operzione costante
            lines += (
                r,
            )  # per concatenare da tupla a tupla, e il suo costo computazionale è O(len(lines)+1),  caso peggiore=O(n^2)
        r += 1
    f.close()
    return lines


t = find_in_file("lezione 17.py", "lines")
print(t)


# COSTO COMPUTAZIONALE
# nel caso peggiore , n in ogni riga, il costo è O(n^2)

# come si può migliorare ?


# In[]
# invece di usare una tupla potremmo utilizzare una lista cosi possiamo usare l'append
def find_in_file2(filename, k):
    # costo computazionale
    f = open(filename)  # O(1) ovvero costo costante
    lines = []  # O(1)
    r = 1  # riga corrente
    for line in f:  # eseguito O(n)
        if (
            k in line
        ):  # se len(line) é O(1), ricerca lineare nel caso peggiore, ma len(line) = O(1), quindi operzione costante
            lines.append(r)  # O(1)
        r += 1
    f.close()  # O(1)
    return tuple(
        lines
    )  # cosi rispettiamo le regole dell'output, ma a costo O(n) (la conversione costa)


t = find_in_file("lezione 17.py", "lines")
print(t)
# COSTO COMPUTAZIONALE
# nel caso peggiore, k in ogni riga, il costo è O(n)

# se len(line) è O(m)
# if k in line: se len(line)è O(m), O(m) operazioni (poichè è una ricerca
# lineare ma prima era fatto O(1) ora però è O(m) nel caso peggiore)

# nel caso peggiore il for richiede O(nm) operazioni

# il costo della funzione è O(nm)


# In[]
# esercizio 16 con (r0,c0)def find_in_file(filename,k):
def find_in_file(filename, k):
    # costo computazionale
    f = open(filename)  # O(1) ovvero costo costante
    lines = []  # O(1)
    r = 1  # riga corrente
    for line in f:  # eseguito O(n)
        for c in range(len(line) - len(k) + 1):  # costa O(len(line)-len(k)) sempre
            if (
                k == line[c : c + len(k)]
            ):  # len(line)-len(k)[uguale a c]+len(k) ultimo punto che ci può controllare
                lines.append((r, c))  # O(1)
        r += 1
    f.close()  # O(1)
    return tuple(lines)  # cosi rispettiamo le regole dell'output, ma a costo O(n)


t = find_in_file("lezione 17.py", "lines")
print(t)


# In[]
def bin_search(k, bins):
    """
    sia n-1 la lunghezza di bins, ritorna 0 se k < bins[0],
    n-1 se k>= bin[n-2], i se bins[i-1]<= k > bin[i]
    """
    n = len(bins) + 1  # numero di segmento
    if k < bins[0]:
        return 0
    if k >= bins[n - 2]:
        return n - 1
    lx, rx = 0, n
    trovato = False
    while not trovato:
        cx = (lx + rx) // 2
        # cx è il segmento mediano tra lx e rx
        if k >= bins[cx - 1] and k < bins[cx]:
            trovato = True
        elif k < bins[cx - 1]:
            # a sx del segmento cx
            rx = cx - 1
        else:
            lx = cx + 1
    return cx


print(bin_search(25, [6, 8, 12, 23]))
# %%
