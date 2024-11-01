import json
from django.http import JsonResponse
from django.core.mail import send_mail
from django.http import HttpResponse
from django.urls import reverse
from django.core.paginator import Paginator
from .models import Vaccines, MarcVaccine
from .forms import VaccineForm, MarcVaccineForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# pagina de entrada
def home(request):
    return render(request, "vaccines/home.html" )

def about(request):
    return render(request, "vaccines/about.html" )

def is_admin(user):
    return user.is_staff

# admin registra uma nova vacina
@user_passes_test(is_admin)
def register_vaccine(request):
    if request.method == "POST":
        form = VaccineForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = VaccineForm()
    return render(request, 'vaccines/register_vaccines.html', {'form':form})


#admin update vacina
class VaccineUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Vaccines
    fields = ['name_vacinne', 'description' , 'age_group', 'doses']
    template_name = 'vaccines/register_vaccines.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        #verifica se o usuário tem permissão
        return self.request.user.is_staff
    
    def get_success_url(self):
        return reverse('vaccine-detail', args=[self.object.pk])

# admin deleta vacina
class VaccineDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Vaccines
    template_name = 'vaccines/confirm_delete.html'
    success_url = 'vaccines/list_vaccines.html'
    
    def test_func(self):
        return self.request.user.is_staff
    
    
# barra de pesquisa e lista
@login_required
def list_vaccines(request):
    query = request.GET.get('search')
     
    # filtro de pequisa
    if query:
        vaccines_search = Vaccines.objects.filter(name_vacinne__icontains=query)
        print(f"Query: {query}, Resultados: {vaccines_search}")  
    else:
        vaccines_search = Vaccines.objects.all()
        
    # sistema de paginação
    paginator = Paginator(vaccines_search, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    
    context = {
        'vaccines_search':vaccines_search,
        'page_obj':page_obj,
    }
    
    return render(request, 'vaccines/list_vaccines.html', context)


#ver datalhe das vacinas
class VaccinesDetail(DetailView):
    model = Vaccines
    template_name = 'vaccines/detail_vaccines.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vaccine'] = self.object  # Isso garante que `vaccine` está disponível no template
        return context

@login_required
def formScheduledVacina(request):
    if request.method == "POST":
        form = MarcVaccineForm(request.POST)
        
        if form.is_valid():
            marc_vaccine = form.save(commit=False)
            marc_vaccine.user = request.user
            marc_vaccine.save()
            return redirect('scheduled_vaccine')
    else:
        form = MarcVaccineForm()
    return render(request, 'vaccines/form_marc_vaccine.html', {'form': form})

@login_required
def vaccinesScheduled(request):
     scheduled = MarcVaccine.objects.filter(user=request.user).select_related('vaccines').order_by('-next_dose')  
     
     # sistema de paginação
     paginator = Paginator(scheduled, 6)
     page_number = request.GET.get('page')
     page_obj = paginator.get_page(page_number)
     
     context ={
         'scheduled':scheduled,
         'page_obj':page_obj,
     }
     return render(request, 'vaccines/scheduled_vaccine.html', context)

@login_required
def calendar_vaccines(request):
    allevents = MarcVaccine.objects.filter(user=request.user)
    return render(request, 'vaccines/calendar.html', {'allevents':allevents})

@user_passes_test
def allevents(request):
    allevents = MarcVaccine.objects.filter(user=request.user)
    out=[]
    for marcacao in allevents:
        out.append({
            'title': marcacao.vaccines.name_vacinne,  # Nome da vacina
            'start': marcacao.next_dose.strftime('%Y-%m-%d'),
        })
    return JsonResponse(out, safe=False)

