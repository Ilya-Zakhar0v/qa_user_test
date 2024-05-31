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
    @pytest.mark.parametrize("user_data, expected_status", [
        ({"id": 1, "username": "user1", "firstName": "Test", "lastName": "User", "email": "testuser1@example.com",
          "password": "pass1", "phone": "1234567890", "userStatus": 1}, 200),
        ({"id": 2, "username": "user2", "firstName": "Example", "lastName": "User", "email": "testuser2@example.com",
          "password": "pass2", "phone": "0987654321", "userStatus": 1}, 404),
        # Добавьте дополнительные наборы данных с разными ожидаемыми результатами
    ])
    def test_update_user(self, user_data, expected_status):
        """ Тестирование эндпоинта обновления данных пользователя по его username """

        res = self.user.update_user(headers=self.user.headers, body=user_data, params=user_data['username'])

        with allure.step(f'Check status code equals {expected_status}'):
            check.equal(res.status_code, expected_status,
                        f"Expected status code {expected_status}, but got {res.status_code}")

    @allure.story('Delete User')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.parametrize("user_name, expected_status", [("user1", 200), ("user2", 404), ("user3", 404)])
    def test_delete_user(self, user_name, expected_status):
        """ Тестирование эндпоинта удаления пользователя по его username """

        res = self.user.delete_user(headers=self.user.headers, params=user_name)
        with allure.step(f'Check status code equals {expected_status}'):
            check.equal(res.status_code, expected_status, f"Expected status {expected_status}, got {res.status_code}")



