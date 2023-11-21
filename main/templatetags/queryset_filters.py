from django import template

register = template.Library()

@register.filter
def zip_querysets(queryset1, queryset2):
    return zip(queryset1, queryset2)