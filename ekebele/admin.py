from django.contrib.admin import AdminSite
from accounts.admin import CustomUserAdmin
from accounts.models import User
from vital_events.models import BirthCertificate
from vital_events.admin import BirthCertificateAdmin


class CustomAdminSite(AdminSite):
    site_header = "eKebele Control Panel"
    site_title = "eKebele Admin"
    index_title = "Welcome to the eKebele Admin Dashboard"


# Create an instance of the custom admin site
custom_admin_site = CustomAdminSite(name="custom_admin")

# Register models with the custom admin site
custom_admin_site.register(User, CustomUserAdmin)
custom_admin_site.register(BirthCertificate, BirthCertificateAdmin)
