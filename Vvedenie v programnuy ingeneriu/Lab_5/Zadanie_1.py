Tanks = [
  ["IS-3", 2250],
  ["Maus", 3000 ],
  ["T110E4", 2000],
  ["FV217 Badger", 2100],
  ]


def MHP():
    max_hp = 0
    current_hp = 0

    for i in range(len(Tanks)):
        for i2 in range(len(Tanks[i])):
            current_hp = Tanks[i][i2+1]
            if current_hp >= max_hp:
                max_hp = current_hp
            break
    return max_hp
print("Максимальный запрос прочности из танков равен: ") 
print(MHP())