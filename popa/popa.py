def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    
    base = lst[0]
    left = list(filter(lambda x: x < base, lst))
    center = [x for x in lst if x == base]
    right = list(filter(lambda x: x > base, lst))

    return quick_sort(left) + center + quick_sort(right)


print(quick_sort())



# def bin_search(lst, val):
#     l = 0
#     h = len(lst) - 1
#     res = False
#     while l < h and not res:
#         m = (l + h) // 2
#         if lst[m] == val:
#             res = True
#             return res
#         elif val < lst[m]:
#             h = m 
#         else:
#             l = m 


# print(bin_search([x for x in range(100000000)], 54534593))
# import itertools as it


# alf = 'ABCD'
# re_pl = []
# for pl in it.product(alf, repeat=4):
#     pl = ''.join(pl)
#     re_pl.append(pl)

# f = open('c:\\Users\\Ярик\\Desktop\\C++ode\\popa\\24.txt').readline()
# for i in re_pl:
#     f = f.replace(i, '!')

# a = f.split('!')
# ans = [len(i) for i in a]
# print(max(ans))


# a = [int(i) for i in open('17.txt').readlines()]
# b = min([i for i in a if str(i)[-2:] == '11'])
# ans = []

# for i in range(len(a) - 1):
#     if ( len(str(a[i])) != 3 or len(str(a[i + 1])) != 3) and (a[i] + a[i + 1]) % b == 0:
#         ans.append(a[i] + a[i + 1])

# print(len(ans), max(ans))


# import fnmatch as fn 


# pat = '523?0?3*8'

# for i in range(1891, 10 ** 10, 1891):
#     if fn.fnmatch(str(i), pat):
#         print(i, i // 1891)


# def f(x, y):
#     if x == y:
#         return 1
#     if x > y or x == 11:
#         return 0
#     else:
#         return f(x + 1, y) + f(x * 2, y)
    
# print(f(2, 16) * f(16, 34))


# import sys
# sys.setrecursionlimit(3000)

# memo = {}

# def f(n):
#     if n in memo:
#         return memo[n]
#     if n == 1:
#         return 1
#     if n == 2:
#         return 4
#     if n > 2:
#         result = f(n - 1) + (n - 1) * f(n - 2)
#         memo[n] = result
#         return result

# print(f(1604)/f(1600))


# def f1(a, s):
#     if a >= 140 or s > 3:
#         return s == 3
#     if s % 2 == 0:
#         return any([f1(a + 1, s + 1), f1(a + 3, s + 1), f1(a * 4, s + 1) ])
#     else:
#         return all([f1(a + 1, s + 1), f1(a + 3, s + 1), f1(a * 4, s + 1) ])
    
# for a in range(1, 140):
#     if f1(a, 0):
#         print(a)
#         break

# print()
# def f2(a, s):
#     if a >= 140 or s > 4:
#         return s == 2 or s == 4
#     if s % 2 == 0:
#         return all([f2(a + 1, s + 1), f2(a + 3, s + 1), f2(a * 4, s + 1) ])
#     else:
#         return any([f2(a + 1, s + 1), f2(a + 3, s + 1), f2(a * 4, s + 1) ])
    
# for a in range(1, 140):
#     if f2(a, 0):
#         print(a)


# def f3(a, s):
#     if a >= 140 or s > 2:
#         return s == 2
#     if s % 2 == 0:
#         return all([f3(a + 1, s + 1), f3(a + 3, s + 1), f3(a * 4, s + 1) ])
#     else:
#         return any([f3(a + 1, s + 1), f3(a + 3, s + 1), f3(a * 4, s + 1) ])
    
# for a in range(1, 140):
#     if f3(a, 0):
#         print(a)

# def f(x, a):
#     return ((x & a != 0) <= ((x & 14 == 0) <= (x & 17 != 0)))


# for a in range(1000, 0 , -1):
#     fl = 1
#     for x in range(1, 100000):
#         if not(f(x, a)):
#             fl = 0
#             break
#     if fl:
#         print(a)
#         break
# for x in '0123456789a':
#     a = f'1800{x}6'
#     b = f'6{x}107'
#     c = f'1{x}63'
#     if (int(a, 11) + int(b, 11) - int(c, 11)) % 7 == 0:
#         print((int(a, 11) + int(b, 11) - int(c, 11)) // 7)
#         break

