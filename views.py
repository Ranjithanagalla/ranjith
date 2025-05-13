

from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import UserLogin, Title

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            Title.objects.create(user=user, title_text="Welcome to our django's page")
            request.session['user_id'] = user.id
            return redirect('title')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def title_view(request):
    user_id = request.session.get('user_id')
    if user_id:
        title = Title.objects.filter(user_id=user_id).first()
        return render(request, 'accounts/title.html', {'title': title})
    return redirect('login')
