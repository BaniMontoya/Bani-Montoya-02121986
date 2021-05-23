from django.db import models


class CurencyFormat(models.Model):
    '''
    Class to manage records about relation currency and country, also options of display data.
    @autor Bani Montoya 05/2021
    '''
    '''
    filter data
    '''
    country = models.CharField(max_length=10)
    currency_symbol = models.CharField(max_length=30)
    currency_code = models.CharField(max_length=30)
    '''
    options data
    '''
    # Currency can display currency code or symbol
    currency_nomenclature = models.CharField(max_length=30)
    # Currency can be shown after or before price
    currency_symbol_pos = models.CharField(max_length=30)
    cents_enabled = models.BooleanField(
        default=False)  # Show cents or no cents
    # Display formats such as #,###.## or #.###,##
    display_format = models.CharField(max_length=30)
    
    class Meta:
        unique_together = ('country', 'currency_code',)
        