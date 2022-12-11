file = open('resource/inputDay1', 'r')
Lines = file.readlines()
count = 0
values = []
currentCalories = 0

for line in Lines:
    if line.strip():
        currentCalories += int(line)
    else:
        values.append(currentCalories)
        currentCalories = 0
values.sort(reverse=True)
print(values[0])
