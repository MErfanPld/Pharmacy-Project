from django import template

register = template.Library()

@register.filter
def sum_price(order_items):
    total = 0
    for item in order_items:
        total += item.price * item.quantity
    return total
