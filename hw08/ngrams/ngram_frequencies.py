import re


class NgramFrequencies:
    """A class representing ngram frequencies"""
    def __init__(self):
        """Creats three instances: one for unigrams, one for bigrams, and one
        for trigrams"""
        self.unigrams_counts = {"total_count": 0}
        self.bigrams_counts = {"total_count": 0}
        self.trigrams_counts = {"total_count": 0}

    def add_item(self, ngram):
        """Takes an n-gram and increments its count in the dictionary"""
        ngram = re.sub(" ", "_", ngram)
        if len(ngram.split("_")) == 1:
            self.unigrams_counts["total_count"] += 1
            if ngram in self.unigrams_counts.keys():
                self.unigrams_counts[ngram] += 1
            else:
                self.unigrams_counts[ngram] = 1
        elif len(ngram.split("_")) == 2:
            self.bigrams_counts["total_count"] += 1
            if ngram in self.bigrams_counts.keys():
                self.bigrams_counts[ngram] += 1
            else:
                self.bigrams_counts[ngram] = 1
        elif len(ngram.split("_")) == 3:
            self.trigrams_counts["total_count"] += 1
            if ngram in self.trigrams_counts.keys():
                self.trigrams_counts[ngram] += 1
            else:
                self.trigrams_counts[ngram] = 1

    def top_n_freqs(self, ngram_kind):
        """Takes a ngram kind, returns a list of items sorted on the frequency,
        with the most frequent first"""
        return [(item[0], self.frequency(item))
                for item in self.top_n_counts(ngram_kind)]

    def top_n_counts(self, ngram_kind):
        """Takes a ngram kind, returns a list of items sorted on the count,
        with the most frequent first"""
        if ngram_kind == "unigrams":
            return sorted(
                self.unigrams_counts.items(),
                key=lambda x: x[1],
                reverse=True
            )[1:11]
        elif ngram_kind == "bigrams":
            return sorted(
                self.bigrams_counts.items(),
                key=lambda x: x[1],
                reverse=True
            )[1:11]
        elif ngram_kind == "trigrams":
            return sorted(
                self.trigrams_counts.items(),
                key=lambda x: x[1],
                reverse=True
            )[1:11]

    def frequency(self, item):
        """Takes an item and return its frequency"""
        if item in self.unigrams_counts.items():
            return round(item[1]/self.unigrams_counts["total_count"], 3)
        elif item in self.bigrams_counts.items():
            return round(item[1]/self.bigrams_counts["total_count"], 3)
        elif item in self.trigrams_counts.items():
            return round(item[1]/self.trigrams_counts["total_count"], 3)
