import pytest
from endpoints.user.api import User
import pytest_check as check
import allure


@allure.feature('User Management')
@pytest.mark.usefixtures("user_name")
class TestUser:

    user = User()

    @allure.story('Create User')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user(self):
        """ Тестирование эндпоинта создания пользователя """

        res = self.user.create_user(self.user.headers, self.user.body_data)

        with allure.step('Check response code equals 200'):  # Добавляем шаг в отчет
            check.equal(res.json()['code'], 200, "err")

        with allure.step('Check status code equals 200'):
            check.equal(res.status_code, 200, "status code error")

    @allure.story('Get User Info')
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_user(self, user_name):
        """ Тестирование эндпоинта получения пользователя по его username """

        res = self.user.get_user(headers=self.user.headers, params=self.user_name)

        with allure.step('Check status code equals 200'):
            check.equal(res.status_code, 200, "status code error")

    @allure.story('Update User')
    @allure.severity(allure.severity_level.NORMAL)
    def test_update_user(self, user_name):
        """ Тестирование эндпоинта обновления данных пользователя по его username """

        json_data = {
            "id": 0,
            "username": "string",
            "firstName": "string",
            "lastName": "string",
            "email": "string",
            "password": "string",
            "phone": "string",
            "userStatus": 0
        }

        res = self.user.update_user(headers=self.user.headers, body=json_data, params=self.user_name)

        with allure.step('Check status code equals 200'):
            check.equal(res.status_code, 200, "status code error")

    @allure.story('Delete User')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.parametrize("user_name, expected_status", [("user1", 200), ("user2", 404), ("user3", 404)])
    def test_delete_user(self, user_name, expected_status):
        """ Тестирование эндпоинта удаления пользователя по его username """

        res = self.user.delete_user(headers=self.user.headers, params=user_name)
        with allure.step(f'Check status code equals {expected_status}'):
            check.equal(res.status_code, expected_status, f"Expected status {expected_status}, got {res.status_code}")



