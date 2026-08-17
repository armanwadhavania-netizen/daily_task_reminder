from datetime import datetime

from django.core.mail import send_mail
from django.utils import timezone

from .models import Task, Reminder


def check_due_tasks():

    now = timezone.localtime()

    tasks = Task.objects.filter(
        completed=False,
        reminder_sent=False
    )

    for task in tasks:

        task_datetime = datetime.combine(
            task.due_date,
            task.due_time
        )

        task_datetime = timezone.make_aware(
            task_datetime,
            timezone.get_current_timezone()
        )

        if task_datetime <= now:

            subject = f"Task Reminder: {task.title}"

            message = (
                f"Your task '{task.title}' is due now!\n\n"
                f"Description: {task.description}\n"
                f"Due Date: {task.due_date}\n"
                f"Due Time: {task.due_time}"
            )

            send_mail(
                subject,
                message,
                None,
                [task.email],
                fail_silently=False,
            )

            Reminder.objects.create(
                task=task,
                message=f"Task '{task.title}' is due now!"
            )

            task.reminder_sent = True
            task.save()

            print(f"Email sent to {task.email}")

    print("CRON: Task check completed")