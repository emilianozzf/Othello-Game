from queue import Queue
from stack import Stack


class WordLadder:
    """A class providing functionality to create word ladders"""
    def __init__(self, w1, w2, wordlist):
        self.w1 = w1.lower()
        self.w2 = w2.lower()
        self.wordlist = wordlist

    def make_ladder(self):
        """Find the shortest word ladder"""
        ALPAHBET = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]
        seen_words = set()

        if len(self.w1) != len(self.w2):
            return None
        else:
            seen_words.add(self.w1)
            word_ladder = Stack()
            word_ladder.push(self.w1)
            word_ladders = Queue()
            word_ladders.enqueue(word_ladder)
            while not word_ladders.isEmpty():
                word_ladder = word_ladders.dequeue()
                top_word = word_ladder.peek()
                for _ in range(len(top_word)):
                    top_word_list = list(top_word)
                    for letter in ALPAHBET:
                        top_word_list[_] = letter
                        candidate_new_word = "".join(top_word_list)
                        if ((candidate_new_word not in seen_words)
                           and (candidate_new_word in self.wordlist)):
                            seen_words.add(candidate_new_word)
                            new_word_ladder = word_ladder.copy()
                            new_word_ladder.push(candidate_new_word)
                            if candidate_new_word == self.w2:
                                return new_word_ladder
                            else:
                                word_ladders.enqueue(new_word_ladder)
