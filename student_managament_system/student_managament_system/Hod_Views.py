from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from app.models import Course, Session, CustomUser, Student, Staff, Subject,Staff_Notification
from django.contrib import messages


@login_required(login_url="/")
def HOME(request):
    student_count = Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    course_count = Course.objects.all().count()
    subject_count = Subject.objects.all().count()

    student_gender_male = Student.objects.filter(gender='Male').count()
    student_gender_female = Student.objects.filter(gender = 'Female').count()


    context = {
        "student_count": student_count,
        "staff_count": staff_count,
        "course_count": course_count,
        "subject_count": subject_count,
        'student_gender_male' : student_gender_male,
        'student_gender_female': student_gender_female,

    }
    return render(request, "Hod/home.html", context)


@login_required(login_url="/")
def add_student(request):
    course = Course.objects.all()
    session_year = Session.objects.all()
    if request.method == "POST":
        profile_pic = request.FILES.get("profile_pic")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        gender = request.POST.get("gender")
        course_id = request.POST.get("course_id")
        session_year_id = request.POST.get("session_year_id")
        address = request.POST.get("address")

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, "Email is Already Taken")
            return redirect("add_student")
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "Username is Already Taken")
            return redirect("add_student")
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=3,
            )
            user.set_password(password)
            user.save()

            course = Course.objects.get(id=course_id)
            session_year = Session.objects.get(id=session_year_id)

            student = Student(
                admin=user,
                address=address,
                session_year_id=session_year,
                course_id=course,
                gender=gender,
            )
            student.save()
            messages.success(
                request,
                user.first_name + " " + user.last_name + "Was successfully Added! ",
            )
            return redirect("add_student")

    context = {"course": course, "session": session_year}
    return render(request, "Hod/add_student.html", context)


@login_required(login_url="/")
def view_student(request):
    student = Student.objects.all()

    context = {"student": student}
    return render(request, "Hod/view_student.html", context)


@login_required(login_url="/")
def edit_student(request, id):
    student = Student.objects.filter(id=id)
    course = Course.objects.all()
    session = Session.objects.all()

    context = {
        "student": student,
        "course": course,
        "session": session,
    }
    return render(request, "Hod/edit_student.html", context)


@login_required(login_url="/")
def update_student(request):
    if request.method == "POST":
        student_id = request.POST.get("student_id")
        print("Student id is ", student_id, "")
        profile_pic = request.FILES.get("profile_pic")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        gender = request.POST.get("gender")
        course_id = request.POST.get("course_id")
        session_year_id = request.POST.get("session_year_id")
        address = request.POST.get("address")

        user = CustomUser.objects.get(id=student_id)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        user.password = password

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        student = Student.objects.get(admin=student_id)
        student.address = address
        student.gender = gender

        course = Course.objects.get(id=course_id)
        student.course_id = course

        session_year = Session.objects.get(id=session_year_id)
        student.session_year_id = session_year

        student.save()
        messages.success(request, "Record Are Successfully Updated! ")
        return redirect("view_student")
    return render(request, "Hod/edit_student.html")


@login_required(login_url="/")
def delete_student(request, admin):
    student = CustomUser.objects.get(id=admin)
    student.delete()
    messages.success(request, "Record Are Succesfully Deleted !")
    return redirect("view_student")


@login_required(login_url="/")
def add_course(request):
    if request.method == "POST":
        course_name = request.POST.get("course_name")
        course = Course(
            name=course_name,
        )
        course.save()
        messages.success(request, "Course Added SuccessFully!")
        return redirect("add_course")
    return render(request, "Hod/add_course.html")


@login_required(login_url="/")
def view_course(request):
    course = Course.objects.all()
    context = {"course": course}
    return render(request, "Hod/view_course.html", context)


@login_required(login_url="/")
def edit_course(request, id):
    course = Course.objects.get(id=id)
    context = {"course": course}
    return render(request, "Hod/edit_course.html", context)


@login_required(login_url="/")
def update_course(request):
    if request.method == "POST":
        name = request.POST.get("name")
        course_id = request.POST.get("course_id")

        course = Course.objects.get(id=course_id)
        course.name = name
        course.save()
        messages.success(request, "Course Are Succesfully Update !")
        return redirect("view_course")
    return render(request, "Hod/edit_course.html")


@login_required(login_url="/")
def delete_course(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    messages.success(request, "Course are Successfully Deleted")
    return redirect("view_course")


@login_required(login_url="/")
def add_staff(request):
    if request.method == "POST":
        profile_pic = request.FILES.get("profile_pic")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        gender = request.POST.get("gender")
        address = request.POST.get("address")

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, "Email Is Already taken !")
            return redirect("add_staff")

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "Username Is Already taken !")
            return redirect("add_staff")

        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=2,
            )
            user.set_password(password)
            user.save()

        staff = Staff(admin=user, address=address, gender=gender)
        staff.save()
        messages.success(request, "Staff are successfully Added !")
        return redirect("add_staff")

    return render(request, "Hod/add_staff.html")


