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
        # This is the alphabet
        ALPHABET = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]
        # Use a set to store seen-words
        seen_words = set()

        # If the lengths of two words are not the same, return None
        if len(self.w1) != len(self.w2):
            return None

        # Updates the seen-words set
        seen_words.add(self.w1)
        # Initialize an empty word ladder
        word_ladder = Stack()
        # Push the input word1 onto the word ladder
        word_ladder.push(self.w1)
        # Initialize an empty queue to store word ladders
        word_ladders = Queue()
        # Enqueue the word ladder
        word_ladders.enqueue(word_ladder)
        # Loop through every word ladder in the queue
        while not word_ladders.isEmpty():
            # Dequeue a word ladder
            word_ladder = word_ladders.dequeue()
            # Peek at the top word of the dequeued word ladder
            top_word = word_ladder.peek()
            # Loop through each character of the top word
            for _ in range(len(top_word)):
                # Cast the top word into a list
                top_word_list = list(top_word)
                # Loop though each letter in the alphabet
                for letter in ALPHABET:
                    # Replace the character with this letter
                    top_word_list[_] = letter
                    # Generate a candidate new word
                    candidate_new_word = "".join(top_word_list)
                    # Check whether the candidate is a valid English word and
                    # has not been seen before
                    if ((candidate_new_word not in seen_words)
                       and (candidate_new_word in self.wordlist)):
                        # Updates the seen-words set
                        seen_words.add(candidate_new_word)
                        # Make a duplicate of the word ladder
                        new_word_ladder = word_ladder.copy()
                        # Push the new word onto the new word ladder
                        new_word_ladder.push(candidate_new_word)
                        # Check if the word is the last word of the word ladder
                        if candidate_new_word == self.w2:
                            # Complete the word ladder finding process and
                            # return the new word ladder
                            return new_word_ladder
                        # Otherwise
                        else:
                            # Enqueue the new word ladder onto the end of the
                            # queue
                            word_ladders.enqueue(new_word_ladder)
