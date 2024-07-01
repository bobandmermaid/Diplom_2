# Diplom_2

## Дипломный проект. Задание 2: API

### Тестирование API [Stellar Burgers](https://stellarburgers.nomoreparties.site/)

Созданы тесты API, покрывающие сценарии `Создание пользователя`, `Логин пользователя`, `Изменение данных пользователя`,`Создание заказа`, 
`Получение заказов конкретного пользователя`

Отчет Allure: `allure_results`

### Структура

- `tests` - Содержит тесты, разделенные по классам.
- `conftest.py` - Содержит фикстуры, используемые в тестах.
- `data.py` - Содержит константы.

### Запуск автотестов

1. **Установка зависимостей**

    ```bash
     pip install -r requirements.txt
    ```

2. **Запуск автотестов и создание Allure-отчета**

    ```bash
    pytest -v tests --alluredir allure_results && allure serve allure_results
    ```