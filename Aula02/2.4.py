temp = (36.5, 37.2, 38.0, 36.8, 39.1)
for temp in temp:
    if temp < 37.5:
        print(temp,": Normal")
    elif temp > 38.5:
        print(temp,": Febre alta")
    else:
        print(temp,": Febre moderada")
