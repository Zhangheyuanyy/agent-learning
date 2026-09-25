import httpx

url = "https://jsonplaceholder.typicode.com/todos/1"

response = httpx.get(url)

print("状态码：")
print(response.status_code)

print("服务器返回的内容：")
print(response.text)