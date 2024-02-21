# 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13....)

last_total = 0.0
total = 1.0
last_fraction = -1/3
tracker = 2
while abs(total - last_total) > 0.0000001:
    last_total = total
    total += last_fraction #total = total + last_fraction
    denominator = tracker * 2 + 1
    if last_fraction > 0:
        denominator *= -1 #denominator = denominator * -1
    last_fraction = 1.0 / denominator
    tracker += 1 # tracker = tracker + 1

print(4 * total, tracker)