# import math


# def prime(x):
#     return x > 1 and all(x % i != 0 for i in range(2, int(math.sqrt(x)) + 1))


# for i in range(100):
#     s = '>' + '0' * 56 + '1' * 49 + '2' * i
#     while '>1' in s or '>2' in s or '>0' in s:
#         if '>1' in s:
#             s = s.replace('>1', '12>', 1)
#         if '>2' in s:
#             s = s.replace('>2', '5>', 1)
#         if '>0' in s:
#             s = s.replace('>0', '22>', 1)

#     if prime(int(sum(map(int, s[:-1])))):
#         print(i)



# from math import *

# def parash_Vy_t():
#     g = 9.81
#     m = 0.8
#     H = 100
#     Vy = 0
#     Vx = 20
#     cx = 1.1
#     cy = 1.1
#     S = 0.0063
#     Fw = 5
#     t = 0
#     Sp = 0.08
#     cyp = 3.4
#     al = 30 * pi / 180
#     ro = 1.22
#     for _ in range(0, 150000):
#         Dt = 0.00001
#         L = 0.5 * cy * ro * S * Vy ** 2
#         a = (L - Fw * 0.5 - m * g) / m
#         H = H + Vy * Dt + (a * Dt ** 2) / 2
#         Vy = Vy + a * Dt
#         t += Dt
#         print(Vy,'|', H,'|', a,'|', t)
#     while H > 0:
#         Dt = 0.00001
#         L = 0.5 * cyp * ro * Sp * Vy ** 2
#         a = (L - Fw * 0.5 - m * g) / m
#         H = H + Vy * Dt + (a * Dt ** 2) / 2
#         Vy = Vy + a * Dt
#         t += Dt
#         print(Vy,'|', H,'|', a,'|',  t)

# def parash_Vx():
#     g = 9.81
#     m = 0.8
#     H = 100
#     Vy = 0
#     Vx = 20
#     cx = 1.1
#     cy = 1.1
#     S = 0.0063
#     Fw = 5
#     t = 0
#     Sp = 0.08
#     cyp = 3.4
#     al = 30 * pi / 180
#     ro = 1.22
#     for _ in range(0, 1205250):
#         Dt = 0.00001
#         Q = 0.5 * cx * ro * S * Vx ** 2
#         a = (Fw * cos(al) - Q) / m
#         Vx = Vx + a * Dt
#         t += Dt
#         print(Vx,'|', a,'|', t)    

# parash_Vx()



# from ipaddress import *

# net = [bin(int(i))[2:] for i in ip_network('197.132.34.160/255.255.240.0', 0)]
# goal = bin(int(ip_address('197.132.34.160')))[2:]

# res = [i for i in net if i.count('1') % 3 == 0] 

# counter = 0
# for qur in net:
#     if qur[:-16].count('1') < qur[-16:].count('1'):
#         counter += 1
        
# print(net.index(goal), len(net), len(res), counter, sep='\n')

# def f(qur):
#     res = ''
#     while qur > 0:
#         res = str(qur % 3) + res
#         qur //= 3
#     return res

# c = set()
# for qur in range(1, 1000):
#     r_qur = f(qur)
#     if qur % 3 == 0:
#         r_qur = r_qur + r_qur[-3:]
#     else:
#         r_qur = r_qur + f((qur % 3) * 3)
#     r_qur = int(r_qur, 3)
#     if r_qur > 150:
#         c.add(qur)
        
# print(min(c))




# import matplotlib.pyplot as plt
# import numpy as np

# fig = plt.figure()
# ax1 = fig.add_subplot(111)


# r1 = 0.03
# r2 = 0.04
# def J(m, l, r):
#     Ha = 1.26
#     Hb = 0.833
#     j = (m * r**2 * (4 * (Ha - Hb) * Hb - l**2)) / l**2
#     return j

