from stack import Stack


class BracketMatch:
    """Class for evaluating parenthetical strings"""
    def __init__(self):
        self.OPEN_BRACKETS = ['(', '[', '{']
        self.CLOSING_BRACKETS = [')', ']', '}']

    def brackets_match(self, line):
        """Given a line, determine whether the line's brackets are mathced"""
        brackets_stack = Stack()
        for char in line:
            if char in self.OPEN_BRACKETS:
                brackets_stack.push(char)
            elif char in self.CLOSING_BRACKETS:
                last = brackets_stack.peek()
                if last:
                    if (self.OPEN_BRACKETS.index(last) ==
                       self.CLOSING_BRACKETS.index(char)):
                        brackets_stack.pop()
                    else:
                        return False
                else:
                    return False

        if not brackets_stack.peek():
            return True
        else:
            return False
