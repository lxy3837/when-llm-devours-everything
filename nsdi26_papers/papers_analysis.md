# NSDI 2026 论文分析与热门方向总结

> 数据来源: https://www.usenix.org/conference/nsdi26/technical-sessions
> 接收率: Spring 24.2% (50/207), Fall 22.1% (100/452)

---

## 一、大语言模型 (LLM) 相关论文 —— 绝对主导

NSDI 2026 最显著的特点是 **LLM 相关论文占据了大幅版面**，涵盖训练、推理、调度、存储等全栈方向。

### 1. LLM 训练 (Training)

| 论文 | 机构 | 关键词 |
|------|------|--------|
| **SYMI**: Efficient MoE Training via Model and Optimizer State Decoupling | Stanford, NVIDIA, OpenAI | MoE, 训练优化, 解耦 |
| **Checkpoint Lite, Recover Right**: Fault Tolerant Training of MoE with Sparse Checkpoints | Stanford, NVIDIA | MoE, 容错, 检查点 |
| **Di-PS**: Async Heterogeneous Cross-Cluster LLM Training at Scale | NUDT, Shanghai AI Lab, NTU | 跨集群训练, 异步 |
| **Attack of the Bubbles**: Straggler-Resilient Pipeline Parallelism | HKUST, Alibaba | 流水线并行, 容错 |
| **Flare**: Anomaly Diagnostics for LLM Training in GPU Clusters (6000+ GPUs) | SJTU, Ant Group, NUS | 异常诊断, 大规模集群 |
| **EROICA**: Online Performance Troubleshooting (100,000 GPUs, 1.5年生产部署) | Alibaba | 在线排障, 生产系统 |
| **RollPacker (Flexes)**: Taming Long-Tail Rollouts for RL Post-Training | HKUST, Alibaba | RL后训练, 强化学习 |
| **Wormhole**: Packet-Level Network Simulation of Large Model Training (744x加速) | 清华, 华为 | 网络仿真, 训练建模 |
| **GPUSynth / Phantora**: ML Training Performance Estimation | Duke, UC Berkeley, Meta | GPU仿真, 性能预估 |

### 2. LLM 推理 (Inference)

| 论文 | 机构 | 关键词 |
|------|------|--------|
| **FastServe**: Iteration-Level Preemptive Scheduling for LLM Inference | 北大 | 抢占式调度, vLLM替代 |
| **JITServe**: SLO-aware LLM Serving with Imprecise Request Info | UIUC, NJU, Google Labs | SLO感知, 在线调度 |
| **Libra**: Flexible Request Partitioning and Scheduling for LLM | NUS, USTC, UC Berkeley | 请求分区, 负载均衡 |
| **FlexLLM**: Token-Level Co-Serving of LLM Inference + Finetuning | CMU, Purdue, Anthropic | 推理+微调共部署 |
| **HydraServe**: Minimizing Cold Start Latency for Serverless LLM | 北大, 阿里云 | Serverless, 冷启动 |
| **SwiftEP**: Accelerating MoE Inference with Buffer Fusion | Tencent, NJU | MoE推理加速 |
| **Agentix**: Serving Engine for LLM Agents as General Programs | UC Berkeley, Google DeepMind | LLM Agent, 程序级调度 |
| **Cortex**: Semantic-Aware Knowledge Caching for LLM Agents | NUS, USTC, UofT, Sea AI Lab | 语义缓存, Agent |
| **SMetric**: Session-Centric Scheduling for Agentic LLM Serving | SJTU, Alibaba | Agent调度, KV Cache |

### 3. KV Cache 管理 (热门子方向)

| 论文 | 机构 | 关键词 |
|------|------|--------|
| **DroidSpeak**: KV Cache Sharing Across Fine-tuned Model Variants | UChicago, Microsoft | KV Cache复用, 跨模型 |
| **SYMPHONY**: Improving Memory Management for LLM Inference | UT Austin, UW-Madison | KV Cache迁移, 多轮对话 |

### 4. LLM 微调与存储

| 论文 | 机构 | 关键词 |
|------|------|--------|
| **MuxTune**: Multi-Task LLM Fine-Tuning via Backbone Multiplexing | SJTU, NUS | 多任务微调, 多租户 |
| **ZipLLM**: Efficient LLM Storage via Deduplication and Compression | UVA, Harvard | 模型存储压缩 |

---

## 二、机器学习在网络系统中的应用

| 论文 | 机构 | 关键词 |
|------|------|--------|
| **UNUM**: Network Control Framework using Transformers | UT Austin | Transformer, 网络控制, 拥塞控制 |
| **PolicyCache**: Intra-flow Learning in Congestion Control | USTC, HKUST, 华为 | 在线学习, 拥塞控制 |
| **Oscar**: O(1)-Step Convergence Congestion Control | NJU, SJTU | 拥塞控制, 快速收敛 |
| **SpliDT**: Partitioned Decision Trees for Line-Rate Stateful Inference | Purdue, UMich, UCSB | 决策树, 线速推理 |

