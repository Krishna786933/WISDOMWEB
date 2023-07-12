from django import template
import math
register = template.Library()
@register.simple_tag
def call_sellprice(price,discount):
    a = int(price)
    b = int(discount)
    if a is None or b is 0:
        return price
    sellprice = a
    sellprice = a - (a * b * 0.01)
    return math.ceil(sellprice)