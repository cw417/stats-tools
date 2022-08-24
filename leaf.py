def get_stems(nums, stems_per_int):
  """
  Takes in array of numbers and integer number of stems per integer.
  Returns list of stems.
  """
  stems = set([int(i) for i in nums])
  stem_set = {i for i in stems}
  width  = round((1/stems_per_int), 2)
  for i in range(stems_per_int):
    add_width = width * i
    for s in stems:
      stem = s + add_width
      stem_set.add(stem)
  return_list = list(stem_set)
  return_list.sort()
  return return_list

def make_stem_dict(nums, stems):
  """Returns dictionary of stems with associated numbers."""
  width = round((stems[1]-stems[0]), 2)
  stem_dict = {k:[] for k in stems}
  for key in stem_dict:
    for num in nums:
      if num >= key and num < key+width:
        stem_dict[key].append(num)
  for num_list in stem_dict.values():
    num_list.sort()
  return stem_dict

def remove_blank_stems(stem_dict):
  """Removes blank stems from top and bottom of stem dictionary."""
  min_checked = False
  max_checked = False

  # remove lower stems
  while min_checked == False:
    min_val = min([i for i in stem_dict.keys()])
    if stem_dict.get(min_val) == []:
      stem_dict.pop(min_val)
    else:
      min_checked = True

  # remove upper stems
  while max_checked == False:
    max_val = max([i for i in stem_dict.keys()])
    if stem_dict.get(max_val) == []:
      stem_dict.pop(max_val)
    else:
      max_checked = True

  return stem_dict

def make_leaf_plot(stem_dict):
  """Strips integers off of floats in each stem and converts decimal to int."""
  return {k:[round((i-int(k))*10) for i in v] for (k,v) in stem_dict.items() for (k,v) in stem_dict.items()}

def print_plot(leaf_plot_dict):
  print() 
  for k,v in leaf_plot_dict.items():
    line = f'{int(k)}|'
    for num in leaf_plot_dict.get(k):
      num = str(num)
      line = f'{line}{num}'
    print(line)

def check_num_type(nums):
  inp = input("Are the numbers integers or floats? (i/f)\n")
  if inp.lower() == "i":
    return [(i/10) for i in nums]
  return nums

def main(nums):
  nums = check_num_type(nums)
  stems_per_int = int(input("\nHow many stems per integer?\n"))
  stems = get_stems(nums, stems_per_int)
  stem_dict = make_stem_dict(nums, stems)
  stem_dict = remove_blank_stems(stem_dict)
  leaf_plot = make_leaf_plot(stem_dict)
  print_plot(leaf_plot)

if __name__ == '__main__':
  x = [4.8, 4.6, 4.5, 5.3, 5.5, 5.9, 5.8, 5.7, 5.4, 5.3, 4.9, 4.7, 5.3, 5.7, 5.8, 4.5, 6.0, 6.2, 6.1, 6.4, 6.6, 6.5, 6.2, 6.0, 6.1]
  y = [(i*10) for i in x]
  main(y)