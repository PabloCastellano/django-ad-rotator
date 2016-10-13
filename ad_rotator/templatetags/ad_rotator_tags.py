"""Template tags for the ``ad_rotator`` app."""
import random

from django import template
from django.utils.timezone import now

from .. import models

register = template.Library()


@register.inclusion_tag('ad_rotator/partials/banner.html')
def get_banner(size):
    """
    Returns a random ``BannerAd`` instance.

    Usage:
    {% load ad_rotator_tags %}
    {% get_banner 'leaderboard' %}

    """
    banner = None

    banners = models.BannerAd.objects.filter(
        start_date__lte=now().date(),
        end_date__gte=now().date(),
        size=size)

    if banners.count():
        banner = random.choice(banners)

    return {'banner': banner}
