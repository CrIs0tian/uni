/* Includi le librerie necessarie per il programma
 * nota su cosa servono :
 * stdio.h (standard input output)
 * pthread (librerie per chiamate per creazione, gestione e sincronizzazione dei
 * thread) stdlib.h (librearia standard per funzioni come gestione processi
 * (exit()), e gestione memoria (malloc(), free()) ) unistd.h (include chiamate
 * come fork, pipe)
 *
 */
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// Definisci una costante per il numero di thread da creare
#define NUMBER_OF_THREADS 10

// Funzione che verrà eseguita da ogni thread
void *print_hello_world(void *tid) { // tid= thread id
  // Genera un numero casuale tra 0 e 4 (quanti secondi far dormire il thread)
  int r = rand() % 5;

  // Fa dormire il thread per un numero casuale di secondi
  sleep(r);

  // Stampa un messaggio con l'ID del thread
  printf("Hello World. Greetings from thread %d\n", tid);

  // Termina il thread e restituisce NULL
  pthread_exit(NULL);
}

int main(int arg, char *argv[]) {
  // Dichiarazione di un array di thread
  pthread_t
      threads[NUMBER_OF_THREADS]; // pthread_t indentifica un thread o un'array
                                  // di thread, come in questo caso
  int status, i;

  // Ciclo per creare NUMBER_OF_THREADS thread
  for (i = 0; i < NUMBER_OF_THREADS; i++) {

    // Crea un nuovo thread e assegna la funzione print_hello_world come
    // funzione di avvio, restituisce lo stato del thread
    status = pthread_create(
        &threads[i], NULL, print_hello_world,
        (void *)i); // pthread_Create (crea processo thread), con parametri
                    //(indirizzo thread, attributi thread(puntatore)(in questo
                    //caso nietne attributi) ,
    // funzione di avvio, parametri funzione, (come puntatore a void))

    // Stampa l'ID del thread creato e il suo stato
    printf("Process %d created with status %d\n", i, status);

    // Se ci sono problemi nella creazione del thread, stampa un messaggio di
    // errore e termina il programma
    if (status != 0) {
      printf("Problems while creating process %d\n", i);
      exit(-1);
    }
  }

  // Ciclo per attendere che tutti i thread terminino
  for (i = 0; i < NUMBER_OF_THREADS; i++) {
    status = pthread_join(threads[i],
                          NULL); // dice al processore principale di apsettare
                                 // che il thread finisca il suo lavoro

    // Stampa l'ID del thread che ha terminato e il suo stato
    printf("Process %d terminated with status %d\n", i, status);

    // Se ci sono problemi nell'attesa del thread, stampa un messaggio di errore
    // e termina il programma
    if (status != 0) {
      printf("Problems while waiting for process %d\n", i);
      exit(-1);
    }
  }

  // Termina il programma principale
  return 0;
}
