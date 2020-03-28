from django.views.generic import TemplateView

class LandingView(TemplateView):
    template_name = "live/landing.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        return ctx
