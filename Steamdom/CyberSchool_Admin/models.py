from django.db import models

# Create your models here.
class Schools(models.Model):
    schools_name = models.CharField(default='')
    nss = models.CharField(default='')
    npsn = models.CharField(default='')
    school_type_choice = [
        ("Sekolah_Nasional", "Sekolah_Nasional"),
        ("Sekolah_Nasional_Plus", "Sekolah_Nasional_Plus"),
        ("Sekolah_Internasional", "Sekolah_Internasional"),
        ("Sekolah_Alam", "Sekolah_Alam"),
        ("Madrasah", "Madrasah"),
        ("Sekolah_Rumah", "Sekolah_Rumah")
    ]
    school_type = models.CharField(max_length=25,
        choices = school_type_choice,
        default = '1')
    school_addres_street = models.CharField(default='')
    school_addres_province = models.CharField(default='')
    school_addres_city = models.CharField(default='')
    school_addres_district = models.CharField(default='')
    telephone = models.CharField(default='')
    website = models.CharField(default='')
    email = models.EmailField(default='')
    school_status = models.CharField(default='')
    accreditation_score = models.CharField(default='')