# l = [
#     0.878,
#     0.869,
#     0.876,
#     0.896
#           ]
# m_plots = [0.0261,
#            0.0782,
#            0.133,
#            0.1842
#                   ]
# y_plots  = [J(m_plots[0], l[0], r1),
#             J(m_plots[1], l[1], r1),
#             J(m_plots[2], l[2], r1),
#             J(m_plots[3], l[3], r1)
#                                 ]
# t1 = np.arange(0, 0.4, 0.2)
# plt.plot(t1, (sum(m_plots) / sum(y_plots)) * t1, lw=1)
# plt.plot(m_plots, y_plots, marker='o', fillstyle='full', color='black', lw=0)
# plt.grid(1)
# plt.show()


# print(len([i for i in [input() for _ in range(8)] if (int(i) % 3 == 0 and i[-1] == '4')]))

# arr = [input() for _ in range(8)]
# counter = 0

# for i in arr:
#     if int(i) % 3 == 0 and i[-1] == '4':
#         counter += 1
# print(counter)




# l1 = [1,2,3]
# l2 = [4,6,7]

# dif = 0
# ans = []

# if len(l1) > len(l2):
#     max_len, arr_max = len(l1), l1
#     min_len = len(l2)
# else:
#     max_len, arr_max = len(l2), l2
#     min_len = len(l1)
        
# for i in range(min_len):
#     if dif == 0:
#         ans.append((l1[i] + l2[i]) % 10)
#     else:
#         ans. append((l1[i] + l2[i] + dif) % 10)
#         dif = 0
#     dif = (l1[i] + l2[i] + dif) // 10
            
# for n in range(min_len, max_len):
#     if dif == 0:
#         ans.append(arr_max[n] % 10)
#     else:
#         ans. append((arr_max[n] + dif) % 10)
#         dif = 0
#     dif = (arr_max[n] + dif) // 10
    
# if dif == 0:
#     print(ans)
# else:
#     ans.append(dif)
#     print(ans)


# nums = [2,4,6,7]
# target = 6
# numMap = {}
# n = len(nums)

# # Build the hash table
# for i in range(n):
#     numMap[nums[i]] = i
# print(numMap)
# print()
# # Find the complement
# for i in range(n):
#     complement = target - nums[i]
#     if complement in numMap and numMap[complement] != i:
#         print( [i, numMap[complement]])

#  # No solution found


#s = input()

#print(max(s, key=s.count), s.count('p'), s.count('w'))


#P.S. ��� �� ���� ������ ������ ��������������� a = format(a, 'b') , b � ���� ������ � ��������� �������� ����� ���������� � 2-����� �������.

# s - ������, ����� �� ���������, ������������ �� ���������;
#b - �������� ������;
#� - ����������� ����� ����� � ������ Unicode;
#d - ���������� ������;
#e - ������� ������, �� �������� ������ e;
#E - ������� ������, � E ������� ���������;
#f - ������ ����� � ��������� �������;
#F - ������ ����� � ��������� �������, ������� �������;
#g - ����� ������, ������ �������;
#G - ����� ������, ������� �������;
#o - ������������ ������;
#x - ����������������� ������, ������ �������;
#X - ����������������� ������, ������� �������;
#n - ������ ����� �����;
#%- ���������� ������. �������� ����� �� 100 � ���������� f ��� ������. � ����� �������� %;
##- �������������� ������� ������ ���������� �������, �������� � ��������� b, o, x


#for a in range(1, 50):
#    for c in range(1, a):
#        for d in range(1, c):
#            for b in range(1, d):
#                if a ** 3 + b ** 3 == c ** 3 + d ** 3:
#                    print(a ** 3 + b ** 3)




#collection = []
#collection_del_sums = []
#max_sum = -1
#max_index = -1
#start = int(input())
#end = int(input()) + 1

#for i in range(start, end):
#    collection.append(i)
    
#for u in collection:
#    collection_del = set()
#    for q in range(1, int(u**0.5) + 1):
#        if u % q == 0:
#            collection_del.add(q)
#            collection_del.add(u // q)
#    collection_del_sums.append((u, sum(collection_del)))
#    collection_del = []
    
#for cur_index, cur_sum in collection_del_sums:
#    if max_sum <= cur_sum:
#        max_index, max_sum = cur_index, cur_sum

