from django.views.generic import TemplateView

class LandingView(TemplateView):
    template_name = "live/landing.html"

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        # adjust Content-Security-Policy for arbitrary ext. iframe content
        response._csp_update = {"child-src": 'https:'}
        return response

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        return ctx
