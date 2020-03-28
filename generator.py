class HTMLGenerator:
    def __init__(self, text):
        self.text = text
        self.word = ""
        self.output = ""
        self.line = ""
        self.final_output = ""
        self.line = ""

    def replace(self):
        self.word = self.word.replace(self.word[0], "")
        self.word = self.word.replace(self.word[-1], "")

    def sharp_parentheses(self):
        if self.check_heading():
            self.word = "#<q>{}</q>".format(self.word[3:-2])
        else:
            self.word = "<q>{}</q>".format(self.word[2:-2])

    def one_star(self):
        if self.check_heading():
            self.word = "#<em>{}</em>".format(self.word[3:-2])
        else:
            self.word = "<em>{}</em>".format(self.word[1:-1])

    def two_stars(self):
        if self.check_heading():
            self.word = "#<strong>{}</strong>".format(self.word[3:-2])
        else:
            self.word = "<strong>{}</strong>".format(self.word[2:-2])

    def underscore_exclamation(self):
        if self.check_heading():
            self.word = "#<ins>{}</ins>".format(self.word[3:-2])
        else:
            self.word = "<ins>{}</ins>".format(self.word[2:-2])

    def dash_exclamation(self):
        if self.check_heading():
            self.word = "#<del>{}</del>".format(self.word[3:-2])
        else:
            self.word = "<del>{}</del>".format(self.word[2:-2])

    def check_url_text(self):
        if "[" in self.word and "|" in self.word and "]" in self.word:
            return True

    def paragraph(self):
        if self.check_heading():
            pass
        else:
            self.word = "<p>{}</p>".format(self.word[0:])

    def link_text(self):
        while "[" in self.line and "|" in self.line and "]" in self.line:
            left_parenthesis_index = self.line.index("[")
            line_index = self.line.index("|")
            right_parenthesis_index = self.line.index("]")
            link = self.line[left_parenthesis_index + 1:line_index]
            text = self.line[line_index + 1:right_parenthesis_index]
            self.line = self.line[0:left_parenthesis_index] + '<a href="{}">{}</a>'.format(link, text) + \
                        self.line[right_parenthesis_index+1:]

    def check_line(self):
        if '\n' in self.text:
            self.text = self.text.split('\n')

    def delete_first_line(self):
        self.output = self.output.split('\n')[1:]

    def check_heading(self):
        if self.word[0] == "#":
            return True

    def heading(self, heading_id):
        self.line = self.line[1:]
        self.line = self.line.replace(" ", "\n")
        self.line = "<h1 id=”{}”>{}</h1>".format(heading_id, self.line)

    def output_line(self):
        heading_id = 0
        for self.line in self.output:
            # Removing space as the last character in line.
            self.line = self.line[:-1]
            if self.line[0] == "#":
                self.heading(heading_id)
                heading_id += 1
            self.link_text()
            self.final_output += self.line
            self.final_output += "\n"

    def print(self):
        print(self.final_output)

    def characters(self):
        for self.line in self.text:
            self.line = self.line.split()
            self.output += "\n"
            for self.word in self.line:
                if ">>" in self.word and "<<" in self.word:
                    self.sharp_parentheses()
                elif self.word[0] == "*" and self.word[1] != "*" and self.word[-1] == "*":
                    self.one_star()
                elif self.word[0] == "*" and self.word[1] == "*" and self.word[-1] == "*" and self.word[-2] == "*":
                    self.two_stars()
                elif self.word[0] == "_" and self.word[1] == "!" and self.word[-1] == "_" and self.word[-2] == "!":
                    self.underscore_exclamation()
                elif self.word[0] == "-" and self.word[1] == "!" and self.word[-1] == "-" and self.word[-2] == "!":
                    self.dash_exclamation()
                elif self.word[0] != "[":
                    self.paragraph()
                self.output += self.word + " "
