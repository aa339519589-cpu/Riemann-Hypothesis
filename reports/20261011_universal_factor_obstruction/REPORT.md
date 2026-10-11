# 真实 theta 核的十二阶对数喷射：通用因子构造的全参数排除

日期：2026-10-11。读取基线：`4d2cc4cf6a147078c7a4bcc4922f7d5639223d5e`。

**NO NEW UNCONDITIONAL RH THEOREM PROVED。** 本文记录一次直接构造完整证明的尝试及其严格失败点。没有改变真实核，没有注入模拟零点，没有把局部数值当成全零点结论。

目标原为：从已知 Fourier 变换全实零的 Bessel/Pólya 种子出发，乘上 Pólya 通用因子，精确得到真实 theta 核，或构造能传递零点性质的逼近。下面证明这一具体构造在原点十二阶喷射处已经不可能，且对所有正 Bessel 参数同时成立。另给出固定整个种子下更弱的逐点逼近障碍。

这是关于一种充分构造机制的否定结果，不是 RH 的反例。特别是，“源函数不是通用因子”和“源函数的 Fourier 变换有非实零点”是不同断言。

## 1. 完整真实对象与来源

采用仓库第四、第五轮的 x 尺度：

\[
\Phi(x)=\sum_{n\ge1}(4\pi^2n^4e^{9x/2}-6\pi n^2e^{5x/2})e^{-\pi n^2e^{2x}},
\qquad \widehat\Phi(z)=\xi(1/2+iz).
\tag{1}
\]

\(\Phi\) 为正偶函数，在复条带 \(|\Im x|<\pi/4\) 内解析。所有固定阶实导数具有双指数尾。本文既不使用第五轮待完整复审的谱结论，也不假定零点简单或 RH。

Pólya 通用因子定理的适用条件是 \(U(iz)\) 属于 Laguerre–Pólya 类，不能以 U 正、偶、对数凹代替。对偶函数且 \(U(0)=1\)，其标准乘积形状为

\[
U(x)=e^{a x^2}\prod_j(1+t_jx^2),\qquad a\ge0,\quad t_j>0,\quad\sum_jt_j<\infty.
\tag{2}
\]

可允许空乘积和有限乘积。实零种子 \(\exp[-A\cosh(bx)]\) 的 Fourier 变换由 \(K_{iz/b}(A)\) 给出。相关来源见文末 [1] 的通用因子定理与 [2] 的 Bessel 积分平方公式。本文新计算和以下排除证明均不借用来源中的 RH 结论。

## 2. 已认证的真实源喷射

在原点定义实解析对数

\[
\log\frac{\Phi(x)}{\Phi(0)}=\sum_{k\ge1}\ell_{2k}x^{2k},
\qquad p_k=(-1)^{k+1}k\ell_{2k}\quad(k\ge2).
\tag{3}
\]

随附仅用 Python 标准库的有理区间程序严格认证了

\[
\begin{aligned}
24.217595281065&<p_4<24.217595281066,\\
74.323417808078&<p_5<74.323417808080,\\
220.503643148115&<p_6<220.503643148117,
\end{aligned}
\tag{4}
\]

以及

\[
\boxed{-183.902446914<p_4p_6-p_5^2<-183.902446911<0.}
\tag{5}
\]

这里的行列式来自源函数的对数 Taylor 系数，不是 Xi 的 Taylor 系数行列式，也不是仓库的 \(D_\beta(n,r)\)。这三种对象不能混用。

## 3. 认证为何覆盖完整无限 theta 和

令

\[
P_0(u)=2u-3,\qquad
P_{j+1}(u)=(5/2-2u)P_j(u)+2uP'_j(u).
\tag{6}
\]

直接微分单模态给出

\[
\Phi^{(j)}(0)=2\pi\sum_{n\ge1}n^2e^{-\pi n^2}P_j(\pi n^2).
\tag{7}
\]

次数为 \(j+1\)，且

