#!/usr/bin/env python3
"""Generate 4 data visualization charts for the AI Research Landscape report."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import os

# ===== 全局样式 =====
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 150
plt.rcParams['savefig.dpi'] = 150
plt.rcParams['savefig.bbox'] = 'tight'
plt.rcParams['savefig.pad_inches'] = 0.2

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ===== 配色方案 =====
C_LLM     = '#E74C3C'  # 红 - LLM
C_SEC     = '#8E44AD'  # 紫 - 安全
C_SYS     = '#2980B9'  # 蓝 - 系统
C_NET     = '#27AE60'  # 绿 - 网络
C_ML      = '#F39C12'  # 橙 - ML/AI
C_CNN     = '#95A5A6'  # 灰 - CNN/RNN
C_SSM     = '#1ABC9C'  # 青 - SSM
C_DIFF    = '#E67E22'  # 棕 - Diffusion
C_TRANS   = '#2C3E50'  # 深蓝 - Transformer
C_FL      = '#16A085'  # 墨绿 - FL
C_AGENT   = '#D35400'  # 暗橙 - Agent

# ============================================================
# 图1: 各顶会/期刊 AI/ML 论文数量 & 接受率
# ============================================================
def chart1_venue_overview():
    venues = ['ICML\n2026', 'S&P\n2023-25', 'USENIX\n2023-26', 'SIGCOMM\n2023-25',
              'INFOCOM\n2025-26', 'NDSS\n2023-25', 'TDSC\n2025-26', 'NSDI\n2026']
    ai_papers = [6352, 51, 38, 19, 106, 55, 46, 45]
    total_accept = [6352, None, None, 136, 601, None, None, 150]
    accept_rate = [26.6, None, None, 16.1, 18.8, None, None, 23.1]

    fig, ax1 = plt.subplots(figsize=(10, 5.5))

    x = np.arange(len(venues))
    width = 0.55
    colors = [C_ML, C_SEC, C_SYS, C_NET, C_NET, C_SEC, C_SEC, C_SYS]

    bars = ax1.bar(x, ai_papers, width, color=colors, edgecolor='white', linewidth=0.5, alpha=0.9)
    for bar, val in zip(bars, ai_papers):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 30,
                 str(val), ha='center', va='bottom', fontsize=8, fontweight='bold', color='#333')

    ax1.set_ylabel('AI/ML 相关论文数量', fontsize=11, color='#555')
    ax1.set_xticks(x)
    ax1.set_xticklabels(venues, fontsize=9)
    ax1.set_ylim(0, max(ai_papers) * 1.25)

    # 右侧Y轴: 接受率
    ax2 = ax1.twinx()
    valid_idx = [i for i, r in enumerate(accept_rate) if r is not None]
    ax2.scatter([x[i] for i in valid_idx], [accept_rate[i] for i in valid_idx],
                color=C_LLM, s=100, zorder=5, marker='D', edgecolors='white', linewidth=0.5)
    for i in valid_idx:
        ax2.annotate(f'{accept_rate[i]}%', (x[i], accept_rate[i]),
                     textcoords="offset points", xytext=(0, 12), ha='center',
                     fontsize=9, fontweight='bold', color=C_LLM)
    ax2.set_ylabel('接受率 (%)', fontsize=11, color=C_LLM)
    ax2.set_ylim(10, 32)
    ax2.tick_params(axis='y', colors=C_LLM)

    # 标注
    ax1.text(0.02, 0.97, '[!] ICML 6352篇远超其他, 单独用柱高表示',
             transform=ax1.transAxes, fontsize=7.5, color='#999', va='top')

    ax1.grid(axis='y', alpha=0.3, linestyle='--')
    ax1.set_axisbelow(True)
    ax1.spines['top'].set_visible(False)
    ax2.spines['top'].set_visible(False)

    plt.title('各顶级会议/期刊 AI/ML 论文数量与接受率\n'
              '（ICML 为 AI 原生会议，其余为安全/系统/网络会议）',
              fontsize=13, fontweight='bold', pad=15)

    path = os.path.join(OUTPUT_DIR, 'chart1_venue_overview.png')
    plt.savefig(path)
    plt.close()
    print(f'[OK] {path}')


# ============================================================
# 图2: 跨领域"温差"热力图
# ============================================================
def chart2_temperature_heatmap():
    topics = ['联邦学习\n安全', 'LLM推理\n系统', 'LLM安全\n/越狱', '扩散模型',
              'Mamba\n/SSM', 'KV Cache\n优化', 'Agent\n系统']
    venues = ['ML/AI\n会议', '安全\n会议', '系统\n会议', '网络\n会议']

    # 热度矩阵 (0-5, 0=无)
    data = np.array([
        [3, 5, 1, 4],  # FL安全
        [2, 0, 5, 5],  # LLM推理
        [3, 5, 0, 0],  # LLM安全
        [5, 1, 0, 2],  # 扩散
        [4, 0, 2, 0],  # Mamba
        [2, 0, 5, 4],  # KV Cache
        [4, 0, 5, 0],  # Agent
    ])

    fig, ax = plt.subplots(figsize=(8, 6))
    im = ax.imshow(data, cmap='YlOrRd', aspect='auto', vmin=0, vmax=5)

    ax.set_xticks(range(len(venues)))
    ax.set_yticks(range(len(topics)))
    ax.set_xticklabels(venues, fontsize=10)
    ax.set_yticklabels(topics, fontsize=9)

    # 数值标注
    for i in range(len(topics)):
        for j in range(len(venues)):
            val = data[i, j]
            color = 'white' if val >= 3 else '#333'
            text = '—' if val == 0 else '◆' * val
            ax.text(j, i, text, ha='center', va='center', fontsize=9, color=color,
                    fontweight='bold' if val >= 3 else 'normal')

    # 颜色条
    cbar = plt.colorbar(im, ax=ax, shrink=0.85, pad=0.02)
    cbar.set_label('热度等级', fontsize=10)
    cbar.set_ticks([0, 1, 2, 3, 4, 5])

    ax.set_title('同一研究方向在不同顶会社区的"温差"', fontsize=13, fontweight='bold', pad=15)

    # 标注
    ax.text(3.7, 6.3, '◆ = 热度等级\n— = 无该方向论文', fontsize=7, color='#999', va='top',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f9f9f9', edgecolor='#ddd', alpha=0.8))

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, 'chart2_temperature_heatmap.png')
    plt.savefig(path)
    plt.close()
    print(f'[OK] {path}')


# ============================================================
# 图3: LLM 论文在非AI会议中的爆发式增长
# ============================================================
def chart3_llm_growth():
    years = ['2022', '2023', '2024', '2025', '2026']
    venues_label = ['IEEE S&P', 'USENIX\n(Security)', 'SIGCOMM', 'NDSS', 'INFOCOM', 'NSDI']

    # 估算的 LLM 相关论文数 (基于 summary 文件的描述)
    # S&P: 2023前=0, 2023=0, 2024=6, 2025=15
    # USENIX Security: 2023=2, 2024=5, 2025=4
    # SIGCOMM: 2023=0, 2024=4, 2025=6
    # NDSS: 2022=2, 2023=1, 2024=4, 2025=5
    # INFOCOM: 2025=11, 2026=5
    # NSDI: 2026=20

    sp   = [0, 0, 0, 6, 15]
    usnx = [0, 0, 2, 5, 4]
    sigc = [0, 0, 0, 4, 6]
    ndss = [0, 2, 1, 4, 5]
    info = [0, 0, 0, 11, 5]
    nsdi = [0, 0, 0, 0, 20]

    all_data = [sp, usnx, sigc, ndss, info, nsdi]
    colors = [C_SEC, C_SEC, C_NET, C_SEC, C_NET, C_SYS]

    fig, ax = plt.subplots(figsize=(10, 5.5))

    x = np.arange(len(years))
    width = 0.12
    for i, (data, label, c) in enumerate(zip(all_data, venues_label, colors)):
        offset = (i - 2.5) * width
        bars = ax.bar(x + offset, data, width, label=label.replace('\n', ' '), color=c,
                      alpha=0.85, edgecolor='white', linewidth=0.3)
        # 标记非零值
        for j, val in enumerate(data):
            if val > 0:
                ax.text(x[j] + offset, val + 0.3, str(val), ha='center', va='bottom',
                        fontsize=6.5, fontweight='bold', color=c)

    ax.set_xticks(x)
    ax.set_xticklabels(years, fontsize=11)
    ax.set_ylabel('LLM 相关论文数量', fontsize=11)
    ax.legend(loc='upper left', fontsize=8, ncol=2, framealpha=0.9)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # 标注 ChatGPT 发布时间
    ax.axvline(x=1.5, color=C_LLM, linestyle='--', linewidth=1.2, alpha=0.6)
    ax.text(1.5, ax.get_ylim()[1] * 0.95, '← ChatGPT\n  (2022.11)', fontsize=8,
            color=C_LLM, ha='right', fontstyle='italic')

    plt.title('LLM 论文在非 AI 顶会中的爆发式增长 (2022–2026)', fontsize=13, fontweight='bold', pad=15)

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, 'chart3_llm_growth.png')
    plt.savefig(path)
    plt.close()
    print(f'[OK] {path}')


# ============================================================
# 图4: 热门研究方向跨会议分布 (雷达图风格的分组柱状)
# ============================================================
def chart4_topic_distribution():
    topics = ['联邦学习', 'LLM推理/部署', 'LLM安全\n/越狱', '后门攻击', '扩散模型\n/生成式',
              'Agent/\n多模态', 'KV Cache', '差分隐私', 'RL\n后训练']
    venues = ['ICML\n(ML/AI)', 'IEEE S&P\n(安全)', 'SIGCOMM\n(网络)', 'NDSS\n(安全)',
              'TDSC\n(安全)', 'INFOCOM\n(网络)', 'NSDI\n(系统)']

    # 每个会议中每个方向的相对热度 (0-10)
    data = np.array([
        # FL, LLM推理, LLM安全, 后门, 扩散, Agent, KVCache, DP, RL
        [6, 3, 3, 0, 8, 5, 0, 0, 10],  # ICML
        [5, 0, 8, 6, 2, 0, 0, 7, 1],   # S&P
        [1, 8, 0, 0, 2, 0, 7, 0, 0],   # SIGCOMM
        [8, 0, 7, 8, 3, 2, 0, 3, 1],   # NDSS
        [10, 0, 2, 9, 3, 1, 0, 4, 0],  # TDSC
        [9, 7, 0, 0, 3, 0, 2, 0, 2],   # INFOCOM
        [0, 10, 0, 0, 1, 6, 8, 0, 2],  # NSDI
    ])

    fig, ax = plt.subplots(figsize=(13, 6))

    x = np.arange(len(topics))
    width = 0.11
    colors = [C_ML, C_SEC, C_NET, C_SEC, C_SEC, C_NET, C_SYS]

    for i, (row, label, c) in enumerate(zip(data, venues, colors)):
        offset = (i - 3) * width
        bars = ax.bar(x + offset, row, width, label=label.replace('\n', ' '), color=c,
                      alpha=0.85, edgecolor='white', linewidth=0.3)

    ax.set_xticks(x)
    ax.set_xticklabels(topics, fontsize=9)
    ax.set_ylabel('相对热度 (0–10)', fontsize=11)
    ax.legend(loc='upper right', fontsize=7.5, ncol=2, framealpha=0.9)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_ylim(0, 11)

    plt.title('热门研究方向的跨会议分布 (相对热度 0–10)', fontsize=13, fontweight='bold', pad=15)

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, 'chart4_topic_distribution.png')
    plt.savefig(path)
    plt.close()
    print(f'[OK] {path}')


# ============================================================
if __name__ == '__main__':
    print('Generating charts...')
    chart1_venue_overview()
    chart2_temperature_heatmap()
    chart3_llm_growth()
    chart4_topic_distribution()
    print('All 4 charts generated.')
