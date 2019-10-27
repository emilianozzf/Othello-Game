import sys
import re
from text_cleaner import TextCleaner
from ngram_frequencies import NgramFrequencies


def main(file_name):
    tc = TextCleaner(file_name)
    nf = NgramFrequencies()

    clean_sentences = tc.clean_sentences()
    for sentence in clean_sentences:
        unigrams = re.findall(r"\b\S+\b", sentence)
        bigrams = re.findall(r"(?=(\b\S+ \S+\b))", sentence)
        trigrams = re.findall(r"(?=(\b\S+ \S+ \S+\b))", sentence)
        for unigram in unigrams:
            nf.add_item(unigram)
        i = 0
        while i < len(bigrams):
            nf.add_item(bigrams[i])
            if -1 < bigrams[i].find("'") < bigrams[i].find(" "):
                i += 3
            else:
                i += 1
        i = 0
        while i < len(trigrams):
            nf.add_item(trigrams[i])
            if -1 < trigrams[i].find("'") < trigrams[i].find(" "):
                i += 3
            else:
                i += 1

    ngrams = ["unigrams", "bigrams", "trigrams"]
    for ngram_kind in ngrams:
        print("Top 10 " + ngram_kind + ":")
        for ngram_freq in nf.top_n_freqs(ngram_kind):
            print("    ", ngram_freq)


main(sys.argv[1])
