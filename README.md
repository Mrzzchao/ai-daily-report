# 🤖 AI 每日情报生成工具

自动生成每日AI行业资讯、GitHub热门项目的HTML日报，每天定时推送。

## 功能特点

- ✅ 每日自动抓取AI行业最新新闻
- ✅ 实时获取GitHub热门AI开源项目
- ✅ 生成美观的响应式HTML日报
- ✅ 支持定时自动推送（每天早上8点）
- ✅ 历史报告自动归档保存30天

## 项目结构

```
ai-daily-report/
├── main.py              # 主程序，生成日报
├── template.html        # HTML模板
├── requirements.txt     # 依赖包
├── .github/
│   └── workflows/
│       └── daily.yml    # GitHub Actions 定时任务
└── README.md
```

## 本地运行

```bash
# 安装依赖
pip install -r requirements.txt

# 生成日报
python main.py
```

## 配置说明

### 1. 定时任务
默认每天北京时间早上8点自动运行，生成并推送日报。可以修改 `.github/workflows/daily.yml` 中的 cron 表达式调整时间。

### 2. 数据源
- 新闻：支持对接各类资讯API，默认内置示例数据
- GitHub项目：自动获取过去24小时Star增长最快的AI类项目

### 3. 推送配置
需要在GitHub仓库的Secrets中配置 `OPENCLAW_API_KEY` 用于推送消息到微信。

## 自定义修改

- 修改 `template.html` 可以调整日报的样式和布局
- 修改 `main.py` 中的 `get_ai_news()` 函数可以对接你自己的新闻数据源
- 可以添加更多板块：论文速递、产品动态、行业政策等

## 效果预览

生成的HTML日报包含：
- 每日日期标题
- 3条AI行业要闻（带原文链接）
- 6个GitHub热门AI项目（带Star数、语言、描述）
- 响应式设计，手机和电脑都能完美查看
