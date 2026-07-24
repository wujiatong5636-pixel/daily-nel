#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Daily-NEL 主程序入口
自动收集和整理全球重要科技新闻，每日发送至邮箱
"""

import sys
import logging
import os
from datetime import datetime

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import LOG_CONFIG

# 配置日志
logging.basicConfig(
    level=getattr(logging, LOG_CONFIG['log_level']),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_CONFIG['log_file']),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def main():
    """主函数"""
    try:
        logger.info("=" * 50)
        logger.info("开始执行每日科技新闻采集和发送")
        logger.info(f"执行时间: {datetime.now().isoformat()}")
        logger.info("=" * 50)
        
        # TODO: 导入并执行新闻收集、处理、发送逻辑
        # from news_collector import NewsCollector
        # from news_processor import NewsProcessor
        # from email_sender import EmailSender
        
        logger.info("✅ 每日科技新闻采集和发送完成")
        logger.info("=" * 50)
        
    except Exception as e:
        logger.error(f"❌ 执行过程中出现错误: {str(e)}", exc_info=True)
        sys.exit(1)


if __name__ == '__main__':
    main()
