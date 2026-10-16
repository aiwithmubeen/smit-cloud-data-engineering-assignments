# Assignment - Python Dictionaries Practice

# Q31
student = {"name": "Ali", "age": 22, "course": "Python", "marks": 85}
print(student["name"])
print(student["marks"])
print(student.get("city", "Karachi"))


# Q32
employee = {"name": "Sara", "salary": 100000, "department": "IT"}
employee["salary"] = employee["salary"] + employee["salary"] * 20 / 100
employee["bonus"] = 15000
employee["department"] = "Data Engineering"
print(employee)


# Q33
product = {"id": 101, "name": "Laptop", "price": 120000, "stock": 5}
print(list(product.keys()))
print(list(product.values()))
print(list(product.items()))
stock_value = product.pop("stock")
print(product)
print(stock_value)


# Q34
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 50, "d": 40}
merged = dict1 | dict2
print(merged)


# Q35
marks = {"Ali": 85, "Sara": 92, "Ahmed": 78, "Zain": 88}
highest = max(marks.values())
lowest = min(marks.values())
average = sum(marks.values()) / len(marks)
top = max(marks, key=marks.get)
print(highest)
print(lowest)
print(average)
print(top)


# Q36
employees = {
    "E101": {"name": "Ali", "salary": 80000},
    "E102": {"name": "Sara", "salary": 120000},
    "E103": {"name": "Ahmed", "salary": 95000}
}
print(employees["E102"]["salary"])
employees["E101"]["salary"] = employees["E101"]["salary"] + employees["E101"]["salary"] * 15 / 100
total = employees["E101"]["salary"] + employees["E102"]["salary"] + employees["E103"]["salary"]
print(total)


# Q37
data = {"Python": "Ali", "SQL": "Sara", "AWS": "Ahmed"}
inverse = dict(zip(data.values(), data.keys()))
print(inverse)


# Q38
order = {
    "laptop": {"price": 120000, "quantity": 2},
    "mouse": {"price": 1500, "quantity": 5},
    "keyboard": {"price": 3500, "quantity": 3}
}
sub1 = order["laptop"]["price"] * order["laptop"]["quantity"]
sub2 = order["mouse"]["price"] * order["mouse"]["quantity"]
sub3 = order["keyboard"]["price"] * order["keyboard"]["quantity"]
grand = sub1 + sub2 + sub3
discount = grand - grand * 10 / 100
print(sub1, sub2, sub3)
print(grand)
print(discount)


# Q39
employees = {
    "Ali": {"python": 90, "sql": 85, "aws": 88},
    "Sara": {"python": 95, "sql": 92, "aws": 90},
    "Ahmed": {"python": 80, "sql": 87, "aws": 84}
}
avg_ali = sum(employees["Ali"].values()) / 3
avg_sara = sum(employees["Sara"].values()) / 3
avg_ahmed = sum(employees["Ahmed"].values()) / 3
print(avg_ali, avg_sara, avg_ahmed)

averages = {"Ali": avg_ali, "Sara": avg_sara, "Ahmed": avg_ahmed}
top = max(averages, key=averages.get)
print(top)

sql_scores = {"Ali": 85, "Sara": 92, "Ahmed": 87}
print(max(sql_scores.values()))


# Q40
inventory = {
    "P101": {"name": "Laptop", "price": 120000, "stock": 5},
    "P102": {"name": "Mouse", "price": 1500, "stock": 20},
    "P103": {"name": "Keyboard", "price": 3500, "stock": 10}
}
val1 = inventory["P101"]["price"] * inventory["P101"]["stock"]
val2 = inventory["P102"]["price"] * inventory["P102"]["stock"]
val3 = inventory["P103"]["price"] * inventory["P103"]["stock"]
total_value = val1 + val2 + val3
print(total_value)

values = {"P101": val1, "P102": val2, "P103": val3}
top_item = max(values, key=values.get)
print(inventory[top_item]["name"])

inventory["P101"]["stock"] = inventory["P101"]["stock"] - 2
inventory["P102"]["stock"] = inventory["P102"]["stock"] - 5
print(inventory)