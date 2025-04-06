customer = {
    "name": "Gaurav Kadam",
    "age": 30,
    "is_verified": True
}
print(customer["name"])

print(customer.get("birthdate"))
print(customer.get("birthdate", "Jan 1 1980"))

customer["name"] = "Jack Smith"
print(customer["name"])