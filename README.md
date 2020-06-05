# HTML-Code-Generator-Script

A script that accepts text formatted with the tags described below, then returns the HTML code in the newly created file or error information in case of incorrect closing of characters.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Available Tags and What They Generate

Nesting inside the line

```
>>sample_text<< ---> <q>sample_text</q> 
```
```
*sample_text* ---> <em>sample_text</em>
```
```
**sample_text** ---> <strong>sample_text</strong>
```
```
_!sample_text!_ ---> <ins>sample_text</ins>
```
```
-!sample_text!- ---> <del>sample_text</del>
```
---

Inside the line

```
[address|text] ---> <a href=”address”>text</a>
```
---

It covers the entire line, if the first character is #, then it make the header

```
#Text ---> <h1 id=”nX”>Text</h1>
```
---

It covers the entire line, it doesn't have to be the first word

```
{type|Title} Text ---> <aside cat=”type”><header>Title</header><main>Text</main></aside>
```
---

A line that does not create a header

```
sample_text ---> <p>sample_text</p>
```
---

### Rules for Entering Characters

The same markers should be even numbers, otherwise the program will return information about incorrect closing of characters.

```
Like this: **sample_text**>>sample_text2<< | Not this: **sample_text**>>**sample_text2<<<<
```
---

We can only make one header per line.

```
Like this: #sample_text | Not this: ##sample_text
```
---

We can only make one "<aside" tag per line.

```
Like this: {type|Title} >>sample_text<< | Not this: {type|Title} >>sample_text {type|Title}
```
---

We can't use the same characters a second time to create a header.

```
Like this: {type|Title} >>sample_text<< | Not this: {type|Title} >>sample_text { | }
```
---

### Running

```
Download project
```
```
Create a new .txt file, write in it the text formatted with the tags provided above
```
```
Paste the file into the project folder where the "generator.py" file is located
```
```
Open terminal with choosen folder "HTML-Code-Generator-Script>"
```
```
Type "python generator.py --file_name [your_file_name]"
```

If you did everything as instructed, a new file should appear in the project folder called "output.html" containing the generated HTML code

---

## Built With

* [Python 3.8](https://www.python.org/) - The programming language used

## Authors

* **Jan Kacper Sawicki** - [szypkiwonsz](https://github.com/szypkiwonsz)

## Acknowledgments

* The script was written as a study assignment.
