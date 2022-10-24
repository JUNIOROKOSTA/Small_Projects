from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FormContaro


def login(request):
    if request.method != 'POST':
        return render(request, template_name='accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'Usuário ou senha inválidos')
        return render(request, template_name='accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Login efetuado com sucesso!!!')
        return redirect('dashboard')


def logout(request):
    auth.logout(request)
    return redirect('login')


def cadastro(request):
    if request.method != 'POST':
        return render(request, template_name='accounts/cadastro.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    conf_senha = request.POST.get('conf_senha')

    if not nome or not sobrenome or not email or not usuario or not senha or not conf_senha:
        messages.error(request, 'Todos os campos devem ser preenchidos.')
        return render(request, template_name='accounts/cadastro.html')

    try:
        validate_email(email)

    except Exception as e:
        messages.error(request, 'Email inválidado.')
        return render(request, template_name='accounts/cadastro.html')

    if len(senha) < 6:
        messages.error(request, 'Senha deve ter mais de 6 caracteres.')
        return render(request, template_name='accounts/cadastro.html')

    if len(usuario) < 6:
        messages.error(request, 'Usuário deve ter mais de 6 caracteres.')
        return render(request, template_name='accounts/cadastro.html')

    if senha != conf_senha:
        messages.error(request, 'Senhas devem ser iguais.')
        return render(request, template_name='accounts/cadastro.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Já existe esse usuário cadastrado.')
        return render(request, template_name='accounts/cadastro.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Já existe esse E-mail cadastrado.')
        return render(request, template_name='accounts/cadastro.html')

    messages.success(request, 'Registrado com sucesso!!!')

    user = User.objects.create_user(username=usuario, email=email,
                                    password=senha, first_name=nome, last_name=sobrenome)
    user.save()

    return redirect('login')


@login_required(redirect_field_name='login')
def dashboard(request):
    if request.method != 'POST':
        form = FormContaro()
        return render(request, 'accounts/dashboard.html', {'form': form})

    form = FormContaro(request.POST, request.FILES)

    if not form.is_valid():
        messages.warning(request, 'Erro nos dados do formulário.')
        form = FormContaro(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})

    form.save()
    messages.success(
        request, f'Contato {request.POST.get("nome")} {request.POST.get("sobrenome")}, Foi registrado na agenda. ')
    return redirect('dashboard')
