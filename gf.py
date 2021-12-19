#* ************************************************************************** *#
#*                                                                            *#
#*                                                                            *#
#*   gf.py       	                                                          *#
#*                                                                            *#
#*   By: yhetman <yhetman@student.unit.ua>                                    *#
#*                                                                            *#
#*   Created: 2021/11/29 21:49:25 by yhetman                                  *#
#*   Updated: 2021/11/29 21:49:26 by yhetman                                  *#
#*                                                                            *#
#* ************************************************************************** *#

from random import randint
from consts import *

def power(x, k):
    prod = 1
    while k > 0:
        if k & 1 == 1:
            prod = multiplication(x, prod)
        x = multiplication(x, x)
        k = k >> 1
    return prod


def inverse(x):
    k = (1 << m) - 2 # заменить на константу!
    return power(x, k)



def division(x, y):
    return multiplication(x, inverse(y))



def multiplication(x, y):
    mult = 0
    # print('multipl')
    # print(x.bit_length())
    while x and y:
        if y & 1 == 1:
            mult ^= x
        y >>= 1
        temp = x >> (m - 1)
        x = (x << 1) & prim_eleme
        if temp == 1:
            x ^= prim_eleme & polinominal
    # print(x.bit_length())
    return mult


