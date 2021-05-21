from django.test import TestCase
from apps.api.models import CurencyFormat
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class CurrencyFormatTestCase(TestCase):
    '''
    Class to Test CurencyFormat model
    '''

    def test(self):
        logging.info("Starting Test CurencyFormat model...")
        currency_format_obj = CurencyFormat(country="EC", currency_symbol="$", currency_code="USD",
                                            currency_nomenclature="code", currency_symbol_pos="pos", cents_enabled=True, display_format="#,###.##")
        self.assertEqual(currency_format_obj.country, "EC")
        self.assertEqual(currency_format_obj.currency_symbol, "$")
        self.assertEqual(currency_format_obj.currency_code, "USD")
        self.assertEqual(currency_format_obj.currency_nomenclature, "code")
        self.assertEqual(currency_format_obj.currency_symbol_pos, "pos")
        self.assertEqual(currency_format_obj.cents_enabled, True)
        self.assertEqual(currency_format_obj. display_format, "#,###.##")

