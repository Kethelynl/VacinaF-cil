from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Sua conta {username}!, foi criada com sucesso!')
            return redirect('login')
        else:
            # Este bloco vai capturar erros de validação e permitir exibi-los no template
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        
        if u_form.is_valid:
            u_form.save()
            messages.success(request, 'Conta atualizada com sucesso!')
            return redirect('profile')
    
    else:
        u_form = UserUpdateForm(instance=request.user)
    
    return render(request, 'users/profile.html', {'u_form':u_form})

