# memory
university abm project

italian description
# Progetto di econofisica: Effetti della memoria nel *news spreading*
## Roberto Bertilone, Francesco Fanchin, Nicola Sella
In una rete reale ci chiediamo se la memoria di notizie lette possa influenzare la dinamica ed
eventualmente creare effetti di segregazione. Per modellizzare questo fenomeno di diffusione
implementiamo una rete assegnando comportamenti microscopici per cercare fenomeni
macroscopici emergenti.
I nodi della rete sono costituiti da due tipi di agenti: le fonti e gli utenti.
Le fonti sono il bacino da cui gli utenti possono attingere notizie ed eventualmente diffonderle.
Gli utenti possono diffondere notizie in base a una loro intenzione: sanno crearsi una opinione delle
notizie che leggono e degli utenti primi vicini; inoltre “hanno una memoria” cioè possono ricordare
un certo numero di notizie che hanno visualizzato in precedenza.
I link rappresentano la sola possibilità di instaurare una comunicazione tra due agenti.
In questo progetto intendiamo studiare la lunghezza della memoria degli agenti tramite l’analisi di
misure statistiche della rete.

Inizialmente implementeremo una rete scale free con link indiretti e pesati. La struttura scale free
rappresenta la miglior approssimazione di rete reale essendo la sua distribuzione di grado descritta
da una legge di potenza: dunque costituisce una valida ipotesi iniziale. La tipologia di link scelta
evidenzia la bilateralità e l’intensità della comunicazione tra gli agenti. Prendendo come esempio
uno scambio di informazione tra due persone oppure tra una persona e un giornale, il peso
rappresenta il feeling, l’affiatamento pregresso; un segno posto davanti ad esso ne potrebbe
specificare l’entità (buono, indifferente, cattivo).
Nel corso della dinamica i link possono essere creati o distrutti dagli agenti e il loro peso può
cambiare a seguito di interazioni.
Come detto in precedenza, le fonti sono agenti che per loro natura non ricevono notizie: per
economia di programmazione il link che le collega ad un agente resta comunque indiretto anche se
le notizie sono solo in uscita.
Le notizie sono descritte da vari parametri tra cui un vettore di “topics”: ogni componente di esso è
un valore numerico che rappresenta la percentuale di pertinenza a quel topic all’interno della
notizia.
Ogni fonte è focalizzata, in misura variabile, sugli stessi argomenti. La notizia contiene inoltre
l’identificativo della fonte che l’ha diffusa ed un fattore che ne rappresenta l’importanza. Si terrà
traccia di altri metadati come ad esempio la data di pubblicazione.
Il tempo è scandito dall’observer. Ogni fonte genererà nuove notizie tenendo conto lei stessa del
tempo che passa.
Le notizie al primo ciclo sono diffuse dalle fonti, successivamente lo spread è fra fonti e utenti e fra
utenti e utenti.
L’utente avrà inoltre un tempo di attivazione che sarà regolato attraverso un suo orologio interno
tenendo conto del tempo che scorre nel mondo: solo mentre è attivo sarà possibile per lui interagire
con il sistema. 
Gli utenti hanno uno stato mentale che viene inizializzato al primo ciclo temporale. Questo stato
rappresenta la personalità dell’utente, i suoi interessi e veicola le sue scelte.
Una apposita funzione “distanza” permette di confrontare una notizia con lo stato mentale del
singolo utente; in esso è contenuto un vettore avente come dimensione il numero di topics. Lo stato
contiene inoltre altri parametri che caratterizzano con maggiore specificità il singolo utente, ad
esempio la sua propensione a leggere e diffondere notizie.

La dinamica del sistema sarà determinata dalle azioni degli utenti; i parametri sopra descritti
influenzeranno le loro decisioni.
Intendiamo indagare come la variazione nella lunghezza della memoria possa influenzare le
decisioni degli agenti procedendo con analisi sistematiche, ad esempio, sui tempi di diffusione.
Effettueremo diverse simulazioni a varie lunghezze, fissando le condizioni iniziali (seed) ottenendo
una statistica sufficiente. Eventuali altre variazioni saranno apportate in corso d’opera.

Ci aspettiamo di osservare correlazioni tra la lunghezza della memoria e variazioni macroscopiche
del sistema. Inoltre potrebbero emergere fenomeni di polarizzazione (segregazione, echo
chambers) ampiamente studiati in letteratura, ma non completamente compresi.

## Ulteriori sviluppi
Ulteriori decisioni dell'agente potranno essere implementate in seguito con una rete neurale
interna allenata a prendere vari tipi di decisione in merito alle preferenze sulle notizie o alla
creazione/rimozione dei link.
Un altro punto da analizzare potrebbe essere la topologia iniziale della rete: al variare di essa, si
potrebbero indagare gli effetti macroscopici, in linea di principio molto diversi.