#print(max_index, max_sum)  



#a = 'fUnk Jopa'
#print(a.capitalize()) - Funk jopa
#print(a.lower()) - funk jopa
#print(a.upper()) - FUNK JOPA
#print(a.swapcase()) - FuNK jOPA
#print(a.title()) - Funk Jopa
#print(a.isupper(), a.islower(), a.isdigit())
#print(a.endswith('a'))
#print(a.startswith('f'))
#print(a.split('U')) - ['f', 'nk Jopa']
#print(a.count('f')) - 1
#print(a.rfind('U')) == a.rindex('U') - 1
#print(a.find('U')) == a.index('U') - 1
#print(a.replace('U', 'u', 1)) - funk Jopa
 
#a = '   v   '
#print('1' + a.strip() + '1')
#print('1' + a.lstrip() + '1')
#print('1' + a.rstrip() + '1')


#a = [2, 5, 6, 65, 56]
#a.insert(0, 12) # ������, ������
#print(a)
#a.pop(0) # �������� �� �������
#print(a)
#a.remove(6) # �������� �� �������
#print(a)
#b = [4, 7, 234, 5]
#a.extend(b) # ���������� �������
#print(a, b)
#a.reverse() # == a[::-1], == reversed(a)
#print(a)
#a.clear() # ������ �������
#print(a)




##from datetime import datetime
##start_time = datetime.now()

##arr5 = [i ** 5 for i in range(2, 150)]                           # ������ ����� ��������
##abc = set(a + b + c for a in arr5 for b in arr5 for c in arr5)   # �������� ���� �^5+b^5+ c^5
##de =  set(e - d  for e in arr5 for d in arr5 if e - d > 0)       # �������� �������� �^5 - d^5
##res = abc & de                                                   # ����������� ���������

### ������� a b c ��� ������ �������
##abc_res = [[a + b + c, a, b, c] for a in arr5 for b in arr5 for c in arr5 if a + b + c in res]  

### ������� d e ��� ������ ������� 
##de_res = [[e - d, e , d]  for e in arr5 for d in arr5 if (e - d in res) ]

##elist = []
##for i_res in res:            #  ��������� ����������
##    for i_abc in abc_res:                
##        if i_res == i_abc[0]:
##            aa, bb, cc = i_abc[1:]   
##    for i_de in de_res:
##        if i_res == i_de[0]:
##            ee, dd = i_de[1:]
##    if ee not in elist:     
##        elist.append(ee)
##        aa, bb, cc, dd, ee = sorted([round(aa**0.2), round(bb**0.2), round(cc**0.2), round(dd**0.2), round(ee**0.2)])
##        print(aa, bb, cc, dd, ee,'a+b+c+d+e=',aa + bb + cc + dd + ee)

#end_time = datetime.now()
#print('Duration: {}'.format(end_time - start_time))


#for i in range(10):
#    for z in range(20):
#        for x in range(100):
#            if (i * 10 + z * 5 + x * 0.5 == 100) and (i + z + x == 100):
#                print(f'{i =} {z =} {x =}')
#                break


#mult = 1
#for i in range(1, 11):
#   if i % 2 == 0:
#      continue
#   if i % 9 == 0:
#      break
#   mult *= i
#print(mult)



#def d(x): 
#    a = set()
#    for i in range(1, int(x**0.5) + 1):
#        if x % i == 0:
#            a.add(i)
#            a.add(x // i)
#    return sum(a)
#print(d(70))

#a = int(input())
#[print(f'{a} x {i} = {a * i}') for i in range(1, 11)]



#out = []
#a = input()
#ssum = 0
#while a != 'END':
#    out.append(int(a))
#    a = input()
#d, ost = map(int, input().split())
#for i in a:
#    if (i % d) == ost:
#        ssum += i
#print(ssum)        

#s = 'kapibara'
#print(s.find('b'), s.rfind('a'), s.index('i'))

#mass = [[5, 3, 6], [1, 4, 8], [10, 3, 7], [2, 3, 10], [9, 3, 9]]
#for x, y, z in mass:
#    if not x > 10 and y != 3 or z <= 7:
#        print(f'{x = } {y = } {z = }')

