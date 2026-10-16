"""Independent Arb cell lower bounds for the fixed AM window from attempt024.
The exact input density v(u)=cos(sqrt(2)u)+sum c_j cos(2pi j u), |u|<=1/2,
has mass m0=sqrt(2)sin(1/sqrt(2)). Positivity is certified below.
Taylor bound for normalized Fourier K uses |K''|<=pi^2.
"""
import argparse,json,pathlib,hashlib,struct,time
from flint import arb,ctx
p=argparse.ArgumentParser();p.add_argument('--input',default='rh-research-proportion/attempt024_data.json');p.add_argument('--bits',type=int,default=160);p.add_argument('--cells',type=int,default=524288);p.add_argument('--out',default='rh-research-proportion/independent_am_kernel');args=p.parse_args();ctx.prec=args.bits
src=pathlib.Path(args.input);d=json.loads(src.read_text());cc=d['cosine_coefficients'];den=d['coefficient_denominator'];H=16384;scale=2**28
pi=arb.pi();sq2=arb(2).sqrt();shift=sq2/(2*pi);m0=sq2*(1/sq2).sin();vmin=(1/sq2).cos()-arb(sum(map(abs,cc)))/den;assert vmin>0
coeff=[arb(c)/(2*den)*(-1)**j for j,c in enumerate(cc,1)];rem=pi*pi/(8*H*H);hw=arb(1)/(2*H)
vals=[];start=time.perf_counter()
for k in range(args.cells):
    x=arb(2*k+1)/(2*H);R=arb(0);Rp=arb(0)
    for j,c in enumerate(coeff,1):
        u=x-j;v=x+j;R+=c*(1/u+1/v);Rp-=c*(1/(u*u)+1/(v*v))
    sn=x.sin_pi();cs=x.cos_pi();K=sn*R/pi;Kp=cs*R+sn*Rp/pi
    for z in [x-shift,x+shift]:
        sz=z.sin_pi();cz=z.cos_pi();K+=sz/(2*pi*z);Kp+=(pi*z*cz-sz)/(2*pi*z*z)
    K/=m0;Kp/=m0
    low=(K.abs_lower()-Kp.abs_upper()*hw-rem).lower();val=0 if not low>0 else int((low*low*scale).lower().floor().unique_fmpz());assert 0<=val<=scale;vals.append(val)
    if (k+1)%131072==0:print(json.dumps({'cells':k+1,'seconds':time.perf_counter()-start}),flush=True)
base=pathlib.Path(args.out);txt=''.join(str(v)+'\n' for v in vals).encode();binary=struct.pack('<'+'I'*len(vals),*vals);base.with_suffix('.txt').write_bytes(txt);base.with_suffix('.u32le').write_bytes(binary)
out={'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'builder_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),'bits':ctx.prec,'cells':len(vals),'grid':H,'scale':scale,'m0':m0.str(40),'density_lower':vmin.lower().str(40),'text_sha256':hashlib.sha256(txt).hexdigest(),'binary_sha256':hashlib.sha256(binary).hexdigest(),'seconds':time.perf_counter()-start,'method':'Outward-rounded midpoint Taylor; |Ksecond|<=pi^2 from positive normalized support'}
base.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
