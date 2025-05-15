# new-homework-task-3

### Настройка виртуальной среды:
- перейти в директорию проекта командой:
```shell
   cd new-homework-task-3
```
- создать виртуальную среду:
```shell
   python -m venv venv
```
- Активировать виртуальное окружение:

На Windows
```shell
   .venv\Scripts\activate
```
На macOS и Linux
```shell
   source .venv/bin/activate
```
- Установить все необходимые библиотеки:
```shell
  pip install -r requirements.txt 
```

## Запуск тестов:
#### Выполнить команду:
```shell
   pytest tests
```