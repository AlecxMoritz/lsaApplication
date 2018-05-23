from django.urls import path
from .views import list_contacts, create_contact, update_contact, delete_contact




urlpatterns = [
    path('', list_contacts, name="list_contacts"),
    path('/new', create_contact, name="create_contact"),
    path('/update/<int:id>/', update_contact, name="update_contact"),
    path('/delete/<int:id>/', delete_contact, name="delete_contact"),
]

#  READ CREATE UPDATE DELETE