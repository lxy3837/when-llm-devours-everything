# NDSS 近三年 AI/ML 相关论文爬取汇总 & 热门方向分析

> 数据来源: https://www.ndss-symposium.org/ (NDSS 2023-2025)
> 爬取时间: 2026-07-16
> 爬取方法: 通过网站搜索功能，搜索关键词包括 deep learning, machine learning, reinforcement learning, federated learning, CNN, RNN, transformer, LSTM, RWKV, LLM, GPT, adversarial attack, backdoor, diffusion model, generative AI, watermark, privacy 等

---

## 一、爬取到的 AI/ML 相关论文列表（按方向分类）

### 1. 大语言模型 (LLM) & Transformer 安全

| 年份 | 论文标题 |
|------|----------|
| 2025 | **MASTERKEY: Automated Jailbreaking of Large Language Model Chatbots** |
| 2025 | **BumbleBee: Secure Two-party Inference Framework for Large Transformers** |
| 2025 | **CLIBE: Detecting Dynamic Backdoors in Transformer-based NLP Models** |
| 2025 | **Beyond Classification: Inferring Function Names in Stripped Binaries via Domain Adapted LLMs** |
| 2024 | **Improving the Robustness of Transformer-based Large Language Models with Dynamic Attention** |
| 2024 | **DeGPT: Optimizing Decompiler Output with LLM** |
| 2024 | **Large Language Model guided Protocol Fuzzing** |
| 2024 | **DEMASQ: Unmasking the ChatGPT Wordsmith** |
| 2022 | **Interpretable Federated Transformer Log Learning for Cloud Threat Forensics** |

### 2. 联邦学习 (Federated Learning) 安全

| 年份 | 论文标题 |
|------|----------|
| 2025 | **CENSOR: Defense Against Gradient Inversion via Orthogonal Subspace Bayesian Sampling** |
| 2024 | **Automatic Adversarial Adaption for Stealthy Poisoning Attacks in Federated Learning** |
| 2024 | **CrowdGuard: Federated Backdoor Detection in Federated Learning** |
| 2024 | **FreqFed: A Frequency Analysis-Based Approach for Mitigating Poisoning Attacks in Federated Learning** |
| 2024 | **Pencil: Private and Extensible Collaborative Learning without the Non-Colluding Assumption** |
| 2024 | **FP-Fed: Privacy-Preserving Federated Detection of Browser Fingerprinting** |
| 2023 | **PPA: Preference Profiling Attack Against Federated Learning** |
| 2023 | **Securing Federated Sensitive Topic Classification against Poisoning Attacks** |
| 2022 | **DeepSight: Mitigating Backdoor Attacks in Federated Learning Through Deep Model Inspection** |
| 2022 | **Local and Central Differential Privacy for Robustness and Privacy in Federated Learning** |
| 2022 | **FedCRI: Federated Mobile Cyber-Risk Intelligence** |

### 3. 对抗攻击 & 后门攻击 (Adversarial & Backdoor Attacks)

| 年份 | 论文标题 |
|------|----------|
| 2025 | **BARBIE: Robust Backdoor Detection Based on Latent Separability** |
| 2025 | **CLIBE: Detecting Dynamic Backdoors in Transformer-based NLP Models** |
| 2025 | **AlphaDog: No-Box Camouflage Attacks via Alpha Channel Oversight** |
| 2025 | **Automated Mass Malware Factory: Adversarial Example in Android Malware Generation** |
| 2024 | **DorPatch: Distributed and Occlusion-Robust Adversarial Patch to Evade Certifiable Defenses** |
| 2024 | **Enhance Stealthiness and Transferability of Adversarial Attacks with Class Activation Mapping** |
| 2024 | **Parrot-Trained Adversarial Examples: Black-Box Audio Attacks against Speaker Recognition** |
| 2023 | **RoVISQ: Reduction of Video Service Quality via Adversarial Attacks on Deep Learning-based Video Compression** |
| 2023 | **Backdoor Attacks Against Dataset Distillation** |
| 2023 | **BEAGLE: Forensics of Deep Learning Backdoor Attack for Better Defense** |
| 2022 | **RamBoAttack: A Robust and Query Efficient Deep Neural Network Decision Exploit** |

### 4. 深度神经网络 (DNN) 安全性 & 硬件安全

| 年份 | 论文标题 |
|------|----------|
| 2025 | **ASGARD: Protecting On-Device Deep Neural Networks with Virtualization-Based TEE** |
| 2025 | **BitShield: Defending Against Bit-Flip Attacks on DNN Executables** |
| 2025 | **Compiled Models, Built-In Exploits: Uncovering Pervasive Bit-Flip Attack Surfaces in DNN Executables** |
| 2024 | **ActiveDaemon: Unconscious DNN Dormancy and Waking Up via User-specific Invisible Token** |

