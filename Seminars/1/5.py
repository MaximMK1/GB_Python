# Вагоны в электричке пронумерованы натуральными
# числами, начиная с 1 (при этом иногда вагоны
# нумеруются от «головы» поезда, а иногда – с
# «хвоста»; это зависит от того, в какую сторону едет
# электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке. Напишите
# программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать
# невозможно.

# Input: 3 4(ввод на разных строках)
# Output: 6

i = int (input ("В какой вагон от головы поезда сел Витя? "))
j = int (input ("Какой номер вагона увидел Витя? "))

if i == j :
    print("Требуется информация: C какой стороны поезда идет нумерация вагонов?")
else :
     sum = i + j - 1
     print (f"Количество вагонов в поезде равно {sum}")