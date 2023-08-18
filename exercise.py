# Task 1 - basic math operations

print('1.','48 + 99 =', 48 + 99)
print('2.','-2 - 56 =', -2 - 56)
print('3.','-650 * 4 =', -650 * 4)
print('4.','82 / 5 =', 82 / 5)
print('5.','403 % 5 =', 403 % 5)
print('6.','2 ** 9 =', 2 ** 9)
print('7.','345.132 // 3 =', 345.132 // 3)
print('8.','True * False =', True * False)
print('9.','99 / (6 -87j) =', 99 * (6 - 87j))
print('10.','10 / 3 =', round(10 / 3, 4))
print('11.','2435234.11234 / 1234.3123 =', round(2435234.11234 / 1234.3123, 3))
print('12.','123125234 // 323 =', 123125234 // 323)
g = 123125234 // 323
print('13.','784654645 & 3600=', 784654645 % 3600 )

a = 24324
print('14.', a / 7)
print('15.',round(a / 7, 2))

# Task 2 - basic math functions

import math

a= 123146
b= 3.5623
c= - 654.485
d= 0.1148 * 50
t= 40 * 5j

print('16.', max(a,b,c,d))
print('17.', max(0.14, 54, 32125, True))
print('18.',min(True, False))
print('19.',min(a,b,c,d))
print('20.',abs(-400))
print('21.',abs(a * c))
print('22.',pow(a,3,6))
print('23.',pow(a,4))
print('24.',math.ceil(a /b))
print('25.',math.ceil(7/3))
print('26.',math.floor(7/3))
print('27.',math.floor(b / d))
print('28.',b / d)
print('29.',round(g / 89, 6))
print('30.', g / 89)
print('31.',pow(3, 2))
print('32.',pow(3, 2, 3))
print('33.',4 / t)