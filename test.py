def input_nums(n):
    xy = ["x", "y"]
    a = []
    for i in range(n):
        a.append(int(input(f"Input coordinate ({xy[i]}): ")))
    return a

def lenghts2points(a,b):
    len = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return len

print(f"Lenghts = {lenghts2points(input_nums(2),input_nums(2))}")