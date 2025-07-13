
import requests
import os

url = "https://docs.ozon.ru/api/seller/swagger.json"
headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://docs.ozon.ru/api/seller/"
}

r = requests.get(url, headers=headers)

if r.status_code == 200:
    os.makedirs("docs", exist_ok=True)
    with open("docs/swagger.json", "w", encoding="utf-8") as f:
        f.write(r.text)
    print("✅ swagger.json успешно обновлён.")
else:
    print(f"❌ Ошибка {r.status_code}: не удалось получить swagger.json")
