from src.views.main import generate_main_page_json
import json

if __name__ == "__main__":
    timestamp_str = "2024-06-10 14:30:00"
    print("🚀 Запрашиваем данные для главной страницы...")
    try:
        data = generate_main_page_json(timestamp_str)
        print("✅ Данные получены!\n")
        print(json.dumps(data, ensure_ascii=False, indent=2))
    except Exception as e:
        print(f"❌ Ошибка: {e}")
