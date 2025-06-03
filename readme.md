# Assignment 3 – Limbaje Formale si Automate

## Descriere

Acest proiect rezolva programatic cerintele assignmentului 3:

1. Definirea unei gramatici libere de context (CFG)
2. Generarea de cuvinte din limbaj
3. Realizarea derivailor pas cu pas
4. Recunoasterea apartenentei unui cuvant la limbaj

Functionalitati 

1. Definirea gramaticii (CFG)

Gramatica este stocata în variabila CFG si poate fi modificata usor.

Exemplu folosit:
```bash
S → a S b | ε
```

2. Generare de cuvinte

Optiunea 1 din meniu genereaza cuvinte aleatorii din limbaj
- Programul respectă cerințele assignmentului și poate fi ușor modificat pentru alte gramatici.

- Pentru gramatica data, numărul de cuvinte posibile pentru o anumita lungime este limitat (de ex. pentru lungime 10, doar 5 cuvinte sunt posibile).

- Codul evita duplicatele la generare, dar nu poate garanta lipsa lor daca N depaseste numarul maxim de cuvinte generate de gramatica pentru acea lungime.

3. Derivare pas cu pas

Optiunea 2 afiseaza pasii de derivare de la simbolul de start la un cuvant introdus, daca acesta poate fi generat de gramatica.

- Limita de pasi la derivare este pentru a preveni recursivitatea infinita.

4. Recunoastere apartenenta

Optiunea 3 verifica daca un cuvant dat poate fi generat de gramatica (apartine limbajului).

## Cum se ruleaza

### Cerinte
- Python 3.x

### Comenzi
Dupa rulare vei vedea meniul:

```bash
1. Genereaza N cuvinte
2. Derivare
3. Recunoastere
4. exit
```
- 1. Genereaza N cuvinte:
    introdu numar de cuvinte dorit

- 2. Derivare
    introdu un cuvant. Se vor afisa pasii derivari daca cuvantul poate fi generat

- 3. Recunoastere
    introdu un cuvant. Se va afisa True/False daca acesta apartine limbajului descris de CFG
