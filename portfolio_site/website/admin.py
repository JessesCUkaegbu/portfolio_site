from django.contrib import admin
from .models import *

# Register your models here.
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('skill_1', 'skill_2', 'name', 'bio')
    
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'info')

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'testimony', 'company_name')

class ClientsAdmin(admin.ModelAdmin):
    list_display = ('company_logo',)

class PriceAdmin(admin.ModelAdmin):
    list_display = ('service', 'price', 'hour', 'offer_note')

class EducationAdmin(admin.ModelAdmin):
    list_display = ('year', 'university', 'degree_status', 'info')
    
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('number_of_year', 'company_name', 'role', 'contribution')

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'img', 'date', 'entity')

class DesignSkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'strength_level')

class CodingSkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'strength_level')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'img', 'pub_date', 'post')

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'message')

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'img', 'video', 'detail')


admin.site.register(AboutMe, AboutMeAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Clients, ClientsAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(DesignSkill, DesignSkillAdmin)
admin.site.register(CodingSkill, CodingSkillAdmin)
admin.site.register(ContactForm, ContactFormAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
