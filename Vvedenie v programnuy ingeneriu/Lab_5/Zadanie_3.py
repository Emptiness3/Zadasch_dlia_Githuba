Words = {
	0 : 'Слеваdsfasdf',
	1 : 'Слева',
}
count = 0
len_0 = len(Words[0])
len_1 = len(Words[1])
elem_0 = Words[0]
elem_1 = Words[1]
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
