import time

discs = int(input('Enter a number of discs:'))
moves = 2 ** discs - 1

towerA = []
towerB = []
towerC = []

# append discs into towerA list
for j in range(1,discs + 1):
    towerA.append(j)

print('A',towerA)
print('B',towerB)
print('C',towerC)

# if odd number of moves, the moves are different.
if discs % 2 == 1:
    # iterate the number of total moves
    for i in range(1,moves + 1):
        time.sleep(0)
        # the 1st, 4th, 7th, etc. will be between the a and c poles
        if i % 3 == 1:
            if len(towerA) == 0:
                temp = towerC.pop(0)
                print('move c to a')
                towerA.append(temp)
            elif len(towerC) == 0:
                temp = towerA.pop(0)
                print('move a to c')
                towerC.append(temp)
            elif towerC[0] > towerA[0]:
                temp = towerA.pop(0)
                print('move a to c')
                towerC.append(temp)
            elif towerA[0] > towerC[0]:
                temp = towerC.pop(0)
                print('move c to a')
                towerA.append(temp)
            towerA.sort()
            towerB.sort()
            towerC.sort()
            print('A',towerA)
            print('B',towerB)
            print('C',towerC)
                        
        elif i % 3 == 2:
            # the 2nd, 5th, 8th, etc. will be between the a and b poles
            if len(towerA) == 0:
                temp = towerB.pop(0)
                print('move b to a')
                towerA.append(temp)
            elif len(towerB) == 0:
                temp = towerA.pop(0)
                print('move a to b')
                towerB.append(temp)
            elif towerB[0] > towerA[0]:
                temp = towerA.pop(0)
                print('move a to b')
                towerB.append(temp)
            elif towerA[0] > towerB[0]:
                temp = towerB.pop(0)
                print('move b to a')
                towerA.append(temp)
            towerA.sort()
            towerB.sort()
            towerC.sort()
            print('A',towerA)
            print('B',towerB)
            print('C',towerC)
            
        elif i % 3 == 0:
            # the 3rd, 6th, 9th, etc. will be between the b and c poles
            if len(towerC) == 0:
                temp = towerB.pop(0)
                print('move b to c')
                towerC.append(temp)
            elif len(towerB) == 0:
                temp = towerC.pop(0)
                print('move c to b')
                towerB.append(temp)
            elif towerB[0] > towerC[0]:
                temp = towerC.pop(0)
                print('move c to b')
                towerB.append(temp)
            elif towerC[0] > towerB[0]:
                temp = towerB.pop(0)
                print('move b to c')
                towerC.append(temp)
            # sort the lists to make them maintain the correct position
            # to be popped
            towerA.sort()
            towerB.sort()
            towerC.sort()
            print('A',towerA)
            print('B',towerB)
            print('C',towerC)
           


else:
    for i in range(1,moves + 1):
        time.sleep(0)
        if i % 3 == 1:
            # the 1st, 4th, 7th, etc. will be between the a and b poles
            if len(towerA) == 0:
                temp = towerB.pop(0)
                print('move b to a')
                towerA.append(temp)
            elif len(towerB) == 0:
                temp = towerA.pop(0)
                print('move a to b')
                towerB.append(temp)
            elif towerB[0] > towerA[0]:
                temp = towerA.pop(0)
                print('move a to b')
                towerB.append(temp)
            elif towerA[0] > towerB[0]:
                temp = towerB.pop(0)
                print('move b to a')
                towerA.append(temp)
            towerA.sort()
            towerB.sort()
            towerC.sort()
            print('A',towerA)
            print('B',towerB)
            print('C',towerC)
                        
        elif i % 3 == 2:
            # the 2nd, 5th, 8th, etc. will be between the a and c poles
            if len(towerA) == 0:
                temp = towerC.pop(0)
                print('move c to a')
                towerA.append(temp)
            elif len(towerC) == 0:
                temp = towerA.pop(0)
                print('move a to c')
                towerC.append(temp)
            elif towerC[0] > towerA[0]:
                temp = towerA.pop(0)
                print('move a to c')
                towerC.append(temp)
            elif towerA[0] > towerC[0]:
                temp = towerC.pop(0)
                print('move c to a')
                towerA.append(temp)
            towerA.sort()
            towerB.sort()
            towerC.sort()
            print('A',towerA)
            print('B',towerB)
            print('C',towerC)

            
        elif i % 3 == 0:
            # the 3rd, 6th, 9th, etc. will be between the b and c poles
            if len(towerC) == 0:
                temp = towerB.pop(0)
                print('move b to c')
                towerC.append(temp)
            elif len(towerB) == 0:
                temp = towerC.pop(0)
                print('move c to b')
                towerB.append(temp)
            elif towerB[0] > towerC[0]:
                temp = towerC.pop(0)
                print('move c to b')
                towerB.append(temp)
            elif towerC[0] > towerB[0]:
                temp = towerB.pop(0)
                print('move b to c')
                towerC.append(temp)
            towerA.sort()
            towerB.sort()
            towerC.sort()
            print('A',towerA)
            print('B',towerB)
            print('C',towerC)


