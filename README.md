# 🦒 Учет жирафов  
**Веб-приложение для автоматического подсчёта жирафов на фотографиях**  
*Flask + YOLOv8 + OpenCV.js*

---

## 📋 Описание
Это веб-приложение, которое:
1. Принимает фото или короткое видео через браузер.
2. Детектирует жирафов с помощью модели **YOLOv8** (COCO class 24).
3. Отрисовывает **bounding-box’ы** прямо в браузере.
4. Показывает вывод **количество** найденных жирафов.
5. Позволяет скачать PDF-отчёт по всем обработанным файлам.

---

## 🧩 Структура проекта
```
project_giraff/
│
├── app/                           # Flask-приложение
│   ├── __init__.py                # пустой, делает папку пакетом
│   ├── app.py                     # точка входа Flask
│   ├── routers.py                 # маршруты /detect и /report
│   ├── reporter.py                # генерация PDF-отчётов
│   ├── detector/                  # логика YOLOv8
│   │   ├── __init__.py            # пустой
│   │   └── yolo_detector.py
│   ├── static/                    # статические файлы
│   │   ├── result.jpg             # картинка после обработки
│   │   ├── reports/               # PDF-файлы
│   │   └── fonts/                 # кириллические шрифты
│   │       └── DejaVuSans.ttf
│   └── templates/
│       └── index.html             # единственный HTML-шаблон
│
├── requirements.txt               # все зависимости
```

## ✅ 1. Работа над кодом

### Выбор стека
- **Flask** — потому что лёгкий, минималистичный, знаком по лабораторным.  
- **YOLOv8** — быстрый, вес 6 МБ, достаточная точность для MVP.  
- **SQLite** — никаких миграций, хранит строки «дата-файл-количество».  
- **ReportLab** — рисует PDF-таблицу без сторонних зависимостей.

### Структура

Создала папку `app/`, добавила пустой файл  `__init__.py`, чтобы Python видел пакет.  
Внутри:
- `app.py` — только `create_app()` и запуск самого сервера.  
- `routers.py` — три маршрута: `/`, `/detect`, `/report`.  
- `detector/yolo_detector.py` — одна функция `detect_giraffes(file)`; принимает, обрабатывает байты и возвращает JSON.  
- `reporter.py` — собирает данные из SQLite и рисует PDF «дата-файл-количество».  
- `templates/index.html` — одна страница: кнопка «Обзор», кнопка «Скачать PDF», canvas с результатом.

### 4. Возникшие проблемы при работе в окружении
- **ModuleNotFoundError: cv2** — установила `opencv-python-headless`.
- **NumPy 2.x vs PyTorch 2.6** — обновила `ultralytics`.

```
(venv) PS C:\Users\v.kudasheva\Pictures\project_giraff> pip install flask ultralytics opencv-python-headless numpy==1.26.4
Collecting flask
  Downloading flask-3.1.1-py3-none-any.whl (103 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 103.3/103.3 kB 1.5 MB/s eta 0:00:00
Requirement already satisfied: ultralytics in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (8.0.200)
Requirement already satisfied: opencv-python-headless in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (4.8.1.78)
Requirement already satisfied: numpy==1.26.4 in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (1.26.4)
Collecting blinker>=1.9.0
Collecting click>=8.1.3
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 102.2/102.2 kB 5.7 MB/s eta 0:00:00
```
- **Кириллица в PDF** — возникра проблема с кириллицейпри выгрузке отчета, использовала `reportlab.pdfbase.ttfonts.TTFont` и шрифт DejaVuSans.
- **FileNotFoundError: DejaVuSans.ttf** — скачала шрифт с официального сайта, положила в `app/static/fonts`, прописала абсолютный путь.  


### 📌 Как всё связано
#### Пользователь загружает фото → index.html (/)
#### index.html отправляет файл на /detect → routers.py
#### routers.py вызывает yolo_detector.py
#### yolo_detector.py сохраняет result.jpg и записывает строку в БД
#### index.html показывает изображение и счётчик
#### При нажатии «Скачать PDF» браузер идёт на /report, который вызывает reporter.py → PDF качается.

### ✅ 2. Создание проекта в Visual Studio
#### Создаю виртуальное окружение в VS Code
```
python -m venv venv
```

#### ✅ 3. Запуск приложения 
```
python -m app.app
```
#### Мы попали в сервер разработки, теперь можно тестировать систему учета жирафов:

![](https://github.com/Orrionn/Giraff/blob/main/app.png?raw=true)

#### Переходим на сайт http://127.0.0.1:5000

![](https://github.com/Orrionn/Giraff/blob/main/веб-сервис.png?raw=true)

#### Начинаем учет жирафов. И видим, что ИИ определил что на фото 2 жирафа.

![](https://github.com/Orrionn/Giraff/blob/main/2%20жирафа.png?raw=true)

#### Далее нажимаем "Скачать PDF-отчет". Перехожу в папку, куда скачиваются отчеты и фото с результатами.

![](https://github.com/Orrionn/Giraff/blob/main/генерация%20PDF.png?raw=true)

#### Проверим распознавание других животных. ИИ определил что на фото 1 собака и 1 жираф.

![](https://github.com/Orrionn/Giraff/blob/main/собака%20и%20жираф.png?raw=true)

#### В папке с результатаи всегда будет храниться только последнее фото обработки.

![](https://github.com/Orrionn/Giraff/blob/main/вывод%20собака%20и%20жираф.png?raw=true)






















