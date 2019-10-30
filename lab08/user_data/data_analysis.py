import re


class DataAnalysis:
    """A class representing a data analysis"""
    def __init__(self, file):
        self.file_name = file
        self.lang_counts = {}
        self.lang_total_count = 0
        self.country_tlds_counts = {}
        self.tlds_total_count = 0

    def top_n_lang_freqs(self, n):
        """Takes a number, returns top n languages' frequencies"""
        return self.sorted_lang_freqs[:n]

    def top_n_country_tlds_freqs(self, n):
        """Takes a number, returns top n country top-level domains's frequencies"""
        return self.sorted_tlds_freqs[:n]

    @property
    def sorted_lang_freqs(self):
        """Sorts the languages frequencies"""
        return sorted(
            self.lang_freqs.items(),
            key=lambda x: x[1],
            reverse=True
        )

    @property
    def sorted_tlds_freqs(self):
        """Sorts the top-level domains frequencies"""
        return sorted(
            self.tlds_freqs.items(),
            key=lambda x: x[1],
            reverse=True
        )

    @property
    def lang_freqs(self):
        """Converts the languages counts to languages frequencies"""
        self.read_data(self.file_name)
        return {key: (self.lang_counts[key]/self.lang_total_count)
                for key in self.lang_counts.keys()}

    @property
    def tlds_freqs(self):
        """Converts the country top-level domains counts to top-level domains
        frequencies"""
        return {key: (self.country_tlds_counts[key]/self.tlds_total_count)
                for key in self.country_tlds_counts.keys()}

    def read_data(self, file_name):
        """Reads the data"""
        try:
            f = open(file_name)
        except FileNotFoundError:
            print("Can't find", file_name)
            return

        header = f.readline().strip().split(',')
        position_of_lang = header.index("language")
        position_of_email = header.index("email")

        for line in f:
            new_line = line.strip().split(',')
            the_lang = new_line[position_of_lang]
            the_email = new_line[position_of_email]
            self.add_lang(the_lang)
            self.tlds_total_count += 1
            the_country_tld = ''.join(re.findall(r"\.[a-z]{2}$", the_email))
            if the_country_tld:
                self.add_country_tld(the_country_tld[1:])

    def add_lang(self, lang):
        """Takes a language, adds the language count"""
        self.lang_total_count += 1
        if lang in self.lang_counts:
            self.lang_counts[lang] += 1
        else:
            self.lang_counts[lang] = 1

    def add_country_tld(self, country_tld):
        """Takes a country top-level domain, adds its count"""
        if country_tld in self.country_tlds_counts:
            self.country_tlds_counts[country_tld] += 1
        else:
            self.country_tlds_counts[country_tld] = 1