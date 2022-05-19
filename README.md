# Space Invaders
The classic platformer game using pygame for Python101, spring 2022

Main implementation idea:

Am ales sa implementam o versiune in care pozitiile si vitezele pe axele OX si OY pentru fiecare element de joc: player, invader, bullet; sunt memorate intr-o lista de 2 elemente. Iar numarul de invaders este setat in cod, iar cu acesta se contruieste o lista pentru a contoriza fiecare invader.

Scopul functiilor:

Functiile player(), invader() si bullet() sunt folosite pentru a randa imaginile acestora pe ecran, si primesc ca argumente fereastra si pozitiile pe ecran.

Functia de show_score() afiseaza punctajul obtinut de jucator, cu ajutorul castarii la string a valorii scorului. Variabila globala SCORE_VAL se regaseste in functia "run", unde la fiecare coliziune, se incrementeaza cu 1.

Functia de game_over() semnaleaza incheierea jocului atunci cand un invader loveste nava jucatorului.

Functia isCollision() returneaza true daca se produce o coliziune intre bullet si invader (coliziunea dintre nava si invader fiind tratata separat in cod), si ea functioneaza pe principiul: se calculeaza cea mai scurta distanta dintre bullet si invader iar daca aceasta este mai mica de 50 se considera coliziune, in caz contrar nu.

Game mechanics:

Controlul jocului se face simplu si a fost implementat intr-un mod similar cu jocul original. Am folosit tastele spatiu, sageata dreapta si stanga pentru ca jucătorul să ajusteze poziția navei spațiale în cel mai bun mod tactic si pentru a trage un glont. Invadatorii extratereștri sunt programați să reapară odată doborati și să se deplaseze către jucător, calea lor fiind similară cu traversarea unei matrice. Ei coboară matricea linie cu linie. Când jucătorul nu reușește să doboare un inamic și inamicul ajunge la jucător, jocul afișează „Game Over” și progresul este pierdut.
Functia run() din clasa de joc Game este apelata intr-o bucla infinita, deoarece atunci cand se detecteaza evenimentul de QUIT in functie se opreste executia.




