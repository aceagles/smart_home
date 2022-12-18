from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ScheduledEvent, Usage, AggUsage
from django.utils import timezone
import json

class ControllerView(APIView):
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        if request.method == 'POST':
            #Store the new usage
            print(request.body)
            data = json.loads(request.body)

            # Check for an open usage. If open and currently off then close
            try:
                open_agg_usage = AggUsage.objects.filter(completed = False).get()
            except AggUsage.DoesNotExist:
                open_agg_usage = None
            if open_agg_usage and not data['is_on']:
                    open_agg_usage.completed = True
                    open_agg_usage.end_time = timezone.now()
                    open_agg_usage.save()
            elif not open_agg_usage and data['is_on']:
                    new_agg = AggUsage()
                    new_agg.start_time = timezone.now()
                    new_agg.save()
                

            # Get all incomplete tasks in the past
            print(timezone.now())
            events = ScheduledEvent.objects.filter(completed=False, start_time__lte=timezone.now(), deleted=False).order_by('start_time')
            events = [event for event in events]
            print(events)
            toggle = False
            if events:
                # Get the latest event
                latest_event = events.pop()

                #Delet the rest
                for event in events:
                    event.del_sched()
                
                #Latest Event has been completed
                latest_event.completed = True
                latest_event.del_sched()

                #Evaluate if a toggle is required
                if latest_event.command == ScheduledEvent.TOG:
                    toggle = True
                else:
                    # on command boolean if command to turn on
                    on_cmd = latest_event.command == ScheduledEvent.ON
                    # toggle if command doesn't match status
                    toggle = on_cmd != new_usage.is_on

        return Response(1 if toggle else 0)