\[
\|P_j\|_{\mathrm{coeff},1}\le5\,8^j j!.
\tag{8}
\]

证明：递推使系数绝对值之和至多乘 \(2j+13/2\le8(j+1)\)，初值为 5。对 \(j\le12,n\ge8\)，用 \(3<\pi<4\) 得到每个绝对导数项至多为

\[
C n^{28}e^{-3n^2},\qquad C=10\,4^{14}8^{12}12!.
\]

这些项的相邻比不超过

\[
(9/8)^{28}(3/8)^{51}<1/2,
\]

其中 \(e>8/3\) 可由其正 Taylor 和立即验证。因此所有未计算模态 \(n\ge8\) 的导数尾，在 \(0\le j\le12\) 上统一满足

\[
\boxed{\Delta=2C8^{28}(3/8)^{192}<10^{-27}.}
\tag{9}
\]

每个偶阶导数先计算 n=1,...,7 的有理区间，再加入 \([-\Delta,\Delta]\)。奇阶导数按真实 theta 反射恒等式准确为零，不以浮点残差代替偶性。

设 \(a_j=\Phi^{(j)}(0)/j!\)。对数转换使用有限代数递推

\[
\ell_n=\frac{n a_n-\sum_{k=1}^{n-1}k\ell_k a_{n-k}}{n a_0}.
\tag{10}
\]

程序已包围 \(a_0>0\)，所以所有除法合法。

pi 由 Machin 公式 \(16\arctan(1/5)-4\arctan(1/239)\) 的交错级数包围；指数先把 \(\pi n^2\) 除以256，在 [0,1] 用交错级数包围，再取256次幂。每次区间运算使用精确 `Fraction`，随后向外取到指定十进制有理格点。没有普通浮点值、特殊函数库或经验安全系数进入断言。

60 位和90位有理格点两次运行均通过同一组严格有理断言。`crosscheck_log_series.py` 另以有限形式级数 \(\log(1+u)=\sum_{j=1}^6(-1)^{j+1}u^j/j\) 重算对数转换并通过。这是第二种对数算法的交叉检查，不声称独立重证了 theta 尾或基础常数。

## 4. 全参数排除定理

### 定理1

设 V 为原点邻域内的偶实解析函数，记 \(v_j=[x^j]V(x)\)。若

\[
v_8\ge0,\qquad v_{10}\ge0,\qquad v_{12}\ge0,
\tag{11}
\]

则

\[
U(x)=\frac{\Phi(x)}{\Phi(0)}e^{V(x)-V(0)}
\tag{12}
\]

不可能在原点邻域等于满足 (2) 的函数。因此，它不能成为一个解析 Pólya 通用因子的限制。

### 证明

对 (2) 的乘积取局部对数。因为 \(\sum t_j<\infty\)，每个 \(k\ge2\) 的系数为绝对收敛和：

\[
s_k:=(-1)^{k+1}k[x^{2k}]\log U=\sum_jt_j^k.
\tag{13}
\]

从而 \(s_k\ge0\)，且由 Cauchy–Schwarz，

\[
s_4s_6-s_5^2
=\left(\sum t_j^4\right)\left(\sum t_j^6\right)
-\left(\sum t_j^5\right)^2\ge0.
\tag{14}
\]

但 (12) 给出

\[
s_4=p_4-4v_8,\qquad s_5=p_5+5v_{10},\qquad s_6=p_6-6v_{12}.
\tag{15}
\]

若 \(s_4<0\) 或 \(s_6<0\)，已经矛盾。否则，由 (4)、(11)、(15)，

\[
0\le s_4\le p_4,\quad s_5\ge p_5>0,\quad 0\le s_6\le p_6.
\]

所以

\[
s_4s_6-s_5^2\le p_4p_6-p_5^2<0,
\]

与 (14) 矛盾。证毕。

### 推论1A：任意 Bessel 参数与任意二次修正均被排除

对全部 \(A,b>0\) 及全部实 c，取

