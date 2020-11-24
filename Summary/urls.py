from django.urls import path, register_converter
from Summary import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('', views.SummaryList.as_view(), name='summary'),
    path('<yyyy:year>', views.SummaryDetails.as_view(), name='summary_details'),
]
