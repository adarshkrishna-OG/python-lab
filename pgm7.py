students = {
    "anu": 340,
    "teena": 458,
    "john": 300

}
asc_by_name=dict(sorted(students.items()))
print("sorted by name(Ascending):")
print(asc_by_name)

desc_by_name= dict(sorted(students.items(),reverse=True))
print("\nsorted by Name(descending):")
print(desc_by_name)