#
# Copyright Cameron Curry (c) 2017
#

from rest_framework.test import APITestCase

from nabla_core.models import QTAccount
from nabla_core.models import QTBalance


class TestQTBalanceView(APITestCase):

    def setUp(self):
        qt_account1 = QTAccount.objects.create(type='Margin',
                                               number=26598146,
                                               status='Active',
                                               primary=True,
                                               client_account_type='Individual')
        qt_account2 = QTAccount.objects.create(type='Margin',
                                               number=26598147,
                                               status='Active',
                                               primary=True,
                                               client_account_type='Individual')
        QTBalance.objects.create(qt_account=qt_account1,
                                 type='COMBINED',
                                 currency='USD',
                                 cash=198259.05,
                                 market_value=53745,
                                 total_equity=252004.05,
                                 buying_power=461013.3)
        QTBalance.objects.create(qt_account=qt_account2,
                                 type='COMBINED',
                                 currency='USD',
                                 cash=198259.05,
                                 market_value=53745,
                                 total_equity=252004.05,
                                 buying_power=461013.3)

    def test_summary(self):
        response = self.client.get('/api/qt-balance/summary')
        self.assertEqual(response.data, {'USD': 504008.1})
