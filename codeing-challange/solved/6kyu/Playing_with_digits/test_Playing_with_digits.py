import unittest
from Playing_with_digits import dig_pow


def find_n_p_for_k(k, n_max=10001, p_max=11):
    results = []
    for n in range(10, n_max):  # kleine n’s erstmal
        for p in range(1, p_max):
            value_x = sum(int(digit) ** (p + i) for i, digit in enumerate(str(n)))
            if value_x == n * k:
                results.append((n, p))
    return results
class MyTestCase(unittest.TestCase):

    def test_find_k(self):
        print(find_n_p_for_k(5))

    def test_create(self):
        print(dig_pow(180,2))
    def test_1(self):
        self.assertEqual(dig_pow(89,1), 1)
    def test_2(self):
        self.assertEqual(dig_pow(150,2),-1)
    def test_3(self):
        self.assertEqual(dig_pow(180,2),-1)
    def test_4(self):
        self.assertEqual(dig_pow(695,2),2)

    def test_5(self):
        self.assertEqual(dig_pow(43,2),1)

if __name__ == '__main__':
    unittest.main()
