package it.uniroma2.lmp.cardreader;

import java.io.File;
import java.util.Map;

import it.uniroma2.lmp.cardreader.io.CardReader;
import it.uniroma2.lmp.cardreader.io.CardReadingException;
import it.uniroma2.lmp.cardreader.model.Attivita;
import it.uniroma2.lmp.cardreader.model.Negozio;
import it.uniroma2.lmp.cardreader.model.Ristorante;

public class AttivitaFactory {

	public static final String FILETYPE = "filetype";
	public static final String PARTITA_IVA = "partita_IVA";
	public static final String SEDE = "sede";
	public static final String MERCE_VENDUTA = "merce_venduta";
	public static final String IN_ATTIVITA_DAL = "in_attività_dal";
	public static final String CATEGORIA = "categoria";
	public static final String SCOPO = "scopo";


	public Attivita creaAttivita(File card) throws CardReadingException {
		//Nota: facciamo gestire l'eccezione a CardReadingException
		
		Map<String, String> map = CardReader.readCard(card);

		String fileType = map.get(FILETYPE);
		if (fileType == null){
			throw new CardReadingException("fileType non trovato");
		}
		switch (fileType){
			case "negozio":
				return new Negozio(processInizioAttiva(map.get(IN_ATTIVITA_DAL)), checkNotNull(map.get(SEDE), SEDE), checkNotNull(map.get(PARTITA_IVA), PARTITA_IVA), checkNotNull(map.get(MERCE_VENDUTA), MERCE_VENDUTA) );

			case "ristorante":
				return null;

			case "associazione":
				return null;


			default:
				throw new CardReadingException("Il tipo attività: " + fileType + " non è riconosciuto");
		}

	}

	public Attivita creaAttivita(String cardPath) throws CardReadingException{
			return creaAttivita(new File(cardPath));
	}

	private String checkNotNull(String value, String prop) throws CardReadingException {
		if (value == null){
			throw new CardReadingException("valore per: " + prop + " assente");
		}
		return value;
	}

	private Ristorante.Categoria processCategoria(String value) throws CardReadingException {
		checkNotNull(value, CATEGORIA);
		return Ristorante.Categoria.valueOf(value);

	}

	private int processInizioAttiva(String value) throws CardReadingException {
		checkNotNull(value, IN_ATTIVITA_DAL);
		return Integer.parseInt(value);

	}

}
