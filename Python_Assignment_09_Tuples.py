# Assignment - Python Tuples Practice

# Q11
colors = ("red", "green", "blue", "yellow", "purple")
print(colors[1])
print(colors[-1])
print(colors[1:4])


# Q12
employee = ("Ali", 28, "Data Engineer", 150000)
name, age, job, salary = employee
print(name)
print(salary)


# Q13
tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)
combined = tuple1 + tuple2
rev = combined[::-1]
print(combined)
print(rev)


# Q14
numbers = (10, 20, 30, 20, 40, 20, 50)
print(numbers.count(20))
print(numbers.index(20))


# Q15
data = (100, 200, 300, 400, 500, 600)
a, b, *rest, last = data
print(a)
print(b)
print(last)
print(rest)


# Q16
numbers = (10, 20, 30, 40, 50)
i = numbers.index(30)
new = numbers[:i] + (300,) + numbers[i+1:]
print(new)


# Q17
students = (
    ("Ali", (85, 90, 88)),
    ("Sara", (92, 87, 95)),
    ("Ahmed", (78, 84, 80))
)
print(students[1][1][1])
ali_avg = sum(students[0][1]) / len(students[0][1])
print(ali_avg)
print(max(students[2][1]))


# Q18
employees = {
    ("Ali", 80000),
    ("Sara", 120000),
    ("Ahmed", 95000)
}
sorted_emp = sorted(employees, key=lambda x: x[1], reverse=True)
print(sorted_emp)


# Q19
matrix = ((2, 4, 6), (8, 10, 12), (14, 16, 18))
diag = (matrix[0][0], matrix[1][1], matrix[2][2])
product = diag[0] * diag[1] * diag[2]
row_sums = (sum(matrix[0]), sum(matrix[1]), sum(matrix[2]))
print(diag)
print(product)
print(row_sums)


# Q20
records = {
    ("Laptop", 120000, 5),
    ("Mouse", 1500, 20),
    ("Keyboard", 3500, 10)
}
values = [p * q for p, q in [(r[1], r[2]) for r in records]]
total = sum(values)
expensive = max(records, key=lambda x: x[1])
names = tuple(r[0] for r in records)[::-1]
print(total)
print(expensive)
print(names)