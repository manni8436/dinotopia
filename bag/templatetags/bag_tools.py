from django import template


register = template.Library()

@register.filter(Name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
