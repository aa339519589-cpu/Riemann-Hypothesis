# 真临界子空间的准确正基底解耦与迹范数误差

2026-10-12。继承本目录 `REPORT.md`，固定提交 `eba84eb15ce0992ea644d87ac7414b22de8fc85f`。最终目标仍为完整无条件 RH。

本稿把刚建立的无限真核投影用于原有符号 Birman–Schwinger 问题，而非继续替换素数移位为对角上界。得到一个**不改变原算子、保留非负基底、在已知无限临界子空间上准确解耦**的构造；其有限秩基底修正可以用对数阶的模式数达到指定的全空间迹范数误差。已知块可被一次性证明不会产生临界阈值以上的 Birman–Schwinger 本征值。剩余块的符号没有证明，故 RH 未闭合。

## 1. 输入、空间与有限投影

在原完整偶 Hilbert 空间 `L²_even(dx)` 上保留
\[
H=B-V=ULU^{-1}-\tfrac12 I,
\quad B=M_m b(D)M_m\ge0,
\quad\operatorname{Dom}H=\operatorname{Dom}B,
\]
\[
m^2=\Phi/(2\cosh(x/2)),\quad
V=C_0M_{m^2}+\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
M_m(\tau_{\log n}+\tau_{-\log n})M_m.
\tag{1.1}
\]
`B` 是原非负闭形式的自伴实现，`V` 有界自伴。所有素数幂及完整 Gamma 符号均在内。

本目录已构造由明确真 theta 平移向量生成的闭无限维子空间 `K_b subset ker H`，以及其准确正交投影 `P`。`P_M` 是到前 `M` 个模式线性包的准确正交投影；它们嵌套，秩为 `M`。已证，对 `M>=1`，
\[
R_M=P-P_M\text{ 是正交投影},\quad
\|BR_M\|=\|VR_M\|\le d_M:=(M+7)^2 16^{-M}.
\tag{1.2}
\]
`range P subset Dom H=Dom B` 且 `HP=0`，所以
\[
BP=VP\quad\text{为全空间上的有界算子},\qquad
PB=PV\quad\text{在 }\operatorname{Dom}B\text{ 上}.
\tag{1.3}
\]
后一式由自伴性取得。不能假定 `B,V` 在解耦前各自保持 `range P`。

### 一个完整素数的明确范数界

以下需要统一数值而非未指定的 `||V||`。原 theta 给
\[
\|m\|_\infty^2\le A_*e^{-\pi},\quad
\|M_m\tau_{\log n}M_m\|\le A_*n^2e^{-\pi n},
\quad A_*<128,\quad C_0<8.
\]
因 `Lambda(n)<=log n<=sqrt n`，取 `q=(3/8)^3=27/512`，并用 `pi>3,e>8/3`，得
\[
\begin{aligned}
\|V\|&<8\cdot128q+256\sum_{n\ge2}n^2q^n\\
&=8\cdot128q+256\left(\frac{q(1+q)}{(1-q)^3}-q\right)\\
&=\frac{13055795757}{228168250}<64.
\end{aligned}
\tag{1.4}
\]
这项界支付了全部素数幂，未将有限项和当作原算子。

## 2. 从算子范数尾提升到实际迹范数尾

这里 `||.||_1` 表示算子的核范数。令 `D_n=P_{n+1}-P_n`，这是秩一正交投影，且 `D_n=R_nD_n`。所以
\[
\|BD_n\|_1=\|BD_n\|\le d_n,\qquad n\ge1.
\]
对 `n>=M>=1`，
\[
\frac{d_{n+1}}{d_n}
=\frac1{16}\left(\frac{n+8}{n+7}\right)^2
\le\frac{81}{1024}.
\]
故 `sum_{n>=M} B D_n` 在迹范数中收敛。其算子范数极限由 (1.2) 确认正是 `BR_M`，不是另外定义的算子。因此
\[
\boxed{\|BR_M\|_1=\|VR_M\|_1
\le\frac{1024}{943}d_M<\rho_M:=\frac{12}{11}d_M.}
\tag{2.1}
\]
特别地 `BP=VP` 为迹类：第一项 `BP_1` 有限秩，余项由 (2.1) 控制。原 `B` 本身仍无界，`P` 仍非紧；本结论没有改变这些事实。

## 3. 正基底与有符号势的同步解耦

