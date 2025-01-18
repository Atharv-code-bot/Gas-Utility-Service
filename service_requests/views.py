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
            service_request.customer = request.user  # Associate with the logged-in user
            service_request.save()
            return redirect('track_request')  # Redirect to the tracking page after submission
    else:
        form = RequestForm()
    return render(request, 'requests/create_request.html', {'form': form})


@login_required
def track_request_view(request):
    # Fetch all service requests for the logged-in user
    service_requests = ServiceRequest.objects.filter(customer=request.user)

    # Render the tracking page with the service requests
    return render(request, 'requests/track_request.html', {'service_requests': service_requests})
