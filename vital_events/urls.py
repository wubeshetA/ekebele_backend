from django.urls import path
from .views import BirthCertificateListCreateView, BirthCertificateDetailView, BirthCertificateByAppNumber

urlpatterns = [


    path('vital-events/birth-certificate/',
         BirthCertificateListCreateView.as_view(), name='vital-events-list-create'),
    path('vital-events/birth-certificate/<id>/',
         BirthCertificateDetailView.as_view(), name='vital-events-detail'),

    path('vital-events/applications/<str:application_number>/',
         BirthCertificateByAppNumber.as_view(), name='application-detail'),

    #     path('vital-events/mine/', BirthCertificateListView.as_view(),
    #          name='vital-events-mine'),

]