---

## 三、分布式训练基础设施

| 论文 | 机构 | 关键词 |
|------|------|--------|
| **Checkmate**: Zero-Overhead Checkpointing via Network Gradient Replication | Tufts, MIT | 检查点优化, 网络内计算 |
| **FAST**: Efficient Scheduler for All-to-All GPU Communication | CMU, MangoBoost, UW | All-to-All通信, MoE |
| **FalconFS**: Distributed File System for Deep Learning Pipeline | SJTU, 华为 | 分布式文件系统, DL Pipeline |

---

## 四、生成式AI与多模态

| 论文 | 机构 | 关键词 |
|------|------|--------|
| **Morphe**: High-Fidelity Generative Video Streaming with Vision Foundation Model | CUHK-Shenzhen, 北大 | 生成式视频, 视觉基础模型 |
| **From Bits to Tokens**: Knowledge-Driven Generative Communication of Multimodal Data | UCSD, USC, CUHK | 多模态, 生成式通信 |

---

## 五、向量搜索与存储

| 论文 | 机构 | 关键词 |
|------|------|--------|
| **DistVS**: Large-scale Vector Search with Compute-Memory Disaggregation | CUHK, 华为云 | 向量搜索, 存算分离 |

---

## 六、Session 专题名称

会议专门设置了以下与 ML/DL 相关的专题 session：
- **"All Your Networks Are Belong to ML"** — 网络控制全面ML化
- **"Overfitting the Internet"** — 机器学习在网络中的深度应用

---

## 总结：2026年 NSDI 最火的研究方向

### 1. LLM 推理服务化 (最热)
- **请求级/迭代级抢占式调度** (FastServe, JITServe, Libra)
- **SLO感知的在线调度** (TTFT/TPOT保证)
- **Prefill-Decode分离架构**下的调度优化
- **Serverless LLM** 冷启动优化 (HydraServe)

### 2. LLM Agent 服务 (新兴爆发方向)
- Agent程序级调度 (Agentix)
- 语义感知知识缓存 (Cortex)
- Session级别KV Cache管理 (SMetric)
- **Agent正在取代传统Chatbot成为新的LLM服务范式**

### 3. MoE (Mixture-of-Experts) 全栈优化
- MoE训练: 参数/优化器状态解耦 (SYMI)
- MoE推理加速 (SwiftEP)
- MoE通信调度 (FAST)
- **MoE架构已成为大模型的主流选择，对系统提出全新挑战**

### 4. 大规模训练系统的可观测性与容错
- 万卡级GPU集群的异常诊断 (Flare, EROICA)
- 训练性能建模与仿真 (Wormhole, GPUSynth)
- 流水线并行的straggler容忍 (Attack of the Bubbles)
- **从"能不能训练"到"如何高效稳定地训练万卡集群"**

### 5. ML驱动的网络控制
- Transformer用于网络状态嵌入 (UNUM)
- 在线学习拥塞控制 (PolicyCache)
- 决策树线速推理 (SpliDT)
- **ML方法正从"辅助"走向"原生"网络控制方案**

### 6. RL (强化学习) 后训练
- RLHF/RL post-training的调度优化 (RollPacker)
- RL作为LLM推理能力增强的关键技术路线

### 7. KV Cache 优化
- 跨模型KV Cache共享复用
- KV Cache迁移与调度
- 多轮对话场景下的内存管理

---

## 关键词频率统计

| 关键词 | 出现次数 | 趋势 |
|--------|----------|------|
| LLM / Large Language Model | 20+ | **爆发式增长** |
| Inference / Serving | 12+ | **极热** |
| Training | 10+ | **持续热门** |
| MoE (Mixture-of-Experts) | 6+ | **新热点** |
| Agent | 4+ | **新兴方向** |
| KV Cache | 4+ | **热门子方向** |
| Scheduling | 8+ | **核心主题** |
| RL / Reinforcement Learning | 3+ | **稳定关注** |
| Transformer | 2+ | **作为工具出现** |
| Machine Learning (通用) | 多处 | **深度渗透** |
| CNN / RNN / LSTM / RWKV | 0 | **基本未出现** |

> **结论**: CNN、RNN、LSTM、RWKV 等传统架构在 NSDI 2026 基本没有出现。当前系统研究的焦点完全集中在 **LLM (Transformer架构)、MoE、Agent** 三大主题上。联邦学习 (Federated Learning) 也未在 NSDI 2026 主会中出现。
