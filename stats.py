from statistics import mean
from statistics import median
from statistics import mode
from statistics import quantiles
from statistics import stdev

# set number of decimal places to round to
decimal_places = 4

def get_mean(nums):
  """Takes in array of numbers. Returns mean."""
  return round(mean(nums), decimal_places)

def get_median(nums):
  """Takes in array of numbers. Returns median."""
  return median(nums)

def get_mode(nums):
  """Takes in array of numbers. Returns mode."""
  return mode(nums)

def get_range(nums):
  """Takes in array of numbers. Returns range."""
  return nums[-1] - nums[0]

def get_quartiles(nums):
  """Takes in array of numbers. Returns quartiles."""
  return quantiles(nums, n=4)

def get_iqr(nums):
  """Takes in array of numbers. Returns IQR."""
  quarts = get_quartiles(nums)
  return quarts[2] - quarts[0]

def get_outliers(nums):
  """
  Returns array of [boundaries, outliers].
  boundaries is an array of [lower, upper] bounds.
  outliers is an array of all outliers.
  """
  quarts = get_quartiles(nums)
  iqr = get_iqr(nums)
  bounds = [quarts[0] - (iqr*1.5), quarts[2] + (iqr*1.5)]
  outer_bounds = [quarts[0] - (iqr*3), quarts[2] + (iqr*3)]
  outliers = [i for i in nums if (i < bounds[0] and i >= outer_bounds[0]) or (i > bounds[1] and i <= outer_bounds[1])]
  return [bounds, outliers]

def get_extremes(nums):
  """
  Returns array of [boundaries, outliers].
  boundaries is an array of [lower, upper] bounds.
  outliers is an array of all outliers.
  """
  quarts = get_quartiles(nums)
  iqr = get_iqr(nums)
  bounds = [quarts[0] - (iqr*3), quarts[2] + (iqr*3)]
  extremes = [i for i in nums if i < bounds[0] or i > bounds[1]]
  return [bounds, extremes]

def get_stdev(nums):
  """Takes in array of numbers. Returns mode."""
  return round(stdev(nums), decimal_places)

def get_variance(nums):
  """Takes in array of numbers. Returns variance."""
  nums_sq = [i**2 for i in nums]
  sum_1 = sum(nums)
  top_right = (sum_1**2) / len(nums)
  top_left = sum(nums_sq)
  return round((top_left - top_right) / (len(nums) - 1), decimal_places)

def get_whiskers(nums):
  """Takes in array of numbers. Returns array of [left_whisker_length, right_whisker_length]."""
  bounds = get_outliers(nums)
  quarts = get_quartiles(nums)
  lower = bounds[0][0]
  upper = bounds[0][1]
  fenced_nums = [i for i in nums if (i > lower and i < upper)]
  smallest_fenced = min(fenced_nums)
  largest_fenced = max(fenced_nums)
  q1 = quarts[0]
  q3 = quarts[2]
  left_length = q1 - smallest_fenced
  right_length = largest_fenced - q3
  return [left_length, right_length]


def get_data(nums):
  """
  Runs all stats methods.
  Returns dictionary.\n
  Keys: mean, median, mode, range, quartiles, iqr, outliers, std_dev, variance
  """
  nums.sort()
  data = {}
  data["mean"] = get_mean(nums)
  data["median"] = get_median(nums)
  data["mode"] = get_mode(nums)
  data["range"] = get_range(nums)
  data["quartiles"] = get_quartiles(nums)
  data["iqr"] = get_iqr(nums)
  data["outliers"] = get_outliers(nums)
  data["extremes"] = get_extremes(nums)
  data["whiskers"] = get_whiskers(nums)
  data["stdev"] = get_stdev(nums)
  data["variance"] = get_variance(nums)
  return data


def main(nums):
  """Runs all methods. Prints output."""
  data = get_data(nums)
  print()
  for k,v in data.items():
    print(f"{k}: {v}")
  return data

if __name__ == '__main__':
  nums = [4, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 11]
  main(nums)
40, 43, 50, 52, 58, 60, 60, 64, 64, 65 ,65, 66, 66, 67, 68, 69 ,69, 70, 70, 74,79, 81, 91, 102