\[
V(x)=A(\cosh(bx)-1)+cx^2.
\]

它满足 (11)，故不存在

\[
\Phi(x)/\Phi(0)=e^{-A(\cosh(bx)-1)-cx^2}U(x)
\]

的上述通用因子表示。此结论不是在有限 A、b 网格上测试；参数的全量词由定理1的单侧代数比较给出。有限个正系数 cosh 势之和亦在排除范围内。

这没有断言附加任意 c 后的种子仍有实零 Fourier 变换；不论种子是否有那项性质，表示本身已经不可能。

### 推论1B：允许种子参数随逼近改变，也不存在局部 C12 逼近

定义局部构造类 \(K=e^{-V}U\)，其中 V 满足 (11)，U 满足 (2)，允许各项随 K 改变。不存在这样的实函数序列 K_j，在含原点的一个固定实区间上以 C12 拓扑趋于 \(\Phi\)。

证明：先把 \(K_j\) 在0处归一化。C12 收敛与 \(\Phi(0)>0\) 保证对数喷射也收敛。只要三个源喷射坐标落入

\[
24.21<p_4(K)<24.23,\quad
74.31<p_5(K)<74.34,\quad
220.49<p_6(K)<220.52,
\]

其行列式就满足

\[
p_4(K)p_6(K)-p_5(K)^2
<24.23\cdot220.52-74.31^2
=-357553/2000<0.
\]

对这些 K 重复定理1即矛盾。收敛序列最终必进入这个开邻域。证毕。

## 5. 独立的复边界事实：真实源不能在 iπ/4 解析延拓

本节不用喷射证书。

令 \(\Theta(u)=\sum_{n\in\mathbb Z}e^{-\pi n^2u}\)，\(\Re u>0\)。从 (1) 逐项计算，\(u=e^{2x}\) 时

\[
\Phi(x)=2u^{9/4}\Theta''(u)+3u^{5/4}\Theta'(u).
\tag{16}
\]

幂采用由原条带给定的连续分支。对 \(\epsilon>0\)，Poisson 求和给出

\[
\Theta(i+\epsilon)
=\sum_n(-1)^ne^{-\pi\epsilon n^2}
=\epsilon^{-1/2}\sum_{k\in\mathbb Z}e^{-\pi(k+1/2)^2/\epsilon}.
\tag{17}
\]

令 \(a=\pi/4\)。分离 k=0,-1 两项，得到

\[
\Theta(i+\epsilon)=2\epsilon^{-1/2}e^{-a/\epsilon}
\{1+O(e^{-2\pi/\epsilon})\}.
\]

对此 Gaussian 级数逐次微分合法；前两阶余项同样具有额外指数损失，附加有限个 \(\epsilon^{-1}\) 因子不改变主项。因此

\[
\Theta'(i+\epsilon)=2a\epsilon^{-5/2}e^{-a/\epsilon}(1+O(\epsilon)),
\quad
\Theta''(i+\epsilon)=2a^2\epsilon^{-9/2}e^{-a/\epsilon}(1+O(\epsilon)).
\]

令 \(x_\epsilon=\tfrac12\operatorname{Log}(i+\epsilon)\)。由 (16)，

\[
\boxed{\Phi(x_\epsilon)
=\frac{\pi^2}{4}i^{9/4}\epsilon^{-9/2}
 e^{-\pi/(4\epsilon)}(1+O(\epsilon)).}
\tag{18}
\]

而 \(x_\epsilon-i\pi/4=\epsilon/(2i)+O(\epsilon^2)\)。右侧非零但快于每个 \(\epsilon^N\) 趋零。若 \(\Phi\) 在 \(i\pi/4\) 有全邻域的全纯延拓，首个非零 Taylor 项会沿此曲线产生一个有限幂次主项，与 (18) 矛盾；若全部 Taylor 系数为零，延拓局部恒零，同样与 (18) 矛盾。故不存在该延拓。

