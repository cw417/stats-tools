from math import factorial

"""
This program calculates permutations and combinations totals for events.
It can calcluate both single and combined totals for combination events.
Only integer numbers should be used.
The values 'upper' and 'lower' are with respect to standard notation
format for permutations and combinations.
"""

def get_nums():
  """
  Get numbers from user. 
  Return as array of integers. 
  Only integer numbers should be entered by the user.
  """
  upper = int(input("Upper number?\n"))
  lower = int(input("Lower number?\n"))
  return [upper, lower]

def get_permutation(nums):
  """Takes in array of integers [upper, lower]. Return number of permutations."""
  upper = nums[0]
  lower = nums[1]
  top = factorial(upper)
  bottom = factorial(upper - lower)
  return (top / bottom) 

def get_combination(nums):
  """Takes in array of integers [upper, lower]. Return number of combinations."""
  upper = nums[0]
  lower = nums[1]
  top = factorial(upper)
  bottom = factorial(upper - lower)
  bottom = bottom * (factorial(lower))
  return (top / bottom) 

def get_combined():
  """Return number of total combinations for combined combination events."""
  e1 = get_nums()
  c1 = get_combination(e1)
  e2 = get_nums()
  c2 = get_combination(e2)
  e3 = [e1[0]+e2[0], e1[1]+e2[1]]
  c3 = get_combination(e3)
  return ((c1 * c2) / c3)

def main():
  """
  Prompts user for permutation/combination.
  If combination is selected, prompts user for single
  or combined combination event.
  Prints result.
  """
  inp = input("Permutation or combination? (p/c)\n").lower()
  if inp == "p":
    data = get_permutation()
    print(data)
  else:
    inp = input("Single or combined combination? (s/c)\n")
    if inp == "s":
      data = get_combination()
      print(data)
    else:
      data = get_combined()
      print(data)

if __name__ == '__main__':
  main()