#text = input("sprawdź czy wprowadzone wyrażenie jest palindromem:", palindrom)
#palindrom = ([0:-1]=[-1:0])

palindrom = "Kobyla ma maly bok"
palindrom = palindrom.replace(" ", "")
palindrom = palindrom.lower()
print(palindrom == palindrom[::-1])
