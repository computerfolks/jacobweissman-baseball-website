from django.urls import path
from app_bb import views

urlpatterns = [
  path('',views.HomeView.as_view(),name='home'),
  path('home/',views.HomeView.as_view(),name='home'),
  #path('workshop/',views.WorkshopView.as_view(),name='workshop'),
  path('workshop/',views.workshop_view, name='workshop'),
  #path('results/',views.ResultsView.as_view(),name='results'),
  path('results/',views.results_view, name='results'),
  # path('loading/',views.loading_view, name='loading'),
  path('beginner/',views.BeginnerView.as_view(), name='beginner'),
  path('about/',views.AboutView.as_view(), name='about'),
  path('info/',views.InfoView.as_view(), name='info'),
  path('single/',views.single_view, name='single'),
  # path('loaderio-189658c2fc236d9bc89764d0f7b45904/',views.LoaderView.as_view(), name='loaderio-189658c2fc236d9bc89764d0f7b45904'),
]