from django import template

register = template.Library()

@register.filter(name='cut')#second way of registering template filter
def cut(value,arg):
    """
    This cuts out all values of 'arg' from string
    """
    return value.replace(arg,'')

# register.filter('cut',cut)#first way of registering template filter
