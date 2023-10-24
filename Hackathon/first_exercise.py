#Input the whole year in string
birth_date = input()

birth_date = birth_date.split("/")

birth_year = birth_date[-1]

print( 2023 - int(birth_year)) 

#Input just the year

ano = int(input())

print(2023 - ano)