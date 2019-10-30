from stack import Stack


class StringProcessor:
    """A class representing a string processor"""
    def __init__(self):
        self.ASTERISK = '*'
        self.CARET = '^'

    def process_string(self, line):
        """Given a line, return the decoded string"""
        chars_stack = Stack()
        solution_string = ""
        for char in line:
            if (char != self.ASTERISK) and (char != self.CARET):
                chars_stack.push(char)
            elif char == self.ASTERISK:
                if chars_stack.peek():
                    solution_string += chars_stack.pop()
            else:
                for _ in range(2):
                    if chars_stack.peek():
                        solution_string += chars_stack.pop()
        return solution_string
