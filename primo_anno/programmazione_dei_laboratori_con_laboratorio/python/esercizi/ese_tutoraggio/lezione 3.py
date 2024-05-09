GRANDEZZA = 8
# controlloCol(q_i, q_j) => boolean
# Parametri:
# - q_i -> Posizione della regina i (è un'array composto da 2 elementi)
# - q_j -> Posizione della regina j (è un'array composto da 2 elementi)
# Output:
# - Restituisce vero se le due regine non sono sulla stessa colonna
# - Restituisce falso altrimenti
def controlloCol(q_i, q_j):
  if q_i[1] == q_j[1]:
    return False
  return True

# controlloRiga(q_i, q_j) => boolean
# Parametri:
# - q_i -> Posizione della regina i (è un'array composto da 2 elementi)
# - q_j -> Posizione della regina j (è un'array composto da 2 elementi)
# Output:
# - Restituisce vero se le due regine non sono sulla stessa riga
# - Restituisce falso altrimenti
def controlloRiga(q_i, q_j):
  if q_i[0] == q_j[0]:
    return False
  return True

# controlloDiag(q_i, q_j) => boolean
# Parametri:
# - q_i -> Posizione della regina i (è un'array composto da 2 elementi)
# - q_j -> Posizione della regina j (è un'array composto da 2 elementi)
# Output:
# - Restituisce vero se le due regine non sono sulla stessa diagonale
# - Restituisce falso altrimenti
def controlloDiag(q_i, q_j):
  k = abs(q_i[0]-q_j[0])
  h = abs(q_i[1]-q_j[1])
  if k == h:
    return False
  return True

# controlloSoluzione(Q) => boolean
# Parametri:
# - Q -> Insieme delle posizioni delle regine 
#        (è una tabella dove ogni riga rappresenta una regina,
#        mentre ogni colonna rappresenta una delle due coordinate)
# Output:
# - Restituisce vero se la soluzione passata è valida
# - Restituisce falso altrimenti
def controlloSoluzione(Q):
  for q_i in Q:
    for q_j in Q:
      if q_i != q_j:
        if not controlloCol(q_i, q_j): return False
        if not controlloRiga(q_i, q_j): return False
        if not controlloDiag(q_i, q_j): return False
  return True

# copiaSoluzione(Q, S)
# Parametri:
# - Q -> Insieme delle posizioni delle regine 
#        (è una tabella dove ogni riga rappresenta una regina,
#        mentre ogni colonna rappresenta una delle due coordinate)
# - S -> Insieme delle soluzioni corrette
#        (è un'array tridimensionale definito così:
#        la prima dimensione definisce la soluzione considerata,
#        la seconda dimensione la regina della soluzione considerata,
#        la terza dimensione le coordinate della regina della soluzione considerata)
# Procedimento:
# - Realizza una copia della soluzione Q in coda ad S
def copiaSoluzione(Q, S):
  S.append([[0, 0] for i in range(GRANDEZZA)])
  i = len(S)-1
  for j, q in enumerate(Q):
    S[i][j][0], S[i][j][1] = q[0], q[1]

# stampa(Q)
# Parametri:
# - Q -> Insieme delle posizioni delle regine 
#        (è una tabella dove ogni riga rappresenta una regina,
#        mentre ogni colonna rappresenta una delle due coordinate)
# Procedimento:
# - Stampa la soluzione Q disegnando la scacchiera
def stampa(Q):
  C = [[" " for i in range(GRANDEZZA)] for j in range(GRANDEZZA)]
  i = 0
  for q in Q:
    C[q[0]][q[1]] = "Q"
  for j in range(GRANDEZZA*2+1):
    if j % 2 == 0:
      for k in range(GRANDEZZA):
        print("+-", end = '')
      print("+")
    else:
      for k in range(GRANDEZZA):
        print(f"|{C[i][k]}", end = '')
      print("|")
      i += 1