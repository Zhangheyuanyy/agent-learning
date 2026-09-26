import httpx


url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "My First API",
    "body": "I am learning Agent development.",
    "userId": 1
}

response = httpx.post(url, json=data)

print("状态码：", response.status_code)
print("请求头：", response.request.headers)
print("服务器返回：", response.json())