### 5. AI 隐私 & 模型逆向攻击

| 年份 | 论文标题 |
|------|----------|
| 2025 | **A Key-Driven Framework for Identity-Preserving Face Anonymization** |
| 2025 | **CENSOR: Defense Against Gradient Inversion via Orthogonal Subspace Bayesian Sampling** |
| 2024 | **Crafter: Facial Feature Crafting against Inversion-based Identity Theft on Deep Models** |
| 2023 | **MIRROR: Model Inversion for Deep Learning Network with High Fidelity** |
| 2024 | **You Can Use But Cannot Recognize: Preserving Visual Privacy in Deep Neural Networks** |

### 6. 深度伪造 & 音视频安全

| 年份 | 论文标题 |
|------|----------|
| 2025 | **Characterizing the Impact of Audio Deepfakes in the Presence of Cochlear Implant** |
| 2024 | **Detecting Voice Cloning Attacks via Timbre Watermarking** |
| 2024 | **Compensating Removed Frequency Components: Thwarting Voice Spectrum Reduction Attacks** |
| 2024 | **CamPro: Camera-based Anti-Facial Recognition** |
| 2023 | **Attacks as Defenses: Designing Robust Audio CAPTCHAs Using Attacks on ASR Systems** |

### 7. 机器遗忘 (Machine Unlearning)

| 年份 | 论文标题 |
|------|----------|
| 2024 | **A Duty to Forget, a Right to be Assured? Exposing Vulnerabilities in Machine Unlearning Services** |
| 2023 | **Machine Unlearning of Features and Labels** |

### 8. AI 模型水印 & 知识产权保护

| 年份 | 论文标题 |
|------|----------|
| 2024 | **SSL-WM: A Black-Box Watermarking Approach for Encoders Pre-trained by Self-Supervised Learning** |

### 9. AI 辅助安全工具 (AI for Security)

| 年份 | 论文标题 |
|------|----------|
| 2025 | **BinEnhance: Enhancement Framework Based on External Environment Semantics for Binary Code Search** |
| 2024 | **SigmaDiff: Semantics-Aware Deep Graph Matching for Pseudocode Diffing** |
| 2024 | **DeepGo: Predictive Directed Greybox Fuzzing** |
| 2023 | **Smarter Contracts: Detecting Vulnerabilities in Smart Contracts with Deep Transfer Learning** |
| 2023 | **BARS: Local Robustness Certification for Deep Learning based Traffic Analysis Systems** |
| 2023 | **DOITRUST: Dissecting On-chain Compromised Internet Domains via Graph Learning** |
| 2023 | **Detecting Unknown Encrypted Malicious Traffic via Flow Interaction Graph Analysis** |
| 2023 | **HeteroScore: Evaluating and Mitigating Cloud Security Threats Brought by Heterogeneity** |
| 2024 | **Attributions for ML-based ICS Anomaly Detection: From Theory to Practice** |
| 2024 | **Improving In-vehicle Networks Intrusion Detection Using On-Device Transfer Learning** |

### 10. 安全多方计算 + ML (PPML)

| 年份 | 论文标题 |
|------|----------|
| 2025 | **A New PPML Paradigm for Quantized Models** |
| 2025 | **BumbleBee: Secure Two-party Inference Framework for Large Transformers** |
| 2024 | **MPCDiff: Testing and Repairing MPC-Hardened Deep Learning Models** |
| 2023 | **Fusion: Efficient and Secure Inference Resilient to Malicious Servers** |

### 11. 强化学习安全

| 年份 | 论文标题 |
|------|----------|
| 2024 | **ORL-AUDITOR: Dataset Auditing in Offline Deep Reinforcement Learning** |

### 12. 模型劫持 & 投毒攻击

| 年份 | 论文标题 |
|------|----------|
| 2025 | **Automated Mass Malware Factory: Piggybacking + Adversarial Example in Android** |
| 2022 | **Get a Model! Model Hijacking Attack Against Machine Learning Models** |
| 2023 | **Backdoor Attacks Against Dataset Distillation** |

---

## 二、关于 CNN / RNN / LSTM / RWKV 的特别说明

需要指出的是，在近年的 NDSS 上，**CNN/RNN/LSTM 作为独立的论文主题已经很少出现**（约 2020 年前后有涉及）。原因是：
- 这些"经典"神经网络架构在安全领域的研究已经相对成熟
- 学术界的研究重心已经大规模转向 **Transformer 架构**和**大语言模型 (LLM)**
- **RWKV**（一种结合 RNN 和 Transformer 优点的模型架构）在 NDSS 上目前**尚未发现相关论文**，因为 RWKV 在安全领域的研究才刚刚起步

