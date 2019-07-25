from math import sqrt

#for i in range(0, len(midpoints)):
#    print(midpoints[i] * freq[i])


#total = 0

#for i in range(0, len(midpoints)):
#    total += (midpoints[i] * freq[i])

#print(total)


#for i in range(0, len(midpoints)):
#    print(midpoints[i] ** 2)


#for i in range(0, len(midpoints)):
#    print((midpoints[i] ** 2) * freq[i])


heights = [4265, 3545, 4025, 7025, 11413,
           3490, 5370, 4885, 5030, 6830,
           4450, 5775, 3945, 7545, 8450,
           3995, 10140, 6050, 10265, 6965,
           150, 8185, 7295, 2015, 5055]

# mean

mean = (sum(heights) / len(heights))

print("Mean: " + str(mean))

# median

# NOTE - modify for even-number of data

index = (((len(heights) - 1) / 2) + 1)
print("Median: " + str(sorted(heights)[int(index)]))

# mode

heights_mode = {}

for item in sorted(heights):
    if item in heights_mode:
        heights_mode[item] += 1
    else:
        heights_mode[item] = 1

max_mode = heights_mode[heights[0]]

for item in heights_mode:
    if heights_mode[item] > max_mode:
        max_mode = item

if max_mode == 1:
    max_mode = "None"

print("Mode: " + str(max_mode))

# midrange

print("Midrange: " + str((max(heights) + min(heights)) / 2))

# coefficient of variation = standard_deviation / mean  x 100

standard_deviation = sqrt(((sum([x ** 2 for x in heights])) - ((sum(heights) ** 2) / len(heights))) / len(heights) - 1)
print("Standard Deviation: " + str(standard_deviation))

print("Coefficient of Variation: " + str((standard_deviation / mean) * 100))