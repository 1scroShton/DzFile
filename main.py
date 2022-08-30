file = open("test.txt")
filee = []
for i in file:
    filee.append(i)

slovo = input("Введите слово которое хотите заменить: ")
zamena = input(f"Введите слово которым вы хотите заменить слово: {slovo}: ")
zamena_itog = filee.index(slovo+"\n")
filee[zamena_itog] = zamena


