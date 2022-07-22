# At most k paths

## Il problema

![Problema-1](https://user-images.githubusercontent.com/62235561/180224466-e47afb35-b3ab-445f-97d9-4696be3238ef.jpg)



<br/><br/>


## La mia soluzione

Per risolvere il problema ho inizialmente realizzato un algoritmo ricorsivo (inefficiente) che conta il numero di percorsi con al più k svolte per ogni cella della matrice *__n__ x __n__* che rispetta le seguenti regole generali:
* Per la prima cella in alto a sinistra esiste solo un percorso lecito qualunque sia il numero di svolte consentite;
* Per la prima riga esiste solo un percorso lecito se la direzione è orizzontale;
* Per la prima colonna esiste solo un percorso lecito se la direzione è verticale;
* Se il numero di svolte è zero, non ci sono percorsi che arrivano in celle che non sono o nella prima riga o nella prima colonna;
* Se la direzione è orizzontale, sommo il numero di percorsi con al più k svolte della cella precedente *__(j-1)__* con il numero di percorsi con al più *__k-1__* svolte della cella direttamente sopra *__(i-1)__* e inverto la direzione, poiché in questo caso starei compiendo una svolta.
* Se la direzione è verticale, sommo il numero di percorsi con al più k svolte della cella precedente *__(i-1)__* con il numero di percorsi con al più *__k-1__* svolte della cella direttamente sopra *__(j-1)__* e inverto la direzione, poiché in questo caso starei compiendo una svolta.

#### Questa è la funzione ricorsiva per il calcolo:

![unnamed (7)](https://user-images.githubusercontent.com/62235561/180223140-c20d5359-cba4-4dff-b2a6-3a613e6d7688.png)


<br/><br/>
Questa è la funzione chiamante, che chiama la funzione ricorsiva nelle due direzioni. 
![unnamed (15)](https://user-images.githubusercontent.com/62235561/180223484-2a766eb6-e36e-4ba5-98aa-439e332026cf.png)


Chiamando ![unnamed (14)](https://user-images.githubusercontent.com/62235561/180223589-6c202778-82ab-400e-bb1a-2ab64d6d7e1a.png) si otterrà il numero di percorsi che partono da  *__(0,0)__* e arrivano in  *__(n-1,n-1)__* compiendo al più  k svolte.
<br/><br/>

Risultato dell’algoritmo su diversi input.
<br/><br/>
![unnamed (2)](https://user-images.githubusercontent.com/62235561/180223814-b8744490-6e59-47d2-a4aa-6841e55a92fc.png)
<br/><br/>






Il problema di questo algoritmo è la sua inefficienza: durante il conto dei percorsi l’algoritmo si ritroverà a contare più volte il numero di percorsi per la stessa cella.
<br/><br/>
<img width="1245" alt="Immagine 2022-07-21 152841" src="https://user-images.githubusercontent.com/62235561/180225461-4d95d8cd-2a3c-4d83-8153-7f01e229feab.png">






Per esempio, nell’albero di ricorsione si vede chiaramente che ci sono due nodi  *__i-1, j-1, t-2, 0__*. Per questo motivo l’algoritmo avrà una __complessità esponenziale__ in *__O(2^(n+k))__* .


Per ottimizzare l’algoritmo si può usare la tecnica della *memoizzazione*, usando una tabella di dimensioni  *__n__ x __n__ x __(k+1)__* per mantenere in memoria il valore delle celle una volta calcolate e, quindi, evitare di ricalcolarle.

<br/><br/>

La funzione adattata per fare uso della memoizzazione è la seguente:
<br/><br/>

![unnamed (11)](https://user-images.githubusercontent.com/62235561/180230011-edea86f5-75b2-43d5-914e-ce4591361713.png)

<br/><br/>

Utilizzando una matrice *__n__ x __n__ x __(k+1)__*:
<br/><br/>
![unnamed (8)](https://user-images.githubusercontent.com/62235561/180230118-d0f7c889-4fd9-459f-87ee-f0d849432d02.png)
Il valore *__-1__* viene usato per distinguere le celle già calcolate.
<br/><br/>


Dato che la nostra matrice è *__n__ x __n__* e quindi simmetrica rispetto all’asse diagonale, basta contare i percorsi che partono da  *__(0,0)__* in una direzione e poi moltiplicare per due invece di dover calcolare entrambe le direzioni. La funzione ***es(n,k)*** diventerà quindi:
<br/><br/>
![unnamed (13)](https://user-images.githubusercontent.com/62235561/180231065-1126112d-94c9-424f-b10e-cc1c5d0efe09.png)
<br/><br/>

 

Chiamando ![unnamed (14)](https://user-images.githubusercontent.com/62235561/180231194-56f4b5f0-73c9-47a4-b278-f70204345175.png) si otterrà il numero di percorsi che partono da  ***(0,0)*** e arrivano in  ***(n-1,n-1)*** compiendo al più ***k*** svolte.



<br/><br/>
Risultato dell’algoritmo su diversi input.
<br/><br/>
![unnamed (4)](https://user-images.githubusercontent.com/62235561/180231553-02090900-50b5-41d7-9f93-14ce1e8bca87.png)
<br/><br/>



Questa è una soluzione Top-Down al problema, che __ha una complessità in__ ***O((n^2)k)***, poiché conterà il numero di percorsi al più una volta per ogni ***((n^2)k)*** celle della matrice.


Per poter passare da un approccio Top-Down ad un approccio Bottom-Up, bisogna definire meglio la matrice per la memoizzazione e la formula ricorsiva per il calcolo delle celle.


Utilizzo una matrice di dimensioni *__n__ x __n__ x __(k+1)__ x __2__*  dove n è la dimensione della matrice fornita in input, ***k*** è il numero massimo di svolte consentite. Per poter riconoscere le svolte senza utilizzare la ricorsione, ho bisogno di ricordare la direzione, quindi aggiungo un’ulteriore dimensione alla matrice per poterlo fare. 

***T[i,j,t,d] =*** __numero dei cammini che compiono al più t svolte, terminano in posizione ***(i,j)*** e arrivano da una direzione ***d***.__

La soluzione al problema sarà quindi data dalla somma di ***T[n-1][n-2][k][0] + T[n-2][n-1][k][1]***.
<br/><br/>

__A questo punto definisco la ricorrenza per ricavare ***T[i,j,t,d]*** dalle celle precedentemente calcolate:__

***d = 0*** rappresenta la direzione orizzontale, mentre ***d = 1*** rappresenta la direzione verticale.
<img width="644" alt="Immagine 2022-07-21 160832" src="https://user-images.githubusercontent.com/62235561/180234289-95d6674b-e05a-4f92-af1b-ffb603b75733.png">
<br/><br/>


La ricorrenza è corretta per i seguenti motivi:
- esiste un solo cammino lecito che termina in ***(0,0)*** a prescindere dalla direzione;
- esiste un solo cammino lecito per ogni cella della prima riga se la direzione è orizzontale;
- esiste un solo cammino lecito per ogni cella della prima colonna se la direzione è verticale;
- se il numero di svolte è 0 non esiste nessun percorso che arrivi in una cella posizionata in una riga o colonna diversa da quella iniziale;
- se un cammino lecito arriva in ***(i,j)*** devo considerare le due possibili direzioni:
  - se la direzione è orizzontale devo contare i percorsi in due casi:
    - sono arrivato in questa posizione da una riga diversa: ***T[i-1,j,t-1,1]*** (essendoci una svolta decremento t)
    - sono arrivato in questa posizione dalla stessa riga: ***T[i,j-1,t,0]***
  - se la direzione è verticale devo contare i percorsi in due casi:
    - sono arrivato in questa posizione da una colonna diversa:  ***T[i,j-1,t-1,0]*** (essendoci una svolta decremento t)
    - sono arrivato in questa posizione dalla stessa colonna: ***T[i-1,j,t,1]***
Inoltre avrò che se ***n <= 0 OR k < 0*** il risultato sarà  ***0*** e per  ***n = 1*** il risultato sarà ***1***
<br/><br/>

### Utilizzando queste regole ho realizzato il seguente algoritmo iterativo:

Per prima cosa considero i casi particolari e inizializzo la matrice per la memoizzazione:
<br/><br/>
![unnamed (12)](https://user-images.githubusercontent.com/62235561/180234968-a345f7ac-9410-4c54-8546-911f73cc332c.png)
<br/><br/>

Per la matrice utilizzo k+1 per poter contare anche i percorsi che compiono zero svolte. Il valore -1 lo uso per identificare una cella ancora non calcolata. La quarta dimensione la utilizzerò per ricordare la direzione. L’inizializzazione della matrice richiede (n2k).
<br/><br/>

Ora inizio a popolare la matrice T con i casi base:
<br/><br/>
![unnamed (10)](https://user-images.githubusercontent.com/62235561/180235132-58a0f1a4-bf40-49b6-ad07-fca90a1d9282.png)

<br/><br/>





A questo punto posso iniziare il calcolo iterativo delle celle della matrice:
<br/><br/>
![unnamed (9)](https://user-images.githubusercontent.com/62235561/180235259-06d46060-d35b-4bad-afc7-84cab1b75b4e.png)

<br/><br/>

Per poter calcolare correttamente i valori delle celle nella prima riga e nella prima colonna, ho usato due variabili: *north* e *west* che rappresentano il valore delle celle sopra e a sinistra della cella ***(i,j)***. In caso la cella ***(i,j)*** sia nella prima riga o colonna il valore di north o west sarà 0 per considerare un’ipotetica cella fuori dalla matrice.

Infine restituisco la somma dei percorsi delle celle sopra e a sinistra della cella ***(n-1, n-1)*** con rispettive direzioni:
<br/><br/>
![unnamed (5)](https://user-images.githubusercontent.com/62235561/180235435-71ebe054-3ae1-42d4-ad0a-109a3cd6c0f3.png)
<br/><br/>



Chiamando  ![unnamed (3)](https://user-images.githubusercontent.com/62235561/180235616-d23ef7ed-5f42-46a4-8bdc-2d7f8bb1a489.png)  si otterrà il numero di percorsi che partono da  (0,0) e arrivano in  (n-1,n-1) compiendo al più  k svolte.

<br/><br/>
Risultato dell’algoritmo su diversi input
<br/><br/>
![unnamed (4)](https://user-images.githubusercontent.com/62235561/180235786-024cc712-7693-4a45-9122-69dca3cb368f.png)
<br/><br/>







La funzione ***es(n,k)*** ha una complessità in ***O((n^2)k)***:
* Come già detto l’inizializzazione della matrice richiede tempo in ***O((n^2)k)***;
* I tre casi base richiedono tempo in ***O(n^2) + O(k) + O(nk)***
* Il calcolo delle celle rimanenti richiede tempo in ***O((n^2)k)***
Quindi avrò ***O((n^2)k) + O(n^2) + O(k) + O(nk) + O((n^2)k)*** il chè è uguale a ***O((n^2)k)***.


