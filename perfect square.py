start_range=int(input("enter the start range (4 digit min):"))
end_range=int(input("enter the ending range (4 digit min):"))
evendigit =[]
for num in range(start_range,end_range + 1):
    if all(int(digit) % 2 == 0 for digit in str(num)):
        sqrt = int(num** 0.5)
        if sqrt * sqrt == num:
            evendigit.append(num)
if evendigit !=[]:
    print("numbers with all even digits and are perfect square:")
    print(evendigit)
else:
    print("there are no numbers within the given range:")