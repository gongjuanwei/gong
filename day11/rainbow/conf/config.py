import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_path = os.path.join(base_dir, 'logs', 'rainbow.log')  # 日志文件
data_path = os.path.join(base_dir, 'data')  # 存放测试数据的目录
report_path = os.path.join(base_dir, 'report')  # 存放报告的目录
case_path = os.path.join(base_dir, 'cases')  # 存放case的目录
config_path = os.path.join(base_dir, 'conf')  # 存放case的目录

log_level = "DEBUG"
dd_url = "https://oapi.dingtalk.com/robot/send"  #

dingding = {
    "qa": {
        "secret": "SEC16003eafa395e73ddacece95ee6aa72f3eb22ff667a88197ff7c0533053e1225",
        "access_token": "02ba6dbc04ebc825bc6fede96941d42beb45c4e57120db41b824d2161a9e3a76"
    },
    "dev": {
        "secret": "SEC16003eafa395e73ddacece95ee6aa72f3eb22ff667a88197ff7c0533053e1225",
        "access_token": "02ba6dbc04ebc825bc6fede96941d42beb45c4e57120db41b824d2161a9e3a76"
    }
}

ini_file_name = "config.ini"
yaml_config_file = "config.yaml"
