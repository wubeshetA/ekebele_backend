from django.contrib import admin
from .models import BirthCertificate


@admin.register(BirthCertificate)
class BirthCertificateAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = (
        'application_number', 'applicant_name', 'status',
        'dob', 'gender', 'country_of_birth',
        'date_created'
    )

    # Fields to filter in the admin sidebar
    list_filter = ('status', 'gender', 'date_created', 'country_of_birth')

    # Fields to search
    search_fields = ('applicant_name', 'application_number',
                     'father_fullname', 'mother_fullname', 'phone_number')

    # Ordering of records
    ordering = ('-date_created',)

    # Fieldsets for grouping fields in the admin detail view
    fieldsets = (
        ("Application Information", {
            'fields': ('application_number', 'status', 'comment')
        }),
        ("Applicant Details", {
            'fields': ('applicant_name', 'applicant_email_address', 'phone_number', 'user')
        }),
        ("Child Details", {
            'fields': ('first_name', 'middle_name', 'last_name', 'dob', 'gender', 'country_of_birth', 'region_of_birth', 'place_of_birth')
        }),
        ("Parental Details", {
            'fields': ('father_fullname', 'father_nationality', 'mother_fullname', 'mother_nationality')
        }),
    )

    # Read-only fields
    readonly_fields = ('application_number', 'date_created')
