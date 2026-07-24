import os
from dotenv import load_dotenv

load_dotenv()

# 邮件配置
EMAIL_CONFIG = {
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'sender_email': os.getenv('SENDER_EMAIL', 'your-email@gmail.com'),
    'sender_password': os.getenv('SENDER_PASSWORD', 'your-app-password'),
    'receiver_email': os.getenv('RECEIVER_EMAIL', 'recipient@example.com'),
}

# 定时任务配置
SCHEDULER_CONFIG = {
    'hour': int(os.getenv('SCHEDULE_HOUR', 9)),
    'minute': int(os.getenv('SCHEDULE_MINUTE', 0)),
}

# 新闻配置
NEWS_CONFIG = {
    'limit': int(os.getenv('NEWS_LIMIT', 20)),
    'timeout': int(os.getenv('TIMEOUT', 10)),
    'categories': {
        '🤖 人工智能': ['AI', 'artificial intelligence', 'machine learning', 'deep learning', 'neural', 'GPT', 'LLM'],
        '🦾 机器人': ['robot', 'robotics', 'automation', '机器人'],
        '🔬 基础科学': ['physics', 'chemistry', 'biology', 'science', '物理', '化学', '生物'],
        '💻 其他前沿技术': ['technology', 'tech', 'innovation', '科技', '技术'],
    }
}

# 日志配置
LOG_CONFIG = {
    'log_file': 'logs/daily_nel.log',
    'log_level': 'INFO',
}
