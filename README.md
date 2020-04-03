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

Google Chrome

```
Update to the latest version or get the current one from - https://www.google.com/chrome/
```
---

selenium

```
pip install selenium
```
---

### Running

A step by step series of examples that tell you how to run a bot

```
Fill in your Facebook login details in the secrets.py file
```
---
Run a bot

```
python tinder_bot.py
```
---
## Built With

* [Python 3.8](https://www.python.org/) - The programming language used

## Authors

* **Jan Kacper Sawicki** - [szypkiwonsz](https://github.com/szypkiwonsz)

## Acknowledgments

* The bot was created using the techniques from the given video - https://www.youtube.com/watch?v=lvFAuUcowT4&t
