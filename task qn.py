1.#reverse

def reverse_string(s):
    return s[::-1]
text = "Hello"
print("Reversed string:", reverse_string(text))

2.#prime

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
num=int(input("enter number:"))
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is  not a prime number")

numbers = [10, 20, 4, 45, 99, 99]

3.# Second largest number
largest = 0
second_largest = 0
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
if second_largest == 0:
    print("No second largest number")
else:
    print("Second largest number is:", second_largest)
    
4.#merge
    
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

5.# Merge and sort
merged_list = list1 + list2
merged_list.sort()

print("Merged Sorted List:", merged_list)

6.#duplicate

def remove_duplicates(input_list):
    result = []
    for item in input_list:
        if item not in result:
            result.append(item)
    return result

my_list = [1, 2, 2, 3, 4, 3, 5]
new_list = remove_duplicates(my_list)
print("List after removing duplicates:", new_list)

7.#vowels

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
word = "Hello World"
print("Number of vowels:", count_vowels(word))

8.#append list

def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')

print("list1 =", list1)
print("list2 =", list2)
print("list3 =", list3)


9.#missing
def find_missing_number(numbers, n):
    total = n * (n + 1) // 2  # Sum of numbers from 1 to n
    actual_sum = sum(numbers)
    return total - actual_sum
n = 10
numbers = [1, 2, 3, 4, 5, 6, 7, 9, 10]  # 8 is missing
missing = find_missing_number(numbers, n)
print("Missing number is:", missing)


10
def find_intersection(list1, list2):
    return list(set(list1) & set(list2))
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
common = find_intersection(a, b)
print("Common elements:", common)


11
def extendList(val, list=[]):
    list.append(val)
    return list
list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')
print("list1 =", list1)
print("list2 =", list2)
print("list3 =", list3)


12
a = [1, 2, 3]
b = a
c = a[:]
print(a == b) 
print(a is b) 
print(a == c) 
print(a is c) 

13
nums = [1, 2, 3, 4, 5]
result = ['Even' if x % 2 == 0 else 'Odd' for x in nums]
print(result)


14
a, *b, c = [1, 2, 3, 4, 5]
print(a)
print(b)
print(c)

15
words = ['banana', 'pie', 'Washington', 'book']
words.sort(key=lambda x: len(x))
print(words)

16
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a & b) 
print(a | b) 
print(a - b) 
print(a ^ b)


17
a = [True, True, False]
print(all(a))   # All True?
print(any(a))   # At least one True?


18
matrix = [[1, 2, 3], [4, 5, 6]]
transposed = list(zip(*matrix))
print(transposed)


19
def func(val, lst=[]):
    lst.append(val)
    return lst
print(func(1))
print(func(2))
print(func(3, []))
print(func(4))



