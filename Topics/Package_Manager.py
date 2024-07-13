#from mypackage import arithmetic
#from mypackage import greet

from mypackage import *

import pip._vendor.requests

from math import pi as PI

url = 'https://google.com'

response = pip._vendor.requests.get(url)

print(response)
#countries = response.json()
#print(countries)



print(arithmetic.add_numbers(1,2,3,4,5))

print(greet.greet_person("Raj","A"))



print(f'value of PI is approximately {PI:.3f}')