令 `Q=I-P`、`J=I-2P`。定义
\[
\begin{aligned}
B^\flat&=PBP+QBQ=\tfrac12(B+JBJ),\\
V^\flat&=PVP+QVQ=\tfrac12(V+JVJ).
\end{aligned}
\tag{3.1}
\]
对 `P_M` 同样定义 `Q_M,J_M,B^\flat_M,V^\flat_M`。

### 定理 1：原算子不变，完整正基底保留

这些定义给出
\[
\boxed{
B^\flat\ge0,\quad\operatorname{Dom}B^\flat=\operatorname{Dom}B,
\quad V^\flat=(V^\flat)^*,\quad\|V^\flat\|\le\|V\|<64,
\quad B^\flat-V^\flat=H.}
\tag{3.2}
\]
全部有限 `M` 也有同样的准确身份。`P` 同时约化 `B^flat,V^flat,H`；`P_M` 同时约化对应的有限版本。

**证明。** (1.3) 说明 `P,Q,J` 保持原算子域，且
\[
B^\flat=B-BP-PB+2PBP
=B-VP-PV+2PVP.
\tag{3.3}
\]
右侧是 `B` 的有界自伴扰动，故在原域自伴。对域内 `x`，
`<x,B^flat x>=<Px,BPx>+<Qx,BQx>>=0`，由闭形式延拓得到非负性。它的闭形式域也与原 `B` 相同。`V^flat` 为两个酉共轭的平均，故范数不增。因为 `HP=PH=0`，其对 `H` 的相同平均正是 `H`；或直接用 (3.3) 相减，即得 (3.2)。约化关系由分块公式成立。有限 `M` 同理。证毕。

注意：这里只做**同步的准确分块**。没有把 `B` 或 `V` 的任何交叉项单独删去，也没有产生改变 `H` 的正负误差。所有素数移位原来的符号保留在原 `H` 中。

### 定理 2：有限秩基底修正的迹范数误差

对 `M>=1`，
\[
\boxed{
\|B^\flat-B^\flat_M\|_1
\le2\rho_M,\qquad
\|V^\flat-V^\flat_M\|_1\le2\rho_M.}
\tag{3.4}
\]
`B^flat_M-B=V^flat_M-V` 的秩至多 `2M`；无限修正为其迹范数极限。

**证明。** `J-J_M=-2R_M`，所以在共同域上
\[
B^\flat-B^\flat_M=-R_M B J-J_M B R_M.
\tag{3.5}
\]
(2.1)、自伴性和 `J,J_M` 酉给出有界迹类延拓及 (3.4)。`V` 同理。有限修正的值域包含在 `range P_M + range BP_M` 内，维数至多 `2M`。每个分块版本都等于原 `H`，所以两种差其实相等；这里分别列出以明确误差作用在哪个正基底与势上。证毕。

## 4. 真 Birman–Schwinger 的无限解耦及有限误差

对 `epsilon>0`，定义完整的实际算子
\[
A_\epsilon=B^\flat+\epsilon I,\quad
A_{\epsilon,M}=B^\flat_M+\epsilon I,
\]
\[
\mathcal T_\epsilon=A_\epsilon^{-1/2}V^\flat A_\epsilon^{-1/2},\qquad
\mathcal T_{\epsilon,M}=A_{\epsilon,M}^{-1/2}V^\flat_M A_{\epsilon,M}^{-1/2}.
\tag{4.1}
\]
二者正基底均至少为 `epsilon I`，但 `T` 仍可有符号。原形式准确为
\[
H+\epsilon I=A_\epsilon^{1/2}(I-\mathcal T_\epsilon)A_\epsilon^{1/2}
\tag{4.2}
\]
的形式身份，有限版本同样成立。右侧不是把无界平方根误写为全空间有界相似；`A_epsilon^(1/2)` 是从形式域到 Hilbert 空间的双射，故保留负惯性。

### 定理 3：完整预条件算子的迹范数控制

对全部 `0<epsilon<=1/2`、`M>=1`，
\[
\boxed{\|\mathcal T_\epsilon-\mathcal T_{\epsilon,M}\|_1
\le2\rho_M\frac{\epsilon+64}{\epsilon^2}
<144\epsilon^{-2}(M+7)^2 16^{-M}.}
\tag{4.3}
\]
特别地，给定任意 `eta>0`，取
\[
\boxed{M\ge\max\left(8,
\left\lceil\log_8\frac{144}{\eta\epsilon^2}\right\rceil\right)}
\tag{4.4}
\]
即保证全空间算子范数及迹范数误差均至多 `eta`。

