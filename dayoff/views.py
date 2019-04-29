from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.shortcuts import render, redirect

# Create your views here.
from dayoff.forms import RequestModelForm
from dayoff.models import DayOff

@login_required
def index(request):
    print("INDEX.html login by %s" %(request.user))
    data = []
    for detail in request.user.dayoff_set.all():
        data.append(
            {
                'type': detail.type,
                'reason': detail.reason,
                'date_start': detail.date_start,
                'date_end': detail.date_end,
                'approve_status': detail.approve_status,
            }
        )
    DayOffFormSet = formset_factory(RequestModelForm, max_num=len(data))
    context={}
    if request.method == "POST":
        formset = DayOffFormSet(request.POST)
    else:
        formset = DayOffFormSet(initial=data)
    context['formset'] = formset
    return render(request, 'dayoff/index.html', context)
def my_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            next_url = request.POST.get('next_url')
            if next_url:
                return redirect(next_url)
            else:
                if request.user.groups.filter(name="manager").exists():
                    return redirect('/admin/dayoff/dayoff/')
                return redirect('index')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong Username or Passsword'
    next_url = request.GET.get('next')
    if next_url:
        context['next_url'] = next_url
    return render(request, 'dayoff/login.html', context)

def my_logout(request):
    logout(request)
    return redirect('login')

@login_required
def request_form(request):
    print("REQUEST.html login by %s" % (request.user))
    if request.method == 'POST':
        form = RequestModelForm(request.POST)
        if form.is_valid():
            check = form.save(commit=False)
            check.create_by = request.user
            form.save()
            return redirect('index')
    else:
        form = RequestModelForm()
    context = {'form': form}
    return render(request, 'dayoff/request.html', context)
