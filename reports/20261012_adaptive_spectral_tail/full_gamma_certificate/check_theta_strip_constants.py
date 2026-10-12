from fractions import Fraction as F
E=F(211,128) # fourth Taylor lower bound for exp(1/2)
rho=48*E**(-9)/(1-F(81,16)*E**(-15))
C=F(8,5)*2*F(22,7)*F(65,7)*F(32,31)
assert rho<F(3,5)
assert C<100
assert F(81,16)*E**(-15)<1
print('ALL_PASS')
print('theta_ratio_upper_exact',rho)
print('theta_ratio_upper_approx',float(rho))
print('complex_m_square_constant_exact',C)
print('complex_m_square_constant_approx',float(C))