这里只证明这一具体边界点，未声称整条边界都是自然边界。

## 6. 固定整个种子时，实区间逐点逼近也不成立

### 定理2

设 B 是固定整个函数，\(B(0)\ne0\)，且在原点附近一段实区间上为正。不存在满足 (2) 的 U_j 和正归一化常数 c_j，使 \(c_jB(x)U_j(x)\) 在该实区间逐点趋于 \(\Phi(x)\)。

### 证明

原点收敛给 \(c_jB(0)\to\Phi(0)\)。固定区间中的 r>0，逐点收敛保证充分大 j 的 \(U_j(r)\le M\)，其中可取 M>1。写 \(a_j,t_{j,k}\) 为 (2) 的参数，有

\[
a_j\le\frac{\log M}{r^2},\qquad
\sum_kt_{j,k}\le\frac{M-1}{r^2}.
\]

第二式使用 \(\prod_k(1+r^2t_{j,k})\ge1+r^2\sum_kt_{j,k}\)。于是

\[
|U_j(z)|\le\exp\left[\frac{\log M+M-1}{r^2}|z|^2\right]
\]

在整个复平面成立。Montel 定理给整个子列极限 U，实区间恒等定理说明 \(cBU\) 在原条带内等于 \(\Phi\)，其中 \(c=\Phi(0)/B(0)\)。左侧是整个函数，给出第5节不允许的延拓。矛盾。

这一定理只处理固定 B；变化种子的逐点逼近不由该证明排除。变化种子的 C12 逼近则在推论1B的明确系数条件下已排除。

## 7. 与 RH 主目标的严格关系

本次尝试没有进入全空间临界方差不等式的证明，也没有消去真实亚临界本征态。它排除了一种可直接产生全实零 Fourier 逼近的具体构造。不能把它泛化为“所有 Pólya 方法失败”“所有 Bessel 分解失败”或“RH 不成立”。

尤其仍未排除：非通用的、仅对当前种子有效的乘子；带新交叉项定理的积分平方表示；不满足 (11) 的变化势；其他非局部算术结构。它们不能以“未被排除”登记为已有证明。

已有仓库的原种子 theta 唯一性和 Dirichlet 保类障碍原样保留。本文不假定一般亚临界本征源也保持任何原种子或普通 Dirichlet 类，也没有重做有限素数截断、有限秩修正或仅定位本质谱的工作。

## 8. 实际运行、复算与来源

运行环境：Python 3.13.5；无第三方包。主证书60位与90位均通过，形式对数交叉检查90位通过。

```sh
python certify_theta_jet.py --digits 60 --output new_certificate_60.json
python certify_theta_jet.py --digits 90 --output new_certificate_90.json
python crosscheck_log_series.py new_certificate_90.json --output new_crosscheck.json
```

程序使用排他创建。证书保留脚本 SHA-256、源多项式、完整导数包围、未截断 theta 尾界及所有断言。输出中的90位小数是向外包围端点，不代表证明了90位准确值；区间宽度主要由明确的无限尾界决定。

[1] Y. Shi, *Real-rooted Pólya-like approximations to the Riemann Xi-function*, Definition 1 与 Lemma 1：Laguerre–Pólya 乘积和 Pólya 通用因子定理。https://arxiv.org/html/1502.06844

[2] G. Gasper, *Using integrals of squares of certain real-valued special functions...*, §1–2，尤其 (1.5)、(2.6)：Bessel 种子的积分平方证明。https://arxiv.org/html/0801.2996

[3] NIST DLMF §20.7(viii)，theta 模变换；本稿 (17) 同时可由 Gaussian Poisson 求和直接推出。https://dlmf.nist.gov/20.7#viii

[4] 项目当前源刚性与转移边界：`reports/20261011_theta_dirichlet_rigidity/REPORT.md`，固定提交 `4d2cc4cf6a147078c7a4bcc4922f7d5639223d5e`。目标、真实核及符号继续以原仓库为准。
