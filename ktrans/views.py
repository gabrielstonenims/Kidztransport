from django.shortcuts import render,redirect,reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from .models import Students,Drivers,QuickEnquiry
import pytz
from django.core.paginator import Paginator
from .forms import ContactForm



def about(request):
    return render(request,"ktrans/about.html")




def home(request):
    return render(request,'ktrans/home.html')

# list of all drivers
def our_drivers(request):
    drivers = Drivers.objects.all().order_by('-date_posted')

    context = {
        'drivers':drivers
    }

    return render(request,"ktrans/our_drivers.html",context)

def drivers(request):
    return render(request,"ktrans/drivers.html")


def parents(request):
    return render(request,"ktrans/parents.html")


def service_areas(request):
    return render(request,"ktrans/service-areas.html")

def theteam(request):
    return render(request,"ktrans/team.html")

def contact(request):
    if request.method == "POST":
        qform = ContactForm(request.POST)
        if qform.is_valid():
            qform.save()
            name = qform.cleaned_data.get('name').capitalize()
            email = qform.cleaned_data.get('email')
            phone = qform.cleaned_data.get('phone')
            msg_content = qform.cleaned_data.get('message')

            subject = f"New message from  {name}"
            message = f"{msg_content} \n {email}"
            subject1 = f"We have received your message {name}"
            message1= f"We have received your message and thank you for contacting us.We will get back to you soon.\n Kidz Transport Team."
            from_email = settings.EMAIL_HOST_USER
            to_list = [settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_email,to_list, fail_silently=True)

            # to users email
            from_email = settings.EMAIL_HOST_USER
            to_list = [email]
            send_mail(subject1, message1, from_email,to_list, fail_silently=True)
            # messages.success(request,f"Message sent,we will get back to you as soon as possible.")
            return redirect('contact')
    else:
        qform = ContactForm()

    context = {
        "qform":qform
    }

    if request.is_ajax():
        html = render_to_string("ktrans/contact.html",context,request=request)
        return JsonResponse({'form':html})
    return render(request,"ktrans/contact.html",context)

class CreateDriver(CreateView):
    model = Drivers
    fields = ['name','date_of_birth','phone','email','street_address','city','state','start_date','location_to_work','times_available','position_applying_for','certified_driver','us_citizen','over_21','crime_conviction','dui','drug_screening_test','medical_test','license_lapse','demerit_points','work_history','professional_references','referred_by','driver_pic','agree_to_terms']

    success_url = '/our_drivers'

    def form_valid(self, form):
        name = form.cleaned_data.get('name').capitalize()
        ddob = form.cleaned_data.get('date_of_birth')
        dphone = form.cleaned_data.get('phone')
        demail = form.cleaned_data.get('email')
        dstreetaddress = form.cleaned_data.get('street_address')
        dcity = form.cleaned_data.get('city')
        dstate = form.cleaned_data.get('state')
        dstart_date = form.cleaned_data.get('start_date')
        dlocationtowork = form.cleaned_data.get('location_to_work')
        dtimeavailable = form.cleaned_data.get('times_available')
        dpositionapply = form.cleaned_data.get('position_applying_for')
        dcertified = form.cleaned_data.get('certified_driver')
        duscitizen = form.cleaned_data.get('us_citizen')
        dover21 = form.cleaned_data.get('over_21')
        dcrimeconvict = form.cleaned_data.get('crime_conviction')
        ddui = form.cleaned_data.get('dui')
        ddrugtest = form.cleaned_data.get('drug_screening_test')
        dmedicaltest = form.cleaned_data.get('medical_test')
        dlicense = form.cleaned_data.get('license_lapse')
        ddemerits = form.cleaned_data.get('demerit_points')
        dworkhistory = form.cleaned_data.get('work_history')
        dprofessionalref = form.cleaned_data.get('professional_references')
        dreferredby = form.cleaned_data.get('referred_by')
        dagree = form.cleaned_data.get('agree_to_terms')
        dpic = form.cleaned_data.get('driver_pic')

        subject = f"New driver application"
        message = f"Driver's information \n Name:    \t{name} \n DOB:    \t{ddob} \n Phone:    \t{dphone} \n Email:    \t{demail} \n Street Address:   \t{dstreetaddress} \n City: \t{dcity} \n State:    \t{dstate} \n Start Date:    \t{dstart_date} \n Location to work:    \t{dlocationtowork} \n Times available:    \t{dtimeavailable} \n Position applying:    \t{dpositionapply} \n Ceritfied driver:    \t{dcertified} \n US Citizen:    \t{duscitizen} \n Over 21:    \t{dover21} \n Crime conviction:    \t{dcrimeconvict} \n DUI:    \t{ddui} \n Take drug test:    \t{ddrugtest} \n Take medical test:    \t{dmedicaltest} \n License Lapse:    \t{dlicense} \n Demerits:    \t{ddemerits} \n Work History:    \t{dworkhistory} \n Professional References:    \t{dprofessionalref} \n Referred By:    \t{dreferredby} "
        from_email = settings.EMAIL_HOST_USER
        to_list = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, from_email,to_list, fail_silently=True)
        return super().form_valid(form)

