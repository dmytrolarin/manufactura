from django import template
from for_user.models import RestaurantInfo

register = template.Library()
@register.simple_tag()
def get_rest_info():
    return RestaurantInfo.objects.all()[0]