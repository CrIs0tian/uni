"""
Esercizi per casa

Dati 3 segmenti adiacenti ed n float si vuole calcolare quanti degli n float
ricadono in ogni segmento. I segmenti sono rappresentati da 2 float h0 e h1
che definiscono i segmenti: (-∞, h0), [h0, h1), [h1, ∞).
Si progetti una funzione che prenda in input la descrizione
di 3 segmenti (h0 e h1) e un numero variabile di float e restituisca
una terna di interi che rappresenta il numero di float che ricade in ciascuno dei 3 segmenti.

Ad esempio se l'input della funzione fosse -7, 5, 3, 10, -4, 5, -12, 6, 0,
i segmenti sono: i numeri minori di -7; i numeri compresi tra -7 e 5 (escluso);
i numeri maggiori-uguali a 5. I valori -12 e -4 fanno parte del primo segmento;
3 e 0 fanno parte del secondo segmento; 10, 5 e 6 fanno parte del terzo segmento.
Quindi la funzione dovrebbe restituire la terna: 1, 3, 3
"""


def hist(h0, h1, *numbers):
    sol1, sol2, sol3 = 0, 0, 0
    for i in numbers:
        if i < h0:
            sol1 += 1
        elif i >= h1:
            sol3 += 1
        else:
            sol2 += 1
    return (sol1, sol2, sol3)


sol1, sol2, sol3 = hist(-7, 5, 3, 10, -4, 5, -12, 6, 0)
print(sol1, ",", sol2, ",", sol3)
