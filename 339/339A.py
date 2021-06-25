s = input()
a = s.count('1')
b = s.count('2')
c = s.count('3')
answer = a*'1 ' + b*'2 ' + c*'3 '
answer = answer.split(' ')
answer.remove('')
print('+'.join(answer))