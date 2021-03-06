# PolyMult
Recursive FFT polynomial multiplication.

This is an implementation of the method laid out in Ando Emerencia's paper on Huge integer multiplication: http://www.cs.rug.nl/~ando/pdfs/Ando_Emerencia_multiplying_huge_integers_using_fourier_transforms_paper.pdf
## Usage
The class multiplies two polynomials together using the Fast Fourier Transform. To achive this it calculates the complex roots of unity.

The polynomials fed to the class must be in list form:
```
a_0 + a_1*x + ... + a_(n-1)*x^(n-1)
is
a = [a_0, a_1, ..., a_(n-1)]
```
Further the way that this method works is that there needs to be 2 polynomials, of the same degree (n-1), that are padded with zeros such that both lists have their number of elements being a power of two.
```
a = [a_0, a_1, ..., a_(n-1), 0, 0, ..., 0]
b = [b_0, b_1, ..., b_(n-1), 0, 0, ..., 0]

val = PolyMult().PolyMult(a,b)
```
This will then produce a list of complex valued enteries where the modulus of each is equal to the coefficient of the respective degree.
### IntMult
This class adds the functionality for integer multiplication. example
```
val = IntMult().int_mult(a,b)
```
It is currently able to perform correct evaluations up and including 17 digit numbers. After that it appears that the roundoff errors compound enough to make the evaluation wrong after around the 17th digit in the product.
