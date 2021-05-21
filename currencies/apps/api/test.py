from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.test import TestCase
from apps.api.models import CurencyFormat
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class CurrencyFormatTestCase(TestCase):
    '''
    Class to Test CurencyFormat model
    '''

    def test(self):
        currency_format_obj = CurencyFormat(country="EC", currency_symbol="$", currency_code="USD",
                                            currency_nomenclature="code", currency_symbol_pos="pos", cents_enabled=True, display_format="#,###.##")
        self.assertEqual(currency_format_obj.country, "EC")
        self.assertEqual(currency_format_obj.currency_symbol, "$")
        self.assertEqual(currency_format_obj.currency_code, "USD")
        self.assertEqual(currency_format_obj.currency_nomenclature, "code")
        self.assertEqual(currency_format_obj.currency_symbol_pos, "pos")
        self.assertEqual(currency_format_obj.cents_enabled, True)
        self.assertEqual(currency_format_obj. display_format, "#,###.##")


class ApiTestCase(APITestCase):
    def setUp(self):
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()
        self.client.defaults['HTTP_AUTHORIZATION'] = 'Token {}'.format(
            self.token.key)

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            'test',
            email='testuser@test.com',
            password='test'
        )

    def test_currency_format(self):
        '''
        Testing Currency format viewset
        '''
        # get obj, empty
        res = self.client.get('/api/v1/currency/', {
            "country": "Argentina",
            "currency": "USD",
        })
        self.assertEqual(res.status_code, 404)
        # create obj, worng parameters
        res = self.client.post('/api/v1/currency/', {
            "worng": "Argentina",
            "worng2": "USD",
        }, format='json')
        self.assertEqual(res.status_code, 403)
        # create obj, correct parameters
        res = self.client.post('/api/v1/currency/', {
            "country": "Argentina",
            "currency_code": "USD",
            "currency_nomenclature": "code",
            "currency_symbol_pos": "after",
            "cents_enabled": "True",
            "display_format": "#.###,##"
        }, format='json')
        self.assertEqual(res.status_code, 200)
        # get obj, exists
        res = self.client.get('/api/v1/currency/', {
            "country": "Argentina",
            "currency_code": "USD",
        }, format='json')
        self.assertEqual(res.status_code, 200)
        # need extend test for this