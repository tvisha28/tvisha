import math
raw = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered = []
for value in raw:
    if not math.isnan(value):
        filtered.append(value)

print(filtered)