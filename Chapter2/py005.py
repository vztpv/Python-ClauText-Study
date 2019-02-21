# 2-5 problem1, problem2?, problem3

table = { 'name' : '홍길동', 'birth' : 1128, 'age' : 30 }

print(table)

a = { }
a['name'] = 'python'
a[('a',)] = 'python'
a[250] = 'python'

print(a)

a = { 'A':90, 'B':80 }
#if False == 'C' in a :
#   a['C'] = 70
#print(a['C'])
print(a.get('C', 70))
