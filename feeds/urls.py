from django.urls import path

from . import views

urlpatterns = [
    # ex: /feeds/
    path('', views.index, name='home'), #views.IndexView.as_view()
    # ex: /feeds/5/
    path('<int:feed_id>/', views.detail, name='detail'), #views.DetailView.as_view()
]