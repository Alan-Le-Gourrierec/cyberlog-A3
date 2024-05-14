package sdd_tp2c_annuaire;

import java.io.BufferedReader;
import java.io.EOFException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.RandomAccessFile;

public class Annuaire {

	static String ligne;
	static int curseur;
	static int module = 23;
	static int mul = 65536;

	static RandomAccessFile lecteurFichier(String chemin_fichier) throws IOException {
		ligne = "";
		curseur = 0;
		return new RandomAccessFile(chemin_fichier, "r");
	}

	static String lireMot(RandomAccessFile lecteur) throws IOException {
		String mot;
		int i;
		while ((curseur < ligne.length()) && ((ligne.charAt(curseur) == ' ')
				|| (ligne.charAt(curseur) == '\t')))
			curseur++;
		if (curseur == ligne.length()) {
			ligne = lecteur.readLine();
			curseur = 0;
		}
		if (ligne != null) {
			for (i = curseur; (i < ligne.length()) && (ligne.charAt(i) != ' ')
					&& (ligne.charAt(i) != '\t'); i++)
				;
			mot = ligne.substring(curseur, i);
			curseur = i;
			return mot;
		} else
			throw new EOFException();
	}

	static void afficheStringListe(StringListe liste) {
		while (liste.suivant == null) {
			System.out.println(liste.contenu1 + "  " + liste.contenu2);
			liste = liste.suivant;
		}
	}

	static String saisieMot() throws IOException {
		BufferedReader lecteur = new BufferedReader(new InputStreamReader(System.in));
		return lecteur.readLine();
	}

	static int hash(String mot) {
		int hash = 0;

		for (int i = 0; i < mot.length(); i++) {
			hash = (hash + (int) Math.pow(mul, i) * mot.charAt(i)) % module;
		}
		return Math.abs(hash);
	}

	static void insere(String mot, String val, StringListe[] hash_tb) {
		int pos = hash(mot);

		if (hash_tb[pos] != null) {
			hash_tb[pos] = new StringListe(mot, val, hash_tb[0]);
		} else {
			hash_tb[pos] = new StringListe(mot, val, null);
		}

	}

	static String recherche(String mot, StringListe[] hash_tb) {
		int pos = hash(mot);

		StringListe individu = hash_tb[pos];
		while (!individu.contenu1.equals(mot)) {
			if (individu.suivant == null) {
				return null;
			} else {

				individu = individu.suivant;
			}
		}
		return individu.contenu2;
	}

	static void afficheHashTb(StringListe[] hash_tb) {
		int size = hash_tb.length;
		for (int i = 0; i < size; i++) {
			afficheStringListe(hash_tb[i]);
		}
	}

	public static void main(String[] argv) throws IOException {
		StringListe[] hash_tb = new StringListe[23];
		RandomAccessFile lecteur;
		int h;
		String mot, val;
		boolean encore;
		for (h = 0; h < 23; h++)
			hash_tb[h] = null;
		lecteur = lecteurFichier(argv[0]);
		try {
			while (true) {
				mot = lireMot(lecteur);
				val = lireMot(lecteur);
				insere(mot, val, hash_tb);
			}
		} catch (EOFException e) {
		}
		afficheHashTb(hash_tb);
		System.out.println("(Taper q pour finir)");
		for (encore = true; encore;) {
			System.out.print("Rechercher ");
			mot = saisieMot();
			if (mot.equals("q"))
				encore = false;
			else {
				val = recherche(mot, hash_tb);
				if (val != null)
					System.out.println(mot + " " + val);
				else
					System.out.println(mot + " non trouve");
			}
		}
	}
}