from django.shortcuts import render
from heating_control.forms import ScheduleForm
from heating_control.models import Usage
from heating_control.models import ScheduledEvent, Usage
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def toggle_form(request):

    # Save the new event if one has been posted
    if request.method == "POST":
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()

    # Check for the latest usage value
   
    latest_usage = Usage.objects.order_by("date").last()
    

    if latest_usage:
        latest_status = latest_usage.is_on
    else:
        latest_status = None

    scheduled_events = ScheduledEvent.objects.filter(completed=False).order_by(
        "start_time"
    )

    return render(
        request,
        "toggle_form.html",
        {
            "latest_status": latest_status,
            "form": ScheduleForm,
            "scheduled_events": scheduled_events,
        },
    )

@login_required
def toggle_btn(request):
    event = ScheduledEvent()
    event.save()
    return redirect(toggle_form)

