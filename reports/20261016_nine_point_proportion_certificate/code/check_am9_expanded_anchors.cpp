// Independently authored rational branch-and-bound for the nine-point AM window.
// Usage: check_am9_boxes table.u32le taylor.i64le reward_in_1e8_units [maxnodes]
// Table certification is a separate ball-arithmetic proof obligation.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <vector>
#include <chrono>
#include <cmath>
#include "candidate_am9_data.hpp"
using I=long long; using X=__int128_t;
std::vector<std::vector<I>> curvrmq;
struct Box{std::array<int,N> lo,hi;};struct Aff{X s,b;};
std::array<int,36> pi,pj,mp;std::vector<uint32_t> tab;std::vector<std::vector<uint32_t>> rmq;std::vector<int> lg;
constexpr I TSCALE=I(1)<<50;
std::vector<std::array<I,4>> tj; // w lower, wprime lower/upper, wsecond lower on cell

I cmin(int l,int r){int k=lg[r-l+1];return std::min(curvrmq[k][l],curvrmq[k][r-(1<<k)+1]);}
uint32_t rmin(int l,int r){if(l<0||r>=TABSIZE||l>r){std::cerr<<"BAD RANGE "<<l<<" "<<r<<"\n";std::exit(2);}int k=lg[r-l+1];return std::min(rmq[k][l],rmq[k][r-(1<<k)+1]);}
struct Point{int x;X y;};
std::vector<std::vector<Point>> hull;
void addpoint(std::vector<Point>&v,Point p){
 if(!v.empty()&&v.back().x==p.x){if(v.back().y<=p.y)return;v.pop_back();}
 while(v.size()>=2){auto a=v[v.size()-2],b=v.back();X cross=X(b.x-a.x)*(p.y-b.y)-(b.y-a.y)*(p.x-b.x);if(cross>0)break;v.pop_back();}
 v.push_back(p);
}
void build_hulls(){
 hull.resize(2*TABSIZE);
 for(int k=0;k<TABSIZE;k++){
  X base=8*X(GRID)*GRID*tj[k][0]+std::min(I(0),tj[k][3]);
  addpoint(hull[TABSIZE+k],{k,base-4*X(GRID)*tj[k][2]});
  addpoint(hull[TABSIZE+k],{k+1,base+4*X(GRID)*tj[k][1]});
 }
 for(int k=TABSIZE-1;k;k--){const auto &a=hull[2*k],&b=hull[2*k+1];size_t i=0,j=0;hull[k].reserve(a.size()+b.size());while(i<a.size()||j<b.size()){
  if(j==b.size()||(i<a.size()&&a[i].x<=b[j].x))addpoint(hull[k],a[i++]);else addpoint(hull[k],b[j++]);
 }}
}
X hull_min(const std::vector<Point>&v,X q){size_t l=0,r=v.size()-1;while(l<r){size_t m=(l+r)/2;if(v[m].y-q*v[m].x<=v[m+1].y-q*v[m+1].x)r=m;else l=m+1;}return v[l].y-q*v[l].x;}
X support_min(int l,int r,X q){X ans=X(1)<<126;l+=TABSIZE;r+=TABSIZE+1;while(l<r){if(l&1)ans=std::min(ans,hull_min(hull[l++],q));if(r&1)ans=std::min(ans,hull_min(hull[--r],q));l/=2;r/=2;}return ans;}
Aff affine(int l,int r){
 int m=(l+r)/2;I ds=tj[m][1]+(tj[m][2]-tj[m][1])/2;
 return {8*X(GRID)*ds,support_min(l,r,8*X(GRID)*ds)};
}
bool convex_bound(const std::array<int,36>&ll,const std::array<int,36>&rr,const std::array<int,N>&cc,const std::array<int,36>&cent,I reward){
 std::array<X,N> lam{},gl{},gu{};std::array<std::array<I,N>,N> mat{};X fc=0;
 const I curvature_width=(249*TSCALE+GRID-1)/GRID+2;
 for(int i=0;i<N;i++){gl[i]=gu[i]=2*X(GRID)*TSCALE*P[i];fc+=4*X(GRID)*TSCALE*P[i]*cc[i];}
 for(int k=0;k<36;k++){
  if(W[k]==0)continue;
  int lo=ll[k],hi=rr[k];
  if(hi>=TABSIZE)return false;
  I cl=cmin(lo,std::max(lo,hi-1));
  X scalar=X(W[k])*cl;X cq=scalar/TSCALE;if(scalar<0&&scalar%TSCALE)cq--;
  if(cq<-1000000000000LL||cq>1000000000000LL)return false;
  for(int i=pi[k];i<pj[k];i++)for(int j=pi[k];j<pj[k];j++)mat[i][j]+=I(cq);
  if(cl<0){for(int i=pi[k];i<pj[k];i++)lam[i]+=X(W[k])*cl*(pj[k]-pi[k]);}
  else if(pj[k]==pi[k]+1)lam[pi[k]]+=X(W[k])*cl;
  int cm=cent[k]/2,q=cent[k]-(2*cm+1);const auto &j=tj[cm];I cu=j[3]+curvature_width;
  X wl=8*X(GRID)*GRID*j[0]+4*X(GRID)*(q<0?j[2]:j[1])*q+X(j[3])*q*q;
  fc+=X(W[k])*wl;
  X dl=2*X(GRID)*j[1]+X(q)*(q<0?cu:j[3]);
  X du=2*X(GRID)*j[2]+X(q)*(q<0?j[3]:cu);
  for(int i=pi[k];i<pj[k];i++){gl[i]+=X(W[k])*dl;gu[i]+=X(W[k])*du;}
 }
 if(fc<0)return false;
 // All final decisions are integers. Floating Cholesky only suggests R.
 const X scale=2*X(GRID)*TSCALE;
 std::array<I,N> gLo{},gHi{};
 for(int i=0;i<N;i++){
  X a=gl[i]/scale;if(gl[i]<0&&gl[i]%scale)a--;
  X b=gu[i]/scale;if(gu[i]>0&&gu[i]%scale)b++;
  if(a<-1000000000LL||b>1000000000LL)return false;
  gLo[i]=I(a);gHi[i]=I(b);
 }
 std::array<std::array<double,N>,N> L{};
 for(int i=0;i<N;i++)for(int j=0;j<=i;j++){
  if(mat[i][j]<-1000000000000LL||mat[i][j]>1000000000000LL)return false;
  double a=double(mat[i][j]);for(int k=0;k<j;k++)a-=L[i][k]*L[j][k];
  if(i==j){if(!(a>0)||!std::isfinite(a))return false;L[i][j]=std::sqrt(a);}else L[i][j]=a/L[j][j];
 }
 std::array<std::array<I,N>,N> R{};
 constexpr I RS=1000000000LL;
 for(int j=0;j<N;j++){
  std::array<double,N> x{};
  for(int i=N-1;i>=0;i--){double a=(i==j?1.:0.);for(int k=i+1;k<N;k++)a-=L[k][i]*x[k];x[i]=a/L[i][i];}
  for(int i=0;i<N;i++){
   double a=x[i]*double(RS);if(!std::isfinite(a)||std::abs(a)>99999999.)return false;R[i][j]=std::llround(a);
  }
 }
 X d=X(1)<<126;
 for(int i=0;i<N;i++){
  X diagonal=0,off=0;
  for(int j=0;j<N;j++){
   X val=0;for(int a=0;a<N;a++)for(int b=0;b<N;b++)val+=X(R[a][i])*mat[a][b]*R[b][j];
   if(i==j)diagonal=val;else off+=val<0?-val:val;
  }
  d=std::min(d,diagonal-off);
 }
 if(d<=0)return false;
 X lower=fc/(8*X(GRID)*GRID*TSCALE);
 for(int j=0;j<N;j++){
  X a=0,b=0;for(int i=0;i<N;i++){
   a+=X(R[i][j])*(R[i][j]>=0?gLo[i]:gHi[i]);
   b+=X(R[i][j])*(R[i][j]>=0?gHi[i]:gLo[i]);
  }
  X v=std::max(a<0?-a:a,b<0?-b:b);X square=v*v,divisor=2*d;
  lower-=(square+divisor-1)/divisor;
 }
 return lower>=reward;
}
I ceildiv(I a,I b){return a/b+(a%b!=0);}
struct Cell{std::array<std::array<int,N+1>,N+1> d;int root;int aid=-1;};
constexpr int INF=100000000;
bool tighten(Cell&c,int a,int b,int v){
 if(v>=c.d[a][b])return true;
 if(v+c.d[b][a]<0)return false;
 auto old=c.d;
 for(int i=0;i<=N;i++)for(int j=0;j<=N;j++)c.d[i][j]=std::min(old[i][j],old[i][a]+v+old[b][j]);
 return true;
}
// Exact feasible dual transport. Every final flow is checked by construction.
X transport_lower(const Cell& c,const std::array<X,N>& slope){
 std::array<X,N+1> b{};b[0]=-slope[0];b[N]=slope[N-1];for(int i=1;i<N;i++)b[i]=slope[i-1]-slope[i];
 constexpr int V=N+3,src=N+1,snk=N+2;
 struct Edge{int to,rev,cost;X cap;};std::array<std::vector<Edge>,V> es;
 auto add=[&](int a,int z,int cost,X cap){Edge e{z,int(es[z].size()),cost,cap},r{a,int(es[a].size()),-cost,0};es[a].push_back(e);es[z].push_back(r);};
 X total=0;for(int i=0;i<=N;i++)if(b[i]>0)total+=b[i];
 for(int i=0;i<=N;i++){if(b[i]>0)add(src,i,0,b[i]);if(b[i]<0)add(i,snk,0,-b[i]);}
 std::array<std::array<int,N+1>,N+1> original{};
 for(int i=0;i<=N;i++)for(int j=0;j<=N;j++)if(i!=j){original[i][j]=int(es[i].size());add(i,j,c.d[i][j],total);}
 X sent=0,cost=0;
 while(sent<total){
  std::array<long long,V> dist;dist.fill(1000000000000LL);dist[src]=0;std::array<int,V> pv,pe;pv.fill(-1);
  for(int k=0;k<V-1;k++){bool change=false;for(int a=0;a<V;a++)if(dist[a]<1000000000000LL)for(int j=0;j<int(es[a].size());j++){auto &e=es[a][j];if(e.cap>0&&dist[e.to]>dist[a]+e.cost){dist[e.to]=dist[a]+e.cost;pv[e.to]=a;pe[e.to]=j;change=true;}}if(!change)break;}
  if(pv[snk]<0){std::cerr<<"TRANSPORT NO PATH\n";std::exit(2);}
  X push=total-sent;int len=0;for(int z=snk;z!=src;z=pv[z]){if(z<0||++len>V){std::cerr<<"TRANSPORT CYCLE\n";std::exit(2);}push=std::min(push,es[pv[z]][pe[z]].cap);}
  for(int z=snk;z!=src;z=pv[z]){auto &e=es[pv[z]][pe[z]];e.cap-=push;es[z][e.rev].cap+=push;}
  cost+=push*dist[snk];sent+=push;
 }
 std::array<X,N+1> balance{};X checkedcost=0;
 for(int i=0;i<=N;i++)for(int j=0;j<=N;j++)if(i!=j){X flow=total-es[i][original[i][j]].cap;if(flow<0||flow>total){std::cerr<<"BAD TRANSPORT FLOW\n";std::exit(2);}balance[i]+=flow;balance[j]-=flow;checkedcost+=flow*c.d[i][j];}
 for(int i=0;i<=N;i++)if(balance[i]!=b[i]){std::cerr<<"BAD TRANSPORT BALANCE\n";std::exit(2);}
 if(checkedcost!=cost){std::cerr<<"BAD TRANSPORT COST\n";std::exit(2);}
 return -checkedcost;
}
Cell frombox(const Box&b,int id){
 Cell c;c.root=id;for(int i=0;i<=N;i++)for(int j=0;j<=N;j++)c.d[i][j]=(i==j?0:INF);
 for(int i=0;i<N;i++){c.d[i][i+1]=b.hi[i];c.d[i+1][i]=-b.lo[i];}
 for(int k=0;k<=N;k++)for(int i=0;i<=N;i++)for(int j=0;j<=N;j++)c.d[i][j]=std::min(c.d[i][j],c.d[i][k]+c.d[k][j]);
 return c;
}
int main(int argc,char**argv){
 if(argc<4)return 2;
 I reward=std::stoll(argv[3]);uint64_t cap=argc>4?std::stoull(argv[4]):0;
 if(reward<=0||reward>=P[0]*(TABSIZE/GRID)){std::cerr<<"reward not covered by tail cutoff\n";return 2;}
 std::ifstream f(argv[1],std::ios::binary);tab.resize(TABSIZE);for(int k=0;k<TABSIZE;k++){unsigned char b[4];if(!f.read((char*)b,4))return 2;tab[k]=uint32_t(b[0])+(uint32_t(b[1])<<8)+(uint32_t(b[2])<<16)+(uint32_t(b[3])<<24);if(tab[k]>SCALE)return 2;}char extra;if(f.get(extra))return 2;
 std::ifstream tf(argv[2],std::ios::binary);tj.resize(TABSIZE);
 for(auto &row:tj)for(I &v:row){unsigned char b[8];if(!tf.read((char*)b,8))return 2;uint64_t u=0;for(int j=0;j<8;j++)u|=uint64_t(b[j])<<(8*j);if(u<=uint64_t(std::numeric_limits<I>::max()))v=I(u);else v=-I(~u)-1;}
 if(tf.get(extra))return 2;
 for(auto row:tj)if(row[1]>row[2]||row[0]<0||row[0]>TSCALE||row[1]<-8*TSCALE||row[2]>8*TSCALE||row[3]<-64*TSCALE||row[3]>64*TSCALE)return 2;

 for(int i=0,k=0;i<=N;i++)for(int j=i+1;j<=N;j++,k++){pi[k]=i;pj[k]=j;mp[k]=int(*std::min_element(P+i,P+j));}
 for(int i=0;i<N;i++)if(P[i]!=P[N-1-i]||P[i]<P[0])return 2;
 for(int k=0;k<36;k++){bool found=false;for(int j=0;j<36;j++)if(pi[j]==N-pj[k]&&pj[j]==N-pi[k]){found=true;if(W[j]!=W[k])return 2;}if(!found||W[k]<0)return 2;}
 lg.resize(TABSIZE+1);for(int k=2;k<=TABSIZE;k++)lg[k]=lg[k/2]+1;rmq.push_back(tab);for(int p=1;(1<<p)<=TABSIZE;p++){int len=TABSIZE-(1<<p)+1;rmq.emplace_back(len);for(int i=0;i<len;i++)rmq[p][i]=std::min(rmq[p-1][i],rmq[p-1][i+(1<<(p-1))]);}
 curvrmq.emplace_back(TABSIZE);for(int k=0;k<TABSIZE;k++)curvrmq[0][k]=tj[k][3];
 for(int p=1;(1<<p)<=TABSIZE;p++){int len=TABSIZE-(1<<p)+1;curvrmq.emplace_back(len);for(int i=0;i<len;i++)curvrmq[p][i]=std::min(curvrmq[p-1][i],curvrmq[p-1][i+(1<<(p-1))]);}
 build_hulls();
 // Exact-integer diagnostic checks against the literal scanned support formula.
 uint64_t rng=0x8edcad75ba657321ULL;
 for(int trial=0;trial<10000;trial++){
  rng^=rng<<7;rng^=rng>>9;int l=int(rng%TABSIZE);rng^=rng<<7;rng^=rng>>9;int r=std::min(TABSIZE-1,l+int(rng%4096));
  int m=(l+r)/2;I ds=tj[m][1]+(tj[m][2]-tj[m][1])/2;X scanned=X(1)<<126;
  for(int k=l;k<=r;k++){X diff=std::max(X(tj[k][2])-ds,X(ds)-tj[k][1]);X cur=8*X(GRID)*GRID*tj[k][0]-4*X(GRID)*ds*(2*k+1)-4*X(GRID)*diff+std::min(I(0),tj[k][3]);scanned=std::min(scanned,cur);}
  if(scanned!=support_min(l,r,8*X(GRID)*ds)){std::cerr<<"HULL MISMATCH\n";return 2;}
 }
 std::cout<<"HULL_DIAGNOSTIC_PASS trials=10000\n"<<std::flush;

 Box root;root.lo.fill(0);for(int i=0;i<N;i++)root.hi[i]=int(ceildiv(reward*GRID,P[i]));
 // Independent separable pre-cover. F >= sum of all adjacent-pair pieces.
 std::array<std::vector<std::pair<int,int>>,N> intervals;
 std::array<X,N> emin;X esum=0;
 for(int i=0;i<N;i++){
  int adj=-1;for(int k=0;k<36;k++)if(pi[k]==i&&pj[k]==i+1)adj=k;
  if(adj<0)return 2;
  emin[i]=X(reward)*GRID*SCALE;
  for(int k=0;k<root.hi[i];k++)emin[i]=std::min(emin[i],X(P[i])*k*SCALE+X(W[adj])*tab[k]*GRID);
  esum+=emin[i];
 }
 for(int i=0;i<N;i++){
  int adj=-1;for(int k=0;k<36;k++)if(pi[k]==i&&pj[k]==i+1)adj=k;
  for(int k=0;k<root.hi[i];k++){
   X b=X(P[i])*k*SCALE+X(W[adj])*tab[k]*GRID+esum-emin[i];
   if(b>=X(reward)*GRID*SCALE)continue;
   auto &v=intervals[i];if(!v.empty()&&v.back().second==k)v.back().second=k+1;else v.push_back({k,k+1});
  }
  std::cout<<"PRECOVER coordinate="<<i<<" runs="<<intervals[i].size()<<"\n";
 }
 // The independently replayed partition covers the Cartesian product below.
 // Recompute NEW-window precover above, then verify inclusion in that product.
 std::ifstream cover("expanded_partition_coordinate_cover.txt");if(!cover)return 2;
 for(int i=0;i<N;i++){
  int n;if(!(cover>>n)||n<1||n>100)return 2;
  std::vector<std::pair<int,int>> old;
  for(int j=0;j<n;j++){int a,b;if(!(cover>>a>>b)||a<0||b<=a)return 2;old.push_back({a,b});}
  std::sort(old.begin(),old.end());
  for(auto iv:intervals[i]){
   int endpoint=2*iv.first,target=2*iv.second;
   for(auto ov:old){if(ov.first>endpoint)break;if(ov.second>endpoint)endpoint=ov.second;if(endpoint>=target)break;}
   if(endpoint<target){std::cerr<<"UNCOVERED NEW PRECOVER coordinate="<<i<<" lower="<<iv.first<<" upper="<<iv.second<<"\n";return 2;}
  }
 }
 std::string leftover;if(cover>>leftover)return 2;
 std::ifstream cells("verified_expanded_partition_cells.txt");size_t ncell;
 if(!(cells>>ncell)||ncell!=10750)return 2;
 std::vector<Cell> work;work.reserve(ncell);
 for(size_t k=0;k<ncell;k++){
  Cell c;if(!(cells>>c.root)||c.root<0||c.root>=48)return 2;
  for(int i=0;i<=N;i++)for(int j=0;j<=N;j++)if(!(cells>>c.d[i][j])||std::abs(c.d[i][j])>100000000)return 2;
  for(int i=0;i<=N;i++){
   if(c.d[i][i]!=0)return 2;
   for(int j=0;j<=N;j++)for(int z=0;z<=N;z++)if(c.d[i][j]>c.d[i][z]+c.d[z][j])return 2;
  }
  for(int i=0;i<N;i++)if(c.d[i+1][i]>0)return 2;
  c.aid=int(k);work.push_back(c);
 }
 if(cells>>leftover)return 2;

 std::ifstream ap("expanded_partition_anchor_proposals.txt");size_t na;int np;
 if(!(ap>>na>>np)||na!=ncell||np!=34)return 2;
 std::vector<int> term;for(int z=0;z<np;z++){int i,j;if(!(ap>>i>>j))return 2;int k=0;while(k<36&&(pi[k]!=i||pj[k]!=j))k++;if(k==36)return 2;term.push_back(k);}
 std::vector<std::array<I,36>> proposals(ncell);std::vector<bool> hasproposal(ncell);
 for(size_t z=0;z<ncell;z++){
  int flag;if(!(ap>>flag)||(flag!=0&&flag!=1))return 2;hasproposal[z]=flag;
  if(flag)for(int k:term){
   int kind,lam,p,r;if(!(ap>>kind>>lam>>p>>r)||kind<0||kind>3||lam<0||lam>1024||p<0||r<0||p>=2*TABSIZE||r>=2*TABSIZE)return 2;
   auto deriv=[&](int pos){int ix=pos/2;return tj[ix][1]+I(X(tj[ix][3])*(pos-(2*ix+1))/(2*GRID));};
   I ds=0;if(kind==1)ds=deriv(p);if(kind==2)ds=I(X(lam)*deriv(p)/1024);if(kind==3)ds=I((X(1024-lam)*deriv(p)+X(lam)*deriv(r))/1024);
   if(std::abs(ds)>8*TSCALE)return 2;proposals[z][k]=ds;
  }
 }
 if(ap>>leftover)return 2;
 std::reverse(work.begin(),work.end());std::vector<Cell> deferred;
 std::cout<<"NEW_PRECOVER_INCLUSION_PASS partition_cells="<<work.size()<<"\n"<<std::flush;
 uint64_t nodes=0,pressureok=0,basicok=0,affok=0,convexok=0,symok=0,emptyok=0;size_t high=work.size();auto start=std::chrono::steady_clock::now();
 while(!work.empty()||!deferred.empty()){
  if(work.empty()){work.swap(deferred);std::cout<<"INITIAL_PARTITION_SWEEP_DONE pending="<<work.size()<<"\n"<<std::flush;}
  Cell c=work.back();work.pop_back();nodes++;
  if(nodes%100000==0){double sec=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();std::cout<<"PROGRESS nodes="<<nodes<<" root="<<c.root<<" stack="<<work.size()<<" affine="<<affok<<" convex="<<convexok<<" seconds="<<sec<<"\n"<<std::flush;}
  if(-c.d[1][0]>c.d[7][8]){symok++;continue;}
  if(!tighten(c,0,1,c.d[7][8])||!tighten(c,8,7,c.d[1][0])){emptyok++;continue;}
  if(!tighten(c,0,N,int(ceildiv(reward*GRID,*std::min_element(P,P+N))))){pressureok++;continue;}
  I pl=0;for(int i=0;i<N;i++)pl-=P[i]*c.d[i+1][i];
  if(pl>=reward*GRID){pressureok++;continue;}I residual=reward*GRID-pl;bool valid=true;
  for(int k=0;k<36;k++){
   int i=pi[k],j=pj[k];int upper=-c.d[j][i]+int(ceildiv(residual,mp[k]));
   if(!tighten(c,i,j,upper)){valid=false;break;}
  }
  if(!valid){emptyok++;continue;}
  pl=0;for(int i=0;i<N;i++)pl-=P[i]*c.d[i+1][i];
  if(pl>=reward*GRID){pressureok++;continue;}
  X bound=X(pl)*(SCALE/GRID);std::array<int,36> l,r,cent;
  int widest=0;long double bestscore=-1;for(int k=0;k<36;k++){
   l[k]=-c.d[pj[k]][pi[k]];r[k]=c.d[pi[k]][pj[k]];
   cent[k]=c.d[0][pj[k]]-c.d[pj[k]][0]-c.d[0][pi[k]]+c.d[pi[k]][0];
   if(l[k]<0||r[k]>=TABSIZE||r[k]<l[k]){std::cerr<<"BAD DBM RANGE nodes="<<nodes<<" root="<<c.root<<" pair="<<k<<" l="<<l[k]<<" r="<<r[k]<<" pl="<<pl<<"\n";return 2;}
   long double width=r[k]-l[k];
   long double value=0;for(int z=0;z<9;z++){int ix=l[k]+int(width*z/8);value=std::max(value,(long double)tj[ix][0]);}
   long double score=(W[k]?W[k]:1)*value*std::min((long double)1,width/GRID);
   if(width>1&&score>bestscore){bestscore=score;widest=k;}
   if(W[k])bound+=X(W[k])*rmin(l[k],std::max(l[k],r[k]-1));
  }
  if(bound>=X(reward)*SCALE){basicok++;continue;}

  bool contracted=false;
  for(int k=0;k<36;k++)if(W[k]){
   int low=l[k],high=std::max(l[k],r[k]-1);X other=bound-X(W[k])*rmin(low,high);
   auto possible=[&](int a,int b){return other+X(W[k])*rmin(a,b)<X(reward)*SCALE;};
   int a=low,b=high;
   while(a<b){int m=(a+b)/2;if(possible(a,m))b=m;else a=m+1;}int first=a;
   a=low;b=high;while(a<b){int m=(a+b+1)/2;if(possible(m,b))a=m;else b=m-1;}int last=a;
   if(first>l[k]){if(!tighten(c,pj[k],pi[k],-first)){valid=false;break;}contracted=true;}
   int endpoint=(l[k]==r[k]?r[k]:last+1);
   if(endpoint<r[k]){if(!tighten(c,pi[k],pj[k],endpoint)){valid=false;break;}contracted=true;}
  }
  if(!valid){emptyok++;continue;}
  if(contracted){if(nodes<=ncell)deferred.push_back(c);else work.push_back(c);continue;}

  if(c.aid>=0&&hasproposal[c.aid]){
   std::array<X,N> slope;for(int i=0;i<N;i++)slope[i]=8*X(P[i])*GRID*TSCALE;X off=0;
   for(int k=0;k<36;k++){if(W[k]==0)continue;I ds=proposals[c.aid][k];X sl=8*X(GRID)*ds;off+=X(W[k])*support_min(l[k],std::max(l[k],r[k]-1),sl);for(int i=pi[k];i<pj[k];i++)slope[i]+=X(W[k])*sl;}
   X v=off;for(int i=0;i<N;i++)v+=slope[i]*(slope[i]>=0?-c.d[i+1][i]:c.d[i][i+1]);
   if(v<8*X(reward)*TSCALE*GRID*GRID)v=std::max(v,off+transport_lower(c,slope));
   if(v>=8*X(reward)*TSCALE*GRID*GRID){affok++;continue;}
  }
  if(true){
   std::array<X,N> slope;for(int i=0;i<N;i++)slope[i]=8*X(P[i])*GRID*TSCALE;X off=0;
   for(int k=0;k<36;k++){if(W[k]==0)continue;auto a=affine(l[k],std::max(l[k],r[k]-1));off+=X(W[k])*a.b;for(int i=pi[k];i<pj[k];i++)slope[i]+=X(W[k])*a.s;}
   X v=off;for(int i=0;i<N;i++)v+=slope[i]*(slope[i]>=0?-c.d[i+1][i]:c.d[i][i+1]);
   if(v<8*X(reward)*TSCALE*GRID*GRID)v=std::max(v,off+transport_lower(c,slope));
   if(v>=8*X(reward)*TSCALE*GRID*GRID){affok++;continue;}
  }
  if(r[widest]-l[widest]<=8192){
   std::array<int,N> cc;for(int i=0;i<N;i++)cc[i]=c.d[0][i+1]-c.d[i+1][0]-c.d[0][i]+c.d[i][0];
   if(convex_bound(l,r,cc,cent,reward)){convexok++;continue;}
  }
  bool narrow=true;for(int k=0;k<36;k++)if(r[k]-l[k]>1)narrow=false;
  if(narrow){std::cout<<"UNRESOLVED reward="<<reward<<" nodes="<<nodes<<" root="<<c.root<<"\n";return 1;}
  int m=(l[widest]+r[widest])/2,i=pi[widest],j=pj[widest];
  if(r[widest]-l[widest]>GRID/2){int alt=int(std::llround((double)m/GRID*2))*GRID/2;if(alt>l[widest]+32&&alt<r[widest]-32)m=alt;}
  Cell right=c;
  if(tighten(right,j,i,-m)){if(nodes<=ncell)deferred.push_back(right);else work.push_back(right);}else emptyok++;
  if(tighten(c,i,j,m)){if(nodes<=ncell)deferred.push_back(c);else work.push_back(c);}else emptyok++;
  high=std::max(high,work.size());
  if(cap&&nodes>=cap){std::cout<<"LIMIT nodes="<<nodes<<" pending="<<(work.size()+deferred.size())<<" root="<<c.root<<" seconds="<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<"\n";return 3;}
 }
 double sec=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
 std::cout<<"PASS reward="<<reward<<" denominator="<<DEN<<" nodes="<<nodes<<" pressure="<<pressureok<<" basic="<<basicok<<" affine="<<affok<<" convex="<<convexok<<" symmetry="<<symok<<" empty="<<emptyok<<" maxstack="<<high<<" seconds="<<sec<<"\n";
}
