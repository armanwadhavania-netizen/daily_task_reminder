from django.core.management.base import BaseCommand
from tasks.tasks import check_due_tasks


class Command(BaseCommand):
    help = "Check due tasks and send reminder emails"

    def handle(self, *args, **kwargs):
        check_due_tasks()
        self.stdout.write(
            self.style.SUCCESS("Task reminder check completed.")
        )