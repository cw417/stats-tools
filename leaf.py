def create_chart(nums):

  nums = nums.split(", ")
  nums = [float(i) for i in nums]
  # sort nums and get sections
  nums.sort()
  stems = set([int(i) for i in nums])
  stems_per_int = 2
  divider = 1 / stems_per_int
  graph_dict = {}
  final_dict = {}

  # create dict with empty lists
  for i in stems:
    graph_dict[i] = []
    graph_dict[i+divider] = []

  # fill in dict
  for key in graph_dict:
    for num in nums:
      if num >= key and num < key+divider:
        graph_dict[key].append(num)
      
  keys = []

  for i in graph_dict.keys():
    keys.append(i)

  min_checked = False
  max_checked = False

  # remove unneeded stems
  while min_checked == False:
    min_val = keys[0]
    if graph_dict.get(min_val) == []:
      graph_dict.pop(min_val)
      keys.remove(min_val)
    else:
      min_checked = True

  while max_checked == False:
    max_val = keys[-1]
    if graph_dict.get(max_val) == []:
      graph_dict.pop(max_val)
      keys.remove(max_val)
    else:
      max_checked = True

  # remove leading integer for each number
  for key in graph_dict:
    base = int(key)
    final_dict[key] = [round((i-base)*10) for i in graph_dict.get(key)]

  # get updated keys
  keys.clear()
  for i in graph_dict.keys():
    keys.append(i)

  # print chart
  for key in final_dict:
    line = f'{int(key)}|'
    for num in final_dict.get(key):
      num = str(num)
      line = f'{line}{num}'
    print(line)

if __name__ == '__main__':
  nums = input("Please enter the list of numbers:\n")
  create_chart(nums)