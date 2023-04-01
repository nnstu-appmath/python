## Установка python
На этой странице вы можете скачать python для Windows. (https://www.python.org/downloads/windows/)

![image](https://user-images.githubusercontent.com/125145037/224363550-7c01ad22-434f-48e8-9159-a30a5ed9cbde.png)

Для установки `python` нажмите на ссылку, которая начинается со слов “Последний выпуск Python3…” и вы попадете на страницу последней версии `Python3`.

Внизу страницы вы увидите ссылки на скачивание установщиков. Есть возможность скачать python под 64-битную и 32-битную Windows.

![image](https://user-images.githubusercontent.com/125145037/224364226-d05f6bd9-8104-438f-8eea-7cef43b167d8.png)

Скачайте и запустите установщик Python3, он называется “python-3.****.exe”

На первом экране обязательно отметьте пункт “Add python.exe to PATH” и нажмите “Install Now”

![image](https://user-images.githubusercontent.com/125145037/224364939-b582e7a0-e120-43a6-95c9-2d373a089d22.png)

## Как проверить установился ли python

1. Запустите командую строку
2. Введите `python`

В результате командная строка выведет версию python, которая установлена в системе.

![image](https://user-images.githubusercontent.com/125145037/224366689-ed385299-9284-4bdc-8b6e-bdd20513fa87.png)

Если консоль была открыта до установки `python`, то её надо открыть заного, чтобы подцепилась новая запись в PATH.

А ещё лучше перезагрузить пк.

Также рекомендую на всякий случай проверить наличие “pip”

Для этого в командной строке наберите `pip --version`

![image](https://user-images.githubusercontent.com/125145037/224366908-b5b0e783-5d0d-426d-b9bd-0a33e5c8e5de.png)

Если выводит ошибку, это означает, что вы не нажали галочку на “Add python.exe to PATH”

Что бы это исправить, рекомендую зайти на сайт(https://okdk.ru/kak-dobavit-python-v-peremennuju-windows-path/)

На нем подробно представлены различные способы решения этой проблемы.

## Создание и активация виртуального окружения

Для создания виртуального окружения в командной строке набираем команду `python -m venv _имя окружения_`.

![image](https://user-images.githubusercontent.com/125145037/224368910-fde8f1aa-2f53-483d-b407-dc2d69efd18c.png)

Для активации используем команду `_имя окружения_\Scripts\activate`

![image](https://user-images.githubusercontent.com/125145037/224371241-b0ac93f0-8a93-433d-9b3a-23dd94b69658.png)

В `Windows PowerShell` может вылезти ошибка “Невозможно загрузить файл … , так как выполнение сценариев отключено в этой системе”.

Если такое произошло, то следует выполнить следующие действия:

- Запускаем терминал от админа.
- Пишем и запускаем: `Set-ExecutionPolicy RemoteSigned` или `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned`

## Установка и запуск pre-commit
### Установка pre-commit
Установите `pre-commit`, используя команду `pip install pre-commit` в командной строке.

Создайте `.pre-commit-config.yaml` файл в корневой папке вашего проекта и добавьте к нему `pre-commit` конфигурацию.

Вот пример базового `.pre-commit-config.yaml` файла:
```
repos:
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v0.812
    hooks:
      - id: mypy
        args: [--ignore-missing-imports, --strict-optional]  
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.0.1
    hooks:
      - id: end-of-file-fixer
      - id: trailing-whitespace
      - id: check-yaml 
```
В этом примере мы используем два `pre-commit` репозитория с их указанными версиями. Хук `mypy` из репозитория `pre-commit/mirrors-mypy` проверит аннотации типов в коде, а хуки `end-of-file-fixer`, `trailing-whitespace` и `check-yaml` из репозитория `pre-commit/pre-commit-hooks` исправят конец файла, завершающий пробел и проверят YAML файлы соответственно.   

### Запуск pre-commit

Активируйте свою виртуальную среду, набрав команду `_имя окружения_\Scripts\activate`.

Перейдите в корневой каталог вашего проекта, где находится `.pre-commit-config.yaml` файл.

Важно, чтобы `git репозиторий` был уже создан/склонирован.  

Введите команду `pre-commit run --all-files` и нажмите `enter` для запуска всех `pre-commit` хуков, указанных в файле конфигурации.

Так же нужно выполнить `pre-commit install` для автоматического запуска хуков при коммите.
