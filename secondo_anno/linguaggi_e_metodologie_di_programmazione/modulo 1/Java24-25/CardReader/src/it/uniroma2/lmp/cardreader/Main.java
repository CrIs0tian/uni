package it.uniroma2.lmp.cardreader;

import it.uniroma2.lmp.cardreader.io.CardReadingException;
import it.uniroma2.lmp.cardreader.model.Attivita;

import static java.lang.System.err;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        AttivitaFactory af = new AttivitaFactory();
        try {
            Attivita at = af.creaAttivita("Negozio.txt");
            System.out.println(at);
        } catch (CardReadingException e) {
            err.println("Problema nella lettura della carta");
            e.printStackTrace(err);
        }

    }
}