from django.urls import reverse_lazy
from django.views import generic

from src.apps.refugio.forms import MascotaForm
from src.apps.refugio.models import Mascota


class MascotaListview(generic.ListView):
    template_name = 'refugio/mascota_list.html'
    queryset = Mascota.objects.select_related('persona').prefetch_related('vacunas').all()


class MascotaDetailView(generic.DetailView):
    template_name = 'refugio/mascota_detail.html'
    queryset = Mascota.objects.select_related('persona').prefetch_related('vacunas').all()


class MascotaCreateView(generic.CreateView):
    template_name = 'refugio/mascota_form.html'
    form_class = MascotaForm
    success_url = reverse_lazy('mascota_list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'Registrar mascota'
        return ctx


class MascotaUpdateView(generic.UpdateView):
    template_name = 'refugio/mascota_form.html'
    form_class = MascotaForm
    model = Mascota
    success_url = reverse_lazy('mascota_list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'Actualizar mascota'
        return ctx


class MascotaDeleteView(generic.DeleteView):
    template_name = 'refugio/mascota_confirm_delete.html'
    model = Mascota
    success_url = reverse_lazy('mascota_list')
