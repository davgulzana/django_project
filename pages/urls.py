from django.urls import path
from pages.views import HomePageView, AboutPageView, ContactsPageView

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('about/', AboutPageView.as_view(), name = 'about'),
    path('contacts/', ContactsPageView.as_view(), name = 'contacts')
]