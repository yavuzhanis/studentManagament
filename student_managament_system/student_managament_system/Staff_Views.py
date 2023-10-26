from django.shortcuts import redirect, render
from app.models import Staff, Staff_Notification


def home(request):
    return render(request, "Staff/home.html")

def notifications(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id 

        notification = Staff_Notification.objects.filter(staff_id = staff_id)

        context = {
            'notification': notification,
        }
    return render(request, "Staff/notification.html",context)

def staff_notification_mark_as_done(request,status):
    notification = Staff_Notification.objects.get(id=status)
    notification.status= 1
    notification.save()
    return redirect('notifications')

def staff_apply_leave(request):
    return render(request, "Staff/apply_leave.html")