#a, b = [int(input()) for _ in range(2)]
#[print(i) for i in range(a, b - 1, -1)] if a > b else [print(i) for i in range(a, b + 1)]

#from math import sqrt
#a, b, c = [float(input()) for _ in range(3)]
#dis = sqrt((pow(b, 2) - 4 * a * c))
#print(* sorted({(-b + dis)/(2 * a), (-b - dis)/(2 * a)}), sep = '\n') if dis >= 0 else print('hui')

#a = []
#for i in range(3):
#    a.append((input(), len(input())))
#print(a, sep = '\n')

#num = int(input())
#black = [i for i in range(1, 11) if i % 2 == 0] + [i for i in range(11, 19) if i % 2 != 0 ]\
#+ [i for i in range(19, 29) if i % 2 == 0 ] + [i for i in range(29, 37) if i % 2 != 0 ]
#red = [i for i in range(1, 11) if i % 2 != 0] + [i for i in range(11, 19) if i % 2 == 0 ]\
#+ [i for i in range(19, 29) if i % 2 != 0 ] + [i for i in range(29, 37) if i % 2 == 0 ]
#print(red, black)

#alf = {'1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V', '6': 'VI', '7': 'VII', '8': 'VIII', '9': 'IX', '10': 'X'}
#a = input()
#if a in alf:
#    print(alf[a])
#else:
#    print('A')



#def threeSum(nums):
#    out = []
#    nums.sort()
#    for i in range(len(nums)):
#        if i > 0 and nums[i] == nums[i - 1]:
#            continue
#        j = i + 1
#        k = len(nums) - 1
#        while j < k:
#            s = nums[i] + nums[j] + nums[k]
#            if s > 0:
#                k -= 1
#            elif s < 0:
#                j += 1
#            else:
#                out.append((nums[i], nums[j], nums[k]))
#                j += 1
#                while nums[j] == nums[j - 1] and j < k:
#                    j += 1
#    return out
#print(threeSum([-1, 2, 0, -1, 1, 4]))


#def threesum(nums): 
#        nums.sort() # sorting cause we need to avoid duplicates, with this duplicates will be near to each other
#        l=[]
#        for i in range(len(nums)):  #this loop will help to fix the one number i.e, i
#            if i>0 and nums[i-1]==nums[i]:  #skipping if we found the duplicate of i
#                continue 
			
#			#now following the rule of two pointers after fixing the one value (i)
#            j=i+1 #taking j pointer larger than i (as said in ques)
#            k=len(nums)-1 #taking k pointer from last 
#            while j<k: 
#                s=nums[i]+nums[j]+nums[k] 
#                if s>0: #if sum s is greater than 0(target) means the larger value(from right as nums is sorted i.e, k at right) 
#				#is taken and it is not able to sum up to the target
#                    k-=1  #so take value less than previous
#                elif s<0: #if sum s is less than 0(target) means the shorter value(from left as nums is sorted i.e, j at left) 
#				#is taken and it is not able to sum up to the target
#                    j+=1  #so take value greater than previous
#                else:
#                    l.append([nums[i],nums[j],nums[k]]) #if sum s found equal to the target (0)
#                    j+=1 
#                    while nums[j-1]==nums[j] and j<k: #skipping if we found the duplicate of j and we dont need to check 
#					#the duplicate of k cause it will automatically skip the duplicate by the adjustment of i and j
#                        j+=1   
#        return l

#def longestCommonPrefix(v):
#        ans=""
#        v=sorted(v)
#        first=v[0]
#        last=v[-1]
#        print(v)
#        for i in range(min(len(first),len(last))):
#            if(first[i]!=last[i]):
#                return ans
#            ans+=first[i]
#        return ans
#print(longestCommonPrefix(["lover","flow","flight"]))


#def romanToInt(s):
#        l = 0
#        alf = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
#        for i in range(len(s)-1):
#            if alf[s[i]] < alf[s[i+1]]:
#                l -= alf[s[i]]
#            else:
#                l += alf[s[i]]
#        return l + alf[s[-1]]
#print(romanToInt('CVM'))
