import os
import requests
import logging
from dotenv import load_dotenv
from data.user.user_data import UserData
from pydantic import ValidationError
from schemas.user import CreateUserModel, UpdateUserModel
from typing import Type, Any
from schemas.user import T


load_dotenv()


class User:
    def __init__(self):
        self.url = os.getenv('SERVICE_URL')
        self.logger = logging.getLogger("api")
        self.body_data = UserData.BODY_DATA
        self.headers = UserData.headers

    USER = '/user/'

    def validate_json(self, response_json: Any, model: Type[T]) -> T:
        try:
            return model.model_construct(**response_json)
        except ValidationError as e:
            print("Response validation error:", e.json())
            raise

    def create_user(self, headers: dict, body: dict):
        try:
            response = requests.post(f'{self.url}{self.USER}', headers=headers, json=body)
            self.validate_json(response.json(), CreateUserModel)
            self.logger.info(response.text)
            return response
        except requests.exceptions.RequestException as err:
            self.logger.error(f"API request error: {err}")
            return None
        except ValidationError as e:
            self.logger.error(f"Response validation error: {e.json()}")
            return None

    def get_user(self, headers: dict, params: str):
        try:
            response = requests.get(f'{self.url}{self.USER}{params}', headers=headers)
            self.logger.info(response.text)
            return response
        except requests.exceptions.RequestException as err:
            print("Некорректный запрос", err)
            return None

    def update_user(self, headers: dict, body: dict, params: str):
        try:
            response = requests.put(f'{self.url}{self.USER}{params}', headers=headers, json=body)
            self.validate_json(response.json(), UpdateUserModel)
            self.logger.info(response.text)
            return response
        except requests.exceptions.RequestException as err:
            print("Некорректный запрос", err)
            return None

    def delete_user(self, headers: dict, params: str):
        try:
            response = requests.delete(f'{self.url}{self.USER}{params}', headers=headers)
            self.logger.info(response.text)
            return response
        except requests.exceptions.RequestException as err:
            print("Некорректный запрос", err)
            return None

