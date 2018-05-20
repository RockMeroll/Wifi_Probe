import random
import urllib.parse
import http.client


def send_yzm(apikey, content, mobile):
    """
    发送验证码
    """
    # 服务地址
    sms_host = "api.dingdongcloud.com"
    # 端口号
    port = 443
    # 发送验证码
    send_yzm_uri = "/v1/sms/captcha/send"

    params = urllib.parse.urlencode({'apikey': apikey, 'content': content, 'mobile':mobile})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

    conn = http.client.HTTPSConnection(sms_host, port=port, timeout=30)
    conn.request("POST", send_yzm_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()

    return response_str


def gene_text():
    """
    生成验证码
    """
    number = 6  # 位数
    source = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    return ''.join(random.sample(source, number))



