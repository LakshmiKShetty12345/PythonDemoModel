values = [1, 2, "Lakshmi", 6, 7]

print(values[0])

print(values[1:3])
print(values[-1])
values.insert(3, "Shetty")

values.append("End")

values[2] = "Latha"

print(values[2])

del values[2]
print(values)

a = 2
if a == 3:
    print("If block")

else:
    print("Else Block ")

summation = 0
for i in range(1,6):
    summation = summation + i
print(summation)


