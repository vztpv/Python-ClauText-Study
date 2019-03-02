# Study1
# Problem 1
A = 2
B = 3

print("{}".format(A * A + B * A))

# Problem 2
x = 1
y = 2
z = 3

print('{}'.format(y*(y+z)))
print('{}'.format((y*(y+z))**y))
print('{}'.format((y*(y+z))**(x+y)))

#chk) print(23, end=")
# Problem 3
print("23Bc7")
print("23BCDEFG\b\b\b\b\bc7") 
# Problem 3-2
a = '23'
b = 'Bc'
c = '7'
print('{}'.format(a+b+c))
# Problem 3-3
a = '237'
b = 'Bc'
print('{}'.format(a[:2]+b+c[-1:1]))

# Problem 4
a = 2.5
b = 4
c = a * b + b # 4 * a + b
print(c)

# Problem 5
x,y,z,w = 11, 5, 7, 13

print('{}'.format(w-y-z)) #
print('{}'.format(x-w+z+y))  #
print('{}'.format((z+w)*y)) #
print('{}'.format((x-w+z+y)**(-y+w-y))) # 

print('한글테스트')
# Problem 6
print('그대는\n나에게 왔다가\n떠나가네...')

# Problem 7
num = 3
print('{}'.format(0 == num))

# Problem 8
mystr = 'orange'

print(mystr[0])
print(mystr[4])
print(mystr[-3])
print(mystr[-6])

# Problem 9
N = 3

#print('{}', int())
#print('{} {}'.format(chr('a') + N), chr(int('A')+N)))

# Problem 10
num = 40 # num = input()
print('{}'.format(num % 3 == 0 or num & 3 == 0))

# bonus
a = "This is my best"
b = "Do your best"

print('{}'.format( set(a.split()) & set(b.split()) ))

# py clautext test
import ctypes


dll = ctypes.windll.LoadLibrary('C:\\Users\\vztpv\\Desktop\\Clau\\ClauTextDLLForPython\\x64\\Release\\ClauTextDLLForPython.dll')


#import sys
#sys.stdout.reconfigure(encoding='utf-8')

dll.PyClauText('''
    한글 = { 한글1 한글2 }
	
    Main = { $call = { id = 한글 } } 
    Event = {
        id = 한글

        $print = { str = { "Hello World! 한글 테스트" } }
		$print = { enter = { \\n } }
		$print2 = { { /./ } }
    }
'''.encode('ansi'))

