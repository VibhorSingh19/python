
print("Enter any 5 numbers: ", end="")

for i in range(0, 5):
    num = int(input())
    lst.append(int(num))

for i in lst:
    if i in duplicates:
        duplicates[i] += 1
    else:
        duplicates[i] = 1

print("Duplicate found in the list are: ", end="")

for i in duplicates:
    if duplicates[i] > 1:
        print(i, " ", end="")
