import logging
from collections import defaultdict
from datetime import datetime
from src.config import NEWS_CONFIG

logger = logging.getLogger(__name__)


class NewsProcessor:
    """新闻处理器：去重、分类、排序新闻"""
    
    def __init__(self):
        self.categories = NEWS_CONFIG['categories']
        self.news_limit = NEWS_CONFIG['limit']
    
    def process(self, news_list):
        """处理新闻：去重、分类、排序"""
        logger.info("开始处理新闻...")
        
        # 1. 去重
        unique_news = self._deduplicate(news_list)
        logger.info(f"去重后: {len(unique_news)} 条新闻 (移除 {len(news_list) - len(unique_news)} 条重复)")
        
        if not unique_news:
            logger.warning("去重后没有新闻")
            return {}
        
        # 2. 分类和评分
        categorized_news = self._categorize_and_score(unique_news)
        
        # 3. 按重要度排序
        sorted_news = self._sort_by_importance(categorized_news)
        
        # 4. 按分类组织
        organized_news = self._organize_by_category(sorted_news)
        
        logger.info(f"处理完成，分类数: {len(organized_news)}")
        for category, news in organized_news.items():
            logger.info(f"  {category}: {len(news)} 条新闻")
        
        return organized_news
    
    def _deduplicate(self, news_list):
        """去重：基于标题和来源"""
        seen = set()
        unique = []
        
        for news in news_list:
            # 使用标题作为去重的主要依据
            key = news['title'].lower().strip()
            if key not in seen:
                seen.add(key)
                unique.append(news)
        
        return unique
    
    def _categorize_and_score(self, news_list):
        """对新闻进行分类和重要度评分"""
        for news in news_list:
            # 确定分类
            category = self._determine_category(news['title'] + ' ' + news['summary'])
            news['category'] = category
            
            # 计算重要度分数
            score = self._calculate_importance_score(news)
            news['importance_score'] = score
        
        return news_list
    
    def _determine_category(self, text):
        """根据关键词确定新闻分类"""
        text_lower = text.lower()
        
        for category, keywords in self.categories.items():
            for keyword in keywords:
                if keyword.lower() in text_lower:
                    return category
        
        return '💻 其他前沿技术'  # 默认分类
    
    def _calculate_importance_score(self, news):
        """计算新闻重要度分数(0-100)"""
        score = 50  # 基础分数
        
        # 标题长度（较长的标题通常更详细）
        if len(news['title']) > 50:
            score += 10
        
        # 摘要长度
        if len(news['summary']) > 100:
            score += 10
        
        # 包含特定关键词的加分
        high_value_keywords = [
            'breakthrough', 'revolutionary', 'announce', 'release', 'launch',
            'new', 'update', 'innovation', 'discover', 'research',
            '突破', '革命', '宣布', '发布', '新型', '新一代',
            'ai', 'machine learning', 'quantum', 'robot', 'innovation'
        ]
        
        text_lower = (news['title'] + ' ' + news['summary']).lower()
        for keyword in high_value_keywords:
            if keyword.lower() in text_lower:
                score += 5
        
        # 限制最高分
        return min(score, 100)
    
    def _sort_by_importance(self, news_list):
        """按重要度排序"""
        return sorted(news_list, key=lambda x: x.get('importance_score', 50), reverse=True)
    
    def _organize_by_category(self, news_list):
        """按分类组织新闻"""
        organized = defaultdict(list)
        
        # 选取前N条新闻
        for news in news_list[:self.news_limit]:
            category = news['category']
            organized[category].append(news)
        
        # 按分类名称排序（确保顺序一致）
        return dict(sorted(organized.items()))
