# Lean 工具准备与形式化入口审查

状态：**BLOCKED_NETWORK_ALLOWLIST；Lean 未安装；内核验收未运行。**

## 1. 审查对象与范围

- 仓库：<https://github.com/aa339519589-cpu/Riemann-Hypothesis>
- 实际审查提交：`74add2e1350dd4414d83dd46a4e10be8aeb7b42f`。
- 已跟踪文件：770 个；`.lean` 源码：0 个；`lean-toolchain`、`lakefile.lean`、`lakefile.toml`、`lake-manifest.json`：均为 0 个。
- 仅使用助手自己的云端环境，没有访问用户电脑，没有改动已有仓库文件，没有付费。

`history/source-materials/rh_verified_definitions_20261007.md:186` 引用了 `ActualRiemannXiEndpoint.lean`、`ActualRiemannXiTransform.lean`、`ActualRiemannRootExtractionClosure.lean` 以及 Mathlib 中的文件，但这些 Lean 源码及其依赖锁定文件不在本次仓库提交内。

因此，**无法核验被引用定理的完整类型、隐藏前提、依赖公理、是否使用 `sorry`/`admit`、是否实际连接到 Mathlib 的 RH 命题、或是否通过 Lean 内核检查**。Markdown 中的定理名称、行号和既有核验陈述不能代替源码与编译日志。没有发现 `.lean` 文件不能解释成“形式化证明已通过审计”。

## 2. 官方来源与版本选择

该仓库没有既定工具链可匹配，故为独立的核心 Lean 冒烟检查准备了固定稳定版：

- Lean：`leanprover/lean4:v4.34.1`，官方发布于 2026-09-24。
- elan：`v4.2.4`，官方发布于 2026-08-25。
- elan Linux x86_64 压缩包的官方发布元数据 SHA-256：`42b94d4244e8353142c456ec0e4ca6528fd898a6c604d4059f494e706e431f63`。因为压缩包未下载成功，该摘要**尚未与本地二进制校验**。
- 当前 Mathlib `master` 要求 `leanprover/lean4:v4.35.0-rc4`，不应无意跟随该候选版。若后续添加稳定 Mathlib 项目，可以采用 Mathlib `v4.34.0`（提交 `5ed2965256430c3649e86755f9576b54eca72435`）并严格匹配其 `leanprover/lean4:v4.34.0` 工具链。此 Mathlib 尚未安装。

核验来源：

- <https://lean-lang.org/install/>
- <https://github.com/leanprover/elan>
- <https://github.com/leanprover/elan/releases/tag/v4.2.4>
- <https://github.com/leanprover/lean4/releases/tag/v4.34.1>
- <https://github.com/leanprover-community/mathlib4/blob/v4.34.0/lean-toolchain>

## 3. 实际执行结果

| 检查 | 实际结果 |
| --- | --- |
| 初始 `command -v lean` / `command -v elan` | 均未找到 |
| 常见云端工具目录的限定路径检查 | 未找到已有 Lean/elan/lake |
| `/tmp` 空间 | 约 4.1 GiB 可用，容量约 4.9 GiB |
| `/workspace/shared` 空间 | 约 30 GiB 可用，容量约 32 GiB |
| 下载官方 `https://elan.lean-lang.org/elan-init.sh` | 成功，9823 字节；检查脚本指向官方 `leanprover/elan` 发布页 |
| 下载官方 elan v4.2.4 Linux 二进制 | 失败，HTTP 403；没有安装或执行二进制 |
| 对同一官方地址的 HEAD 诊断 | `CONNECT tunnel failed, response 403`；`x-proxy-error: blocked-by-allowlist` |
| 安装脚本与验收脚本的 `bash -n` | 通过，仅说明 shell 语法检查通过 |
| 执行 `check-smoke.sh` | 退出码 127：`NOT_RUN: lean is unavailable on PATH.` |
| 编译 `Smoke.lean` | **未运行** |
| `#print axioms` 检查 | **未运行** |
| RH 形式化证明 | **没有完成，也没有声称完成** |

网络诊断开始时间为 **2026-10-11 12:10:10 UTC / 北京时间 2026-10-11 20:10:10**；代理响应头日期为 **2026-10-11 12:10:26 UTC / 北京时间 2026-10-11 20:10:26**。后者是响应头时间，并非自行推定的编译时间。原始日志保存在 `evidence/`。

这是已核实的网络白名单限制，不是 Lean 本身的编译错误。没有改换非官方镜像、代理、凭证或其他路径绕过该限制。

## 4. 已准备但未经 Lean 编译的验收入口

`formal-smoke/Smoke.lean` 是候选的核心 Lean 小检查，仅依赖 `Init`：

1. 自然数的 `n + 0 = n`。
2. 对任何有限截止值，都存在一个谓词满足该截止值之前的所有自然数、却不满足所有自然数。这只形式表达“任意谓词的有限前缀不能单独推出全称结论”，**不是有关真实 zeta 函数的反例，也不是 RH 的否证或证明**。

该源文件没有 `sorry`、`admit`、自定义 `axiom`、`sorryAx` 或 `unsafe` 标记。但静态文本检查不等于内核验证。源文件、脚本和预期输出格式仍须在实际 Lean 可用后复核。

`check-smoke.sh` 要求：

- 实际调用固定工具链的 `lean`，将警告当作错误；
- 产生 `.olean` 与真实编译日志；
- 两个声明的 `#print axioms` 输出均明确报告不依赖任何公理；
- 只把这个小检查标记为通过，不把它升格为 RH 证明。

## 5. 后续正常安装命令（本次未执行成功）

需在已获准访问官方发布地址的云端环境运行，不能用这些命令绕过当前限制。预留足够磁盘空间；不覆盖已有工具链或修改全局 shell 配置。

```bash
cd formal-smoke
bash scripts/install-lean-isolated.sh /workspace/shared/rh-toolchains-20261011
export ELAN_HOME=/workspace/shared/rh-toolchains-20261011/elan
export PATH="$ELAN_HOME/bin:$PATH"
bash scripts/check-smoke.sh
```

`install-lean-isolated.sh` 对 Linux x86_64 的 elan 压缩包做固定摘要校验，再以 `--no-modify-path --default-toolchain none` 安装到隔离的 `ELAN_HOME`，最后请求固定 Lean v4.34.1。此脚本尚未端到端验证。Mathlib 不是该最小测试的依赖，没有进行大体积 Mathlib 下载。

云端临时目录或工作区的存在不构成跨环境永久保存保证。可靠复用需要保留版本锁定、脚本与编译证据，并在环境更换后重新核验实际工具是否可用。

## 6. 真正 RH 形式化审查仍缺少什么

需要将真实 `.lean` 源文件、匹配的 `lean-toolchain`、Lake 配置和依赖锁定文件纳入获授权的仓库范围，然后：

1. 检查最终定理的完整类型与全部前提，尤其是正性、根提取、覆盖和全量词闭合条件。
2. 运行干净构建，禁止用 `sorry`、`admit` 或自定义 RH 公理补缺口。
3. 对最终定理及其关键桥接声明运行 `#print axioms`，区分标准库基础公理和新增假设。
4. 检查结论确实使用准确的 zeta/RH 定义，而非同名弱化对象。
5. 保存固定提交、依赖版本、命令、退出码和真实编译日志。

本记录不把文稿的逻辑推导、有限数值结果或工具安装本身当作 RH 证明。
