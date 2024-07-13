from datetime import datetime

'''
  display the examination schedule
'''

exam_date = input('enter comma separated exam date (mm, dd, yyyy): ')


dateObj = datetime.strptime(exam_date,'%m, %d, %Y')

formattedDate = dateObj.strftime('%m/%d/%Y')

print(formattedDate)