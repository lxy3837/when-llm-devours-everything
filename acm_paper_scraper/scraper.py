#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ACM Digital Library (via ton.acm.org) 论文爬虫
爬取深度学习、机器学习、强化学习、联邦学习、CNN、RNN、Transformer、LSTM、RWKV 相关论文标题
"""

import requests
import time
import re
import json
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlencode, quote

# ============ 配置 ============
BASE_URL = "https://ton.acm.org"
SEARCH_URL = f"{BASE_URL}/action/doSearch"
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_FILE = os.path.join(OUTPUT_DIR, "papers.json")
SUMMARY_FILE = os.path.join(OUTPUT_DIR, "summary.txt")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}

KEYWORDS = [
    "deep learning",
    "machine learning",
    "reinforcement learning",
    "federated learning",
    "CNN convolutional neural network",
    "RNN recurrent neural network",
    "transformer attention mechanism",
    "LSTM long short-term memory",
    "RWKV",
]

MAX_PAGES_PER_KEYWORD = 3  # 每个关键词最多爬3页（每页约50条）
PAGE_SIZE = 50
REQUEST_DELAY = 2  # 请求间隔秒数


def search_papers(keyword, max_pages=MAX_PAGES_PER_KEYWORD):
    """搜索指定关键词的论文"""
    all_papers = []
    session = requests.Session()
    session.headers.update(HEADERS)

    for page in range(max_pages):
        params = {
            "AllField": keyword,
            "pageSize": PAGE_SIZE,
            "startPage": page,
        }
        try:
            print(f"  正在搜索 '{keyword}' 第 {page + 1} 页...")
            resp = session.get(SEARCH_URL, params=params, timeout=30)
            resp.raise_for_status()

            soup = BeautifulSoup(resp.text, "html.parser")

            # ACM DL 论文标题通常在 h5 或 class 含 title 的元素中
            titles = []
            # 方式1: 查找 .issue-item__title 或类似class
            for el in soup.select(".issue-item__title a, .item-title a, h5.title a, .hlFld-Title a"):
                title = el.get_text(strip=True)
                link = urljoin(BASE_URL, el.get("href", ""))
                if title and len(title) > 5:
                    titles.append({"title": title, "link": link, "keyword": keyword})

            # 方式2: 从 search-result 相关元素中提取
            if not titles:
                for el in soup.select("[class*=result] a[href*='/doi/'], .search-result-item a, li a[href*='/doi/']"):
                    title = el.get_text(strip=True)
                    link = urljoin(BASE_URL, el.get("href", ""))
                    if title and len(title) > 5 and title not in [t["title"] for t in titles]:
                        titles.append({"title": title, "link": link, "keyword": keyword})

            # 方式3: 通用 - 找所有包含 /doi/ 的链接，取其文本
            if not titles:
                for el in soup.find_all("a", href=re.compile(r"/doi/")):
                    title = el.get_text(strip=True)
                    if title and len(title) > 10 and not re.match(r'^\d', title):
                        titles.append({"title": title, "link": urljoin(BASE_URL, el["href"]), "keyword": keyword})

            # 去重
            seen = set()
            unique = []
            for t in titles:
                if t["title"] not in seen:
                    seen.add(t["title"])
                    unique.append(t)
            titles = unique

            print(f"    找到 {len(titles)} 篇论文")
            all_papers.extend(titles)

            if len(titles) < PAGE_SIZE // 2:
                # 结果少于一页的一半，说明后面没有了
                break

            time.sleep(REQUEST_DELAY)

        except requests.exceptions.Timeout:
            print(f"    第 {page + 1} 页超时，跳过")
            break
        except requests.exceptions.RequestException as e:
            print(f"    第 {page + 1} 页请求失败: {e}")
            break

    return all_papers


def main():
    print("=" * 60)
    print("ACM Digital Library 论文爬虫 (via ton.acm.org)")
    print("=" * 60)

    all_results = {}

    for kw in KEYWORDS:
        print(f"\n[关键词] {kw}")
        papers = search_papers(kw)
        all_results[kw] = papers
        total = sum(len(v) for v in all_results.values())
        print(f"  该关键词累计: {len(papers)} 篇, 总计: {total} 篇")
        time.sleep(REQUEST_DELAY)

    # 保存结果
    with open(RESULTS_FILE, "w", encoding="utf-8") as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)

    # 生成汇总
    all_papers = []
    for kw, papers in all_results.items():
        all_papers.extend(papers)

    # 去重（按标题）
    seen_titles = set()
    unique_papers = []
    for p in all_papers:
        if p["title"].lower() not in seen_titles:
            seen_titles.add(p["title"].lower())
            unique_papers.append(p)

    print(f"\n{'=' * 60}")
    print(f"爬取完成！")
    print(f"  总爬取数（含重复）: {len(all_papers)} 篇")
    print(f"  去重后: {len(unique_papers)} 篇")
    print(f"  结果保存在: {RESULTS_FILE}")
    print(f"{'=' * 60}")

    return all_results


if __name__ == "__main__":
    main()
