"""Exact centre and compact-height prerequisites for the continuity proof."""
import sympy as s
alpha,a,t=s.symbols('alpha a t')
D=2*alpha*(37-60*alpha)/(3*(5+2*alpha-24*alpha**2))
p=4*alpha*(12*alpha-5)/(3*(2*alpha-1)*(12*alpha+5))
x2=2*(3+alpha)/(5+2*alpha-24*alpha**2)
y2=D/(2*alpha);xi=p/(4*alpha-s.Rational(5,3));up=p/(2*alpha)
al=s.Rational(47,300)
assert D.subs(alpha,al)==s.Rational(5405,8858)
assert p.subs(alpha,al)==s.Rational(611,4429)
for tt in (s.Rational(0),s.Rational(1,50)):
 xx=(x2+xi*tt).subs(alpha,al);yy=(y2+up*tt).subs(alpha,al)
 target=(D+p*tt).subs(alpha,al)
 assert 1<xx<yy<2
 assert target>1+(4*al-1)*xx
 assert target>2+(4*al-2)*xx
 assert target==2*al*yy
 assert target==2+(4*al-s.Rational(5,3))*xx
 first=(al-s.Rational(1,2))*yy+s.Rational(5,6)+xx/3+tt/3
 assert first==target
assert 0<p.subs(alpha,al)<1
assert all(4*al-r<0 for r in (1,2,s.Rational(5,3)))
print('Local-height compact t endpoints and all residual terms: PASS')
x=s.Rational(269,200);y=s.Rational(1893,1000)
eta=s.Rational(7,500);h=s.Rational(1,100);k=4;zeta=s.Rational(1,100000)
a0=s.Rational(1,6);goal=s.Rational(79,125);v=1+x-y
F=((8*a-4)/5)*y+s.Rational(2,5)+s.Rational(8,15)*(1+x)
G=4*k*h*x+k*(1-2*a)*(x-y)
Da=D.subs(alpha,a-h);pa=p.subs(alpha,a-h)
E={
 'initial':Da,
 'good row':G+1,
 'good column':G+k*v,
 'good cross':G+s.Rational(2,3)*(1+k*v),
 'Fejer error':F-4*eta/5,
 'lattice error':F-2*x/5,
 'bad modes':(a-s.Rational(1,2))*y+s.Rational(1,4)+(1+x)/3+3*Da/8+3*eta*pa/8+3*zeta/4,
 'tail Y':2*a*y,
 'tail M':1+(12*a-3)*x,
 'tail long':6+(12*a-6)*x,
 'tail cross':s.Rational(14,3)+(12*a-5)*x,
}
assert len(E)==11
values={name:s.factor(fun.subs(a,a0)) for name,fun in E.items()}
assert max(values.values())==s.Rational(379,600)
assert min(goal-val for val in values.values())==s.Rational(1,3000)
assert v==s.Rational(113,250)
assert eta+s.Rational(1,500)<s.Rational(1,50)
assert 1-a0+3*h<s.Rational(7,8)
assert s.Rational(9,14)-goal==s.Rational(19,1750)
for name,val in values.items():
 print(name, val, 'margin',goal-val)
# No pole lies at the centre, so the finite set of rational functions
# and their local-height residuals are continuous on some common interval.
for fun in [D,p,x2,y2,xi,up]:
 assert s.denom(s.cancel(fun)).subs(alpha,al)!=0
for fun in E.values():
 assert s.denom(s.cancel(fun)).subs(a,a0)!=0
print('All eleven centre margins, unchanged main scale, and continuity: PASS')
print('ALL MODEWISE UNIFORM CHECKS PASS')
