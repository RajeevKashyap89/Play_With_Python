fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)



##Exercises

lst = []

fruits = ['banana', 'orange', 'mango', 'lemon', 'pineapple', 'watermelon']

print(len(fruits))

print(fruits[0], fruits[(len(fruits))//2],fruits[len(fruits)-1])



mixed_data_types = ['raj', 25 , 5.8 , 'married']
print(mixed_data_types)


it_companies = ['Meta', 'Google', 'Apple' , 'Netflix' , 'Amazon']
it_companies.append('Uber')
print(it_companies)

it_companies_joined = "#;".join(it_companies)
print(it_companies_joined)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)
    

it_companies.remove(it_companies[0])
print(it_companies)     


del it_companies
#print(it_companies)


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()

print(min(ages))
print(max(ages))
print(sum(ages)/len(ages))


countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

scandic_countries = countries[ -4 : ]
print(scandic_countries)

first, second, third, *scandic_countries = countries

print(first, second, third, scandic_countries)


