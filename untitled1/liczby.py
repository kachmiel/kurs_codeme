#koszt wyprawy = (( litry / kilometry) * 120) * 5.04

#l_per_100 = 6.4
#distance = 120
#price_per_l = 5.04

#total = price_per_l * distance/100 * l_per_100
#print(total)



l_per_100 = float(input("Podaj spalanie na 100 km: "))
distance = int(input("Jak daleko jedziemy? "))
price_per_l = 5.04

total = price_per_l * distance/100 * l_per_100
print(round(total, 2))