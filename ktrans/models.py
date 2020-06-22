from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from PIL import Image
import datetime
import calendar

MEDICAL_PLAN = (
    ('Yes','Yes'),
    ('No','No')
)

STATE = (
    ('Alabama','Alabama'),
    ('Alaska','Alaska'),
    ('Arizona','Arizona'),
    ('Arkansas','Arkansas'),
    ('California','California'),
    ('Colorado','Colorado'),
    ('Connecticut','Connecticut'),
    ('Delaware','Delaware'),
    ('Florida','Florida'),
    ('Georgia','Georgia'),
    ('Hawaii','Hawaii'),
    ('Idaho','Idaho'),
    ('Illinois','Illinois'),
    ('Indiana','Indiana'),
    ('Iowa','Iowa'),
    ('Kansas','Kansas'),
    ('Kentucky','Kentucky'),
    ('Louisiana','Louisiana'),
    ('Maine','Maine'),
    ('Maryland','Maryland'),
    ('Massachusetts','Massachusetts'),
    ('Michigan','Michigan'),
    ('Minnesota','Minnesota'),
    ('Mississippi','Mississippi'),
    ('Missouri','Missouri'),
    ('Montana','Montana'),
    ('Nebraska','Nebraska'),
    ('Nevada','Nevada'),
    ('New Hampshire','New Hampshire'),
    ('New Jersey','New Jersey'),
    ('New Mexico','New Mexico'),
    ('New York','New York'),
    ('North Carolina','North Carolina'),
    ('North Dakota','North Dakota'),
    ('Ohio','Ohio'),
    ('Oklahoma','Oklahoma'),
    ('Oregon','Oregon'),
    ('Pennsylvania','Pennsylvania'),
    ('Rhode Island','Rhode Island'),
    ('South Carolina','South Carolina'),
    ('South Dakota','South Dakota'),
    ('Tennessee','Tennessee'),
    ('Texas','Texas'),
    ('Utah','Utah'),
    ('Vermont','Vermont'),
    ('Virginia','Virginia'),
    ('Washington','Washington'),
    ('West Virginia','West Virginia'),
    ('Wisconsin','Wisconsin'),
    ('Wyoming','Wyoming')
)

SERVING_AREA = (
    ('Bolingbrook','Bolingbrook'),
    ('Woodridge','Woodridge'),
    ('Romeoville','Romeoville'),
    ('Plainfield','Plainfield'),
    ('Joliet','Joliet')
)

POSITIONS = (
    ('Driver','Driver'),
    ('Aide','Aide'),
    ('Either Position(Aide or Driver)','Either Position(Aide or Driver)')
)

CERTIFIED = (
    ('Yes','Yes'),
    ('No','No')
)
US_CITIZEN = (
    ('Yes','Yes'),
    ('No','No')
)
UNDER_TWENTYONE = (
    ('Yes','Yes'),
    ('No','No')
)

CONVICTED_OF_CRIME = (
    ('Yes','Yes'),
    ('No','No')
)

DUI = (
    ('Yes','Yes'),
    ('No','No')
)

SUBMIT_DRUG_TEST = (
    ('Yes','Yes'),
    ('No','No')
)

TAKE_MEDICAL_EXAM = (
    ('Yes','Yes'),
    ('No','No')
)

DRIVERS_LICENSE_LAPSE = (
    ('Yes','Yes'),
    ('No','No')
)

REFERRED_BY = (
    ('Online','Online'),
    ('Friend','Friend'),
    ('Vehicle Commercial','Vehicle Commercial'),
    ('Word of mouth','Word of mouth')
)
class Students(models.Model):
    students_name = models.CharField(max_length=60)
    students_address = models.CharField(max_length=200)
    students_phone = models.CharField(max_length=50)
    primary_contact = models.CharField(max_length=200)
    primary_phone = models.CharField(max_length=50)
    secondary_contact = models.CharField(max_length=200)
    secondary_phone = models.CharField(max_length=50)
    emergency_contact = models.CharField(max_length=100)
    emergency_phone = models.CharField(max_length=50)
    relationship_to_student = models.CharField(max_length=100,help_text='Relationship to student')
    medical_plan = models.CharField(max_length=3, choices=MEDICAL_PLAN, default='No',help_text='Does student have a medical plan?')
    medical_reason = models.CharField(max_length=100,blank=True,default='None')
    destination = models.CharField(max_length=50)
    destination_address = models.CharField(max_length=100)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    monday_arrival_and_departure_times = models.CharField(max_length=50,help_text='Eg.8:00:00 am ,12:30:00 pm')
    tuesday_arrival_and_departure_times = models.CharField(max_length=50,help_text='Eg.8:00:00 am ,12:30:00 pm')
    wednesday_arrival_and_departure_times= models.CharField(max_length=50,help_text='Eg.8:00:00 am ,12:30:00 pm')
    thursday_arrival_and_departure_times = models.CharField(max_length=50,help_text='Eg.8:00:00 am ,12:30:00 pm')
    friday_arrival_and_departure_times= models.CharField(max_length=50,help_text='Eg.8:00:00 am ,12:30:00 pm')
    school_contact = models.CharField(max_length=100)
    school_phone = models.CharField(max_length=50)
    additional_info = models.CharField(max_length=250,blank=True)
    # schools_academic_calender = models.FileField(blank=True,upload_to='school_calendar',help_text='Either picture or pdf,leave blank if not available',validators=[FileExtensionValidator(allowed_extensions=['pdf','jpeg','jpg'])])
    date_submitted = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"{self.students_name}"



