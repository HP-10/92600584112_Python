
import matplotlib.pyplot as plt

# Student data
students = ['Amit', 'Rahul', 'Priya', 'Neha', 'Raj']
marks = [85, 90, 78, 95, 88]

# Line Chart
plt.plot(students, marks)
plt.title("Line Chart")
plt.show()

# Bar Chart
plt.bar(students, marks, color='green')
plt.title("Bar Chart")
plt.show()

# Histogram
plt.hist(marks, color='orange')
plt.title("Histogram")
plt.show()

# Pie Chart
plt.pie(marks, labels=students, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()
