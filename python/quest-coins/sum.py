from dict import *

# for testing
merged = NTM_EARLY | NTM_OIL
sum = 0
for value in merged.values():
    sum += value

print(sum)