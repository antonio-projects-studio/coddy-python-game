# Как скачать и запустить игру на `python`

## Качаем игру с `GitHub`

1. Находим репозиторий `GitHub` с кодом вашей игры. Его можно найти, например, на каналах разных ютуберов-программистов. Пример YouTube канала: [ссылка](https://www.youtube.com/watch?v=ECqUrT7IdqQ). Пример репозитория: [ссылка](https://github.com/StanislavPetrovV/DOOM-style-Game)
2. Качаем папку с игрой из репозитория:
	```
	git clone https://github.com/some_repository
	```

## Запускаем игру с помощью `python`

1. Заходим в папку с игрой, видим файлик `requiremets.txt`, в котором лежат все списки нужных библиотек
2. Вспоминаем, что библиотеки скачиваются с помощью **пакетного менеджера** `pip`

	Команда для скачивания библиотеки:
	```
	pip install name_of_library
	```
	Команда для скачивания всех библиотек, которые храняться в файлике `requiremets.txt`:
	```
	pip install -r requirements.txt
	```
	Команда для удаления библиотеки:
	```
	pip uninstall name_of_library
	```
	Чтобы посмотреть команды `pip`:
	```
	pip --help
	```
3. Запустить игру:
	```
	python main.py
	```
	P.S. обычно игра или приложение запускается файлом `main,py`, **НО!!!** не всегда 
