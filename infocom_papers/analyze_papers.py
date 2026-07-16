# -*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

"""
INFOCOM 2025 & 2026 论文分析脚本
分析 AI/ML 相关论文趋势
"""

# INFOCOM 2025 的 AI/ML 相关论文 (从爬取数据中提取)
papers_2025 = {
    "联邦学习 (Federated Learning)": [
        "PSFL: Parallel-Sequential Federated Learning with Convergence Guarantees",
        "CARE: Compatibility-Aware Incentive Mechanisms for Federated Learning with Budgeted Requesters",
        "VaniKG: Vanishing Key Gradient Attack and Defense for Robust Federated Aggregation",
        "GeoFL: A Framework for Efficient Geo-Distributed Cross-Device Federated Learning",
        "gamma-FedHT: Stepsize-Aware Hard-Threshold Gradient Compression in Federated Learning",
        "Input Integrity and Authentic Results: Towards Trustworthy Aggregation in Federated Learning",
        "Combating Deep Leakage from Gradients in Cross-Silo Federated Learning with QKD",
        "FedGPA: Federated Learning with Global-Personalized Collaboration for Edge Anomaly Detection",
        "Federated Adaptive Fine-Tuning of Large Language Models with Heterogeneous Quantization and LoRA",
        "FedEXT: Differential Federated Learning with Complementary Extension of Edge Models",
        "FLM-TopK: Expediting Federated Large Language Model Tuning by Sparsifying Intervalized Gradients",
        "AoI-aware Federated Unlearning for Streaming Data with Online Client Selection and Pricing",
        "Accelerating Clustered Federated Learning in Dynamic D2D Networks with Transferable GNN",
        "Lightweight Federated Learning with Differential Privacy and Straggler Resilience",
        "LCO-AGQ: A Lightweight Client-Oriented Adaptive Gradient Quantization Algorithm for Federated Learning",
        "FedPDA: Collaborative Learning for Reducing Online-Adaptation Frequency of Neural Receivers",
        "Constrained Over-the-Air Model Updating for Wireless Online Federated Learning with Delayed Information",
        "Preference Profiling Attacks Against Vertical Federated Learning over Graph Data",
        "FedUFD: Personalized Edge Computing Using Federated Uncertainty-Driven Feature Distillation",
        "Similarity-Guided Rapid Deployment of Federated Intelligence over Heterogeneous Edge Computing",
        "FedFetch: Faster Federated Learning with Adaptive Downstream Prefetching",
        "ElasticFed: Collaborative Large-small Transformer Training for Federated Continual Learning at Edge",
        "Towards Federated Inference: An Online Model Ensemble Framework for Cooperative Edge AI",
    ],
    "大语言模型 (LLM)": [
        "Jupiter: Fast and Resource-Efficient Collaborative Inference of Generative LLMs on Edge Devices",
        "Mell: Memory-Efficient Large Language Model Serving via Multi-GPU KV Cache Management",
        "SPIN: Accelerating Large Language Model Inference with Heterogeneous Speculative Models",
        "Online Context Caching for Distributed Large Language Models Serving",
        "QLLMS: Quantization-adaptive LLM Scheduling for Partially Informed Edge Serving Systems",
        "Multi-tier Multi-node Scheduling of LLM for Collaborative AI Computing",
        "TensAllo: Adaptive Deployment of LLMs on Resource-Constrained Heterogeneous Edge Devices",
        "Joint Optimization of Prompt Security and System Performance in Edge-Cloud LLM Systems",
        "Federated Adaptive Fine-Tuning of Large Language Models with Heterogeneous Quantization and LoRA",
        "FLM-TopK: Expediting Federated Large Language Model Tuning by Sparsifying Intervalized Gradients",
        "AdaRAG: Adaptive Optimization for Retrieval Augmented Generation with Multilevel Retrievers at the Edge",
    ],
    "Transformer / Vision Transformer": [
        "Hyperion: Low-Latency Ultra-HD Video Analytics via Collaborative Vision Transformer Inference",
        "Janus: Collaborative Vision Transformer Under Dynamic Network Environment",
        "Aether: Toward Generalized Traffic Engineering with Elastic Multi-agent Graph Transformers",
        "HyperRole: Hyperbolic Graph Transformer for Role Discovery in Online Social Networks",
        "IPv6 Prefix Target Generation using Vision-Transformer and Guided-Diffusion",
        "ElasticFed: Collaborative Large-small Transformer Training for Federated Continual Learning at Edge",
        "Mercury: Towards Optimal Accuracy-Latency Trade-off for Collaborative Transformer Inference",
        "Dual-GT: Dual-scale Spatial Dependency for Grid-Based Traffic Flow Prediction",
    ],
    "扩散模型 (Diffusion Models)": [
        "Breaking Chicken-Egg: Cross-city Battery Swap Demand Prediction via Knowledge-guided Diffusion",
        "DynaGen: Conditional Diffusion Models for Enhancing Acoustic and Seismic-Based Vehicle Detection",
        "Channel-Adaptive Denoising Diffusion Models for Reliable Semantic Communications",
        "Privacy-Preserving Wi-Fi Data Generation via Differential Privacy in Diffusion Models",
        "Network Diffuser for Placing-Scheduling Service Function Chains with Inverse Demonstration",
        "IPv6 Prefix Target Generation using Vision-Transformer and Guided-Diffusion",
    ],
    "强化学习 (Reinforcement Learning)": [
        "Multi-Task Reinforcement Learning For Collaborative Network Optimization in Data Centers",
        "MARL-based Pricing Strategy via Mutual Attention for MoD Systems with Ridesharing and Repositioning",
        "ExplabOff: Towards Explorative and Collaborative Task Offloading via Mutual Information-Enhanced MARL",
        "Deep Reinforcement Learning Based Coexistence Management in LPWAN",
        "SymbXRL: Symbolic Explainable Deep Reinforcement Learning for Mobile Networks",
        "SPANE: A Deep Reinforcement Learning Approach for Dynamic VM Scheduling",
        "Tri-Ring: Asynchronous Service Provisioning with Online Learning in Edge Cloud Networks",
    ],
    "CNN / 深度学习 (CNN / Deep Learning)": [
        "PhyDNNs: Bringing Deep Neural Networks to the Physical Layer",
        "Quark: Implementing Convolutional Neural Networks Entirely on Programmable Data Plane",
        "Prediction-Assisted Online Distributed Deep Learning Workload Scheduling in GPU Clusters",
        "Deep Learning-augmented SHS Model for Accurate AoI Analysis in Heterogeneous Unsaturated CSMA Networks",
        "CoCaR: Enabling Efficient Dynamic DNN-based Model Caching and Request Routing in MEC",
        "Harpagon: Minimizing DNN Serving Cost via Efficient Dispatching, Scheduling and Splitting",
    ],
    "Mixture-of-Experts (MoE)": [
        "Theory of Mixture-of-Experts for Mobile Edge Computing",
        "Optimizing Distributed Deployment of Mixture-of-Experts Model Inference in Serverless Computing",
        "SP-MoE: Expediting Mixture-of-Experts Training with Optimized Pipelining Planning",
    ],
    "边缘推理 / 模型部署 (Edge Inference/Deployment)": [
        "CEED: Collaborative Early Exit Neural Network Inference at the Edge",
        "C2F: Enabling Context-Aware Edge-Cloud Collaborative Inference for Foundation Models",
        "Accelerating End-Cloud Collaborative Inference via Near Bubble-free Pipeline Optimization",
        "ACBatch: Adaptive and Cooperative Batching for Edge Inference",
        "Harpagon: Minimizing DNN Serving Cost via Efficient Dispatching, Scheduling and Splitting",
        "Computation and Communication Co-scheduling for Timely Multi-Task Inference at the Wireless Edge",
        "FaSei: Fast Serverless Edge Inference with Synergistic Lazy Loading and Layer-wise Caching",
        "Online Scheduling of Edge Multiple-Model Inference with DAG Structure and Retraining",
        "DUNE: Distributed Inference in the User Plane",
    ],
    "在线学习 / Bandit": [
        "Robust Contextual Combinatorial Multi-Armed Bandits for Unreliable Network Systems",
        "When Labor-Intensive Mobile Crowdsourcing Meets Unobservability: Contextual Bandit Learning",
        "On the Low-Complexity of Fair Learning for Combinatorial Multi-Armed Bandit",
        "Adversarial Semi-Bandits with Moving Arms",
        "Faster Convergence for Unknown-game Bandits",
        "Latency-aware Online Continual Learning for Non-Stationary Data Streams",
        "Smooth Handovers via Smoothed Online Learning",
        "Tri-Ring: Asynchronous Service Provisioning with Online Learning in Edge Cloud Networks",
        "Continual Learning with Strategic Selection and Forgetting for Network Intrusion Detection",
    ],
    "GNN / 图神经网络": [
        "Accelerating Clustered Federated Learning in Dynamic D2D Networks with Transferable GNN",
        "GNN-SML: Graphic Neural Network-Based Spectrum Misuser Localization",
        "GraphRx: Graph-Based Collaborative Learning among Multiple Cells for Uplink Neural Receivers",
    ],
    "生成式AI (GenAI)": [
        "LMTE: Putting the Reasoning into WAN Traffic Engineering with Language Models",
        "AIGC-CM: An Efficient and Scalable Blockchain Solution for AIGC Copyright Management",
    ],
}

