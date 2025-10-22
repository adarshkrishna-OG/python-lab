str = input("enter a strting:")
if str.endswith("ing"):
    str = str + "ly"
else:
    str = str + "ing"
print("modified string:",str)
