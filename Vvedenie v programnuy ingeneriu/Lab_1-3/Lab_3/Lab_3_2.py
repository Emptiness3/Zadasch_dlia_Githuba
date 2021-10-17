CharactersDict = {
  0: ['', '', '', '', ''],
  1: [2, 0, 0, 1, 3],
  2: [2, 0, 3, 1, 2],
  3: [2, 1, 0, 3, 2],
  4: [1, 2, 1, 2, 1]}
def FindBestChDict():
  print('Обработка словаря')
  max = -1
  count = 0
  for index1 in range(len(CharactersDict[0])):
    for index2 in range(len(CharactersDict[index1])):
      if CharactersDict[index2][index1] > max:
        max = CharactersDict[index2][index1]
        count = index2
    print('Лучший персонаж по критерию %s:' % index1, count)
    max = -1
    count = 0
print('''Введите по очереди критерии условного
персонажа, который описан словарем.
Для описания критериев используйте следующие символы:
"0", "1", "2", "3"''')
for index1 in range(len(CharactersDict[0])):
  CharactersDict[0][index1] = int(input('Критерий %s: ' % index1))

FindBestChDict()