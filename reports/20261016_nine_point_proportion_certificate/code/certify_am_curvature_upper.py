"""Certify an upper whole-cell curvature from the previously certified lower jet entry.
Each cell record is four signed64 little-endian integers divided byS=2^50:
(w midpoint lower, wprime midpoint lower, wprime midpoint upper, inf_cell wsecond lower).
H=16384, midpoint=(2k+1)/(2H). Derivatives are in physical t, not grid coordinates.
Since |K^(j)|<=pi^j, |w'''|<=8pi^3. No author code is executed.
"""
import argparse,json,pathlib,hashlib,struct,time
from flint import arb,ctx
p=argparse.ArgumentParser();p.add_argument('--input',default='rh-research-proportion/attempt024_data.json');p.add_argument('--bits',type=int,default=160);p.add_argument('--cells',type=int,default=524288);p.add_argument('--table',default='rh-research-proportion/candidate_am_jets.i64le');p.add_argument('--out',default='rh-research-proportion/candidate_am_upper_curvature.json');args=p.parse_args();ctx.prec=args.bits
src=pathlib.Path(args.input);d=json.loads(src.read_text());cc=d['cosine_coefficients'];den=d['coefficient_denominator'];H=16384;S=2**50
pi=arb.pi();sq2=arb(2).sqrt();shift=sq2/(2*pi);m0=sq2*(1/sq2).sin();vmin=(1/sq2).cos()-arb(sum(map(abs,cc)))/den;assert vmin>0
coeff=[arb(c)/(2*den)*(-1)**j for j,c in enumerate(cc,1)];third_variation=4*pi**3/H
raw=pathlib.Path(args.table).read_bytes();assert len(raw)==32*args.cells; rows=struct.iter_unpack('<qqqq',raw); correction=(249*S+H-1)//H+2; assert 8*pi**3<249; start=time.perf_counter(); min_integer_slack=None
def floor_lower(v):return int((v*S).lower().floor().unique_fmpz())
def ceil_upper(v):return int((v*S).upper().ceil().unique_fmpz())
for k in range(args.cells):
    x=arb(2*k+1)/(2*H);R=arb(0);Rp=arb(0);Rpp=arb(0)
    for j,c in enumerate(coeff,1):
        ui=1/(x-j);vi=1/(x+j)
        R+=c*(ui+vi);Rp-=c*(ui*ui+vi*vi);Rpp+=2*c*(ui**3+vi**3)
    sn=x.sin_pi();cs=x.cos_pi();K=sn*R/pi;Kp=cs*R+sn*Rp/pi;Kpp=-pi*sn*R+2*cs*Rp+sn*Rpp/pi
    for z in [x-shift,x+shift]:
        zi=1/z;sz=z.sin_pi();cz=z.cos_pi()
        K+=sz*zi/(2*pi);Kp+=(cz*zi-sz*zi*zi/pi)/2
        Kpp+=(-pi*sz*zi-2*cz*zi*zi+2*sz*zi**3/pi)/2
    K/=m0;Kp/=m0;Kpp/=m0
    w=K*K;wp=2*K*Kp;wpp=2*(Kp*Kp+K*Kpp)
    row=next(rows); upper=ceil_upper(wpp+third_variation); assert upper<=row[3]+correction,(k,upper,row[3]+correction)
    slack=row[3]+correction-upper; min_integer_slack=slack if min_integer_slack is None else min(min_integer_slack,slack)
    if (k+1)%131072==0:print(json.dumps({'cells':k+1,'seconds':time.perf_counter()-start}),flush=True)
meta={'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'table_sha256':hashlib.sha256(raw).hexdigest(),'builder_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),'bits':ctx.prec,'cells':args.cells,'grid':H,'scale':S,'correction_integer':correction,'minimum_integer_slack':min_integer_slack,'upper_formula':'row[3] + ceil(249*S/H) + 2','seconds':time.perf_counter()-start,'result':'PASS'}
pathlib.Path(args.out).write_text(json.dumps(meta,indent=2)+'\n'); print(json.dumps(meta),flush=True)
