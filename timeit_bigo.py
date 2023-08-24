# Jason Sy
# CSS 340: Applied Computing
# April 28 2022
#
# Used to measure time to load

import timeit

#
# To change data size change the listSize value in the SetupCodes
#

# find1
find1_SetupCode = '''
import random
from bigo import find1
from random import randint
testList = []
listSize = 100
for i in range(listSize):
    testList.append(random.randint(0, listSize))
'''
find1_TestCode = '''
find = 99999
find1(testList, find)
'''

# find2
find2_SetupCode = '''
import random
from bigo import find2
from random import randint
testList = []
listSize = 100
for i in range(listSize):
    testList.append(random.randint(0, listSize))
'''
find2_TestCode = '''
find = 99999
find2(testList, find)
'''

# find3
find3_SetupCode = '''
import random
from bigo import find3
from random import randint
testList = []
listSize = 100
for i in range(listSize):
    testList.append(random.randint(0, listSize))
'''
find3_TestCode = '''
find = 99999
find3(testList, find)
'''

# find4
find4_SetupCode = '''
import random
from bigo import find4
from random import randint
testList = []
listSize = 100
for i in range(listSize):
    testList.append(random.randint(0, listSize))
testList.sort()
'''
find4_TestCode = '''
find = 99999
find4(testList, find)
'''

find1 = timeit.timeit(setup = find1_SetupCode, stmt = find1_TestCode,  number = 10000)
find2 = timeit.timeit(setup = find2_SetupCode, stmt = find2_TestCode, number = 10000)
find3 = timeit.timeit(setup = find3_SetupCode, stmt = find3_TestCode, number = 10000)
find4 = timeit.timeit(setup = find4_SetupCode, stmt = find4_TestCode, number = 10000)


print("find1: {}".format(find1))
print("find2: {}".format(find2))
print("find3: {}".format(find3))
print("find4: {}".format(find4))