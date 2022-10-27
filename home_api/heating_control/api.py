from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ScheduledEvent, Usage
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

        return Response(1 if toggle else 0)