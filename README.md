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

---

## 🧩 Структура проекта

```
project_giraff/
├─ app/                            # Flask-бэкенд
│     ├─ models/                   # Сюда поместить YOLOv8
│     ├─ routers.py/               # Flask маршруты
│     ├─ detector/                 # YOLOv8 логика
│     │   └── yolo_detector.py     # логика YOLOv8
│     ├─ app.py/                   # Точка входа в backend
│
├─ frontend/                       # Дополнительно для dev фронтенда
│  ├─  index.html                  # фронтенд (HTML/CSS/JS + OpenCV.js) как в задании
│  └─script.js
├─ requirements.txt                # Дополнительно для dev фронтенда
└─ README.md
```

### ✅ 1. Работа над кодом

>### app/app.py 
>app/app.py — точка входа во Flask-приложение
>Роль:
>1. создаёт экземпляр Flask;
>2. регистрирует все маршруты (Blueprint);
>3. запускает сервер.
>
> Flask-фабрика (create_app) позволяет легко тестировать приложение и использовать разные конфигурации.
>При запуске python -m app.app именно этот файл выполняется первым.


>### app/routers.py
>app/routers.py — «карта сайта» (все URL-эндпоинты)
>Роль:
>1. описывает, на какой URL какая функция реагирует;
>2. связывает backend и frontend.


>### app/detector/yolo_detector.py
>app/detector/yolo_detector.py — основная часть системы
>Роль:
>1. загружает модель YOLOv8;
>2. принимает бинарное изображение;
>3. возвращает список bounding-box’ей и количество жирафов.


>### app/templates/index.html
>app/templates/index.html — лицо приложения (frontend)
>Роль:
>1. отображает интерфейс;
>2. отправляет файл на /detect;
>3. рисует bounding-box’ы и показывает счётчик.
>   
>Идет взаимодействуе только с этой страницей; всё остальное скрыто за backend-эндпоинтами.

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
#### ✅ 3. Запуск приложения 
```
python -m app.app
```
Мы попали в сервер разработки, теперь можно тестировать систему учета жирафов:

![](https://github.com/Orrionn/Giraff/blob/main/app.png?raw=true)

Переходим на сайт http://127.0.0.1:5000

![](

Начинаем учет жирафов

![](

И видим, что ИИ определил что на фото 2 жирафа.

![](

Проверим распознавание других животных

![](




























