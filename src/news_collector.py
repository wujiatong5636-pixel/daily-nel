import feedparser
import requests
import logging
from datetime import datetime, timedelta
from src.config import NEWS_CONFIG

logger = logging.getLogger(__name__)


class NewsCollector:
    """新闻收集器：从多个RSS源收集新闻"""
    
    def __init__(self):
        self.timeout = NEWS_CONFIG['timeout']
        self.news_sources = self._load_sources()
    
    def _load_sources(self):
        """从JSON配置文件加载新闻源"""
        import json
        try:
            with open('data/news_sources.json', 'r', encoding='utf-8') as f:
                sources = json.load(f)
            logger.info(f"已加载 {len(sources)} 个新闻源")
            return sources
        except FileNotFoundError:
            logger.warning("news_sources.json 未找到，使用默认源")
            return self._get_default_sources()
        except json.JSONDecodeError as e:
            logger.error(f"JSON 解析错误: {e}")
            return self._get_default_sources()
    
    def _get_default_sources(self):
        """默认新闻源"""
        return [
            {
                'name': 'Ars Technica',
                'url': 'https://arstechnica.com/feed/',
                'category': '💻 其他前沿技术'
            },
            {
                'name': 'The Verge',
                'url': 'https://www.theverge.com/rss/index.xml',
                'category': '💻 其他前沿技术'
            },
            {
                'name': 'TechCrunch',
                'url': 'https://techcrunch.com/feed/',
                'category': '🤖 人工智能'
            },
        ]
    
    def collect(self):
        """收集所有新闻源的新闻"""
        all_news = []
        
        for source in self.news_sources:
            try:
                logger.info(f"正在从 {source['name']} 收集新闻...")
                news = self._fetch_from_rss(source['url'], source.get('category', '💻 其他前沿技术'))
                all_news.extend(news)
                logger.info(f"从 {source['name']} 获得 {len(news)} 条新闻")
            except Exception as e:
                logger.error(f"从 {source['name']} 收集新闻时出错: {e}")
                continue
        
        logger.info(f"总共收集 {len(all_news)} 条新闻")
        return all_news
    
    def _fetch_from_rss(self, url, category):
        """从RSS源获取新闻"""
        try:
            feed = feedparser.parse(url)
            news_list = []
            
            for entry in feed.entries[:15]:  # 每个源最多15条
                try:
                    # 提取发布时间
                    published = entry.get('published', '')
                    
                    # 提取摘要或描述
                    summary = entry.get('summary', entry.get('description', 'No Summary'))
                    # 清理HTML标签
                    summary = self._clean_html(summary)[:200]
                    
                    news_item = {
                        'title': entry.get('title', 'No Title'),
                        'link': entry.get('link', ''),
                        'summary': summary,
                        'category': category,
                        'source': feed.feed.get('title', 'Unknown Source'),
                        'published': published,
                        'collected_at': datetime.now().isoformat(),
                    }
                    
                    # 基础验证
                    if news_item['title'] and news_item['link']:
                        news_list.append(news_item)
                except Exception as e:
                    logger.debug(f"处理单条新闻时出错: {e}")
                    continue
            
            return news_list
        except Exception as e:
            logger.error(f"RSS 解析错误 ({url}): {e}")
            return []
    
    @staticmethod
    def _clean_html(text):
        """清理HTML标签"""
        import re
        # 移除HTML标签
        text = re.sub('<[^<]+?>', '', text)
        # 移除多余空白
        text = ' '.join(text.split())
        return text
