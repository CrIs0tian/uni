/* Esercizio 1 Si scriva una funzione C avente il seguente prototipo:
 *
 * char *cat(char *a, char *b);
 *
 * La funzione restituisce una nuova stringa definita dalla concatenazione delle
 * due stringhe in input.
 *
 * Esercizio 2 Si scriva una funzione avente il seguente prototipo:
 *
 * sequenza trova_vocali(char *a)
 *
 * La funzione ritorna una sequenza a valori interi (vedere lezioni 27, 28 e 29)
 * contenente le posizioni di a in cui sono contenute le vocali.
 */
#include <stdio.h>
#include <stdlib.h>
struct seq {
  int *a;
  int n;
  int c;
};
typedef struct seq seq;
char *cat(char *, char *);
seq trova_vocali(char *);
seq new_seq(void);
seq seq_append(seq, int);
void print_seq_vocali(seq);
int len(char *a);
char change_case(char);

int main() {
  char a[] = "di";
  char b[] = "cane";
  char *c = cat(a, b);
  printf("%s\n", c);
  seq s = trova_vocali(c);
  print_seq_vocali(s);
}

seq new_seq(void) {
  seq v = {NULL, 0, 0};
  return v;
}
seq seq_append(seq s, int e) {
  int i, dim = s.n;
  if (s.n == s.c) {
    s.c = s.c * 2 + 1;
    s.a = realloc(s.a, sizeof(int) * s.c);
  }
  s.a[dim] = e;
  s.n++;
  return s;
}

void print_seq_vocali(seq s) {
  int i;
  for (i = 0; i < s.n; i++) {
    printf("%d\n", s.a[i]);
  }
}
int len(char *a) {
  int i, len = 0;
  for (i = 0; a[i] != '\0'; i++) {
    len++;
  }
  return len;
}

char *cat(char *a, char *b) {
  int len_a = len(a), len_b = (len(b));
  char *c = malloc((sizeof(char) * (len_a + len_b)) + 1);
  int i, len_c = sizeof(c);
  for (i = 0; a[i] != '\0'; i++) {
    c[i] = a[i];
  }
  for (i = 0; b[i] != '\0'; i++) {
    c[i + len_a] = b[i];
  }
  c[len_c] = '\0';
  return c;
}
seq trova_vocali(char *a) {
  seq s = new_seq();
  int i, len_a = len(a);
  for (i = 0; i < len_a; i++) {
    a[i] = change_case(a[i]);
  }
  for (i = 0; i < len_a; i++) {
    if (a[i] == 'a' || a[i] == 'e' || a[i] == 'i' || a[i] == 'o' ||
        a[i] == 'u') {
      s = seq_append(s, i + 1);
    }
  }
  return s;
}

char change_case(char c) {
  /*
   * se c e' maiuscolo ritorna il minuscolo e viceversa
   * se c non e' una lettera ritorna c
   * */

  if (c >= 'A' && c <= 'Z') {
    return 'a' + c - 'A';
  }
  return c;
}
