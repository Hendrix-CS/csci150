hello = "zebra"
shoes = 73
z = 5
msg = "hello"
if shoes > z * 7 or msg == "hi":
    z = 7
    if msg == hello:
        z = z + 12
    else:
        z = shoes + z
    shoes = 2
else:
    shoes = z
