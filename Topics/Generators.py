def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]
    
reverse_string = ''
for char in reverse('golf'):
    reverse_string += char
print(reverse_string)    
