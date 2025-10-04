nums = list(map(int, input ("enter a list of integers seperated by spaces: ").split()))
result = []
for n in nums:
    if n % 2 !=0:
        result.append(n)
print("enter numbers:", nums)
print("list after removing even numbers:", result)
