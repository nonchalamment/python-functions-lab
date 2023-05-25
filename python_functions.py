def sum_to(n: int):
  number = 0
  for add in range(n+1):
    number += add
  return number

def largest(list: list):
  max = 0
  for num in list:
    if num > max:
      max = num
  return max

def occurrences(str1: str, str2: str):
  return str1.count(str2)

def product(*args: list):
  prod = 1
  for n in args:
    prod *= n
  return prod