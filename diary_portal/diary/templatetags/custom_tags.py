from django import template

register = template.Library()

@register.simple_tag
def setvar(val=None):
    return val

@register.simple_tag
def changevar(val):
    if var == "True":
        return "False"
    else:
        return "True"
