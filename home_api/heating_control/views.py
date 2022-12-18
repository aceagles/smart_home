from django.shortcuts import render
from heating_control.forms import ScheduleForm
from heating_control.models import Usage
from heating_control.models import ScheduledEvent, Usage, AggUsage
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta


def total_usage(delta):
    now = timezone.now()
    pre_time = now - delta
    usages = AggUsage.objects.filter(start_time__gte = pre_time)
    secs = 0
    for use in usages:
        delta = use.end_time - use.start_time
        secs += delta.total_seconds()
    return timedelta(seconds=secs)


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
    
    usage_history = {
        "today": total_usage(timezone.now() - timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)),
        "7days": total_usage(timedelta(days=7)),
        
    }
    usage_history["7dayAvg"] = usage_history["7days"]/7

    if latest_usage:
        latest_status = latest_usage.is_on
    else:
        latest_status = None

    scheduled_events = ScheduledEvent.objects.filter(completed=False, deleted=False).order_by(
        "start_time"
    )



    return render(
        request,
        "toggle_form.html",
        {
            "latest_status": latest_status,
            "form": ScheduleForm,
            "scheduled_events": scheduled_events,
            "usage_history": usage_history
        },
    )

@login_required
def toggle_btn(request):
    event = ScheduledEvent()
    event.save()
    return redirect(toggle_form)

@login_required
def del_event(request, pk):
    obj = ScheduledEvent.objects.get(pk=pk)
    obj.repeat = "None"
    obj.del_sched()
    return redirect(toggle_form)

