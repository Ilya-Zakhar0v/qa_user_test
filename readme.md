## Установка
```shell
~ >>> cd qaa_test_user_project
~ >>> python3 -m venv venv
~ >>> source venv/bin/activate
~ >>> pip3 install -r requirements.txt
~ >>> cp .env-example .env
~ >>> nano .env  # Здесь вы обязательно должны указать ваш SERVICE_URL='https://petstore.swagger.io/v2'
```

## Запуск
```shell
~ >>> pytest tests/test_user.py -s -v --alluredir tests_results # запуск тестов
~ >>> allure serve tests_results # просмотреть отчет о пройденных тестах
```