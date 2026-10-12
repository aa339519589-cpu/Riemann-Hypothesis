"""Directed interval checks for the analytic exterior bounds, no mesh truncation."""
import mpmath as mp,json
iv=mp.iv;iv.dps=50;mp.mp.dps=70;I=iv.mpf
lo=lambda x:mp.mpf(x._mpi_[0]);hi=lambda x:mp.mpf(x._mpi_[1])
pi=iv.pi;R=I(5)/2;A=4*pi*pi*125/121
ths={j:5**j*iv.exp(-24*pi)/(1-(I(6)/5)**j*iv.exp(-11*pi)) for j in [4,6,8,10]}
S8=sum((I(n)**8*iv.exp(-pi*(n*n-1))for n in range(1,5)),I(0))+ths[8]
assert hi(S8)<2
assert hi(16+112/pi+164/pi**2+36/pi**3)<74
assert hi(8+30/pi+15/pi**2)<20
assert hi(32+360/pi+1056/pi**2+810/pi**3+90/pi**4)<402
assert hi(148*pi**4)<14800
assert hi(I(14800)/pi)<5000
assert hi(A)<49
assert lo(2*iv.exp(1))>5
assert hi(1/iv.exp(1))<lo(pi-I(3)/2)
C=sum((1/(I(j)+I(1)/4)for j in range(6)),I(0))
C0=iv.euler+pi/2+3*iv.ln(2)+iv.ln(pi)
als=[iv.ln(2)/iv.sqrt(2),iv.ln(3)/iv.sqrt(3),iv.ln(2)/2,iv.ln(5)/iv.sqrt(5)]
delta=20*A/9*49*iv.exp(-7*pi)
assert hi(abs(C-C0))<1 and hi(sum(als,I(0)))<3 and hi(delta)<1
mt=iv.sqrt(A)*iv.exp(2*R-pi*iv.exp(2*R)/2)
dtail=I(1)/16-delta-abs(C-C0)*mt**2-2*iv.sqrt(A)*iv.exp(-pi/2)*sum(als,I(0))*mt
assert lo(dtail)>hi(I(1)/50)
E=iv.exp(I(13)*R/2-I(3)*iv.exp(2*R)/2)
D1=3*iv.exp(2*R)-I(13)/2;D2=6*iv.exp(2*R)-13
assert hi(E)<lo(I(10)**-89) and lo(D1)>400
conv=12*I(5)*10**9*E/D1
scalar=I(10)**22*E**2/D2
assert hi(conv)<lo(I(10)**-76)
assert hi(scalar)<lo(I(10)**-150)
assert hi(conv)<lo(I(10)**-45) and hi(scalar)<lo(I(10)**-45)
print(json.dumps({'status':'ALL_DIRECTED_EXTERIOR_ASSERTIONS_PASS','E_R_upper':str(hi(E)),'d_tail_lower':str(lo(dtail)),'convolution_tail_upper':str(hi(conv)),'all_scalar_tails_upper':str(hi(scalar))},indent=2))
