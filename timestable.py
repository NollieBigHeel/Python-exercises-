n = int(input("Please choose a number: "))

line = ""

for row in range(1, n+1):
    for column in range(1, n+1):
       line = line + str(row*column) + "\t"
    line = line + "\n"

print(line)