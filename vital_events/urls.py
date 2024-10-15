from django.urls import path

from .views import BirthCertificateView


urlpatterns = [

    path('apply-birth-certificate/', BirthCertificateView.as_view(),
         name='apply-birth-certificate-list-create'),

    path('vital-events/<int:pk>/', BirthCertificateView.as_view(),
         name='vital-events-update'),

]
