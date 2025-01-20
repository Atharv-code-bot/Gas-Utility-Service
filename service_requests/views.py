from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RequestForm
from .models import ServiceRequest
from django.contrib.auth.decorators import user_passes_test

@login_required
def create_request_view(request):
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('track_request')
    else:
        form = RequestForm()
    return render(request, 'requests/create_request.html', {'form': form})


@login_required
def track_request_view(request):

    service_requests = ServiceRequest.objects.filter(customer=request.user)

    
    return render(request, 'requests/track_request.html', {'service_requests': service_requests})
