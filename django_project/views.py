from django.shortcuts import render, redirect
from .models import Ticket,Region
from .forms import HistoryFilterForm
from datetime import datetime

def home(request):
    if request.method == 'POST':
        time_str = request.POST['time']
        street_address = request.POST['street_address']
        region_id = request.POST['region']

        time = datetime.strptime(time_str, '%Y-%m-%dT%H:%M')
        day = time.strftime('%A')  # Get the day of the week

        region = Region.objects.get(pk=region_id)

        ticket = Ticket(time=time, day=day, region=region, street_address=street_address)
        ticket.save()

        return redirect('home')  # Redirect to the Home page

    regions = Region.objects.all()
    return render(request, 'home.html', {'regions': regions})

def history(request):
    if request.method == 'POST':
        form = HistoryFilterForm(request.POST)
        if form.is_valid():
            region_id = form.cleaned_data['region'].id
            day = form.cleaned_data['day']

            tickets = Ticket.objects.filter(region=region_id, day=day)
            return render(request, 'history.html', {'tickets': tickets, 'form': form})

    form = HistoryFilterForm()
    return render(request, 'history.html', {'form': form})
