from fractions import Fraction as F

# Only rational constant comparisons used in the analytic tail lemma.
assert F(65,24)>F(8,3)
assert F(8,3)**8>2500
assert F(8,3)**3>9
assert F(2*65,3)<7**2
assert 3**8<2**13
assert F(81)*(F(3**8,3)+F(1,9))<2**18
assert 9*2**13<2**17
assert 1274*373<2**19
assert 118174228126<2**37
assert F(1274*373*118174228126,2**42)<2**14
assert F(2**12*3*20,40)<2**13
assert 8*2**14*2==2**18  # both analytic prefactors are strictly smaller
assert 4*65*2**18<2**27
# Cross-lattice bound for midpoint periodized input, input remote images,
# and Q^2 C_N outer-output images, all in their required norms.
tail=F(1,2**3698)+F(1,2**361)+F(1,2**348)
assert tail<F(1,2**347)<F(1,10**100)
assert F(2,2**3698)+F(1,2**361)+F(1,2**348)<F(1,2**347)
# Full Binet angle absorption follows analytically from Re z=257/4;
# its worst case coefficient denominator is at least (257/4)^18.
assert F(257,4)**18>64**18
print('PASS: exact rational constants for the stated tiny-tail lemma only')
