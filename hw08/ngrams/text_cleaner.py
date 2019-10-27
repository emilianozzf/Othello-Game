import re


class TextCleaner:
    """A class representing a text cleaner"""
    def __init__(self, file_name):
        """Creats an instance storing the file name"""
        self.file_name = file_name

    def clean_sentences(self):
        """Cleans the text in the file and splits it into sentences"""
        try:
            f = open(self.file_name)
        except FileNotFoundError:
            print("Can't find", self.file_name)
            return

        clean_text = ''
        clean_text += (f.readline().lower().strip() + '. ')
        clean_text += (f.readline().lower().strip() + '. ')
        for line in f:
            if line != '\n':
                clean_text += (line.lower().strip() + ' ')
        clean_text = self.keep_required_characters(clean_text)
        clean_text = self.render_comma_tokens(clean_text)
        clean_text = self.clean_other_periods(clean_text)
        clean_sentences = self.split_with_periods(clean_text)
        return clean_sentences

    def keep_required_characters(self, text):
        """Takes a text, keeps alphanumerical characters, commas, apostrophes,
         periods, and whitespace and strips all the rest"""
        return "".join(re.findall(r"[a-z0-9\,\.\' ]", text))

    def render_comma_tokens(self, text):
        """Takes a text, renders each comma as the all caps token 'COMMA'"""
        return re.sub(r"\,", " COMMA", text)

    def clean_other_periods(self, text):
        """Takes a text, Gets rid of other periods first, such as those at the
        end of abbreviated like 'Mr.' and 'Dr.'"""
        text = re.sub(r"mr\.", "mr", text)
        text = re.sub(r"mrs\.", "mrs", text)
        text = re.sub(r"ms\.", "ms", text)
        text = re.sub(r"dr\.", "dr", text)
        return text

    def split_with_periods(self, text):
        """Takes a text, splits it into sentences"""
        return text.split(". ")
