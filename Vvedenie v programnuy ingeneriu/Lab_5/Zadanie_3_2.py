Words = [
	['Клубафыв'],
	['Клубника'],
]
count = 0
elem_0 = ''.join(Words[0])
elem_1 = ''.join(Words[1])
len_0 = len(elem_0)
len_1 = len(elem_1)
print(Words[0])
Vivod = 0

if len_0 > len_1:
	max_len = len_0
else:
	max_len = len_1

for i in range(max_len):
	try:
		if elem_0[i] == elem_1[i]:
			count += 1
	except:
		pass
Vivod = count / len_1
print("Процент сходства равен", Vivod)