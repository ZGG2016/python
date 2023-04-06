
import sys
import requests

"""
每周周报邮件提醒：

1.安装cron，在命令行中输入 yum -y install cron

2. vi /etc/crontab 在最后加入:
        0 17 * * 1-5 /usr/bin/python autosend_mail_02.py ....[输入参数]
        周一到周五每天下午 5:00 自动发送周报提醒邮件
"""

def auto_send_mail(subject,body,recipients,URL):

    data = {
        'subject': subject,
        'tos': ','.join(recipients),
        'content': body
    }

    r = requests.post(URL, data=data)

    if r.status_code != 200:
        print('mail failed!')
        print(r.status_code)
        print(r.text)

if __name__ == "__main__":

    subject = u"周报提醒"
    body = u"大家快发周报啦!!!"

    # 邮件接收者
    recipients = ['%s' % sys.argv[1]]
    # 公司邮箱服务器
    URL = sys.argv[2]

    auto_send_mail(subject,body,recipients,URL)