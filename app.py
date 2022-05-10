import stats
import freq_distrib
import leaf
import permutes

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

def get_num_input():
  inp = input("\nPlease enter a string of numbers separated by commas:\n")
  return parse_nums(inp)

if __name__ == '__main__':
  run = True
  nums = []
  while run == True:

    # options and input
    print("\nOPTIONS MENU:")
    print("Enter 'q' to quit")
    print("(0) - Re-enter numbers")
    print("(1) - Descriptive Statistics")
    print("(2) - Leaf and Stem Plot")
    print("(3) - Frequency Distribution Chart")
    print("(4) - Permutations and Combinations")
    print("Please select an option:")
    action = input("")
    action = action.lower()

    if action == 'q':
      exit()

    if (nums == [] and action != "4"):
      nums = get_num_input()

    # re-enter numbers
    if action == "0":
      nums = get_num_input()

    # print total, if numbers entered
    if action != "4":
      print(f"\nCount of numbers entered: {len(nums)}")

    # descriptive stats
    if action == "1":
      stats.main(nums)

    # leaf and stem plot
    if action == "2":
      leaf.main(nums)

    # frequency distribution chart
    if action == "3":
      freq_distrib.main(nums)

    # permutations and combinations
    if action == "4":
      permutes.main()