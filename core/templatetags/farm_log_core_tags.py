from django import template
from django.core.urlresolvers import NoReverseMatch, reverse
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe
from core.utils import get_summary as coreGetSummary
from core.models import get_affinity_state

register = template.Library()

@register.filter
def get_full_affinity_state(affinity):
    return get_affinity_state(affinity)

@register.filter
def get_time(dateTime):
    return dateTime.strftime('%H:%m:%S')

@register.filter
def get_summary(fullText):
    return coreGetSummary(fullText, '')

@register.simple_tag
def farm_log_login(request):
    """
    Include a login snippet if REST framework's login view is in the URLconf.
    """
    try:
        login_url = reverse('admin:login')
    except NoReverseMatch:
        return ''

    snippet = """<li role="presentation">
                    <a class="btn btn-lg"  href='{href}?next={next}'>Log in</a></li>"
                 </li>"""
    snippet = format_html(snippet, href=login_url, next=escape(request.path))

    return mark_safe(snippet)


@register.simple_tag
def farm_log_logout(request, user):
    try:
        logout_url = reverse('admin:logout')
    except NoReverseMatch:
        snippet = format_html('<li class="navbar-text">{user}</li>', user=escape(user))
        return mark_safe(snippet)
    snippet = """<li role="presentation" class="dropdown">
                            <a class="dropdown-toggle btn btn-lg" data-toggle="dropdown"
                               role="button"
                               aria-expanded="false">
                               {user}
                                <b class="caret"></b>
                            </a>
                            <ul class="dropdown-menu nav-submenu" role="menu">
                                <li role="presentation">
                                    <a class="btn btn-lg" href='{href}?next={next}'>Log out</a></li>
                                </li>
                            </ul>
                        </li>"""
    snippet = format_html(snippet, user=escape(user), href=logout_url, next=escape(request.path))

    return mark_safe(snippet)
