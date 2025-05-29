# Data structures are building blocks for any software program
# As a swe, you need to find the right data structure for each program
def get_squared_numbers(numbers):
  squared_nums = []
  for n in numbers:
    squared_nums.append(n^2)
  return squared_nums

# The above has a time complexity of O(n);

def find_first_pe(prices, eps, index):
  pe = prices[index]/eps[index]
  return pe

# The above has a time complexity of O(1);

def t_square(numbers):
  for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
      if numbers[i] == numbers[j]:
        print(f"${numbers[i]} is a duplicate.")

# The above has a time complexity of O(n^2);
numbers = [3,6,2,4,5,3,6,8,9]
duplicate = None
for i in range(len(numbers)):
  for j in range(i+1, len(numbers)):
    if numbers[i] == numbers[j]:
      duplicate = numbers[i]
      break
# n^2

for i in range(len(numbers)):
  if numbers[i] == duplicate:
    print(i)
# n

# time = a*n^2 + b*n + c
# hence time complexity is O(n^2)
 

# Binary search has a time complexity of O(log n);
