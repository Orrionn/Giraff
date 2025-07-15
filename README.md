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
#### 1. Пользователь загружает фото → index.html (*/*)
#### 2. index.html отправляет файл на */detect* → routers.py
#### 3. routers.py вызывает yolo_detector.py
#### 4. index.html показывает изображение и счётчик

### ✅ 2. Создание проекта в Visual Studio
#### Создаю виртуальное окружение в VS Code
```
python -m venv venv
```

#### Обновляю необходимые пакеты:
```
(venv) PS C:\Users\v.kudasheva\Pictures\project_giraff> pip install --upgrade ultralytics 
Requirement already satisfied: ultralytics in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (8.0.200)
Collecting ultralytics              
  Downloading ultralytics-8.3.166-py3-none-any.whl.metadata (37 kB)         
Requirement already satisfied: numpy>=1.23.0 in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from ultralytics) 
Requirement already satisfied: matplotlib>=3.3.0 in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from ultralyti
Requirement already satisfied: opencv-python>=4.6.0 in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from ultral
Requirement already satisfied: pillow>=7.1.2 in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from ultralytics) 
Requirement already satisfied: pyyaml>=5.3.1 in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from ultralytics) 
Requirement already satisfied: requests>=2.23.0 in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from ultralytic
Requirement already satisfied: scipy>=1.4.1 in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from ultralytics) (
Requirement already satisfied: torch>=1.8.0 in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from ultralytics) (
Requirement already satisfied: torchvision>=0.9.0 in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from ultralyt
Requirement already satisfied: tqdm>=4.64.0 in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from ultralytics) (
Requirement already satisfied: psutil in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from ultralytics) (7.0.0)
Requirement already satisfied: py-cpuinfo in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from ultralytics) (9.
Requirement already satisfied: pandas>=1.1.4 in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from ultralytics) 
Collecting ultralytics-thop>=2.0.0 (from ultralytics)
  Downloading ultralytics_thop-2.0.14-py3-none-any.whl.metadata (9.4 kB)
Requirement already satisfied: contourpy>=1.0.1 in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from matplotlib
Requirement already satisfied: cycler>=0.10 in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from matplotlib>=3.
Requirement already satisfied: fonttools>=4.22.0 in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from matplotli
Requirement already satisfied: kiwisolver>=1.3.1 in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from matplotli
Requirement already satisfied: packaging>=20.0 in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from matplotlib>
Requirement already satisfied: pyparsing>=2.3.1 in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from matplotlib
Requirement already satisfied: python-dateutil>=2.7 in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from matplo
Requirement already satisfied: pytz>=2020.1 in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from pandas>=1.1.4-
Requirement already satisfied: tzdata>=2022.7 in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from pandas>=1.1.
Requirement already satisfied: six>=1.5 in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from python-dateutil>=2
Requirement already satisfied: charset_normalizer<4,>=2 in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from re
Requirement already satisfied: idna<4,>=2.5 in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from requests>=2.23
Requirement already satisfied: urllib3<3,>=1.21.1 in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from requests
Requirement already satisfied: certifi>=2017.4.17 in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from requests
Requirement already satisfied: filelock in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from torch>=1.8.0->ultr
Requirement already satisfied: typing-extensions>=4.10.0 in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from t
Requirement already satisfied: sympy>=1.13.3 in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from torch>=1.8.0-
Requirement already satisfied: networkx in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from torch>=1.8.0->ultr
Requirement already satisfied: jinja2 in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from torch>=1.8.0->ultral
Requirement already satisfied: fsspec in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from torch>=1.8.0->ultral
Requirement already satisfied: mpmath<1.4,>=1.1.0 in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from sympy>=1
Requirement already satisfied: colorama in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from tqdm>=4.64.0->ultr
Requirement already satisfied: MarkupSafe>=2.0 in c:\users\v.kudasheva\pictures\project_giraff\venv\lib\site-packages (from jinja2->tor
Downloading ultralytics-8.3.166-py3-none-any.whl (1.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.0/1.0 MB 5.6 MB/s eta 0:00:00
Downloading ultralytics_thop-2.0.14-py3-none-any.whl (26 kB)
Installing collected packages: ultralytics-thop, ultralytics
  Attempting uninstall: ultralytics
    Found existing installation: ultralytics 8.0.200
    Uninstalling ultralytics-8.0.200:
      Successfully uninstalled ultralytics-8.0.200
Successfully installed ultralytics-8.3.166 ultralytics-thop-2.0.14
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






