class Drivers(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50,blank=True)
    email = models.EmailField(unique=True,max_length=245,blank=True)
    # street_address = models.CharField(max_length=100,blank=True)
    city = models.CharField(max_length=100,blank=True)
    # state = models.CharField(max_length=30,choices=STATE,default='Alabama',blank=True)
    # start_date = models.DateField(help_text='<em>Date available to start</em>',default=timezone.now,blank=True)
    # location_to_work = models.CharField(max_length=30,choices=SERVING_AREA,default='Joliet',help_text='<em>Which location are you applying for?</em>',blank=True)
    # times_available = models.CharField(max_length=100,help_text='<em>Your specific times of availability</em>',blank=True)
    # position_applying_for = models.CharField(max_length=40,choices=POSITIONS,default='Driver',help_text='<em>Position applying for</em>',blank=True)
    # certified_driver = models.CharField(max_length=30,choices=CERTIFIED,default='Yes',help_text='<em>Are you a certified school bus driver?</em>',blank=True)
    # us_citizen = models.CharField(max_length=30,choices=US_CITIZEN,default='Yes',help_text="<em>Are you a citizen of the United States?</em>",blank=True)
    # over_21 = models.CharField(max_length=3,choices=UNDER_TWENTYONE,default='Yes',help_text="<em>Are you over the age of 21?</em>",blank=True)
    # crime_conviction = models.CharField(max_length=3,choices=CONVICTED_OF_CRIME,default='No',help_text="<em>Have you ever been convicted of a crime?</em>",blank=True)
    # dui = models.CharField(max_length=3,choices=DUI,default='No',help_text="<em>Have you ever had a DUI?</em>",blank=True)
    # drug_screening_test = models.CharField(max_length=3,choices=SUBMIT_DRUG_TEST,default='Yes',help_text="Are you willing to submit a drug screen test?",blank=True)
    # medical_test = models.CharField(max_length=3,choices=TAKE_MEDICAL_EXAM,default='Yes',help_text="Are you willing to take the medical examination test?",blank=True)
    # license_lapse = models.CharField(max_length=3,choices=DRIVERS_LICENSE_LAPSE,default='No',help_text="Have you ever had a lapse in your driver's license in the past two years?(including expired license)?",blank=True)
    # demerit_points = models.CharField(max_length=100,blank=True,help_text="Do you have enay demirit points or driving infractions on your record?Leave blank if no explain if yes",default='None')
    # work_history = models.TextField(blank=True,help_text="List all the companies you've worked for.Example company name,position held,start and end dates,reason for leaving,managers name and phone",default='None')
    # professional_references = models.TextField(blank=True,help_text="List all your references here.Examples name,phone,relationship",default='None')
    # referred_by = models.CharField(max_length=10,choices=REFERRED_BY,default='Friend',help_text="Who referred you?")
    driver_pic = models.ImageField(upload_to='driver_images')
    # agree_to_terms = models.BooleanField(blank=False,default=False,help_text="By checking this checkbox i verify that all the above information is true and correct to the best of my knowledge")
    date_posted = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.driver_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail = (output_size)
            img.save(self.driver_pic.path)

class QuickEnquiry(models.Model):
    name = models.CharField(max_length=50,help_text='Name is required')
    email = models.EmailField(max_length=245,help_text='Email is required')
    phone = models.CharField(max_length=20,help_text='Phone is required')
    message = models.TextField(help_text='What can we help you with?')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name}"






