from django import template

register = template.Library()
@register.filter(name='split')
def split(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return arg.split('l')

# register.filter('cut',cut)
