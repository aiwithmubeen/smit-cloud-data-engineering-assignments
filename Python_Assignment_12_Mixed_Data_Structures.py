# Assignment - Python Mixed Data Structures Practice

# Q41
students = {
    "id1": {"name": "Ali", "marks": (85, 90, 88)},
    "id2": {"name": "Sara", "marks": (92, 95, 91)},
    "id3": {"name": "Ahmed", "marks": (78, 84, 80)}
}
avg1 = sum(students["id1"]["marks"]) / 3
avg2 = sum(students["id2"]["marks"]) / 3
avg3 = sum(students["id3"]["marks"]) / 3
print(avg1, avg2, avg3)

averages = {"Ali": avg1, "Sara": avg2, "Ahmed": avg3}
top = max(averages, key=averages.get)
print(top)

names = (students["id1"]["name"], students["id2"]["name"], students["id3"]["name"])
print(names)

all_marks = set(students["id1"]["marks"]) | set(students["id2"]["marks"]) | set(students["id3"]["marks"])
print(all_marks)


# Q42
employees = {
    "Ali": {"Python", "SQL", "AWS"},
    "Sara": {"Python", "Databricks", "SQL"},
    "Ahmed": {"AWS", "Snowflake", "SQL"}
}
common = employees["Ali"] & employees["Sara"] & employees["Ahmed"]
print(common)

ali_only = employees["Ali"] - employees["Sara"] - employees["Ahmed"]
print(ali_only)

all_skills = employees["Ali"] | employees["Sara"] | employees["Ahmed"]
print(all_skills)

required = {"Python", "SQL"}
qualified = []
if required.issubset(employees["Ali"]):
    qualified.append("Ali")
if required.issubset(employees["Sara"]):
    qualified.append("Sara")
if required.issubset(employees["Ahmed"]):
    qualified.append("Ahmed")
print(qualified)


# Q43
sales = (
    ("Laptop", 120000, 2),
    ("Mouse", 1500, 5),
    ("Keyboard", 3500, 3)
)
r1 = sales[0][1] * sales[0][2]
r2 = sales[1][1] * sales[1][2]
r3 = sales[2][1] * sales[2][2]
total = r1 + r2 + r3
print(total)

revenues = {sales[0][0]: r1, sales[1][0]: r2, sales[2][0]: r3}
top = max(revenues, key=revenues.get)
print(top)

print(revenues)

prices = {sales[0][1], sales[1][1], sales[2][1]}
print(prices)


# Q44
customers = {
    "C101": {"name": "Ali", "orders": [1200, 2500, 1800]},
    "C102": {"name": "Sara", "orders": [3000, 4500]},
    "C103": {"name": "Ahmed", "orders": [1500, 2000, 1000]}
}
t1 = sum(customers["C101"]["orders"])
t2 = sum(customers["C102"]["orders"])
t3 = sum(customers["C103"]["orders"])
print(t1, t2, t3)

totals = {"Ali": t1, "Sara": t2, "Ahmed": t3}
top = max(totals, key=totals.get)
print(top)

totals_tuple = (t1, t2, t3)
print(totals_tuple)


# Q45
courses = {
    "Python": {"Ali", "Sara", "Ahmed"},
    "SQL": {"Sara", "Ahmed", "Zain"},
    "AWS": {"Ali", "Ahmed", "Zain"}
}
py_sql = courses["Python"] & courses["SQL"]
py_aws = courses["Python"] & courses["AWS"]
sql_aws = courses["SQL"] & courses["AWS"]

exactly_two = (py_sql - courses["AWS"]) | (py_aws - courses["SQL"]) | (sql_aws - courses["Python"])
print(exactly_two)

all_three = courses["Python"] & courses["SQL"] & courses["AWS"]
print(all_three)

only_one = (
    (courses["Python"] - courses["SQL"] - courses["AWS"]) |
    (courses["SQL"] - courses["Python"] - courses["AWS"]) |
    (courses["AWS"] - courses["Python"] - courses["SQL"])
)
print(only_one)

unique_students = courses["Python"] | courses["SQL"] | courses["AWS"]
print(len(unique_students))


# Q46
transactions = (
    {"id": 101, "customer": "Ali", "items": [("Laptop", 120000, 1), ("Mouse", 1500, 2)]},
    {"id": 102, "customer": "Sara", "items": [("Keyboard", 3500, 2), ("Mouse", 1500, 1)]},
    {"id": 103, "customer": "Ali", "items": [("Monitor", 45000, 1)]}
)

t1 = transactions[0]["items"][0][1] * transactions[0]["items"][0][2] + transactions[0]["items"][1][1] * transactions[0]["items"][1][2]
t2 = transactions[1]["items"][0][1] * transactions[1]["items"][0][2] + transactions[1]["items"][1][1] * transactions[1]["items"][1][2]
t3 = transactions[2]["items"][0][1] * transactions[2]["items"][0][2]

revenue = t1 + t2 + t3
print(revenue)

ali_spending = t1 + t3
print(ali_spending)

largest = max(t1, t2, t3)
print(largest)

products = {
    transactions[0]["items"][0][0], transactions[0]["items"][1][0],
    transactions[1]["items"][0][0], transactions[1]["items"][1][0],
    transactions[2]["items"][0][0]
}
print(products)


# Q47
pipelines = {
    "pipeline_1": {"status": "success", "records": (1000, 1200, 1100)},
    "pipeline_2": {"status": "failed", "records": (800, 0, 0)},
    "pipeline_3": {"status": "success", "records": (1500, 1600, 1700)}
}

p1 = sum(pipelines["pipeline_1"]["records"])
p2 = sum(pipelines["pipeline_2"]["records"])
p3 = sum(pipelines["pipeline_3"]["records"])
total = p1 + p2 + p3
print(total)

