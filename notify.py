import requests

# 発行されたトークン
ACCESS_TOKEN = 'yjTVAwzbiqBrhdLHRskPSMAIBWeiNu2BPOv5bBSMNPI'

header = {'Authorization': 'Bearer ' + ACCESS_TOKEN}

message = {
    'message': '@ALL\n本日は日曜日です。\n週報の提出お忘れなく！'
}

requests.post(
    'https://notify-api.line.me/api/notify',
    headers=header,
    data=message,
)