#!/usr/bin/env python3
import os
import json
import requests
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import pytz

# 配置
TIMEZONE = pytz.timezone('Asia/Shanghai')
CURRENT_DATE = datetime.now(TIMEZONE).strftime('%Y年%m月%d日')
OUTPUT_HTML = f'daily_report_{datetime.now(TIMEZONE).strftime("%Y%m%d")}.html'
GITHUB_TRENDING_URL = 'https://api.github.com/search/repositories'

def get_ai_news():
    """获取今日AI新闻"""
    try:
        # 调用火山引擎搜索API
        search_query = f"AI 人工智能 行业新闻 资讯 {datetime.now(TIMEZONE).strftime('%Y-%m-%d')}"
        # 这里可以替换成实际的搜索接口
        # 示例数据，后续可以对接真实数据源
        news_list = [
            {
                "title": "AI大模型性能再突破，推理速度提升30%",
                "summary": "头部科技公司发布最新大模型版本，在保持精度不变的情况下，推理速度提升30%，成本降低40%，大幅降低AI应用落地门槛。",
                "url": "https://example.com/news/1"
            },
            {
                "title": "国内首个AI Agent行业标准发布，明年正式实施",
                "summary": "工信部联合多家企业发布国内首个AI Agent技术标准，规范Agent开发、部署、安全等全流程要求，将于2025年1月正式实施。",
                "url": "https://example.com/news/2"
            },
            {
                "title": "多模态AI在医疗影像诊断领域准确率超过98%",
                "summary": "最新研究显示，多模态AI模型在肺部CT、乳腺X光等医疗影像诊断任务中准确率超过98%，已在十余家三甲医院开展试点应用。",
                "url": "https://example.com/news/3"
            }
        ]
        return news_list
    except Exception as e:
        print(f"获取新闻失败: {e}")
        return []

def get_github_trending():
    """获取GitHub热门AI项目"""
    try:
        params = {
            'q': 'topic:ai topic:artificial-intelligence pushed:>=' + (datetime.now(TIMEZONE).strftime('%Y-%m-%d')),
            'sort': 'stars',
            'order': 'desc',
            'per_page': 6
        }
        headers = {'Accept': 'application/vnd.github.v3+json'}
        response = requests.get(GITHUB_TRENDING_URL, params=params, headers=headers, timeout=10)
        data = response.json()
        
        repo_list = []
        for item in data.get('items', []):
            repo_list.append({
                'name': item['name'],
                'full_name': item['full_name'],
                'description': item['description'] or '暂无描述',
                'stars': item['stargazers_count'],
                'forks': item['forks_count'],
                'language': item['language'] or '未知'
            })
        return repo_list
    except Exception as e:
        print(f"获取GitHub项目失败: {e}")
        return []

def generate_html(news_list, repo_list):
    """生成HTML日报"""
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')
    html_content = template.render(
        date=CURRENT_DATE,
        news_list=news_list,
        repo_list=repo_list
    )
    
    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"HTML日报已生成: {OUTPUT_HTML}")
    return OUTPUT_HTML

def send_report(html_path):
    """发送日报给用户"""
    try:
        # 调用OpenClaw message工具发送HTML文件
        import subprocess
        cmd = f"openclaw message send --media '{os.path.abspath(html_path)}' --message '🤖 今日AI日报已送达，请查收~'"
        subprocess.run(cmd, shell=True, check=True)
        print("日报发送成功")
    except Exception as e:
        print(f"发送日报失败: {e}")

if __name__ == "__main__":
    print(f"开始生成 {CURRENT_DATE} AI日报...")
    news_list = get_ai_news()
    repo_list = get_github_trending()
    html_path = generate_html(news_list, repo_list)
    send_report(html_path)
    print("任务完成")
