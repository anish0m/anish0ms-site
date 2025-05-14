from django import template

register = template.Library()

@register.filter
def render_stars(rating):
    full_stars = int(rating)
    half_star = 1 if (rating - full_stars) >= 0.5 else 0 
    empty_stars = 5 - full_stars - half_star

    stars_html = (
        '<i class="bi bi-star-fill"></i>' * full_stars +
        '<i class="bi bi-star-half"></i>' * half_star +
        '<i class="bi bi-star"></i>' * empty_stars
    )
    return stars_html