import unittest

from werkzeug.test import TestResponse
from api.service.cpf_service import CPFService

from app import app


class CPFTest(unittest.TestCase):
    def setUp(self) -> None:
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_free_cpf(self):
        # Given
        cpf = '00000000000'

        # When
        response: TestResponse = self.client.get(
            f'{cpf}', follow_redirects=True)

        # Then
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['status'], 'FREE')

    def test_block_cpf(self):
        # Given
        cpf = '12345678901'

        # When
        response: TestResponse = self.client.get(
            f'{cpf}', follow_redirects=True)

        # Then
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['status'], 'BLOCK')

    def test_bad_request(self):
        # Given
        cpf = '123'

        # When
        response: TestResponse = self.client.get(
            f'{cpf}', follow_redirects=True)

        # Then
        self.assertEqual(response.status_code, 400)
