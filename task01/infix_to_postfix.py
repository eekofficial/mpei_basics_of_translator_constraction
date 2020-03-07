INPUT_LOOP = True

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items) - 1]

    def is_empty(self):
        return self.items == []


def correct_parentheses(s):
    stack = Stack()
    parentheses = {'open': '([{', 'close':')]}'}
    for c in s:
        if c in parentheses['open']:
            stack.push(c)
        elif c in parentheses['close'] and \
                    (stack.is_empty() or parentheses['close'].index(c) != parentheses['open'].index(stack.pop())):
            return False
    if stack.size() == 0:
        return True
    return False

def delete_spaces(s):
    while ' ' in s:
        s.remove(' ')
    return s

def infix_to_postfix(s):
    operands = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    operators = { '/' : 3, '*' : 3, '+' : 2, '-' : 2, '(' : 1, '[' : 1, '{' : 1}
    parentheses = {'open': '([{', 'close': ')]}'}
    op_stack = Stack()
    postfix_s = list()
    without_operators = True
    token_list = list(s)

    if not correct_parentheses(s):
        return 'Please, check parentheses in your expression'

    if ' ' in token_list:
        token_list = delete_spaces(token_list)

    for token in token_list:
        if token in parentheses['open']:
            op_stack.push(token)
        elif token in operands:
            postfix_s.append(token)
        elif token in operators:
            without_operators = False
            if not op_stack.is_empty() and operators[op_stack.peek()] >= operators[token]:
                postfix_s.append(op_stack.pop())
                op_stack.push(token)
            else:
                op_stack.push(token)
        elif token in parentheses['close']:
            while op_stack.peek() != parentheses['open'][parentheses['close'].index(token)]:
                postfix_s.append(op_stack.pop())
            op_stack.pop()
        else:
            return 'You entered not acceptable symbols'

    if without_operators:
        return 'You entered expression without operands'

    while not op_stack.is_empty():
        postfix_s.append(op_stack.pop())

    return ' '.join(postfix_s)


if __name__ == '__main__':
    if INPUT_LOOP:
        s = ''
        while s != 'exit':
            s = input()
            if s != 'exit':
                print(infix_to_postfix(s))
