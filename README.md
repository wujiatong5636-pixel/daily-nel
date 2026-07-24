# 🌍 Daily-NEL | 全球科技新闻日报

自动收集和整理全球重要科技新闻，每日9点发送至邮箱。

## 📰 新闻分类

- 🤖 **人工智能** - AI技术、模型、应用
- 🦾 **机器人** - 机器人技术、自动化
- 🔬 **基础科学** - 物理、化学、生物等
- 💻 其他前沿技术

## 📧 邮件设置

- **收件地址**: wujiatong5636@gmail.com
- **发送时间**: 每日早上 09:00
- **新闻条数**: 20条
- **排序方式**: 按新闻重要程度

## 📋 日报格式

```
【科技日报】YYYY年MM月DD日

【人工智能】
1. [标题中文]
   📌 内容摘要：简练总结内容
   🔗 来源：[原文链接]

【机器人】
...
```

## 🛠️ 项目结构

```
daily-nel/
├── src/
│   ├── main.py                 # 主程序入口
│   ├── news_collector.py       # 新闻收集器
│   ├── news_processor.py       # 新闻处理/排序
│   ├── email_sender.py         # 邮件发送服务
│   └── config.py               # 配置文件
├── data/
│   ├── news_sources.json       # 新闻源配置
│   └── sent_news.db            # 已发送新闻数据库
├── logs/
│   └── daily_nel.log           # 日志文件
├── requirements.txt            # Python依赖
├── .github/
│   └── workflows/
│       └── daily_news.yml      # GitHub Actions工作流
└── README.md
```

## 🚀 快速开始

### 本地运行

```bash
# 1. 克隆项目
git clone https://github.com/wujiatong5636-pixel/daily-nel.git
cd daily-nel

# 2. 安装依赖
pip install -r requirements.txt

# 3. 配置邮件
cp .env.example .env
# 编辑 .env，填入你的邮箱和应用密码

# 4. 运行程序
python src/main.py
```

### 自动化运行（GitHub Actions）

1. **配置邮件凭证**
   - 打开仓库设置 → Secrets and variables → Actions
   - 添加以下Secrets：
     - `SENDER_EMAIL`: 你的Gmail邮箱
     - `SENDER_PASSWORD`: 应用密码（不是账户密码）

2. **配置时区**
   - GitHub Actions 使用 UTC 时区
   - 北京时间 09:00 = UTC 01:00
   - 在 `.github/workflows/daily_news.yml` 中的 cron 表达式为 `0 1 * * *`

3. **查看运行日志**
   - 打开 GitHub → Actions → Daily News Collection
   - 查看最近的运行记录和日志

## 📖 获取应用密码（Gmail）

1. 打开 [Google Account Security](https://myaccount.google.com/security)
2. 启用 2-Step Verification（两步验证）
3. 在 "App passwords" 选项中选择：
   - App: Mail
   - Device: Other (Windows/Mac/Linux)
4. 复制生成的应用密码到 `.env` 中

## ⚙️ 配置说明

### src/config.py

主要配置项：

```python
EMAIL_CONFIG          # 邮件配置（SMTP、收件人等）
SCHEDULER_CONFIG      # 定时任务配置（时间、频率）
NEWS_CONFIG           # 新闻配置（分类、关键词、数量）
NEWS_SOURCES          # 新闻源配置（RSS、API等）
```

### 支持的新闻源

目前支持的新闻源：

- **Ars Technica** - 科技新闻
- **The Verge** - 科技评论
- **Bloomberg** - 商业科技
- **虎嗅网** - 国内科技新闻

可添加更多RSS源或使用 NewsAPI.org

## ✨ 功能特性

✅ **自动收集** - 从多个来源定时收集新闻  
✅ **智能去重** - 避免重复新闻  
✅ **重要度评估** - 自动评估新闻重要性  
✅ **分类组织** - 按类别组织新闻  
✅ **格式化邮件** - 美观的HTML邮件格式  
✅ **定时发送** - 每日自动发送  
✅ **数据管理** - 数据库管理已发送新闻  
✅ **完整日志** - 完整的执行日志  

## 📊 日报示例

```
【科技日报】2024年1月15日

🤖 人工智能
1. OpenAI 发布 GPT-5 重大突破
   📌 OpenAI宣布推出新一代语言模型GPT-5，在多个任务上刷新记录...
   🔗 来源：OpenAI Official
   📖 阅读原文 →

2. 谷歌发布新型量子芯片
   📌 谷歌展示了新的量子计算芯片Willow，性能提升显著...
   🔗 来源：Google Official
   📖 阅读原文 →

🦾 机器人
...
```

## 🐛 故障排除

### 邮件无法发送

- 检查 `SENDER_EMAIL` 和 `SENDER_PASSWORD` 是否正确
- 确认已启用 2-Step Verification（Gmail）
- 查看日志文件 `logs/daily_nel.log`

### 收集不到新闻

- 检查网络连接
- 验证RSS源是否可访问
- 在日志中查看详细错误信息

### 定时任务未执行

- 确认程序仍在运行
- 检查系统时间是否正确
- 查看日志文件 `logs/daily_nel.log`

## 📝 许可证

MIT License

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📧 联系

有问题或建议？请联系：wujiatong5636@gmail.com
