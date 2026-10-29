import unittest

from get_numbers_ticket import get_numbers_ticket


class GetNumbersTicketTests(unittest.TestCase):
    def test_returns_requested_sorted_unique_numbers_in_range(self):
        numbers = get_numbers_ticket(10, 50, 6)

        self.assertEqual(len(numbers), 6)
        self.assertEqual(numbers, sorted(numbers))
        self.assertEqual(len(numbers), len(set(numbers)))
        self.assertTrue(all(10 <= number <= 50 for number in numbers))

    def test_returns_entire_range_when_quantity_matches_range_size(self):
        self.assertEqual(get_numbers_ticket(3, 6, 4), [3, 4, 5, 6])

    def test_returns_empty_list_for_invalid_bounds(self):
        for bounds in ((0, 49, 6), (10, 1001, 6), (5, 4, 1)):
            with self.subTest(bounds=bounds):
                self.assertEqual(get_numbers_ticket(*bounds), [])

    def test_returns_empty_list_for_invalid_quantity(self):
        for args in ((1, 49, 0), (1, 49, -1), (10, 12, 4)):
            with self.subTest(args=args):
                self.assertEqual(get_numbers_ticket(*args), [])


if __name__ == "__main__":
    unittest.main()
