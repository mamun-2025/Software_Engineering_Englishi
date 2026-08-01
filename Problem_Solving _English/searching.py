

"""


"""

def linear_search(arr, target):
   for index in range(len(arr)):
      if arr[index] == target:
         return index 
   return -1

numbers = [1, 23, 45, 12, 7, 9]

result = linear_search(numbers, 12)
print(f"Element found at index: {result}")




def linear_search(arr, target):
   for index, value in enumerate(arr):
      if value == target:
         return index 
   return -1

numbers = [1, 23, 45, 12, 7, 9]
result = linear_search(numbers, 12)
print(f"Element found at index: {result}")


# 1. একটি List-এ 50 আছে কি না বের করো
numbers = [1, 20, 30, 50, 23]
found = False 

for num in numbers:
   if num == 50:
      found = True
      break 

if found:
   print("50 found in the list.")
else:
   print("50 not found in the list.")


# 2. ২. একটি Function লেখো যা Target-এর Index Return করবে
def find_index(arr, target):
   for index, value in enumerate(arr):
      if value == target:
         return index 
   return -1

numbers = [1, 20, 30, 50, 23]
print(find_index(numbers, 50))



# 3.যদি Target না থাকে তাহলে "Not Found" Print করো
def find_index(arr, target):
   for index in range(len(arr)):
      if arr[index] == target:
         return index 
   return "Not found"

numbers = [1, 20, 30, 50, 23]
result = find_index(numbers, 100)
print(result)


# 4. List-এ "Python" আছে কি না খুঁজে বের করো
languages = ["java", "c++", "python", "javascript"]
found = False 

for language in languages:
   if language.lower() == "python":
      found = True
      break 

if found:
   print("Python found in the list.")
else:
   print("Python not found in the list.")


# 5. একটি List-এ প্রথম Negative Number-এর Index বের করো
numbers = [5, 8, 3, -7, 10]

def find_first_negative_index(arr):
   for index, value in enumerate(arr):
      if value < 0:
         return index 
   return -1

result = find_first_negative_index(numbers)
print(result)


# 6. True বা False Return করবে
def contains_target(arr, target):
   for value in arr:
      if value == target:
         return True
   return False 

numbers = [1, 20, 30, 40, 50, 23]
print(contains_target(numbers, 30))
print(contains_target(numbers, 100))


# 7. একটি List-এ শেষ Negative Number-এর Index বের করো
numbers = [5, 8, -3, 7, -10]

last_index = -10

for index in range(len(numbers)):
   if numbers[index] < 0:
      last_index = index 

print(last_index)


# 8. একটি List-এ কতবার Target এসেছে তা গণনা করো
numbers = [1, 20, 30, 40, 50, 23, 30, 30]
target = 30

count = 0

for num in numbers:
   if num == target:
      count += 1

print(f"{target} appears {count} times in the list.")


# 9. একটি List-এ সব Even Number-এর Index বের করো
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_indices = []

for index, value in enumerate(numbers):
   if value % 2 == 0:
      even_indices.append(index)

print(f"Indices of even numbers: {even_indices}")


# 10. একটি List-এ সবগুলো Index Print করো যেখানে Target আছে
numbers = [1, 20, 30, 40, 50, 23, 30, 30]
target = 30

for index, value in enumerate(numbers):
   if value == target:
      print(f"Target {target} found at index: {index}")

      