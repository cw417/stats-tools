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

def get_distributions(nums, interval):
  start = round(nums[0],-1)
  end = round(nums[-1],-1)
  distribution = {i:[] for i in range(start, end, 10)}
  for num in nums:
    key = int(num/10) * 10
    distribution[key].append(num)
  frequencies = {i:len(distribution[i]) for i in distribution.keys()}
  total_count = sum(frequencies.values())
  rel_freqs = {i:round((frequencies.get(i)/total_count),2) for i in frequencies.keys()}
  percents = {i:round(rel_freqs.get(i)*10,2) for i in rel_freqs.keys()}
    
  return distribution, frequencies, rel_freqs, percents
  
def print_chart(interval, data):
  lines = {i:f'| {i} and up to {i+interval}' for i in data[0].keys()}
  for key in lines.keys():
    lines[key] = f'{lines.get(key)} | {str(data[1].get(key)).rjust(3, " ")} | {"{:.2f}".format(data[2].get(key)).rjust(4, " ")} | {str(data[3].get(key)).rjust(3, " ")} |'
  print("|{}|{}|{}|{}|".format("Values".center(17,"_"), "Freqs", "RelF".center(6,"_"), "%".center(5,"_")))
  for v in lines.values():
    print(v)



if __name__ == '__main__':
  nums = [23, 27, 29, 30, 31, 32, 32, 33, 34, 34, 35, 35, 35, 36, 37, 37, 38, 39, 39, 40, 40, 41, 42, 42, 42, 43, 43, 44, 44, 45, 45, 46, 46, 46, 47, 47, 48, 48, 49, 50, 51, 51, 52, 54, 56, 57, 59, 59, 63, 69]
  interval = 10
  #nums = input("Please enter the numbers separated by commas:\n")
  #interval = input("Please enter an interval:\n")
  nums = parse_nums(nums)
  print_chart(10, get_distributions(nums, interval))