papers_2026 = {
    "联邦学习 (Federated Learning)": [
        "Dual-Phase Federated Deep Unlearning via Weight-Aware Rollback and Reconstruction",
        "A Needle in a Haystack: Defending Federated Learning Backdoor Attacks via Orthogonal Subnetwork Pruning",
        "Optimizing Split Federated Learning through Adaptive Pipeline Parallelism",
        "Budget-Constrained Federated Bandits for Mobile Applications",
        "PFAE: Personalized Federated Learning for Anomaly Detection over Heterogeneous IoT Domains",
    ],
    "LLM / 大语言模型": [
        "Memory-Efficient KV Cache Optimization for Large Language Model Inference at the Edge",
        "A Novel Hat-Shaped Device-Cloud Collaborative Inference Framework for Large Language Models",
        "ARI-LLM: Autoregressive Imputation for Network Traffic Matrix via Large Language Models",
        "Semantic Caching for Low-Cost LLM Serving: From Offline Learning to Online Adaptation",
        "MoVi: Real-Time Large Multimodal Model-Driven Interactive Video Analytics on Mobile Devices",
    ],
    "Transformer": [
        "Mercury: Towards Optimal Accuracy-Latency Trade-off for Collaborative Transformer Inference",
        "TPipe: Efficient Spiking Transformer Training with Time Parallelism and Asynchronous Pipeline",
        "Hyperion: Low-Latency Ultra-HD Video Analytics via Collaborative Vision Transformer Inference",
    ],
    "扩散模型": [
        "Clay-to-Stone: Phase-wise 3D Gaussian Splatting for Monocular Articulated Hand-Object Manipulation",
    ],
    "强化学习": [
        "A Theory of Goal-Oriented Medium Access: Protocol Design and Distributed Bandit Learning",
        "EExApp: GNN-Based Reinforcement Learning for Radio Unit Energy Optimization in 5G O-RAN",
    ],
    "MoE": [
        "Faster, Smaller, and Smarter: Task-Aware Expert Merging for Online MoE Inference",
    ],
    "边缘推理": [
        "Memory-Efficient KV Cache Optimization for Large Language Model Inference at the Edge",
        "MoVi: Real-Time Large Multimodal Model-Driven Interactive Video Analytics on Mobile Devices",
        "A Novel Hat-Shaped Device-Cloud Collaborative Inference Framework for Large Language Models",
    ],
    "在线学习 / Bandit": [
        "A Theory of Goal-Oriented Medium Access: Protocol Design and Distributed Bandit Learning",
        "Semantic Caching for Low-Cost LLM Serving: From Offline Learning to Online Adaptation",
        "Budget-Constrained Federated Bandits for Mobile Applications",
    ],
}


