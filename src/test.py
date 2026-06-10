import unittest

from bubble_sort import bubble_sort_basic, bubble_sort_optimized

# helper
def both(arr: list[int]) -> tuple[list[int], list[int]]:
    a, b = arr[:], arr[:]
    return bubble_sort_basic(a), bubble_sort_optimized(b)


class TestRegularCases(unittest.TestCase):

    def test_random_order(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        expected = sorted(arr)
        basic, optimized = both(arr)
        self.assertEqual(basic, expected)
        self.assertEqual(optimized, expected)

    def test_ascending_order_best_case(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = arr[:]
        basic, optimized = both(arr)
        self.assertEqual(basic, expected)
        self.assertEqual(optimized, expected)

    def test_descending_order_worst_case(self):
        arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected = list(range(1, 11))
        basic, optimized = both(arr)
        self.assertEqual(basic, expected)
        self.assertEqual(optimized, expected)


class TestEdgeCases(unittest.TestCase):

    def test_empty_list(self):
        arr = []
        basic, optimized = both(arr)
        self.assertEqual(basic, [])
        self.assertEqual(optimized, [])

    def test_single_element(self):
        arr = [42]
        basic, optimized = both(arr)
        self.assertEqual(basic, [42])
        self.assertEqual(optimized, [42])

    def test_all_identical_elements(self):
        arr = [7, 7, 7, 7, 7]
        expected = [7, 7, 7, 7, 7]
        basic, optimized = both(arr)
        self.assertEqual(basic, expected)
        self.assertEqual(optimized, expected)

if __name__ == "__main__":
    unittest.main()