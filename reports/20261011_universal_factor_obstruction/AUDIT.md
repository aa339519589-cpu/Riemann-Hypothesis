# 本轮复核与证书使用

目标仍为无条件完整证明 RH；本目录未完成该目标。

1. 已执行主程序的60位、90位有理向外区间计算，两次均通过 REPORT.md 中相同的有理上下界断言。`RUNS.json` 记录实际运行摘要。主程序无第三方依赖。
2. `certificate_portable.json` 将90位运行的端点用精确有理运算向外放宽到30位小数，保留全部0至12阶偶导数的有效包围，便于直接读取和复算。它不是90位精确值列表。原始90位输出可由主程序重新生成。
3. 已实际执行 `python crosscheck_log_series.py certificate_portable.json --output new_crosscheck.json`。另一种形式对数展开仍严格给出负行列式；同一输出保存在 `crosscheck_portable.json`。该交叉检查不独立验证 pi、指数和 theta 尾。
4. 边界论证中的 theta 微分身份及主双高斯项的一、二阶导数，另外用 SymPy 1.14.0 做了精确代数核对，均通过；Poisson 求和、余项微分和不可延拓论证仍由正文解析证明承担，而非由该符号检查认证。
5. 排除结论严格限于所写通用因子类、V 的三个系数符号条件、局部 C12 拓扑，以及固定整个种子的逐点构造。没有把它扩成所有 Pólya 方法或 RH 的否定。
6. 没有执行 Lean 内核验证，也没有获得外部独立评审。长任务检查点服务两次网络超时，没有产生有效回执；未将服务调用登记为验收。

## 复算

```sh
python certify_theta_jet.py --digits 90 --output new_certificate_90.json
python crosscheck_log_series.py new_certificate_90.json --output new_crosscheck_90.json
python crosscheck_log_series.py certificate_portable.json --output new_crosscheck_portable.json
```

所有输出均排他创建。保留旧仓库和旧输入不变。`REPORT.md`、两个程序的提交 blob 均已与本地文件的 Git SHA-1 核对一致。
