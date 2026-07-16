# USENIX 近两年（2023-2025）深度学习/机器学习相关论文总结

> 数据来源：USENIX Security, OSDI, ATC, NSDI 等顶会  
> 抓取时间：2026-07-16

---

## 一、爬取到的相关论文列表（按方向分类）

### 1. 大语言模型（LLM）推理/服务优化 —— 最热门方向

| 论文 | 会议 | 年份 | 要点 |
|------|------|------|------|
| **Sarathi-Serve: Taming Throughput-Latency Tradeoff in LLM Inference** | OSDI | 2024 | chunked-prefill 方法，比 vLLM 吞吐提升 2.6-5.6 倍 |
| **ServerlessLLM: Low-Latency Serverless Inference for LLMs** | OSDI | 2024 | 多级 checkpoint 加载 + Serverless 架构 |
| **CachedAttention: Cost-Efficient LLM Serving for Multi-turn Conversations** | ATC | 2024 | KV Cache 跨轮复用，TTFT 降低 87%，成本降 70% |
| **PUZZLE: Efficiently Aligning LLMs through Light-Weight Context Switch** | ATC | 2024 | LLM 对齐阶段的多模型/多工作负载高效切换 |
| **StreamBox: A Lightweight GPU SandBox for Serverless Inference Workflow** | ATC | 2024 | GPU 细粒度隔离，内存减 82%，吞吐提 6.7 倍 |
| **μ-Serve: Power-aware Deep Learning Model Serving** | ATC | 2024 | GPU 频率动态调节，功耗节省 1.2-2.6 倍 |
| **Obscura: Computationally Efficient Pipeline Training for LLMs** | ATC | 2025 | 流水线并行中优化重计算开销 |
| **FlexLLM: Co-serving LLM Inference and PEFT-based Finetuning** | NSDI | 2026 | 推理+微调共享 GPU，token 级融合计算 |
| **WaferLLM: Sub-millisecond-per-token Inference on Wafer-Scale Chips** | ;login: | 2025 | 晶圆级芯片上的 LLM 推理系统 |

### 2. 深度学习模型安全攻击

| 论文 | 会议 | 年份 | 要点 |
|------|------|------|------|
| **PELICAN: Exploiting Backdoors of Naturally Trained DL Models in Binary Code Analysis** | Security | 2023 | Transformer 模型在二进制分析中的自然后门利用 |
| **EaTVul: ChatGPT-based Evasion Attack Against Software Vulnerability Detection** | Security | 2024 | 用 ChatGPT 生成对抗样本绕过漏洞检测 |
| **Dirty Road Can Attack: Security of DL-based Automated Lane Centering** | Security | 2021 | 物理世界对抗攻击自动驾驶车道居中 |
| **Deep-Dup: Adversarial Weight Duplication Attack in Multi-Tenant FPGA** | Security | 2021 | FPGA 多租户场景下的 DNN 权重复制攻击 |
| **DeepRed: ML-powered C2 Framework using GANs** | WOOT | 2025 | 用 GAN 生成对抗流量绕过 ML-NIDS |
| **A Plot is Worth a Thousand Words: Model Information Stealing via Scientific Plots** | Security | 2023 | 从论文图表反向推断模型架构/超参数 |
| **Hard-Label Adversarial Attack with Theoretical Foundations** | Security | 2026 | 黑盒硬标签对抗攻击 |

### 3. 深度学习模型隐私

| 论文 | 会议 | 年份 | 要点 |
|------|------|------|------|
| **How Does a DL Model Architecture Impact Its Privacy? CNNs vs Transformers** | Security | 2024 | Transformer 比 CNN 更容易受隐私攻击（成员推断、属性推断、梯度反演） |
| **Fast and Private Inference of DNNs by Co-designing Activation Functions** | Security | 2024 | 通过激活函数协同设计实现快速隐私推理 |
| **LOHEN: Layer-wise Optimizations for NN Inferences over Encrypted Data** | Security | 2025 | 全同态加密下的神经网络推理，性能提升 1.08-2.88x |
| **Compass: Encrypted Semantic Search with High Accuracy** | OSDI | 2025 | 加密语义搜索 |

### 4. 深度学习赋能安全检测/分析

| 论文 | 会议 | 年份 | 要点 |
|------|------|------|------|
| **Breaking the Blindfold: DL-based Blind Side-channel Analysis** | Security | 2025 | 首个成功的盲侧信道分析（AES/Ascon/Kyber） |
| **AI Psychiatry: Forensic Investigation of DL Networks in Memory Images** | Security | 2024 | 从内存镜像中取证分析深度学习网络 |

### 5. 神经架构搜索（NAS）

| 论文 | 会议 | 年份 | 要点 |
|------|------|------|------|
| **LitePred: Transferable and Scalable Latency Prediction for Hardware-Aware NAS** | NSDI | 2024 | VAE+分布相似度检测，85 个边缘平台 99.3% 精度预测延迟 |

### 6. 其他 AI/ML 系统方向的论文

