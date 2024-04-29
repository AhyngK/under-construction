import json
import requests

logstash_host = "localhost"
logstash_port = 9001

url = f"http://{logstash_host}:{logstash_port}"
headers = {"Content-Type": "application/json"}

# 전송할 데이터
data = {
  "timestamp": 1622633590923000,
  "body": "User authentication successful",
  "severity": "INFO",
  "attributes": {
    "userId": "123",
    "username": "john.doe"
  },
  "traceId": "4bf92f3577b34da6a3ce929d0e0e4736",
  "spanId": "2e7d0ad2a6d7a0e7"
}

# 데이터를 JSON 형식으로 직렬화
json_data = json.dumps(data)

# HTTP POST 요청을 사용하여 데이터 전송
response = requests.post(url, data=json_data, headers={"Content-Type": "application/json"})

# 응답 확인
if response.status_code == 200:
    print("데이터가 성공적으로 전송되었습니다.")
else:
    print(f"데이터 전송 실패. 상태 코드: {response.status_code}")