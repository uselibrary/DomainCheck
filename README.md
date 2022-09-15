# DomainCheck

基于Python 3的域名扫描工具，支持任意后缀，可设置扫描间隔，并可添加自定义字典。

使用方法如下，以Debian 11为例：
```
apt update && apt install git python3 -y
cd ~
git clone https://github.com/uselibrary/DomainCheck
cd DomainCheck
python3 GetDomain.py
```
随后进入扫描参数设置过程，其中会询问三个数据：
```
Enter tld name: xyz #输入需要查询的后缀
Enter dict name: allpy #输入字典，位于dict文件夹下
Enter delay: 0 # 查询间隔（秒），部分whois/nic对频繁查询行为进行了限制
Task Start
****************
bo.xyz is available #可以注册的域名
bai.xyz is NOT available #不可注册的域名
```

`tld.json`为域名的字典，格式如下：
```
  "xyz": { #域名后缀
    "nic": "whois.nic.xyz", #whois/nic服务器
    "response": "object does not exist" #未注册域名的响应反馈
  }
```

`dict`为字典：
- allpy 所有单拼
- test 测试


Check the available domain of a TLD with dict, based on Python.
