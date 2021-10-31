from django.urls import path
from . import views
 # TEMPLATE TAGGING
app_name = 'basic_app'  # NAMESPACING

urlpatterns = [
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
]