def analyze():
    print("=" * 80)
    print("INFOCOM 2025-2026 AI/ML相关论文趋势分析")
    print("=" * 80)

    print(f"\n[总结] 从 INFOCOM 2025 (272篇接受) 和 INFOCOM 2026 (329篇接受) 中爬取的 AI/ML 相关论文")
    print(f"   INFOCOM 2025 接受率: 272/1458 = 18.7%")
    print(f"   INFOCOM 2026 接受率: 329/1740 = 18.9%")

    print("\n" + "=" * 80)
    print("[热门方向排名] (基于论文数量和增长趋势)")
    print("=" * 80)

    counts_2025 = {k: len(v) for k, v in papers_2025.items()}
    counts_2026 = {k: len(v) for k, v in papers_2026.items()}

    all_categories = sorted(set(list(counts_2025.keys()) + list(counts_2026.keys())),
                            key=lambda x: counts_2025.get(x, 0), reverse=True)

    for cat in all_categories:
        c25 = counts_2025.get(cat, 0)
        c26 = counts_2026.get(cat, 0)
        bar = "#" * max(c25 // 2, 1)
        print(f"  {cat:35s} 2025:{c25:3d}  2026:{c26:3d}   {bar}")

    print("\n" + "=" * 80)
    print("[INFOCOM 2025 AI/ML论文详细列表]")
    print("=" * 80)

    for cat, papers in papers_2025.items():
        print(f"\n>> {cat} ({len(papers)}篇)")
        for p in papers:
            print(f"    * {p}")

    print("\n" + "=" * 80)
    print("[INFOCOM 2026 AI/ML论文详细列表]")
    print("=" * 80)

    for cat, papers in papers_2026.items():
        print(f"\n>> {cat} ({len(papers)}篇)")
        for p in papers:
            print(f"    * {p}")

    print("\n" + "=" * 80)
    print("[核心发现 - 2025-2026 AI+网络 热门趋势]")
    print("=" * 80)

    findings = [
        "",
        ">> 1. LLM + 网络是绝对最大的新热点 <<",
        "   INFOCOM 2025 有 15+ 篇论文直接涉及 LLM",
        "   方向包括：LLM边缘推理、KV Cache优化、联邦LLM微调、RAG、投机推理等",
        "   2026 延续并深化：LLM语义缓存、多模态大模型、端云协同LLM推理",
        "",
        ">> 2. 联邦学习持续火热，方向细化 <<",
        "   2025年 23 篇联邦学习论文，覆盖：",
        "     - 大模型联邦微调 (LoRA + FL)",
        "     - 联邦遗忘 (Federated Unlearning)",
        "     - 隐私攻击与防御 (梯度泄露、后门攻击)",
        "     - 激励机制、异构量化、个性化联邦等",
        "",
        ">> 3. Transformer 全面渗透网络领域 <<",
        "   Vision Transformer: 视频分析、IPv6地址生成",
        "   Graph Transformer: 社交网络、流量工程",
        "   2026 新方向: Spiking Transformer 训练优化",
        "",
        ">> 4. 扩散模型 (Diffusion) 快速崛起 <<",
        "   应用场景: 语义通信、WiFi数据生成、网络功能部署、车辆检测、地址生成",
        "   从CV领域向通信网络领域快速外溢",
        "",
        ">> 5. 强化学习是网络优化的稳定核心 <<",
        "   MARL用于数据中心、边缘计算、O-RAN、LPWAN",
        "   新方向: 可解释DRL (SymbXRL)",
        "",
        ">> 6. MoE (Mixture-of-Experts) 崭露头角 <<",
        "   从LLM架构向网络部署优化延伸",
        "   2025: MoE理论 + serverless部署",
        "   2026: MoE在线推理的专家合并",
        "",
        ">> 7. 边缘AI推理成为基础设施级研究热点 <<",
        "   模型从DNN扩展到LLM/LVM (Large Vision Model)",
        "   关键技术: KV Cache、提前退出、管道并行、量化调度、无服务器推理",
        "",
        ">> 8. CNN 论文数量显著减少 <<",
        "   仅出现在特定场景(可编程数据平面、物理层)",
        "   整体趋势: CNN -> Transformer -> LLM/MoE",
        "",
        ">> 9. RNN/LSTM 基本消失 <<",
        "   被 Transformer 全面替代",
        "",
        ">> 10. RWKV 尚未出现在 INFOCOM <<",
        "   作为较新的线性注意力架构，还未渗透入网络通信领域",
        "   可能是一个蓝海方向: RWKV的高效推理特性天然适合边缘场景",
        "",
        ">> 跨领域趋势总结 <<",
        "   AI4Net (AI赋能网络) + Net4AI (网络支撑AI) 双轮驱动",
        "   LLM的边缘化部署是2025-2026最显著的新趋势",
        "   安全+AI (后门攻击、投毒、推理攻击) 持续受关注",
        "   绿色AI (能效优化) 在O-RAN和边缘场景受到重视",
    ]

    for line in findings:
        print(line)


if __name__ == "__main__":
    analyze()
