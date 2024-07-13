'''
    display the current date and time.
'''

from datetime import datetime

currDate = datetime.now()


print(currDate.strftime("%m/%d/%Y %H:%M:%S"))