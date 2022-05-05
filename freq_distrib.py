def get_frequencies(nums, interval):
  nums = [int(i) for i in nums]
  start = round(nums[0],-1)
  end = round(nums[-1],-1)
  distrib_dict = {i:0 for i in range(start, end, interval)}
  for num in nums:
    diff = num % interval
    key = num - diff
    distrib_dict[key] += 1
  return distrib_dict 

def get_relative_frequencies(frequencies):
  total_count = sum([i for i in frequencies.values()])
  return {k:round((v/total_count),2) for (k,v) in frequencies.items()}
  
def get_percents(relative_frequencies):
  return {i:round(relative_frequencies.get(i)*100,2) for i in relative_frequencies.keys()}

def get_data(nums, interval):
  freq = get_frequencies(nums, interval)
  rel_freq = get_relative_frequencies(freq)
  perc = get_percents(rel_freq)
  return freq, rel_freq, perc

def print_chart(interval, data):
  print()
  lines = {i:f'| {i} and up to {i+interval}' for i in data[0].keys()}
  for key in lines.keys():
    lines[key] = f'{lines.get(key)} | {str(data[0].get(key)).rjust(3, " ")} | {"{:.2f}".format(data[1].get(key)).rjust(5, " ")} | {str(data[2].get(key)).rjust(5, " ")} |'
  print("|{}|{}|{}|{}|".format("Values".center(17,"_"), "Freqs", "RelF".center(7,"_"), "%".center(7,"_")))
  for v in lines.values():
    print(v)
  print()

def main(nums):
  interval = int(input("What is the interval?\n"))
  data = get_data(nums, interval)
  print_chart(interval, data)

if __name__ == '__main__':
  nums = [23, 27, 29, 30, 31, 32, 32, 33, 34, 34, 35, 35, 35, 36, 37, 37, 38, 39, 39, 40, 40, 41, 42, 42, 42, 43, 43, 44, 44, 45, 45, 46, 46, 46, 47, 47, 48, 48, 49, 50, 51, 51, 52, 54, 56, 57, 59, 59, 63, 69]
  main(nums)