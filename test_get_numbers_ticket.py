import unittest

from get_numbers_ticket import get_numbers_ticket


class GetNumbersTicketTests(unittest.TestCase):
    def test_returns_requested_sorted_unique_numbers_in_range(self):
        numbers = get_numbers_ticket(1, 10, 6)

        self.assertEqual(len(numbers), 6)
        self.assertEqual(numbers, sorted(numbers))
        self.assertEqual(len(numbers), len(set(numbers)))
        self.assertTrue(all(1 <= number <= 10 for number in numbers))

    def test_returns_entire_range_when_quantity_matches_range_size(self):
        self.assertEqual(get_numbers_ticket(1, 5, 5), [1, 2, 3, 4, 5])

    def test_returns_empty_list_for_invalid_bounds(self):
        for bounds in ((0, 10, 1), (1, 1001, 1), (5, 4, 1)):
            with self.subTest(bounds=bounds):
                self.assertEqual(get_numbers_ticket(*bounds), [])

    def test_returns_empty_list_for_non_positive_quantity(self):
        for quantity in (0, -1):
            with self.subTest(quantity=quantity):
                self.assertEqual(get_numbers_ticket(1, 10, quantity), [])


if __name__ == "__main__":
    unittest.main()
