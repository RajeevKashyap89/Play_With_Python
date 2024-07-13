import re

## match()
## search()
## findall()
## sub()
## split()


txt = "I love to teach Python and Java"
match = re.match("I love to teach", txt, re.I)
print(match)


txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match = re.search('I',txt,re.I)
print(match)
span = match.span()
print(span)
start, end = span
substring = txt[start : end]
print(substring)

print("\n")

matches = re.findall('language', txt, re.I)
print(matches)

matches = re.findall('Python|python', txt)
print(matches)

matches = re.findall('[Pp]ython', txt)
print(matches)

replaced_txt = re.sub('[Pp]ython', 'Java', txt, re.I)
print(replaced_txt)


txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

replaced_txt = re.sub('%', '',txt)
print(replaced_txt)


txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''

print(re.split('\n', txt))


regex_pattern = r'[Aa]pple | [Bb]anana | ^do'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern,txt)
print(matches)