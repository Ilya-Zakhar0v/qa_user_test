import pytest
from endpoints.user.api import User
import pytest_check as check
import allure

# master

@allure.feature('User Management')
@pytest.mark.usefixtures("user_name")
class TestUser:

    user = User()

    @allure.story('Create User')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("body_data, expected_status_code", [
        ({"username": "user1", "firstName": "FirstName1", "lastName": "LastName1", "email": "email1@example.com",
          "password": "", "phone": 89997775544, "userStatus": '1'}, 400),
        # Ожидаем 400 из-за неправильного пароля и значения int в ключе phone
        ({"username": "user2", "firstName": "FirstName2", "lastName": "LastName2", "email": "email2@example.com",
          "password": "password2", "phone": "222-222-2222", "userStatus": 2}, 200),
        ({"username": "user3", "firstName": "FirstName3", "lastName": "LastName3", "email": "email3@example.com",
          "password": "password3", "phone": "333-333-3333", "userStatus": 3}, 200)
    ])
    def test_create_user(self, body_data, expected_status_code):
        """ Тестирование эндпоинта создания пользователя """

        body_data_merged = self.user.body_data.copy()
        body_data_merged.update(body_data)

        res = self.user.create_user(self.user.headers, body_data_merged)

        with allure.step(f'Check response code equals {expected_status_code}'):
            check.equal(res.status_code, expected_status_code,
                        f"Expected status code was {expected_status_code}, but got {res.status_code}")

            if expected_status_code == 200:
                with allure.step('Check JSON code in response equals 200'):
                    check.equal(res.json()['code'], 200, "Expected JSON response code 200, but got an error")

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



