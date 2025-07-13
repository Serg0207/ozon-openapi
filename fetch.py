import requests

url = "https://docs.ozon.ru/api/seller/swagger.json"
output_path = "docs/swagger.json"

response = requests.get(url, headers={
    "User-Agent": "Mozilla/5.0"
})
response.raise_for_status()

with open(output_path, "w", encoding="utf-8") as f:
    f.write(response.text)

print(f"Файл сохранён в {output_path}")
