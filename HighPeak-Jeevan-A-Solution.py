import sys

goodies = []

numberOfGoodies = int(input("Enter number of goodies: "))

print("Reading goodies: ")

for i in range(0, numberOfGoodies):
    ele = int(input())
    goodies.append(ele)

goodies.sort()

numberOfEmployees = int(input("Enter the number of employees: "))

result = sys.maxsize

start = 0
end = numberOfEmployees - 1

while end < numberOfGoodies:
    result = min(result, goodies[end] - goodies[start])
    start += 1
    end += 1
print("The result is: ")
print(result)