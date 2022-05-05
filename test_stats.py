import unittest
import stats

class TestStats(unittest.TestCase):

  def test_get_mean(self):
    nums = [4, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 11]
    decimal_places = 1 
    mean1 = 6.9
    mean2 = round(stats.get_mean(nums), decimal_places)
    self.assertEqual(mean1, mean2)

  def test_get_median(self):
    nums = [4, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 11]
    self.assertEqual(7, stats.get_median(nums))

  def test_get_mode(self):
    nums = [4, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 11]
    self.assertEqual(7, stats.get_mode(nums))

  def test_get_range(self):
    nums = [4, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 11]
    self.assertEqual(7, stats.get_range(nums))

  def test_get_quartiles(self):
    nums = [4, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 11]
    self.assertEqual([6.0, 7.0, 8.0], stats.get_quartiles(nums))

  def test_get_iqr(self):
    nums = [4, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 11]
    self.assertEqual(2.0, stats.get_iqr(nums))

  def test_get_outliers(self):
    nums = [-1, 0, 4, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 11, 15, 50]
    iqr = stats.get_iqr(nums)
    quartiles = stats.get_quartiles(nums)
    b1 = quartiles[0] - (iqr*1.5)
    b2 = quartiles[2] + (iqr*1.5)
    bounds = [b1, b2]
    self.assertEqual([bounds, [-1, 0, 15, 50]], stats.get_outliers(nums))
  
  def tests_get_variance(self):
    nums = [4, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 11]
    var = round(stats.get_variance(nums), 1)
    self.assertEqual(3.1, var)



if __name__ == '__main__':
  unittest.main()