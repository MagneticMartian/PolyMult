import cmath as cm

class PolyMult:
    def FFT(self, a, omega):
        n = len(a)
        if(n == 1):
            return a
    
        n_half = int(n/2)
        a_even = [0]*n_half
        a_odd = [0]*n_half
    
        for i in range(n_half):
            a_even[i] = a[2*i]
            a_odd[i] = a[2*i+1]

        y_even = self.FFT(a_even, omega**2)
        y_odd  = self.FFT(a_odd,  omega**2)
    
        y = [0]*n
        x = 1
        for i in range(n_half):
            y[i] = y_even[i] + x*y_odd[i]
            y[i + n_half] = y_even[i] - x*y_odd[i]
            x = x*omega

        return y

    def PolyMult(self, a, b):
        n = len(a)
        omega = cm.exp(1j*2*cm.pi/n)

        p = self.FFT(a, omega)
        q = self.FFT(b, omega)

        c = [p[i]*q[i] for i in range(n)]

        mult = self.FFT(c,1/(omega))
        m = [mult[i]/n for i in range(len(mult))]
        return m