不过，CNN 仍然出现在一些应用场景中，比如作为**对抗攻击的受害者模型**（如图像分类器）或用于**侧信道分析**。

---

## 三、近三年最热门的研究方向总结

### 热度排行（从高到低）：

### 第1名：联邦学习安全 (Federated Learning Security)
这是近三年 NDSS 上最持续火热的方向。每年都有多篇论文涉及，且涵盖面广：
- **投毒攻击与防御**（最热门子方向）：FreqFed, CrowdGuard, DeepSight, Securing Federated...
- **梯度泄露/逆向攻击**：CENSOR, Automatic Adversarial Adaption
- **差分隐私与联邦学习结合**：Local and Central Differential Privacy
- **联邦学习在安全应用中的落地**：FP-Fed (浏览器指纹), FedCRI (移动端)

### 第2名：LLM/大模型安全 (LLM Security)
这是2024-2025年**爆发式增长**的方向，从几乎为零猛增到每年多篇：
- **越狱攻击 (Jailbreaking)**：MASTERKEY
- **后门检测**：CLIBE
- **LLM 辅助安全任务**：LLM guided Protocol Fuzzing, DeGPT（反编译优化）, Beyond Classification（二进制分析）
- **AI 生成文本检测**：DEMASQ（检测 ChatGPT 生成文本）
- **Transformer 鲁棒性**：Improving Robustness with Dynamic Attention

### 第3名：对抗攻击与防御 (Adversarial Attack & Defense)
持续多年的大热方向，每年都有稳定产出：
- **物理世界对抗攻击**：DorPatch, AlphaDog（Alpha通道攻击）
- **黑盒音频对抗攻击**：Parrot-Trained Adversarial Examples
- **对抗补丁逃逸**：DorPatch
- **盗版检测/后门取证**：BARBIE, BEAGLE
- **对抗样本生成自动化**：Automated Mass Malware Factory

### 第4名：深度伪造与多模态安全 (Deepfake & Multimodal Security)
2024-2025年快速上升的新方向：
- **语音克隆检测**：Timbre Watermarking
- **音频深度伪造**：Characterizing Impact of Audio Deepfakes
- **人脸识别对抗**：CamPro, UniID, Crafter
- **声学侧信道**：多个声学攻击论文

### 第5名：隐私保护机器学习 (PPML)
经典但持续有进展的方向：
- **安全多方计算+推理**：BumbleBee, Fusion, MPCDiff
- **机器遗忘 (Machine Unlearning)**：被 GDPR 等法规驱动
- **模型逆向攻击防御**：CENSOR, MIRROR
- **水印保护**：SSL-WM

### 第6名：AI for Security（用AI做安全）
持续发展，应用场景不断拓宽：
- **模糊测试智能化**：DeepGo, LLM guided Protocol Fuzzing
- **二进制/代码分析**：BinEnhance, SigmaDiff, DeGPT
- **威胁检测**：图神经网络用于恶意域名检测、加密流量检测

---

## 四、2025 年 vs 2024 年的趋势变化

| 趋势 | 变化 |
|------|------|
| **LLM 安全** | 爆炸式增长，从 few-shot 学习检测、ChatGPT文本检测扩展到越狱、后门、安全辅助 |
| **联邦学习** | 热度持续但略有饱和趋势，研究从"攻击"转向"实用防御" |
| **DNN 硬件层安全** | 新热点，BitShield/Compiled Models 聚焦DNN编译后的比特翻转攻击面 |
| **对抗攻击** | 从数字域转向物理域（摄像头、音频设备），更贴近真实攻击场景 |
| **机器遗忘** | 从2023年开始出现，受隐私法规驱动，有望持续增长 |
| **CNN/RNN/LSTM** | 不再作为论文主题出现，已被 Transformer/LLM 取代 |

---

## 五、核心结论

1. **LLM/大模型安全是当前最火的方向**，2024-2025两年间论文数量激增，涵盖越狱防御、后门检测、LLM辅助安全工具等多个子方向。这是最值得关注的研究前沿。

2. **联邦学习安全热度不减但逐渐成熟**，从早期的"能攻击吗"转变为"如何实用化防御"。

3. **AI安全正在从数字域走向物理域**，音频、摄像头、VR设备等物理世界攻击面成为新热点。

4. **经典架构(CNN/RNN/LSTM)在安全顶会已退潮**，建议将研究重心放在 Transformer 和 LLM 的安全问题上。

5. **RWKV 等新型架构在安全领域几乎空白**，存在潜在的研究机会（但风险是：安全社区对新架构的关注度取决于该架构在工业界的普及度）。

6. **"AI for Security"前景广阔**，LLM + 安全工具（fuzzing、逆向、代码审计）的结合正在催生新一代安全分析工具。
