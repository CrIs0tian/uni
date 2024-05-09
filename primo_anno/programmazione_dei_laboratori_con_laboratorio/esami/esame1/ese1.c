#include <stdio.h>
#include <stdlib.h>

struct int_array {
  int *a;
  int size;
};
typedef struct int_array int_array;

void int_array_cat(int_array *, int_array);
void print_list(int_array *);

int main() {
  int_array a1 = {NULL, 0};
  int_array *a2 = malloc(sizeof(int_array));
  a2->a = malloc(sizeof(int) * 8);
  a2->size = 8;
  a1.a = malloc(sizeof(int) * 8);
  a1.size = 6;
  for (int i = 0; i < 8; i++) {
    a2->a[i] = i;
  }
  for (int i = 0; i < 6; i++) {
    a1.a[i] = i;
  }
  int_array_cat(a2, a1);
  print_list(a2);
}

void int_array_cat(int_array *v0, int_array v1) {
  int n = v0->size;
  v0->size = v0->size + v1.size;
  v0->a = realloc(v0->a, sizeof(int) * v0->size);
  for (int i = 0; i < v1.size; i++) {
    v0->a[n + i] = v1.a[i];
  }
}

void print_list(int_array *a) {
  for (int i = 0; i < a->size; i++) {
    printf("%d ", a->a[i]);
  }
}
