"""Certified midpoint Taylor jets of w=K^2 for the fixed AM probability window.
Each cell record is four signed64 little-endian integers divided byS=2^50:
(w midpoint lower, wprime midpoint lower, wprime midpoint upper, inf_cell wsecond lower).
H=16384, midpoint=(2k+1)/(2H). Derivatives are in physical t, not grid coordinates.
Since |K^(j)|<=pi^j, |w'''|<=8pi^3. No author code is executed.
"""
import argparse,json,pathlib,hashlib,struct,time
from flint import arb,ctx
p=argparse.ArgumentParser();p.add_argument('--input',default='rh-research-proportion/attempt024_data.json');p.add_argument('--bits',type=int,default=160);p.add_argument('--cells',type=int,default=524288);p.add_argument('--out',default='rh-research-proportion/independent_am_jets');args=p.parse_args();ctx.prec=args.bits
src=pathlib.Path(args.input);d=json.loads(src.read_text());cc=d['cosine_coefficients'];den=d['coefficient_denominator'];H=16384;S=2**50
pi=arb.pi();sq2=arb(2).sqrt();shift=sq2/(2*pi);m0=sq2*(1/sq2).sin();vmin=(1/sq2).cos()-arb(sum(map(abs,cc)))/den;assert vmin>0
coeff=[arb(c)/(2*den)*(-1)**j for j,c in enumerate(cc,1)];third_variation=4*pi**3/H
outbytes=bytearray();start=time.perf_counter()
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
    record=(floor_lower(w),floor_lower(wp),ceil_upper(wp),floor_lower(wpp-third_variation))
    assert all(-2**63<v<2**63 for v in record);outbytes.extend(struct.pack('<qqqq',*record))
    if (k+1)%131072==0:print(json.dumps({'cells':k+1,'seconds':time.perf_counter()-start}),flush=True)
base=pathlib.Path(args.out);base.with_suffix('.i64le').write_bytes(outbytes)
meta={'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'builder_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),'bits':ctx.prec,'cells':args.cells,'grid':H,'scale':S,'record_schema':['w_mid_lower','wprime_mid_lower','wprime_mid_upper','wsecond_cell_lower'],'byte_order':'little','type':'signed64','derivative_coordinate':'physical t','binary_sha256':hashlib.sha256(outbytes).hexdigest(),'seconds':time.perf_counter()-start,'third_derivative_bound':'8*pi^3','cell_radius':'1/(2H)'}
base.with_suffix('.json').write_text(json.dumps(meta,indent=2)+'\n');print(json.dumps(meta),flush=True)
