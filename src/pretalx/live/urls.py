from django.conf.urls import include, url

from pretalx.event.models.event import SLUG_CHARS

from .views import landing


app_name = "live"
urlpatterns = [
    url(
        fr"^(?P<event>[{SLUG_CHARS}]+)/",
        include(
            [
                url("^live/$", landing.LandingView.as_view(), name="live.landing"),
            ]
        ),
    ),
]
