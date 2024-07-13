def http_error(status):
    match status:
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"
        case 500:
            return "Internal server error"
        case _:
            return "something's wrong with the internet"
        

print(http_error(500))        



tup = (2,2) #'abc' #4
match tup:
    case (0,0):
        print('origin')
    case (1,x):
        print(x)
    case (2,y):
        print(str(y) + "**")    
    case (x,y):
         print(x+y)
    case _:
        print('default ' + str(tup))        