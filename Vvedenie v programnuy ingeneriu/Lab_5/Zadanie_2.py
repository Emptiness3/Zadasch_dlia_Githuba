Tanks = {
	1 : 250, 
	2 : 450, 
	3 : 850, 
    4 : 1000,
    5 : 1250,
    10: 2500
}


def MHP():
	max_hp = 0
	current_hp = 0
	
	for i in Tanks:
		current_hp = Tanks[i]
		if current_hp >= max_hp:
			max_hp = current_hp
	return max_hp
print("Максимальный запрос прочности из танков равен: ") 
print(MHP())
