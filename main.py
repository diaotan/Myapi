list1 = input().split('-')
list2 = input().split('-')
list3 = list1 + list2
A = {'3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, '10': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}
B = {'3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0, 'A': 0}
C = {}
for m in list3:
    if m not in ['2', 'B', 'C']:
        B[m] = B[m] + 1
list4 = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
for n in list4:
    if B[n] == 4:
        list4.remove(n)
list0 = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
list_04 = sorted(list(set(list0) - set(list4)))
for k in list_04:
    list5 = []
    for i in range(len(list0)):
        if i+1 < A[k]:
            list5.append(list0[i])
        if i+1 == A[k]:
            if len(list5) > 4:
                C[i] = '-'.join(list5)
            list5.clear()
m = ''
for k in C.keys():
    for n in C.keys():
        if len(C[k]) >= len(C[n]):
            m = C[k]
        else:
            m = C[n]
print(m)
