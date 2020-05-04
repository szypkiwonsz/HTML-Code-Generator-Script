import argparse
import sys


class HTMLGenerator:
    def __init__(self, text):
        self.text = text
        self.raw_lines = self.text.split('\n')
        self.lines = self.text.split('\n')

    def check_chars(self, open_char, close_char, new_open_char, new_close_char):
        single_char = '*'
        for i, line in enumerate(self.lines):
            check = True
            while check:
                line = self.lines[i]
                try:
                    open_char_index = line.index(open_char)
                    close_char_index = line.index(close_char, open_char_index + 2)
                    # Dodajemy znak '$' przed i po każdym nowym znaczniku,
                    # aby nasze znaki nie połączyły się ze znacznikami html.
                    if open_char == single_char:
                        self.lines[i] = f'{line[:open_char_index]}${new_open_char}$' \
                            f'{line[open_char_index + 1:close_char_index]}${new_close_char}$' \
                            f'{line[close_char_index + 1:]}'
                    else:
                        self.lines[i] = f'{line[:open_char_index]}${new_open_char}$' \
                            f'{line[open_char_index + 2:close_char_index]}${new_close_char}$' \
                            f'{line[close_char_index + 2:]}'
                except ValueError:
                    check = False
            # Usuwamy wszystkie znaki dolara z linii.
            self.lines[i] = self.lines[i].replace('$', '')

    def check_heading(self):
        id_header = 0
        for i, line in enumerate(self.lines):
            if line[0] == '#':
                self.lines[i] = f'<h1 id="{id_header}X">{line[1:]}</h1>'
                id_header += 1
            elif '{' in line and '|' in line and '}' in line:
                index_left_parenthesis = line.index('{')
                index_center = line.index('|')
                index_right_parenthesis = line.index('}')
                if index_left_parenthesis < index_center < index_right_parenthesis:
                    aside_type = line[index_left_parenthesis + 1:index_center]
                    header_title = line[index_center + 1:index_right_parenthesis]
                    main_text = line[:index_left_parenthesis] + line[index_right_parenthesis+1:]
                    self.lines[i] = f'<aside cat="{aside_type}"><header>{header_title}</header><main>{main_text}' \
                        f'</main></aside>'
                else:
                    sys.exit(f'Niepoprawnie utworzony nagłówek w linii ---> {self.raw_lines[i]}')
            else:
                self.lines[i] = f'<p>{line}</p>'

    def check_href(self):
        for i, line in enumerate(self.lines):
            check = True
            while check:
                line = self.lines[i]
                try:
                    index_left_parenthesis = line.index('[')
                    index_center = line.index('|')
                    index_right_parenthesis = line.index(']')
                    if index_left_parenthesis < index_center < index_right_parenthesis:
                        href_address = line[index_left_parenthesis + 1:index_center]
                        href_text = line[index_center + 1:index_right_parenthesis]
                        self.lines[i] = f'{line[:index_left_parenthesis]}<a href="{href_address}">{href_text}</a>' \
                            f'{line[index_right_parenthesis + 1:]}'
                    else:
                        sys.exit(f'Niepoprawnie utworzony atrybut "<a href" w linii ---> {self.raw_lines[i]}')
                except ValueError:
                    check = False

    def check_correct_characters(self, chars, message):
        for i, line in enumerate(self.lines):
            for char in chars:
                if char in line:
                    sys.exit(f'{message} ---> {self.raw_lines[i]}')

    @staticmethod
    def write_to_file(name_of_file, data):
        f = open(name_of_file, "w")
        f.write(data)
        f.close()

    def output(self):
        text = ''
        self.check_chars('>>', '<<', '<q>', '</q>')
        self.check_chars('**', '**', '<strong>', '</strong>')
        self.check_chars('*', '*', '<em>', '</em>')
        self.check_chars('_!', '!_', '<ins>', '</ins>')
        self.check_chars('-!', '!-', '<del>', '</del>')
        self.check_correct_characters(['>>', '<<', '*', '**', '-!', '!-', '_!', '!_'],
                                      'Niepoprawnie domknięte znaki w linii')
        try:
            self.check_heading()
        except IndexError:
            print('Usuń puste linie z pliku!')
            sys.exit()

        self.check_correct_characters(['#', '{', '}'], 'Nie możesz tworzyć więcej niż jednego nagłówka w linii lub'
                                                       'nagłówek został niepoprawnie stworzony.')
        self.check_href()
        self.check_correct_characters(['[', ']'], 'Niepoprawnie utworzony atrybut "<a href" w linii')
        for line in self.lines:
            text += line + '\n'
        self.write_to_file('output.html', text)
        print('---> Poprawnie zapisano dane do pliku output.html')


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--file_name", help="Wybiera plik z którego pobiera tekst.")

    args = parser.parse_args()
    if not any(vars(args).values()):
        print("Nie podałeś nazwy pliku!")
    elif args.file_name:
        try:
            input_text = open(args.file_name).read()
            generator = HTMLGenerator(input_text)
            generator.output()
        except FileNotFoundError as e:
            print('Nieprawidłowa nazwa pliku. Pamiętaj aby dodać rozszerzenie do nazwy pliku.')
