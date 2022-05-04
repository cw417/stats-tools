def parse_nums(nums):
  """
  Takes in string of numbers separated by commas.
  Returns sorted array of numbers.
  """
  nums = nums.replace(" ", "").split(",")
  nums = [float(i) for i in nums]
  nums.sort()
  return nums

def get_mean(nums):
  """Takes in array of numbers. Returns mean."""
  mean = round(sum(nums) / len(nums),2)
  return mean

def get_median(nums):
  """
  Takes in array of numbers.
  Returns an array of [median, index].
  """
  med = 0
  mid = 0
  if len(nums) % 2 == 0:
    mid = len(nums)/2
    med = (nums[mid - 1] + nums[mid]) / 2
  else:
    mid = int(len(nums)/2)
    med = nums[mid]
  return [med, mid]

def get_mode(nums):
  """Takes in array of numbers. Returns mode."""
  counts = {num:nums.count(num) for num in nums}
  max = -99999999999999999
  for num in counts.values():
    if num > max:
      max = num
  mode = []
  if max == 1:
    print("No Mode")
  for key in counts.keys():
    if counts.get(key) == max:
      mode.append(key)
  return mode

def get_range(nums):
  """Takes in array of numbers. Returns range."""
  ran = nums[-1] - nums[0]
  return ran

def get_quartiles(nums):
  q2 = get_median(nums)[1]
  half_1 = nums[0:q2]
  half_2 = nums[q2+1:]
  q1 = get_median(half_1)[1]
  q3 = get_median(half_2)[1] + q2
  q1 = [nums[q1], q1+1]
  q2 = [nums[q2], q2+1]
  q3 = [nums[q3], q3+1]
  return [q1, q2, q3]

def print_formatted(mea, med, mo, ran, quarts):
  """Print formatted data."""
  print(f'Mean: {mea}')
  print(f'Median: {med[0]}, Index: {med[1]}')
  print(f'Mode: {mo}')
  print(f'Range: {ran}')
  print(f'Quartiles: Q1({quarts[0]}) Q2({quarts[1]}) Q3({quarts[2]})')

def main(nums):
  """Get data and print results."""
  nums = parse_nums(nums)
  mea = get_mean(nums)
  med = get_median(nums)
  mo = get_mode(nums)
  ran = get_range(nums)
  quarts = get_quartiles(nums)
  print_formatted(mea, med, mo, ran, quarts)

if __name__ == '__main__':
  #nums = input("Please enter the numbers:\n")
  nums1 = "5, 6, 6, 8, 7, 7, 9 , 5, 4, 8, 11, 6, 7, 8, 7"
  nums2 = "5,6,6,8,7,7,9,5,4,8,11,6,7,8,7"
  nums3 = "5,8,15,26,10,18,3,12,6,14,11"
  #main(nums1)
  #main(nums2)
  main(nums3)
