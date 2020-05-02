# HTML-Code-Generator-Script

Skrypt który przyjmuje na wejściu tekst sformatowany znacznikami opisanymi poniżej, po czym zwraca kod HTML w nowo utworzonym pliku lub informację o błędnym kodzie w wypadku niepoprawnych domknięć.

## Od czego zacząć

Ta instrukcja pokaże Ci jak uruchomić skrypt na swoim systemie oraz jakich zasad powinienieś się trzymać.

### Dostępne znaczniki i co generują

Wewnątrz lini zagnieżdzanie

```
>>przykładowy_tekst<< ---> <q>przykładowy_tekst</q> 
```
```
*przykładowy_tekst* ---> <em>przykładowy_tekst</em>
```
```
**przykładowy_tekst** ---> <strong>przykładowy_tekst</strong>
```
```
_!przykładowy_tekst!_ ---> <ins>przykładowy_tekst</ins>
```
```
-!przykładowy_tekst!- ---> <del>przykładowy_tekst</del>
```
---

Wewnątrz linii

```
[adres|tekst] ---> <a href=”adres”>tekst</a>
```
---

Obejmuje całą linię, jeśli pierwszym znakiem jest #, to robimy nagłówek

```
# Tekst ---> <h1 id=”nX”>Tekst</h1>
```
---

Objemuje całą linie jeśli jest pierwszym wyrazem

```
{typ|Tytuł} Tekst ---> <aside cat=”typ”><header>Tytuł</header><main>Tekst</main></aside>
```
---

Linia nie tworząca nagłówka

```
przykładowy_tekst ---> <p>przykładowy_tekst</p>
```
---

### Zasady wprowadzania znaków

Każdy wyraz, znacznik musi być oddzielony od siebie spacją

```
Tak: **przykładowy_tekst** >>przykładowy_tekst2<< | Nie: **przykładowy_tekst**>>przykładowy_tekst2<<
```
---

Jeśli chcemy zrobić nagłówek w linii, wyrazy po pierwszym znaku jakim jest "#" muszą być oddzielone od niego spacją

```
Tak: # przykładowy_tekst | Nie: #przykładowy_tekst
```
---

Jeśli chcemy zrobić znaczik "<aside..." w linii, musimy dać podać znacznik na początku linii

```
Tak: {typ|Tytuł} >>przykładowy_tekst<< | Nie: >>przykładowy_tekst {typ|Tytuł}
```
---

### Jak uruchomić skrypt

```
Stwórz nowy plik .txt, napisz w nim tekst sformatowany powyżej podanymi znacznikami
```
```
Wklej go do folderu z projektem gdzie znajduje się plik "generator.py"
```
```
Uruchom terminal z wybranym folderem "HTML-Code-Generator-Script>"
```
```
Wpisz komende: python generator.py --file_name [twoja_nazwa_pliku]
```

Jeśli wykonałeś wszystko zgodnie z instrukcją, w folderze projektu powinien pojawić się nowy plik o nazwie "output.html", zawierający wygenerowany kod HTML

---

## Stworzony za pomocą

* [Python 3.8](https://www.python.org/) - język programowania

## Autor

* **Jan Kacper Sawicki** - [szypkiwonsz](https://github.com/szypkiwonsz)

## Informacje dodatkowe

* Skrypt został napisany jako zadanie na studia.
