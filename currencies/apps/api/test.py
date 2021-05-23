from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory

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

    def test_currency_format_(self):
        '''
        Testing Currency format viewset
        '''
        # get obj, empty
        get_empty = self.client.get('/api/v1/currency_query/', {
            "country": "Argentina",
            "currency": "USD",
        })
        self.assertEqual(get_empty.status_code, 404)
        # create obj, correct parameters
        create = self.client.post('/api/v1/currency/', {
            "country": "Argentina",
            "currency_code": "USD",
            "currency_nomenclature": "code",
            "currency_symbol_pos": "after",
            "cents_enabled": "True",
            "display_format": "#.###,##"
        }, format='json')
        self.assertEqual(create.status_code, 200)
        create = self.client.post('/api/v1/currency/', {
            "country": "Argentina2",
            "currency_code": "USD",
            "currency_nomenclature": "code",
            "currency_symbol_pos": "after",
            "cents_enabled": "True",
            "display_format": "#.###,##"
        }, format='json')
        self.assertEqual(create.status_code, 200)
        # list obj
        get = self.client.get('/api/v1/currency/')
        self.assertEqual(get.status_code, 200)
        # get obj, exists
        get_exists = self.client.get('/api/v1/currency_query/', {
            "country": "Argentina",
            "currency": "USD",
        })
        self.assertEqual(get_exists.status_code, 200)
        # update obj
        up = self.client.put(f"/api/v1/currency/1/", {
            "country": "Argentina",
            "currency_code": "USD",
            "currency_symbol": "USDModified",
            "currency_nomenclature": "code",
            "currency_symbol_pos": "after",
            "cents_enabled": "True",
            "display_format": "#.###,##"
        }, format='json')
        self.assertEqual(up.status_code, 200)
        # delete obj
        delete = self.client.delete(f"/api/v1/currency/1/", {
        }, format='json')
        self.assertEqual(delete.status_code, 200)
