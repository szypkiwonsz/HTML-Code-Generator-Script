class HTMLGenerator:
    def __init__(self, text):
        self.text = text

    def sharp_parentheses(self):
        sentence = ""
        text = self.text.split()
        for word in text:
            if word[0] == ">" and word[1] == ">" and word[-1] == "<" and word[-2] == "<":
                word = "<q>{}</q>".format(word[2:-2])
                sentence += word + " "
            else:
                sentence += word + " "
        return sentence
