import datetime
from django import template

register = template.Library()

#@register.simple_tag(takes_context=True)
#def get_now(context, format_string):
#    timezone = context['timezone']
#    return datetime.datetime.now(timezone, format_string)

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)

#@register.simple_tag
#def get_today(request):
#    return tz.localtime(tz.now()).date()