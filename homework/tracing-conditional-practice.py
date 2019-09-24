t = 5
nn = 2 + t
zebra = "fish"
if 3 * nn < t + 18:
    fish = "zebra"
    if zebra == fish:
        fish = zebra
        t = t + 1
    elif zebra == "zebra":
        t = t - 1
    else:
        zebra = fish
        t = t + 2
    nn = nn + 3

if t * 2 > nn:
    t = nn + 1
else:
    t = nn - 1

print(t)
print(nn)
print(zebra)
print(fish)