class RegisterStudent(CreateView):
    model = Students
    fields = ['students_name','students_address','students_phone','primary_contact','primary_phone','secondary_contact','secondary_phone','emergency_contact','emergency_phone','relationship_to_student','medical_plan','medical_reason','destination','destination_address','start_date','end_date','monday_arrival_and_departure_times','tuesday_arrival_and_departure_times','wednesday_arrival_and_departure_times','thursday_arrival_and_departure_times','friday_arrival_and_departure_times','school_contact','school_phone','additional_info']

    success_url ='/parents'

    def form_valid(self, form):
        name = form.cleaned_data.get('students_name').capitalize()
        address = form.cleaned_data.get('students_address')
        phone = form.cleaned_data.get('students_phone')
        pcontact = form.cleaned_data.get('primary_contact')
        pphone = form.cleaned_data.get('primary_phone')
        scontact = form.cleaned_data.get('secondary_contact')
        sphone = form.cleaned_data.get('secondary_phone')
        econtact = form.cleaned_data.get('emergency_contact')
        ephone = form.cleaned_data.get('emergency_phone')
        relationship = form.cleaned_data.get('relationship_to_student')
        mplan = form.cleaned_data.get('medical_plan')
        mreason = form.cleaned_data.get('medical_reason')
        destination = form.cleaned_data.get('destination')
        daddress = form.cleaned_data.get('destination_address')
        sdate = form.cleaned_data.get('start_date')
        edate = form.cleaned_data.get('end_date')
        monarrivedepart = form.cleaned_data.get('monday_arrival_and_departure_times')
        tuesarrivedepart = form.cleaned_data.get('tuesday_arrival_and_departure_times')
        wedarrivedepart = form.cleaned_data.get('wednesday_arrival_and_departure_times')
        thursarrivedepart = form.cleaned_data.get('thursday_arrival_and_departure_times')
        friarrivedepart = form.cleaned_data.get('friday_arrival_and_departure_times')
        sc = form.cleaned_data.get('school_contact')
        sp = form.cleaned_data.get('school_phone')
        addinfo = form.cleaned_data.get('additional_info')
        subject = f"New student"

        message = f"Name: \t {name} \n Address: \t{address} \n Phone: \t{phone} \n Primary Contact: \t{pcontact} \n Primary Phone: \t{pphone} \n Secondary Contact: \t{scontact} \n Secondary Phone: \t{sphone} \n Emergency Contact: \t{econtact} \n Emergency Phone: \t{ephone} \n Relationship to Student: \t{relationship} \n Medical Plan: \t{mplan} \n Medical Reason: \t{mreason} \n Destination: \t{destination} \n Address: \t{daddress} \n Start Date: \t{sdate} \n End Date: \t{edate} \n Monday Arrival and Departure Times:  \t{monarrivedepart} \n Tuesday Arrival and Departure Times: \t{tuesarrivedepart} \n Wednesday Arrival and Departure Times: \t{wedarrivedepart} \n Thursday Arrival and Departure Times: \t{thursarrivedepart} \n Friday Arrival and Departure Times: \t{friarrivedepart} \n School Contact: \t{sc} \n School Phone: \t{sp} \n Additional Information: \t{addinfo} \n "
        from_email = settings.EMAIL_HOST_USER
        to_list = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, from_email,to_list, fail_silently=True)
        return super().form_valid(form)