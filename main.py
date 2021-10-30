shopping_dictionary = {
    "piekarnia":["chleb","bułki","pączek"],
    "warzywniak":["marchew","seler","rukola"],
    }

#Liczenie produktów, tu korzystałem z forum
i = 0
for value in shopping_dictionary:
    value_list = shopping_dictionary[value]
    how_much = len(value_list)
    i = i + how_much

#Wyświetlanie kluczy i wartość oraz napisów
for shop in shopping_dictionary:
    print("Idę do: {shop} kupuję tam: {value}".format(shop=shop, value = shopping_dictionary[shop]))

print("   ")

print("W sumie kupuję tu ", i, "produktów.")

#Wyświetla liczby podzielne przez 5, a w kolejnej lini trzecie potęgii tych liczb

for i in range(0, 101):
    if i%5==0:
        print(i)

print("A teraz trzecie potęgi liczb wyświetlonych powyżej:")

[print(i**3) for i in range(0, 101) if i%5==0]

#Wyświetla liczby podzielne przez 5, a w kolejnej lini trzecie potęgii tych liczb

[print(i) for i in range(0, 101) if i%5==0]

print("A teraz trzecie potęgi liczb wyświetlonych powyżej:")

[print(i**3) for i in range(0, 101) if i%5==0]