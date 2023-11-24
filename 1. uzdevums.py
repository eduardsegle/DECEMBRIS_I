manejais_skaitlis = int(input("Ievadi skaitli: "))
summa = 0
for skaitlis in range(1, manejais_skaitlis + 1):
    summa += skaitlis
print(f"Summa no 1 līdz {manejais_skaitlis} ir {summa}")