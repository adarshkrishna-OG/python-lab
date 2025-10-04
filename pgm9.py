students={
    "sunil": [85,90,78],
    "teena": [72,88,91],
    "sunil": [95,80,85]
}
for name,marks in students.items():
    total=sum(marks)
    average=sum(marks)/len(marks)
    print(f"Student:{name}")
    print(f"Marks: {marks}")
    print(f"Average marks: {average:.2f}")
    print(f"Total marks: {total}")
    print("." * 20)