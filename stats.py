from statistics import mean
from statistics import median
from statistics import mode
from statistics import quantiles
from statistics import stdev

def parse_nums(nums):
  """
  Takes in string of numbers separated by commas.
  Returns sorted array of numbers.
  """
  # if nums is a string, parse into numbers
  if isinstance(nums, str):
    nums = nums.replace(" ", "").split(",")
    nums = [float(i) for i in nums]
  nums.sort()
  return nums

def get_range(nums):
  """Takes in array of numbers. Returns range."""
  return nums[-1] - nums[0]

def print_formatted(mea, med, mo, ran, quarts, iqr, std_dev, outliers):
  """Print formatted data."""
  print(f'Mean: {mea}')
  print(f'Median: {med}')
  print(f'Mode: {mo}')
  print(f'Range: {ran}')
  print(f'Quartiles: Q1({quarts[0]}) Q2({quarts[1]}) Q3({quarts[2]})')
  print(f'IQR: {iqr}')
  print(f'Outliers: [{outliers[0]}, {outliers[1]}]')
  print(f'Std dev: {std_dev}')

def main(nums):
  nums = parse_nums(nums)
  mea = mean(nums)
  med = median(nums)
  mo = mode(nums)
  ran = get_range(nums)
  quarts = quantiles(nums, n=4)
  iqr = quarts[2] - quarts[0]
  std_dev = stdev(nums)
  outliers = [quarts[0] - (iqr*1.5), quarts[2] + (iqr*1.5)]
  print_formatted(mea, med, mo, ran, quarts, iqr, std_dev, outliers)

if __name__ == '__main__':
  #nums1 = "5, 6, 6, 8, 7, 7, 9 , 5, 4, 8, 11, 6, 7, 8, 7"
  #nums2 = "5,6,6,8,7,7,9,5,4,8,11,6,7,8,7"
  nums3 = "5,8,15,26,10,18,3,12,6,14,11"
  #nums = input("Please enter the numbers separated by commas:\n")
  main(nums3)