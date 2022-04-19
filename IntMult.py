from PolyMult import PolyMult
from math import log10, log2
# This class does integer multiplication using the PolyMult class.
# It creates and pads the coefficent vectors so that no matter what
# the digit length of either one is, they will both be the same
# length and the length will be a power of 2.
def is_pow2(a):
    n = a
    while n != 1:
        if n % 2 != 0:
            return False
        n = n >> 1
    return True

# Create the integer vector.
def int_vect(a):
    vec = []
    m = a
    num_dig = int(log10(a))
    for i in range(num_dig + 1):
        res = m % 10
        vec.append(res)
        m = int(m/10)

    return vec

class IntMult:
    def int_mult(self,a,b):
        coeff_a = int_vect(a)
        coeff_b = int_vect(b)
        len_a = len(coeff_a)
        len_b = len(coeff_b)
        if is_pow2(len_a):
            m_a = int(log2(len_a))
        else:
            m_a = int(log2(len_a)) + 1
        
        if is_pow2(len_b):
            m_b = int(log2(len_b))
        else:
            m_b = int(log2(len_b)) + 1

        new_len_a = 2**m_a
        new_len_b = 2**m_b

        pad_coeff_a = []
        pad_coeff_b = []

        for val in coeff_a:
            pad_coeff_a.append(val)
        n_zero_a = 2*new_len_a - len_a
        for i in range(n_zero_a):
            pad_coeff_a.append(0)

        for val in coeff_b:
            pad_coeff_b.append(val)
        n_zero_b = 2*new_len_b - len_b
        for i in range(n_zero_b):
            pad_coeff_b.append(0)

        if len(pad_coeff_a) < len(pad_coeff_b):
            diff = len(pad_coeff_b) - len(pad_coeff_a)
            for i in range(diff):
                pad_coeff_a.append(0)

        if len(pad_coeff_b) < len(pad_coeff_a):
            diff = len(pad_coeff_a) - len(pad_coeff_b)
            for i in range(diff):
                pad_coeff_b.append(0)

        res0 = PolyMult().PolyMult(pad_coeff_a,pad_coeff_b)
        res1 = [int(round(abs(i))) for i in res0]
        return sum([res1[i]*10**i for i in range(len(res1))])
