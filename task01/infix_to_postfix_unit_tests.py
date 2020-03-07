import unittest
from infix_to_postfix import infix_to_postfix

class TestInfixToPostfix(unittest.TestCase):

    def test(self):
        for (test, answer) in [
            ('A*B+C*D', 'A B * C D * +'),
            ('( A + B ) * C - ( D - E ) * ( F + G )', 'A B + C * D E - F G + * -'),
            ('94', 'You entered not acceptable symbols'),
            ('( A + B ) * ( C + D )', 'A B + C D + *'),
            ('( A + B ) * C', 'A B + C *'),
            ('A + B * C', 'A B C * +'),
            ('( A + B) * (C+ D)', 'A B + C D + *'),
            ('( A +B ) * [ C + D ]', 'A B + C D + *'),
            ('{( A + B ) * ( C + D )}', 'A B + C D + *'),
            ('[ A + B ] * {C+D}', 'A B + C D + *'),
            ('( A + B } * ( C + D )', 'Please, check parentheses in your expression'),
            ('a b c', 'You entered expression without operands')
        ]:
            self.assertEqual(infix_to_postfix(test), answer)

if __name__ == '__main__':
    unittest.main()