**证明。** 对任意自伴 `A,D>=epsilon I` 且差 `A-D` 为有界迹类，谱积分
\[
A^{-1/2}=\frac1\pi\int_0^\infty s^{-1/2}(A+s)^{-1}ds
\]
和预解式恒等式给
\[
\|A^{-1/2}-D^{-1/2}\|_1
\le\frac{\|A-D\|_1}{\pi}
\int_0^\infty\frac{s^{-1/2}}{(\epsilon+s)^2}ds
=\frac{\|A-D\|_1}{2\epsilon^{3/2}}.
\tag{4.5}
\]
该积分在迹范数中绝对收敛；最后常数用 `s=epsilon u²` 的初等积分可直接核对。将 (3.4) 代入，得两逆平方根的迹范数差至多 `rho_M epsilon^(-3/2)`。

在 (4.1) 中分别替换左逆平方根、势、右逆平方根；用 `||A^(-1/2)||<=epsilon^(-1/2)`、势范数 `<64` 和 (3.4)，得 (4.3) 第一式。`(24/11)(64+1/2)=1548/11<144` 给第二式。

对 `M>=8`，有 `(M+7)²<=2^M`：在 `M=8` 为 `225<256`，随后比值 `((M+8)/(M+7))²<2` 允许归纳。因此 `(4.3)<=144 epsilon^(-2)8^(-M)`，(4.4) 使它至多为 `eta`。证毕。

(4.4) 是**基底解耦修正的模式数**，不是整个未知 Birman–Schwinger 算子的有限矩阵秩或其计算耗时。有限 `M` 版本仍需原全 Gamma/有符号素数 resolvent 的真实误差认证；不能只计算这些真核列便说其余矩阵已经通过。

## 5. 指定的整个无限临界块可以准确排除

在 `K_b=range P` 上定义
\[
C=B^\flat|_{\mathcal K_b}=PBP|_{\mathcal K_b}
=V^\flat|_{\mathcal K_b}.
\]
它是有界、非负、迹类算子。由 `b(t)>0` 对 `t!=0`、`m>0`，原 `B` 的形式零空间平凡；因此 `C` 在非零向量上严格为正，且其无穷个正本征值只可能积聚到零。由分块函数演算，
\[
\boxed{\mathcal T_\epsilon|_{\mathcal K_b}
=C(C+\epsilon I)^{-1},\qquad
\|\mathcal T_\epsilon|_{\mathcal K_b}\|
\le\frac{64}{64+\epsilon}<1.}
\tag{5.1}
\]
所以这**整个指定无限真临界子空间**对 `T_epsilon` 在 `1` 以上的惯性计数贡献为零，不依赖有限 Ritz 结果。

其余谱问题准确落在 `K_b^perp`。令 `n_>(T,1)` 表示严格超过 1 的谱子空间维数，则
\[
\boxed{\operatorname{ind}_-(H+\epsilon I)
=n_>(\mathcal T_\epsilon|_{\mathcal K_b^\perp},1).}
\tag{5.2}
\]
这可以按闭形式负子空间解释，不需先假设原 `T` 为迹类。原基态 `sqrt(p)` 与 `K_b` 正交，所以其已知负方向仍留在右侧，不会被错误消去。

### 已知块的完整迹尾

将 `C` 的正本征值按非增顺序记为 `gamma_j`。由在 `range(P-P_M)` 上的 Rayleigh 上界 (1.2) 和极小极大原理，
\[
\gamma_{M+1}\le d_M,\qquad M\ge1.
\]
因此
\[
\sum_{j>M}\frac{\gamma_j}{\gamma_j+\epsilon}
\le\epsilon^{-1}\sum_{n\ge M}d_n
<\frac{12}{11\epsilon}(M+7)^2 16^{-M}.
\tag{5.3}
\]
这里是已知块的谱截断迹尾；没有将其与 `P_M` 的坐标截断混同。真实坐标有限投影的误差已另由 (3.4)-(4.3) 证明。

### 已知投影确实不完备：补空间仍有明确的无限零态