| 论文 | 会议 | 年份 | 要点 |
|------|------|------|------|
| **Fast-PGM: Fast Inference for Probabilistic Graphical Models** | ATC | 2024 | 概率图模型推理加速 3-20x |
| **RUMMY: Fast Vector Query Processing Beyond GPU Memory** | NSDI | 2024 | 向量检索中数据传输与计算流水线重排，比 CPU 快 23.1x |
| **Bayesian Code Diffusion for Efficient Automatic DL Program Optimization** | OSDI | 2025 | 贝叶斯+代码扩散模型优化深度学习程序 |
| **Accelerating Software Development: The LLM (R)evolution** | OSDI/ATC | 2025 | 联合 Keynote：LLM 将引发软件开发工具的寒武纪大爆发 |

### 7. 可持续 AI / AI 基础设施

| 论文 | 会议 | 年份 | 要点 |
|------|------|------|------|
| **Scaling AI Sustainably** | OSDI/ATC | 2024 | Joint Keynote: AI 碳足迹优化，从芯片制造到数据中心全生命周期 |
| **Understanding the Workload Characteristics of LLM Development** | ;login: | 2024 | 上海 AI 实验室 6 个月 GPU 集群 trace 分析 |
| **EcoScale: Giving Old Servers New Life at Hyperscale** | OSDI | 2025 | 老旧服务器再利用 |
| **Low-Overhead Silent Data Corruption Detection for LLM Training** | OSDI | 2025 | LLM 训练中的静默数据损坏检测 |

---

## 二、最近火的方向总结

### 热点 1：LLM 推理/服务系统优化（绝对 C 位）

这是 2024-2025 年 USENIX 系列会议中最密集的方向。从 OSDI '24 开设专门的 "Low-Latency LLM Serving" session，到 ATC '25/OSDI '25 延续相关 track，可以清晰看到：

- **KV Cache 优化**：多轮对话复用 KV Cache（CachedAttention）、KV Cache 工作负载特征分析
- **调度优化**：chunked-prefill（Sarathi-Serve）、推理+微调共置调度（FlexLLM）
- **Serverless 架构**：GPU 沙箱（StreamBox）、checkpoint 快速加载（ServerlessLLM）
- **硬件加速**：晶圆级芯片（WaferLLM）
- **功耗优化**：GPU 频率动态调节（μ-Serve）

**一句话：LLM 推理的性价比优化是当前系统工程研究的第一战场。**

### 热点 2：AI 安全 —— 攻击面向 LLM 全面迁移

Security 会议上 ML 相关论文占比越来越高，且重心从传统 DNN 攻击转向 LLM：

- **LLM 辅助攻击**：用 ChatGPT 生成对抗样本绕过检测（EaTVul）
- **模型隐私对比**：Transformer vs CNN 的隐私脆弱性系统研究
- **同态加密推理**：全同态加密下的神经网络推理（LOHEN）
- **大模型供应链安全**：模型权重复制攻击、内存取证

### 热点 3：AI for Security（用 AI 做安全）

- **侧信道分析**：深度学习首次成功实现盲侧信道分析
- **恶意流量生成**：用 GAN 生成对抗流量测试 NIDS

### 热点 4：可持续 AI / 绿色计算

- OSDI '24 和 ATC '24 的联合 Keynote 主题就是可持续 AI
- LLM 训练的能耗分析成为关注焦点
- 老旧服务器再利用、静默数据损坏检测等基础设施方向

### 热点 5：向量/Embedding 基础设施

- 向量检索加速（RUMMY）、加密语义搜索（Compass）

### 较少出现的方向（在 USENIX 这些会议上）

- **联邦学习**：在 USENIX Security/OSDI/ATC 中几乎看不到联邦学习论文
- **强化学习**：很少出现，更多在 ML 专属会议（NeurIPS/ICML）
- **CNN/RNN/LSTM**：这些传统架构已不是研究热点，被 Transformer/LLM 取代
- **RWKV**：完全没有出现在 USENIX 会议上
- **图神经网络（GNN）**：零星出现

---

## 三、趋势判断

1. **LLM 吃掉一切**：系统会议（OSDI/ATC/NSDI）的 ML 研究 80%+ 围绕 LLM 展开，传统 CV/NLP 模型的系统优化论文急剧减少。

2. **从训练到推理的转变**：2023 年还有不少训练优化论文，2024-2025 明显转向推理/部署优化，因为推理成本已成为实际生产中的主要瓶颈。

3. **AI 安全热度持续攀升**：Security 会议上 ML 安全论文占比逐年增加，尤其是 LLM 特有的安全问题（提示注入、越狱、对齐）。

4. **软硬协同成为标配**：单纯软件优化已不够，晶圆级芯片、CXL 内存、GPU 频率调节等硬件层面的协同设计成为新趋势。

5. **绿色 AI 成为主流叙事**：从可选题变成必答题，Keynote 都在讲可持续。

---

*本文件根据 USENIX 官网公开的论文标题和摘要整理，覆盖 2023-2025 年主要 USENIX 会议。*
