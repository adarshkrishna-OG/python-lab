contacts1 = {

    "sunil": "9745925673",
    "teena": "6478493758"
}
contacts2 = {
    "abhinav": "7654321098",
    "adith": "6549824860"
}
print("contact1:",contacts1)
print("contact2:",contacts2)

merged_contacts=contacts1.copy()
merged_contacts.update(contacts2)

print("merged_contacts:")
print(merged_contacts)
