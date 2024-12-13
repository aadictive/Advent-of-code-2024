from solutions import *
import unittest
import tracemalloc


class MyTestCase(unittest.TestCase):

    def setUp(self):
        tracemalloc.start()
    def test_example_files(self):
        result = solution_day1_part1.execute_example_file()
        self.assertEqual(11, result)

        result = solution_day1_part2.execute_example_file()
        self.assertEqual(31, result)

        result = solution_day2_part1.execute_example_file()
        self.assertEqual(2, result)

        result = solution_day2_part2.execute_example_file()
        self.assertEqual(4, result)

        result = solution_day3_part1.execute_example_file()
        self.assertEqual(161, result)

        result = solution_day3_part2.execute_example_file()
        self.assertEqual(161, result)

        result = solution_day4_part1.execute_example_file()
        self.assertEqual(18, result)

        result = solution_day4_part2.execute_example_file()
        self.assertEqual(9, result)

    def test_puzzle_files(self):
        result = solution_day1_part1.execute_puzzle_file()
        self.assertEqual(2378066, result)

        result = solution_day1_part2.execute_puzzle_file()
        self.assertEqual(18934359, result)

        result = solution_day2_part1.execute_puzzle_file()
        self.assertEqual(490, result)

        result = solution_day2_part2.execute_puzzle_file()
        self.assertEqual(536, result)

        result = solution_day3_part1.execute_puzzle_file()
        self.assertEqual(183380722, result)

        result = solution_day3_part2.execute_puzzle_file()
        self.assertEqual(82733683, result)

        result = solution_day4_part1.execute_puzzle_file()
        self.assertEqual(2551, result)

        result = solution_day4_part2.execute_puzzle_file()
        self.assertEqual(1985, result)

    def tearDown(self):
        snapshot = tracemalloc.take_snapshot()
        top_stats = snapshot.statistics('lineno')

        print("[ Top 10 ]")
        for stat in top_stats[:10]:
            print(stat)


if __name__ == '__main__':
    unittest.main()
