from django.template import Library
register = Library()

@register.filter
def yuan(value):
    return '¥%s'% value


@register.filter
def mod_num(value,a):
    return value%a