# CSV Processor CLI

Простой CLI-инструмент для фильтрации и агрегации данных из CSV-файлов.

---

## Возможности

- Фильтрация строк по числовым и текстовым значениям:
    
    - `price>500`
        
    - `brand=apple`
        
- Агрегации: `avg`, `min`, `max` по числовым колонкам
    
- Красивый вывод таблицы с помощью `tabulate`
    
- Обработка ошибок (неверный путь, неизвестные колонки и т.д.)
    
- Модульная архитектура и покрытие тестами через `pytest`
    

---

## Пример CSV-файла

Пример содержится в файле `products.csv`, который включён в проект.

---

## Примеры запуска

### Фильтрация

```bash
python main.py --file products.csv --filter price>500
```

### Агрегация

```bash
python main.py --file products.csv --aggregate avg:price
```

![[Pasted image 20250620224104.png]]

---

## Установка и запуск тестов

```bash
pip install -r requirements.txt
pytest --cov=csv_processor --cov-report=term-missing
```

