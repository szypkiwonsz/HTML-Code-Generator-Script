class HTMLGenerator:
    def __init__(self, text):
        self.text = text
        self.word = ""
        self.output = ""

    def split_text(self):
        self.text = self.text.split()

    def split(self, char):
        self.word = self.word.split(char)

    def replace(self):
        self.word = self.word.replace(self.word[0], "")
        self.word = self.word.replace(self.word[-1], "")

    def sharp_parentheses(self):
        if self.word[0] == ">" and self.word[1] == ">" and self.word[-1] == "<" and self.word[-2] == "<":
            return True

    def one_star(self):
        if self.word[0] == "*" and self.word[1] != "*" and self.word[-1] == "*":
            return True

    def two_stars(self):
        if self.word[0] == "*" and self.word[1] == "*" and self.word[-1] == "*" and self.word[-2] == "*":
            return True

    def underscore_exclamation(self):
        if self.word[0] == "_" and self.word[1] == "!" and self.word[-1] == "_" and self.word[-2] == "!":
            return True

    def dash_exclamation(self):
        if self.word[0] == "-" and self.word[1] == "!" and self.word[-1] == "-" and self.word[-2] == "!":
            return True

    def check_url_text(self):
        if "[" in self.word and "|" in self.word and "]" in self.word:
            return True

    def url_text(self):
        self.replace()
        self.split("|")
        self.word = "<a href=”{}”>{}</a>".format(self.word[0][1:], self.word[1][:-1])

    def characters(self):
        for self.word in self.text:
            if self.sharp_parentheses():
                if self.check_url_text():
                    self.url_text()
                    self.word = "<q>{}</q>".format(self.word)
                else:
                    self.word = "<q>{}</q>".format(self.word[2:-2])
            elif self.one_star():
                if self.check_url_text():
                    self.url_text()
                    self.word = "<em>{}</em>".format(self.word)
                else:
                    self.word = "<em>{}</em>".format(self.word[1:-1])
            elif self.two_stars():
                if self.check_url_text():
                    self.url_text()
                    self.word = "<strong>{}</strong>".format(self.word)
                else:
                    self.word = "<strong>{}</strong>".format(self.word[2:-2])
            elif self.underscore_exclamation():
                if self.check_url_text():
                    self.url_text()
                    self.word = "<ins>{}</ins>".format(self.word)
                else:
                    self.word = "<ins>{}</ins>".format(self.word[2:-2])
            elif self.dash_exclamation():
                if self.check_url_text():
                    self.url_text()
                    self.word = "<del>{}</del>".format(self.word)
                else:
                    self.word = "<del>{}</del>".format(self.word[2:-2])
            elif self.check_url_text():
                self.word = self.word.split("|")
                self.word = "<a href=”{}”>{}</a>".format(self.word[0][1:], self.word[1][:-1])
            else:
                pass
            self.output += self.word + " "
