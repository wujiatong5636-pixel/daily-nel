import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from src.config import EMAIL_CONFIG

logger = logging.getLogger(__name__)


class EmailSender:
    """邮件发送器：发送格式化的新闻日报邮件"""
    
    def __init__(self):
        self.smtp_server = EMAIL_CONFIG['smtp_server']
        self.smtp_port = EMAIL_CONFIG['smtp_port']
        self.sender_email = EMAIL_CONFIG['sender_email']
        self.sender_password = EMAIL_CONFIG['sender_password']
        self.receiver_email = EMAIL_CONFIG['receiver_email']
    
    def send(self, organized_news):
        """发送新闻日报邮件"""
        try:
            if not organized_news:
                logger.warning("没有新闻可发送")
                return False
            
            # 生成邮件内容
            html_content = self._generate_html(organized_news)
            
            # 创建邮件
            msg = MIMEMultipart('alternative')
            msg['Subject'] = self._generate_subject()
            msg['From'] = self.sender_email
            msg['To'] = self.receiver_email
            
            # 添加HTML部分
            msg.attach(MIMEText(html_content, 'html', 'utf-8'))
            
            # 发送邮件
            logger.info(f"正在发送邮件到 {self.receiver_email}...")
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
            
            logger.info(f"邮件已成功发送到 {self.receiver_email}")
            return True
        
        except smtplib.SMTPAuthenticationError:
            logger.error("SMTP 认证失败，请检查邮箱和应用密码")
            return False
        except smtplib.SMTPException as e:
            logger.error(f"SMTP 错误: {e}")
            return False
        except Exception as e:
            logger.error(f"发送邮件时出错: {e}")
            return False
    
    def _generate_subject(self):
        """生成邮件主题"""
        today = datetime.now().strftime('%Y年%m月%d日')
        return f"【科技日报】{today}"
    
    def _generate_html(self, organized_news):
        """生成HTML格式的邮件内容"""
        today = datetime.now().strftime('%Y年%m月%d日')
        
        html = f"""
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                * {{
                    margin: 0;
                    padding: 0;
                }}
                body {{
                    font-family: 'Microsoft YaHei', 'Segoe UI', Arial, sans-serif;
                    background-color: #f5f5f5;
                    color: #333;
                    line-height: 1.6;
                }}
                .container {{
                    max-width: 800px;
                    margin: 20px auto;
                    background-color: #fff;
                    padding: 30px;
                    border-radius: 8px;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                }}
                .header {{
                    text-align: center;
                    border-bottom: 3px solid #007bff;
                    padding-bottom: 20px;
                    margin-bottom: 30px;
                }}
                .header h1 {{
                    margin: 0 0 10px 0;
                    color: #007bff;
                    font-size: 28px;
                    font-weight: bold;
                }}
                .header p {{
                    margin: 0;
                    color: #666;
                    font-size: 14px;
                }}
                .category {{
                    margin: 30px 0;
                }}
                .category-title {{
                    font-size: 18px;
                    font-weight: bold;
                    color: #007bff;
                    margin-bottom: 15px;
                    padding-bottom: 8px;
                    border-bottom: 2px solid #e0e0e0;
                }}
                .news-item {{
                    margin-bottom: 20px;
                    padding: 15px;
                    background-color: #f9f9f9;
                    border-radius: 4px;
                    border-left: 4px solid #007bff;
                    transition: box-shadow 0.3s ease;
                }}
                .news-item:hover {{
                    box-shadow: 0 2px 4px rgba(0,123,255,0.2);
                }}
                .news-number {{
                    display: inline-block;
                    background-color: #007bff;
                    color: white;
                    width: 28px;
                    height: 28px;
                    text-align: center;
                    line-height: 28px;
                    border-radius: 50%;
                    font-weight: bold;
                    margin-right: 10px;
                    font-size: 14px;
                }}
                .news-title {{
                    font-weight: bold;
                    color: #333;
                    margin: 8px 0;
                    font-size: 15px;
                    word-break: break-word;
                }}
                .news-summary {{
                    color: #666;
                    font-size: 13px;
                    margin: 10px 0;
                    line-height: 1.5;
                    word-break: break-word;
                }}
                .news-meta {{
                    font-size: 12px;
                    color: #999;
                    margin: 8px 0;
                    display: flex;
                    justify-content: space-between;
                }}
                .news-source {{
                    background-color: #e8f4f8;
                    padding: 2px 8px;
                    border-radius: 3px;
                    display: inline-block;
                }}
                .news-link {{
                    display: inline-block;
                    margin-top: 10px;
                    padding: 8px 12px;
                    background-color: #007bff;
                    color: white;
                    text-decoration: none;
                    border-radius: 4px;
                    font-size: 12px;
                    transition: background-color 0.3s ease;
                }}
                .news-link:hover {{
                    background-color: #0056b3;
                }}
                .footer {{
                    text-align: center;
                    margin-top: 40px;
                    padding-top: 20px;
                    border-top: 1px solid #e0e0e0;
                    color: #999;
                    font-size: 12px;
                }}
                .footer a {{
                    color: #007bff;
                    text-decoration: none;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>📰 科技日报</h1>
                    <p>{today}</p>
                </div>
        """
        
        # 添加各分类的新闻
        for category, news_list in organized_news.items():
            html += f"""
                <div class="category">
                    <div class="category-title">{category}</div>
            """
            
            for idx, news in enumerate(news_list, 1):
                source = news.get('source', 'Unknown')
                link = news.get('link', '#')
                title = news.get('title', 'No Title')
                summary = news.get('summary', 'No Summary')[:150]
                
                html += f"""
                    <div class="news-item">
                        <div>
                            <span class="news-number">{idx}</span>
                            <div class="news-title">{title}</div>
                        </div>
                        <div class="news-summary">📌 {summary}...</div>
                        <div class="news-meta">
                            <span class="news-source">来源：{source}</span>
                        </div>
                        <a href="{link}" class="news-link">🔗 阅读原文 →</a>
                    </div>
                """
            
            html += "</div>"
        
        # 添加页脚
        html += """
                <div class="footer">
                    <p>📧 由 <strong>Daily-NEL</strong> 自动生成 | 
                    <a href="https://github.com/wujiatong5636-pixel/daily-nel">GitHub</a> | 
                    每日北京时间 09:00 自动发送</p>
                    <p>如有问题或建议，欢迎反馈</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        return html
