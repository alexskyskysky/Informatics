t = "1" + "5" * 25
while ("15" in t) or ("1" in t):
    if "15" in t:
        t = t.replace("15", "5551", 1)
    elif "1" in t:
        t = t.replace("1", "5", 1)
print(t.count("5"))
