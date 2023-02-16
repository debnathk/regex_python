import re

x = open('regex_sum_1751776.txt')

y = []

for line in x:
    line = line.rstrip()
    y.append(re.findall('[0-9]+', line))

s_int = []
for i in range(len(y)):
    s = 0
    if len(y[i]) > 0:
        for j in range(len(y[i])):
            k = int(y[i][j])
            s += k
        s_int.append(s)

print(sum(s_int))

# Correct Answer: 405302
# Output: 405302
# Solution is correct!!!