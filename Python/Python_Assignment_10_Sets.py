# Assignment - Python Sets Practice

# Q21
numbers = [10, 20, 10, 30, 40, 20, 50]
s = set(numbers)
print(s)
print(len(s))


# Q22
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a | b)
print(a & b)
print(a - b)
print(a ^ b)


# Q23
skills = {"Python", "SQL", "AWS"}
skills.add("Snowflake")
skills.add("Databricks")
skills.discard("AWS")
print(skills)


# Q24
python_students = {"Ali", "Sara", "Ahmed", "Zain"}
sql_students = {"Sara", "Ahmed", "Hamza", "Usman"}
both = python_students & sql_students
only_one = python_students ^ sql_students
print(both)
print(only_one)


# Q25
required = {"Python", "SQL"}
candidate = {"Python", "SQL", "AWS", "Snowflake"}
print(required.issubset(candidate))
print(candidate.issuperset(required))


# Q26
numbers = {1, 2, 4, 6, 8, 10}
full = set(range(1, 11))
missing = full - numbers
print(missing)


# Q27
python = {"Ali", "Sara", "Ahmed", "Zain"}
sql = {"Sara", "Ahmed", "Hamza"}
aws = {"Ahmed", "Zain", "Hamza"}

all_three = python & sql & aws
py_sql_only = (python & sql) - aws
at_least_two = (python & sql) | (python & aws) | (sql & aws)

print(all_three)
print(py_sql_only)
print(at_least_two)


# Q28
day1 = {101, 102, 103, 104}
day2 = {103, 104, 105, 106}
day3 = {104, 106, 107, 108}

all_days = day1 & day2 & day3

only_one = (day1 - day2 - day3) | (day2 - day1 - day3) | (day3 - day1 - day2)

at_least_two = (day1 & day2) | (day1 & day3) | (day2 & day3)

print(all_days)
print(only_one)
print(at_least_two)


# Q29
required_perms = {"read", "write", "execute"}
user_perms = {"read", "write", "delete"}

missing = required_perms - user_perms
extra = user_perms - required_perms

print(missing)
print(extra)
print(required_perms.issubset(user_perms))


# Q30
website = {"C1", "C2", "C3", "C4", "C5"}
mobile = {"C3", "C4", "C6", "C7"}
store = {"C2", "C4", "C7", "C8"}

all_three = website & mobile & store

only_one = (
    (website - mobile - store) |
    (mobile - website - store) |
    (store - website - mobile)
)

exactly_two = (
    ((website & mobile) - store) |
    ((website & store) - mobile) |
    ((mobile & store) - website)
)

print(all_three)
print(only_one)
print(exactly_two)