failed = []
if pipelines["pipeline_1"]["status"] == "failed":
    failed.append("pipeline_1")
if pipelines["pipeline_2"]["status"] == "failed":
    failed.append("pipeline_2")
if pipelines["pipeline_3"]["status"] == "failed":
    failed.append("pipeline_3")
print(failed)

totals = {"pipeline_1": p1, "pipeline_2": p2, "pipeline_3": p3}
top = max(totals, key=totals.get)
print(top)

avg1 = p1 / 3
avg2 = p2 / 3
avg3 = p3 / 3
print(avg1, avg2, avg3)


# Q48
accounts = {
    "A101": {"holder": "Ali", "transactions": [5000, -2000, 3000, -1000]},
    "A102": {"holder": "Sara", "transactions": [10000, -3000, -2000]},
    "A103": {"holder": "Ahmed", "transactions": [7000, -1500, 2500]}
}

b1 = sum(accounts["A101"]["transactions"])
b2 = sum(accounts["A102"]["transactions"])
b3 = sum(accounts["A103"]["transactions"])
print(b1, b2, b3)

balances = {"Ali": b1, "Sara": b2, "Ahmed": b3}
top = max(balances, key=balances.get)
print(top)

withdrawals = abs(accounts["A101"]["transactions"][1]) + abs(accounts["A101"]["transactions"][3]) + abs(accounts["A102"]["transactions"][1]) + abs(accounts["A102"]["transactions"][2]) + abs(accounts["A103"]["transactions"][1])
print(withdrawals)

all_deposits = [accounts["A101"]["transactions"][0], accounts["A101"]["transactions"][2], accounts["A102"]["transactions"][0], accounts["A103"]["transactions"][0], accounts["A103"]["transactions"][2]]
print(max(all_deposits))


# Q49
users = {
    "Ali": {"purchased": {"Laptop", "Mouse"}, "wishlist": {"Keyboard", "Monitor", "Mouse"}},
    "Sara": {"purchased": {"Keyboard", "Monitor"}, "wishlist": {"Laptop", "Mouse"}},
    "Ahmed": {"purchased": {"Laptop", "Keyboard"}, "wishlist": {"Monitor", "Headphones"}}
}

at_least_two = (users["Ali"]["purchased"] & users["Sara"]["purchased"]) | (users["Ali"]["purchased"] & users["Ahmed"]["purchased"]) | (users["Sara"]["purchased"] & users["Ahmed"]["purchased"])
print(at_least_two)

ali_wish_minus = users["Ali"]["wishlist"] - users["Ali"]["purchased"]
print(ali_wish_minus)

shared_wishlist = users["Ali"]["wishlist"] & users["Sara"]["wishlist"] & users["Ahmed"]["wishlist"]
print(shared_wishlist)

all_products = (
    users["Ali"]["purchased"] | users["Ali"]["wishlist"] |
    users["Sara"]["purchased"] | users["Sara"]["wishlist"] |
    users["Ahmed"]["purchased"] | users["Ahmed"]["wishlist"]
)
print(all_products)


# Q50
company = {
    "departments": {
        "Engineering": {
            "employees": (
                ("Ali", 120000, {"Python", "AWS", "SQL"}),
                ("Sara", 150000, {"Python", "Databricks", "SQL"})
            ),
            "budget": 500000
        },
        "Analytics": {
            "employees": (
                ("Ahmed", 100000, {"SQL", "Power BI"}),
                ("Zain", 130000, {"Python", "SQL", "Tableau"})
            ),
            "budget": 400000
        }
    }
}

eng = company["departments"]["Engineering"]["employees"]
ana = company["departments"]["Analytics"]["employees"]

# 1. Payroll per department
eng_payroll = eng[0][1] + eng[1][1]
ana_payroll = ana[0][1] + ana[1][1]
print("Engineering payroll:", eng_payroll)
print("Analytics payroll:", ana_payroll)

# 2. Company payroll
company_payroll = eng_payroll + ana_payroll
print("Company payroll:", company_payroll)

# 3. Highest-paid employee
salaries = {"Ali": eng[0][1], "Sara": eng[1][1], "Ahmed": ana[0][1], "Zain": ana[1][1]}
top = max(salaries, key=salaries.get)
print("Highest paid:", top)

# 4. Skills shared by all
shared = eng[0][2] & eng[1][2] & ana[0][2] & ana[1][2]
print("Shared skills:", shared)

# 5. Engineering-only skills
eng_only = (eng[0][2] | eng[1][2]) - (ana[0][2] | ana[1][2])
print("Engineering only:", eng_only)

# 6. Remaining budget per department
eng_budget = company["departments"]["Engineering"]["budget"]
ana_budget = company["departments"]["Analytics"]["budget"]
print("Engineering remaining:", eng_budget - eng_payroll)
print("Analytics remaining:", ana_budget - ana_payroll)

# 7. Department with higher average salary
eng_avg = eng_payroll / 2
ana_avg = ana_payroll / 2
print("Engineering avg:", eng_avg)
print("Analytics avg:", ana_avg)
if eng_avg > ana_avg:
    print("Higher average: Engineering")
else:
    print("Higher average: Analytics")

# 8. Name-to-salary dictionary
name_salary = {"Ali": eng[0][1], "Sara": eng[1][1], "Ahmed": ana[0][1], "Zain": ana[1][1]}
print(name_salary)

# 9. (already covered in 1 and 2)

# 10. Is combined budget sufficient?
combined_budget = eng_budget + ana_budget
print("Combined budget:", combined_budget)
print("Sufficient:", combined_budget >= company_payroll)