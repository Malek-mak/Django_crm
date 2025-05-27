from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .Forms import SignUpForm, addRecord
from .models import record

# Create your views here.
def index(request):
    records = record.objects.all
    #logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #cheking if user is real
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in')
            return redirect('index')
        else:
            messages.success(request, 'There was an error, try again.')
            return redirect('index')
    else: 
        return render(request, 'index.html', {'records': records})



def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid() :
            form.save()
            # log them in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            messages.success(request, 'You have succefully registerd')
            return redirect('index')
            
            
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    
    return render(request, 'register.html', {'form':form})


def customer_record(request, pk):
    if request.user.is_authenticated :
        customer_record = record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else :
        messages.success(request, 'You must be logged in')
        return redirect('index')
            
            
def delete_record(request, pk):
    if request.user.is_authenticated :
        delete_record = record.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, 'Customer deleted succusfully')
        return redirect('index') 
    else: 
        messages.success(request, 'You must be logged in')
        return redirect('index')
    
    
def add_record(request):
    if request.user.is_authenticated :
        if request.method == 'POST':
            customer = addRecord(request.POST)
            if customer.is_valid() :
                customer.save()
                messages.success(request, 'Recored added')
                return redirect('index')
        else :

            customer = addRecord()
            return render(request, 'add_record.html', {'customer': customer})
    else:
        return redirect('index')
    
    return render(request, 'add_record.html', {'customer': customer})
        
        
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = record.objects.get(id = pk)
        form = addRecord(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'update_record.html', {'form': form})
        
    else:
        return redirect('index')