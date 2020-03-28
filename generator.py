class HTMLGenerator:
    def __init__(self, text):
        self.text = text
        self.word = ""
        self.output = ""
        self.line = ""

    def replace(self):
        self.word = self.word.replace(self.word[0], "")
        self.word = self.word.replace(self.word[-1], "")

    def sharp_parentheses(self):
        if self.check_url_text():
            self.url_text()
            self.word = "<q>{}</q>".format(self.word)
        else:
            self.word = "<q>{}</q>".format(self.word[2:-2])

    def one_star(self):
        if self.check_url_text():
            self.url_text()
            self.word = "<em>{}</em>".format(self.word)
        else:
            self.word = "<em>{}</em>".format(self.word[1:-1])

    def two_stars(self):
        if self.check_url_text():
            self.url_text()
            self.word = "<strong>{}</strong>".format(self.word)
        else:
            self.word = "<strong>{}</strong>".format(self.word[2:-2])

    def underscore_exclamation(self):
        if self.check_url_text():
            self.url_text()
            self.word = "<ins>{}</ins>".format(self.word)
        else:
            self.word = "<ins>{}</ins>".format(self.word[2:-2])

    def dash_exclamation(self):
        if self.check_url_text():
            self.url_text()
            self.word = "<del>{}</del>".format(self.word)
        else:
            self.word = "<del>{}</del>".format(self.word[2:-2])

    def check_url_text(self):
        if "[" in self.word and "|" in self.word and "]" in self.word:
            self.word = self.word.split("|")
            self.word = "<a href=”{}”>{}</a>".format(self.word[0][1:], self.word[1][:-1])

    def url_text(self):
        self.replace()
        self.word = self.word.split("|")
        self.word = "<a href=”{}”>{}</a>".format(self.word[0][1:], self.word[1][:-1])

    def check_line(self):
        if '\n' in self.text:
            self.text = self.text.split('\n')

    def delete_first_line(self):
        self.output = self.output.split('\n')[1:]

    def print(self):
        output = ""
        for line in self.output:
            output += line
            output += "\n"
        print(output)

    def characters(self):
        for self.line in self.text:
            self.line = self.line.split()
            self.output += "\n"
            for self.word in self.line:
                if self.word[0] == ">" and self.word[1] == ">" and self.word[-1] == "<" and self.word[-2] == "<":
                    self.sharp_parentheses()
                elif self.word[0] == "*" and self.word[1] != "*" and self.word[-1] == "*":
                    self.one_star()
                elif self.word[0] == "*" and self.word[1] == "*" and self.word[-1] == "*" and self.word[-2] == "*":
                    self.two_stars()
                elif self.word[0] == "_" and self.word[1] == "!" and self.word[-1] == "_" and self.word[-2] == "!":
                    self.underscore_exclamation()
                elif self.word[0] == "-" and self.word[1] == "!" and self.word[-1] == "-" and self.word[-2] == "!":
                    self.dash_exclamation()
                self.check_url_text()
                self.output += self.word + " "
