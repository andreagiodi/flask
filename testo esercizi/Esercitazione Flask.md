1. Realizzare un server web che come home page presenti tre immagini della stessa dimensione una di fianco all'altra. La prima immagine deve avere a che fare con le previsioni del tempo, la seconda deve contenere un libro e la terza deve contenere un calendario. Utilizzare un file css per definire la grafica della pagina.


2. modificare il server precedente per far sì che quando l'utente clicca sulla prima immagine vengano fornite le previsioni del tempo. Visto che, comunque, le previsioni dei vari servizi metereologici sono sempre sbagliate, il nostro server genera un numero casuale compreso tra 0 e 8: se il numero è minore di 2 la previsione è "pioggia", se è compreso tra 3 e 5 la previsione è "nuvoloso", se è maggiore di 5 la previsione è "sole". Abbinare ad ogni previsione un'immagine adatta. Utilizzare un css per definire la grafica. La route per accedere al serizio deve essere /meteo

3. modificare il server precedente per far sì chhe quando l'utente clicca sulla seconda immagine il server web risponde con una frase celebre, scelta casualmente da un elenco di 10 frasi (per ispirazione  https://www.frasimania.it/frasi-corte/). Utilizzare una struttura dati adatta per contenere le frasi e gli autori Il sito deve visualizzare la frase con una certa grafica (a scelta) e anche l'autore (da visualizzare con una grafica diversa). Utilizzare un file css per definire la grafica della pagina. .La route per accedere al serizio deve essere /frasicelebri


4. modificare il server precedente per far sì che quando l'utente clicca sulla terza immagine venga visualizzato il numero di giorni che mancano alla fine della scuola. Utilizzare un file css per definire la grafica della pagina. La route per accedere al serizio deve essere /quantomanca


#Riferimento a appes.py