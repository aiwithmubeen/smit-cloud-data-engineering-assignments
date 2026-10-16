# Assignment - Python Lists Practice

# Q1
numbers = [10, 20, 30, 40, 50, 60, 70]
first = numbers[0]
middle = numbers[3]
last = numbers[-1]
print(first, middle, last)


# Q2
numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
a = numbers[:5]
b = numbers[6:]
c = numbers[::-2]
print(a)
print(b)
print(c)


# Q3
fruits = ["apple", "banana", "cherry", "mango"]
fruits[1] = "orange"
fruits.insert(2, "grapes")
fruits.remove("cherry")
print(fruits)


# Q4
numbers = [12, 45, 23, 67, 89, 34]
rev = numbers[::-1]
print(rev)
print(numbers)


# Q5
numbers = [45, 12, 89, 34, 89, 67, 45, 23]
u = sorted(set(numbers))
print(u[-2])


# Q6
numbers = [10, 20, 30, 40, 50, 60]
k = 2
result = numbers[-k:] + numbers[:-k]
print(result)


# Q7
numbers = [10, 20, 10, 30, 20, 40, 30, 50]
new = list(dict.fromkeys(numbers))
print(new)


# Q8
data = [[10, 20], [30, 40], [50, 60]]
flat = sum(data, [])
print(flat)


# Q9
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
main = [matrix[0][0], matrix[1][1], matrix[2][2]]
sec = [matrix[0][2], matrix[1][1], matrix[2][0]]
mid = [matrix[0][1], matrix[1][1], matrix[2][1]]
print(main, sum(main))
print(sec, sum(sec))
print(mid, sum(mid))


# Q10
data = [15, 5, 25, 10, 35, 20, 30]
u = sorted(set(data))
result = u[-3:] + u[1::-1]
print(result)