from django.core.management.base import BaseCommand
from heating_control.models import Usage, AggUsage
class Command(BaseCommand):
    def handle(self, *args, **options):
        # Your command logic goes here
        off_usages = Usage.objects.filter(is_on=False)
        num_delete = off_usages.delete()
        print(f"{num_delete} were deleted")
        on_usages = Usage.objects.filter(is_on=True).order_by('date')
        agg_usage = None
        for i, usage in enumerate(on_usages):
            if not agg_usage:
                agg_usage = AggUsage()
                agg_usage.start_time = usage.date
                print(agg_usage.start_time)
                agg_usage.save()
            try:
                delta = on_usages[i+1].date - usage.date
                if  delta.total_seconds() > 10:
                    agg_usage.end_time = usage.date
                    agg_usage.completed = True
                    agg_usage.save()
                    agg_usage = None

            except IndexError:
                agg_usage.end_time = usage.date
                agg_usage.completed = True
                agg_usage.save()
                agg_usage = None
        on_usages.delete()