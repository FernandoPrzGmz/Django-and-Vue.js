from django.views import generic

class VueView(generic.TemplateView):
    template_name = 'vue/index.html'
