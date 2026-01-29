import smtplib
import email.utils
from email.message import EmailMessage


class EmailNotify:

    SMTP_SERVER = "smtp.qq.com"
    FROM_ADDR = "1417412005@qq.com"
    # qq授权码
    FROM_ADDR_AUTH = ""

    def __init__(self, smtp_server=SMTP_SERVER, from_addr=FROM_ADDR, auth=FROM_ADDR_AUTH,
                 port=465, use_ssl=True, debug=False):
        self.smtp_server = smtp_server
        self.from_addr = from_addr
        self.auth = auth
        self.port = port
        self.use_ssl = use_ssl
        self.debug = debug

    def send_email(self, to_addr, send_name="测试标题", msg_content="测试内容", msg_subject="测试主题!!!!!"):
        """Send a simple email (no attachments).

        Args:
            to_addr (str): recipient email address
            send_name (str): display name for sender
            msg_content (str): body text
            msg_subject (str): subject line
        """
        try:
            # 建立连接
            if self.use_ssl:
                conn = smtplib.SMTP_SSL(self.smtp_server, self.port)
            else:
                conn = smtplib.SMTP(self.smtp_server, self.port)
            conn.set_debuglevel(1 if self.debug else 0)
            conn.login(self.from_addr, self.auth)

            # 创建邮件对象
            msg = EmailMessage()
            msg.set_content(msg_content)
            msg["subject"] = msg_subject
            msg["from"] = f"{send_name}<{self.from_addr}>"

            conn.sendmail(self.from_addr, [to_addr], msg.as_string())
            conn.quit()
            print("📧 Email sent successfully.")
        except Exception as e:
            print(f"❌ Failed to send email: {e}")
# 添加附件
# with open("D:\Desktop\Alipay.jpg", "rb") as f:
#     # 添加第一个附件
#     msg.add_attachment(f.read(), maintype="image",
#                        subtype="jpeg", filename="coffee.png", cid=first_id)
# with open("C:/Users/Public/Pictures/lyn/s009.jpg", "rb") as f:
#     # 添加第二个附件
#     msg.add_attachment(f.read(), maintype="image",
#                        subtype="jpeg", filename="test.jpeg", cid=second_id)
# with open("E:/Manual/pdf/laravel-source-analysis.pdf", "rb") as f:
#     # 添加第三个附件，邮件正文不需引用该附件，因此不指定cid
#     msg.add_attachment(f.read(), maintype="application",
#                        subtype="pdf", filename="test.pdf",)

# 发送邮件

if __name__ =="__main__":
    notifier = EmailNotify(debug=True)
    notifier.send_email(to_addr="1312765847@qq.com")