@login_required(login_url="/")
def view_staff(request):
    staff = Staff.objects.all()

    context = {
        "staff": staff,
    }
    return render(request, "Hod/view_staff.html", context)


@login_required(login_url="/")
def edit_staff(request, id):
    staff = Staff.objects.get(id=id)
    context = {
        "staff": staff,
    }
    return render(request, "Hod/edit_staff.html", context)


@login_required(login_url="/")
def update_staff(request):
    if request.method == "POST":
        staff_id = request.POST.get("staff_id")
        profile_pic = request.FILES.get("profile_pic")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        gender = request.POST.get("gender")
        address = request.POST.get("address")

        user = CustomUser.objects.get(id=staff_id)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        staff = Staff.objects.get(admin=staff_id)
        staff.gender = gender
        staff.address = address

        staff.save()
        messages.success(request, "Staff is Successfuly Updated")
        return redirect("view_staff")

    return render(request, "Hod/edit_staff.html")


@login_required(login_url="/")
def delete_staff(request, admin):
    staff = CustomUser.objects.get(id=admin)
    staff.delete()
    messages.success(request, "Staff Are Successfuly Deleted")
    return redirect("view_staff")


@login_required(login_url="/")
def add_subject(request):
    course = Course.objects.all()
    staff = Staff.objects.all()

    if request.method == "POST":
        subject_name = request.POST.get("subject_name")
        course_id = request.POST.get("course_id")
        staff_id = request.POST.get("staff_id")

        course = Course.objects.get(id=course_id)
        staff = Staff.objects.get(id=staff_id)

        subject = Subject(
            name=subject_name,
            course=course,
            staff=staff,
        )
        subject.save()
        messages.success(request, "Subjects Are Successfuly Added ! ")
        return redirect("add_subject")

    context = {
        "course": course,
        "staff": staff,
    }
    return render(request, "Hod/add_subject.html", context)


@login_required(login_url="/")
def view_subject(request):
    subject = Subject.objects.all()
    context = {
        "subject": subject,
    }
    return render(request, "Hod/view_subject.html", context)


@login_required(login_url="/")
def edit_subject(request, id):
    subject = Subject.objects.get(id=id)
    course = Course.objects.all()
    staff = Staff.objects.all()
    context = {
        "subject": subject,
        "course": course,
        "staff": staff,
    }
    return render(request, "Hod/edit_subject.html", context)


@login_required(login_url="/")
def update_subject(request):
    if request.method == "POST":
        subject_id = request.POST.get("subject_id")
        course_id = request.POST.get("course_id")
        staff_id = request.POST.get("staff_id")
        subject_name = request.POST.get("subject_name")

        course = Course.objects.get(id=course_id)
        staff = Staff.objects.get(id=staff_id)

        subject = Subject(
            id=subject_id,
            name=subject_name,
            course=course,
            staff=staff,
        )
        subject.save()
        messages.success(request, "Subject updated successfully")
        return redirect("view_subject")


@login_required(login_url="/")
def delete_subject(request, id):
    subject = Subject.objects.filter(id=id)
    subject.delete()
    messages.success(request, "Subject deleted successfully")
    return redirect("view_subject")


@login_required(login_url="/")
def add_session(request):
    if request.method == "POST":
        session_year_start = request.POST.get("session_year_start")
        session_year_end = request.POST.get("session_year_end")

        session = Session(
            session_start=session_year_start, session_end=session_year_end
        )
        session.save()
        messages.success(request, "Session Are  Successfully Created")
        return redirect("add_session")

    return render(request, "Hod/add_session.html")


@login_required(login_url="/")
def view_session(request):
    session = Session.objects.all()

    context = {"session": session}
    return render(request, "Hod/view_session.html", context)


@login_required(login_url="/")
def edit_session(request, id):
    session = Session.objects.filter(id=id)
    context = {
        "session": session,
    }
    return render(request, "Hod/edit_session.html", context)


def update_session(request):
    if request.method == "POST":
        session_id = request.POST.get("session_id")
        session_year_start = request.POST.get("session_year_start")
        session_year_end = request.POST.get("session_year_end")

        session = Session(
            id=session_id,
            session_start=session_year_start,
            session_end=session_year_end,
        )
        session.save()
        messages.success(request, "Session are Successfully Updated")
        return redirect("view_session")


def delete_session(request, id):
    session = Session.objects.get(id=id)
    session.delete()
    messages.success(request, "Session are Successfully Deleted")
    return redirect("view_session")


def staff_send_notification(request):
    staff = Staff.objects.all()
    see_notifications =Staff_Notification.objects.all().order_by('-id')[0:5]
    context = {
        'staff':staff,
        'see_notifications':see_notifications,
    }
    return render(request,'Hod/staff_notification.html',context)

def staff_save_notification(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        message = request.POST.get('message')

        staff = Staff.objects.get(admin=staff_id)
        notification = Staff_Notification(
            staff_id=staff,
            message = message,
        )
        notification.save()
        messages.success(request,'Notification  Are Successfully Sended !')
        return redirect('staff_send_notification')