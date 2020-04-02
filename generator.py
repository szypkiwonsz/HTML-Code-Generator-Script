import sys


class HTMLGenerator:
    def __init__(self, text):
        self.text = text
        self.lines = None
        self.output = ''
        self.href_check = True

    def split_for_lines(self, data):
        self.lines = data.split('\n')

    def check_for_headings_in_lines(self):
        lines = ''
        id_heading = 0
        for line in self.lines:
            if line[0] == '#':
                line = f'<h1 id="{id_heading}X"> {line[1:]} </h1>'
                id_heading += 1
            lines += line + '\n'
        self.lines = lines
        self.split_for_lines(self.lines[:-1])

    def check_for_aside_in_lines(self):
        lines = ''
        for line in self.lines:
            if line and line[0] == '{':
                if '|' in line:
                    if '}' in line:
                        center_index = line.index('|')
                        right_parenthesis_index = line.index('}')
                        if center_index < right_parenthesis_index:
                            aside_type = line[1:center_index]
                            aside_title = line[center_index + 1:right_parenthesis_index]
                            line = f'<aside cat=”{aside_type}”><header>{aside_title}</header>' \
                                f'<main> {line[right_parenthesis_index+1:]} </main></aside>'
                        else:
                            sys.exit(f'Niepoprawnie domknięte znaki!')
                    else:
                        sys.exit(f'Niepoprawnie domknięte znaki!')
                else:
                    sys.exit(f'Niepoprawnie domknięte znaki!')
            lines += line + '\n'
        self.lines = lines
        self.split_for_lines(self.lines[:-1])

    def check_for_href(self):
        lines = ''
        for line in self.lines:
            if '[' in line:
                if '|' in line:
                    if ']' in line:
                        left_parenthesis_index = line.index('[')
                        center_index = line.index('|')
                        right_parenthesis_index = line.index(']')
                        if center_index < right_parenthesis_index:
                            href_address = line[left_parenthesis_index+1:center_index]
                            href_text = line[center_index + 1:right_parenthesis_index]
                            href = f'<a href=”{href_address}”>{href_text}</a>'
                            line = line[:left_parenthesis_index] + href + line[right_parenthesis_index+1:]
                    else:
                        sys.exit(f'Niepoprawnie domknięte znaki!')
                else:
                    sys.exit(f'Niepoprawnie domknięte znaki!')
            lines += line + '\n'
        self.lines = lines
        self.split_for_lines(self.lines[:-1])

    def split(self):
        lines = []
        for line in self.lines:
            if line[0:6] == '<aside':
                index_aside = line.index('<main>')
                aside = line[0:index_aside+6]
                line = line[index_aside+7:]
                line = line.split(' ')
                line.insert(0, aside)
                lines.append(line)
            elif line[0:3] == '<h1':
                index_h1 = line.index('<h1')
                h1 = line[0:index_h1+12]
                line = line[index_h1+13:]
                line = line.split(' ')
                line.insert(0, h1)
                lines.append(line)
            else:
                line = line.split(' ')
                lines.append(line)
        self.lines = lines

    def check_for_double_char(self, char_left, char_right, html):
        lines = ''
        for word in self.lines:
            if char_left in word:
                if char_right in word:
                    word = word.replace(char_left, f'<{html}>')
                    word = word.replace(char_right, f'</{html}>')
            lines += word + '\n'
        self.lines = lines
        self.split_for_lines(self.lines[:-1])

    def check_for_single_char(self, char_left, char_right, html):
        lines = ''
        for word in self.lines:
            if char_left == word[0]:
                if char_right in word[-1]:
                    word = word.replace(char_left, f'<{html}>')
                    word = word.replace(char_right, f'</{html}>')
            lines += word + '\n'
        self.lines = lines
        self.split_for_lines(self.lines[:-1])

    def split_two_arrays(self):
        lines = []
        for line in self.lines:
            for word in line:
                lines.append(word)
        self.lines = lines

    def add_parentheses(self):
        lines = []
        for word in self.lines:
            if word.isalnum():
                word = f'<p>{word}</p>'
            lines.append(word)
        self.lines = lines

    def print(self):
        self.split_for_lines(self.text)

        self.check_for_headings_in_lines()
        self.check_for_aside_in_lines()
        self.split()
        self.split_two_arrays()
        while self.href_check:
            for line in self.lines:
                if '[' in line:
                    pass
                else:
                    self.href_check = False
                self.check_for_href()
        self.check_for_double_char('>>', '<<', 'q')
        self.check_for_double_char('**', '**', 'strong')
        self.check_for_single_char('*', '*', 'em')
        self.check_for_double_char('_!', '!_', 'ins')
        self.check_for_double_char('-!', '!-', 'del')
        self.add_parentheses()
        for word in self.lines:
            print(word)


if __name__ == "__main__":
    generator = HTMLGenerator("{safa|sf}>>XD<< >>XD<< W **Ddddd** *[link|text]* **WWw** _!pwoep!_ -!safasf!- dfsg **[link|text]\n"
                              "#xdddddxd [link|text]\n#xddddddd")

    generator.print()
