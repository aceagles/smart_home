from django.shortcuts import render
from heating_control.forms import ScheduleForm
from heating_control.models import Usage
from heating_control.models import ScheduledEvent, Usage
from django.shortcuts import redirect
import json
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.
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


def toggle_btn(request):
    event = ScheduledEvent()
    event.save()
    return redirect(toggle_form)

@csrf_exempt
def update_usage(request):
    if request.method == 'POST':
        #Store the new usage
        print(request.body)
        data = json.loads(request.body)
        new_usage = Usage(is_on= data['is_on'])
        new_usage.save()
    
        # Get all incomplete tasks in the past
        print(timezone.now())
        events = ScheduledEvent.objects.filter(completed=False, start_time__lte=timezone.now()).order_by('start_time')
        events = [event for event in events]
        print(events)
        toggle = False
        if events:
            # Get the latest event
            latest_event = events.pop()

            #Delet the rest
            for event in events:
                event.delete()
            
            #Latest Event has been completed
            latest_event.completed = True
            latest_event.save()

            #Evaluate if a toggle is required
            if latest_event.command == ScheduledEvent.TOG:
                toggle = True
            else:
                # on command boolean if command to turn on
                on_cmd = latest_event.command == ScheduledEvent.ON
                # toggle if command doesn't match status
                toggle = on_cmd != new_usage.is_on

        return HttpResponse(1 if toggle else 0)


    
