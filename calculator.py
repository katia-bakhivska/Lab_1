what = input( 'What we are doing?( +, -, *, /): ')
a = float(input('Enter a first number: '))
b = float(input('Enter a second number: '))

if what == '+':
    c = a + b
    print ('Result:' + str(c))
elif what == '-':
    c = a - b
    print('Result:' + str(c))
elif what == '*':
    c = a * b
    print('Result: ' + str(c))
elif what == '/':
    c = a / b
    print('Result: ' + str(c))
else:
    print('Incorrect operation')