这里不仅保守地“不假定完备”，还可以直接证明 `P` 不是整个真核投影。
取交错的真实参数
\[
\widetilde c_j=2^{-128}16^{-j},\qquad
z_j=v_{t(\widetilde c_j)}/\|v_{t(\widetilde c_j)}\|.
\tag{5.4}
\]
原序列正是 `z_{2j}=u_j`。本目录双参数 Gram 估计的相对误差 `beta=2^-20` 给
`(1+beta)/(1-beta)<5/4`，因此对 `j!=k`，
\[
|\langle z_j,z_k\rangle|
\le\frac{15}{2}\,32^{-|j-k|}.
\]
全无限非对角行和至多 `15/31<1/2`，所以交错序列的完整 Gram 介于 `I/2` 与 `3I/2` 之间。

令 `W_odd` 为奇数项合成，定义真实残余列
\[
\mathcal R=(I-P)W_{\rm odd},\qquad r_j=(I-P)z_{2j+1}.
\]
对任意有限或 `ell²` 系数 `a`，在偶数项系数上最小化完整 Gram，得到
\[
\boxed{\tfrac12\|a\|_2^2\le\|\mathcal R a\|_2^2
\le\tfrac{33}{32}\|a\|_2^2.}
\tag{5.5}
\]
上界使用奇数项自身的参数比仍为 256。故 `ker H intersect K_b^perp` 包含这组**明确的无限 Riesz 序列**。

这也排除了一个可能的错误验收目标：解耦后，不能要求剩余 Birman–Schwinger 块在去掉有限个方向后，对所有 `epsilon` 都位于同一 `1-eta` 以下，其中 `eta>0` 固定。具体地，在任意固定的 `r` 维残余零态子空间 `F_r` 上，原 `B^flat` 形式严格为正，有限维紧致性给常数 `b_r>0`。对 `z=A_epsilon^(1/2)w`、`w in F_r`，
\[
\frac{\langle z,\mathcal T_\epsilon z\rangle}{\|z\|^2}
=\frac{\langle w,B^\flat w\rangle}
 {\langle w,B^\flat w\rangle+\epsilon\|w\|^2}
\ge\frac{b_r}{b_r+\epsilon}\longrightarrow1.
\tag{5.6}
\]
这些 `z` 都位于 `K_b^perp`。因此其在任意固定 `1-eta` 以上的谱子空间维数，随 `epsilon` 变小可超过任意固定整数。这个结论来自**真实零态**，并非未知负态，也不说明有谱超过 1。它要求实际证书随 `epsilon` 缩小误差，而不是继续采用固定正裕量。

## 6. 为什么这没有偷渡 RH

虽然 (5.1) 排除了一个完整无限块，(5.5) 已证明 `K_b` 严格小于 `ker H`；在 `K_b^perp` 上是否只剩原基态一个负方向，仍没有证明。完整 RH 仍要求对所有充分小 `epsilon>0` 控制 (5.2)，或直接证明原均值零空间 `H>=0`。

随附精确有理矩阵反检查刻意取
\[
H_\mathrm{test}=\operatorname{diag}(0,0,-1/2,-1/16,1/3).
\]
取实际正矩阵 `B_test=I+LL*/16`，定义 `V_test=B_test-H_test`，并投影到前两个真零方向。同步解耦准确保留 `H_test`，已知块的 Birman–Schwinger 谱严格小于 1；但在 `epsilon=1/128` 时整个 `H_test+epsilon I` 仍有**两个**负方向。此例不是原 theta 算子模型或 RH 反例，仅核验逻辑：已知核块安全并不推出补空间安全。

## 7. 实际执行与来源

`check_decoupling.py` 只用标准库 `Fraction`，已实际执行并生成 `decoupling_checks.json`。它验证完整素数范数界的有理常数、几何迹尾预算、(4.4) 的确切整数参数选择，以及上述有理矩阵的同步分块、修正秩和两负方向保留。它不替代无界算子域、迹理想积分或真 theta 的解析证明。

依赖来源：本目录 `REPORT.md` 的全部参数稳定真临界序列和完整作用尾，提交 `eba84eb15ce0992ea644d87ac7414b22de8fc85f`；原基础实现见 `../20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md`。本稿的同步分块、迹类提升及 (4.3)-(5.3) 在上面完整推导。没有外部独立评审或形式化内核验收。

```sh
python check_decoupling.py --output new_decoupling_checks.json
```

输出排他创建。全部原有文件保持不变。

**状态：新增准确无限块解耦及可复算的全空间误差定理；NO NEW UNCONDITIONAL RH THEOREM PROVED。**
