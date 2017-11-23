#
# Copyright Cameron Curry (c) 2017
#

from unittest.mock import patch
from rest_framework.test import APITestCase

from nabla_core.models import QTAccess


class TestQTAccessView(APITestCase):

    def setUp(self):
        self.qt_access = QTAccess.objects.create(scope=QTAccess.account_data_scope_entry(),
                                                 refresh_token='aSBe7wAAdx88QTbwut0tiu3SYic3ox8F')

    def test_get(self):
        response = self.client.get('/api/qt-access')

        self.assertEqual(len(response.data), 1)
        expected_response = (
            (response.data[0]['id'], str(self.qt_access.id)),
            (response.data[0]['scope'], QTAccess.account_data_scope_entry()),
            (response.data[0]['refresh_token'], 'aSBe7wAAdx88QTbwut0tiu3SYic3ox8F')
        )
        for result, expected in expected_response:
            with self.subTest(result=result):
                self.assertEqual(result, expected)

    @patch('questrade.access.QTAccessService.refresh')
    def test_put(self, mock):
        mock.return_value.access_token = 'C3lTUKuNQrAAmSD/TPjuV/HI7aNrAwDp'
        mock.return_value.token_type = 'Bearer'
        mock.return_value.expires_in = 300
        mock.return_value.refresh_token = 'aSBe7wAAdx88QTbwut0tiu3SYic3ox8F'
        mock.return_value.api_server = 'https://api01.iq.questrade.com'

        response = self.client.put('/api/qt-access/{}'.format(self.qt_access.id))
        expected_response = (
            (response.data['id'], str(self.qt_access.id)),
            (response.data['scope'], QTAccess.account_data_scope_entry()),
            (response.data['access_token'], 'C3lTUKuNQrAAmSD/TPjuV/HI7aNrAwDp'),
            (response.data['refresh_token'], 'aSBe7wAAdx88QTbwut0tiu3SYic3ox8F'),
            (response.data['api_server'], 'https://api01.iq.questrade.com')
        )
        for result, expected in expected_response:
            with self.subTest(result=result):
                self.assertEqual(result, expected)

    def test_delete(self):
        self.client.delete('/api/qt-access/{}'.format(self.qt_access.id))
        self.assertEqual(len(QTAccess.objects.all()), 0)
