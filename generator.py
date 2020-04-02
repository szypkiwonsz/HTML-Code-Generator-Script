import sys


class HTMLGenerator:
    def __init__(self, text):
        self.text = text
        self.lines = None

    def split_to_lines(self):
        self.lines = self.text.split("\n")

    def check_for_double_char(self, char_left, char_right, html):
        lines = ""
        for line in self.lines:
            for word in line.split(" "):
                if char_left in word:
                    if char_right in word:
                        word = word.replace(char_left, f'<{html}>')
                        word = word.replace(char_right, f'</{html}>')
                    else:
                        sys.exit(f'Niepoprawnie domknięte znaki! ---> {word}')
                lines += word + ' '
            lines += '\n'
        self.lines = [lines[:-2]]

    def check_for_stars(self, char_left, char_right):
        lines = ""
        for line in self.lines:
            for word in line.split(" "):
                if word[0:2] == char_left:
                    if word[-2:] == char_right:
                        word = f'<strong>{word[2:-2]}</strong>'
                    else:
                        sys.exit(f'Niepoprawnie domknięte znaki! ---> {word}')
                lines += word + ' '
            lines += '\n'
        self.lines = [lines[:-2]]

    def check_for_single_star(self, char_left, char_right):
        lines = ""
        for line in self.lines:
            for word in line.split(' '):
                try:
                    if word[0] == char_left and word[1] != '*':
                        if word[-1] == char_right and word[-2] != '*':
                            word = f'<em>{word[1:-1]}</em>'
                        else:
                            sys.exit(f'Niepoprawnie domknięte znaki! ---> {word}')
                except IndexError as e:
                    sys.exit(f'Nie możesz dodać spacji przed nową linią ---> "\\n", sprawdź wprowadzone dane.')
                lines += word + ' '
            lines += '\n'
        self.lines = [lines[:-2]]

    def check_for_href(self):
        lines = ""
        for line in self.lines:
            for word in line.split(' '):
                if '[' in word and '|' in word:
                    if ']' in word:
                        index_left_parenthesis = word.index('[')
                        index_center = word.index('|')
                        index_right_parenthesis = word.index(']')
                        word = f'<a href=”{word[index_left_parenthesis+1:index_center]}”>' \
                            f'{word[index_center+1:index_right_parenthesis]}</a>'
                    else:
                        sys.exit(f'Niepoprawnie domknięte znaki! ---> {word}')
                lines += word + ' '
            lines += '\n'
        self.lines = [lines[:-2]]

    def check_for_heading(self):
        lines_of_text = ""
        id_heading = 0
        for lines in self.lines:
            lines = (lines.split('\n'))
            for line in lines:
                if line[0] == '{':
                    if '|' in line and '}' in line:
                        index_center = line.index('|')
                        index_right_parenthesis = line.index('}')
                        if index_center < index_right_parenthesis:
                            aside_type = line[1:index_center]
                            aside_title = line[index_center+1:index_right_parenthesis]
                            line = f'<aside cat=”{aside_type}”><header>{aside_title}</header><main>' \
                                f'{line[index_right_parenthesis+1:-1]}</main></aside>'
                elif line[0] == '#':
                    line = f'<h1 id=”{id_heading}X”>{line[1:-1]}</h1>'
                    id_heading += 1
                else:
                    line = f'<p>{line[:-1]}</p>'
                lines_of_text += line
                lines_of_text += '\n'
            self.lines = [lines_of_text[:-1]]

    def output(self):
        self.split_to_lines()
        self.check_for_double_char('>>', '<<', 'q')
        self.check_for_stars('**', '**')
        self.check_for_single_star('*', '*')
        self.check_for_double_char('_!', '!_', 'ins')
        self.check_for_double_char('-!', '!-', 'del')
        self.check_for_href()
        self.check_for_heading()
        self.lines = generator.lines[0].split('\n')
        for line in self.lines:
            print(line)


if __name__ == "__main__":

    input_text = ""
    generator = HTMLGenerator(input_text)
    generator.output()
