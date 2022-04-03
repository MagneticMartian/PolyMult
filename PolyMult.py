import cmath as cm
# Polynomial multiplication done the naive way is a O(n^2) time procedure.
# However, by introducing the FFT which is a divide and conqure algorithm
# we can change this into a O(nlog n) time algorithm. This is achived by
# using the DFT with primitive nth roots of unity. By doing so we change
# the DFT from O(n^2) to O(nlog n), thus giving the FFT.
#
# The inputs of the PolyMult function are two 2n degree padded polynomials.
# They need to be padded, due to the fact that multiplying two polynomials
# of degree n-1 will result in one polynomial of degree 2n-2. Further more
# the padding is there to ensure that 2n is a power of 2. Thus, n is also a
# power of 2.
# 
# In the particular implementation bellow, we use the complex roots of unity.
# These are used for two properties:
#     1. Reduction Property
#     2. Reflection Property
# These two properties allow us to take advantage of the divide and conqure
# nature of the FFT.
class PolyMult:
    def FFT(self, a, omega):
        n = len(a)
        if(n == 1):
            return a
        # Python treats division as a float operation.
        n_half = int(n/2)
        a_even = [0]*n_half
        a_odd = [0]*n_half
        # Spliting the coefficient vector into two half sized vectors
        for i in range(n_half):
            a_even[i] = a[2*i]
            a_odd[i] = a[2*i+1]
        # The recursive calls are taking advantage of the reduction properties
        y_even = self.FFT(a_even, omega**2)
        y_odd  = self.FFT(a_odd,  omega**2)
    
        y = [0]*n
        x = 1
        for i in range(n_half):
            y[i] = y_even[i] + x*y_odd[i]
            y[i + n_half] = y_even[i] - x*y_odd[i] # The reflective property
            x = x*omega

        return y

    def PolyMult(self, a, b):
        # This is 2n. Where n is size of the original coeffiecent vector
        n = len(a)
        omega = cm.exp(1j*2*cm.pi/n) # Implicitly a 2nth root of unity

        p = self.FFT(a, omega)
        q = self.FFT(b, omega)

        c = [p[i]*q[i] for i in range(n)]

        mult = self.FFT(c,1/(omega)) # Inverse FFT
        m = [mult[i]/n for i in range(len(mult))]
        return m

