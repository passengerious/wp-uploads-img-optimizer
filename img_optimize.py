import os
from pathlib import Path
from PIL import Image
import pillow_heif  # Додаємо підтримку HEIC

# Потрібно зареєструвати HEIF оупенер для Pillow
pillow_heif.register_heif_opener()

def process_images(root_directory, quality=80, delete_original=True):
    # Додали .gif, .heic та .tif до списку
    extensions = {".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".tif", ".gif", ".heic"}
    
    # Перетворюємо відносний шлях у абсолютний для надійності
    base_path = Path(root_directory).resolve()
    
    if not base_path.exists():
        print(f"Помилка: Папка {base_path} не знайдена!")
        return

    print(f"Починаю обробку в: {base_path}")

    for root, dirs, files in os.walk(base_path):
        for file in files:
            file_path = Path(root) / file
            
            if file_path.suffix.lower() in extensions:
                try:
                    with Image.open(file_path) as img:
                        # Створюємо шлях для нового файлу .webp В ТІЙ ЖЕ ПАПЦІ
                        webp_path = file_path.with_suffix(".webp")
                        
                        # Конвертуємо (з підтримкою прозорості)
                        img.save(webp_path, "webp", quality=quality, method=6)
                        print(f"✅ Готово: {file_path.name} -> {webp_path.name}")
                    
                    # Видаляємо оригінал, якщо розширення відрізняється
                    if delete_original and file_path.suffix.lower() != ".webp":
                        os.remove(file_path)
                        
                except Exception as e:
                    print(f"❌ Помилка файлу {file}: {e}")

if __name__ == "__main__":
    # Оптимізуємо ВСЕ в ./uploads, зберігаючи структуру папок
    process_images("./uploads", quality=80, delete_original=True)