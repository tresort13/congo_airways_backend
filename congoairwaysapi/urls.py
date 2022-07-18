from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from congoairwaysapi import views
from .views import RegisterAPI, UpdateBagages,UpdatePoidsBagages
from .views import ManifestUpload
from knox import views as knox_views
from .views import LoginAPI
from .views import PassagerInformations
from .views import BagageInformations
from .views import UpdatePassagers
from .views import VolInformations
from .import views

urlpatterns = [
    path('',views.welcom, name='welcom'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('passager_info/<str:pk>', views.passager_informations_detail),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/manifestUpload/',ManifestUpload.as_view()),
    path('api/passagerInformation/', PassagerInformations.as_view(), name='passagerInformation'),
    path('api/bagageInformation/', BagageInformations.as_view(), name='bagageInformation'),
    path('api/updateBagage/', UpdateBagages.as_view(), name='updateBagage'),
    path('api/updatePoidsBagage/', UpdatePoidsBagages.as_view(), name='updatePoidsBagage'),
    path('api/updatePassager/', UpdatePassagers.as_view(),name='updatePassager'),
    path('api/volInformation/', VolInformations.as_view(),name='volInformation'),
    path('api/bagageAutoQuery/<str:pk>/',views.bagageAutoQuery,name='bagageAutoQuery'),
    path('api/passagerAutoQuery/<str:pk>/',views.passagerAutoQuery,name='passagerAutoQuery'),
    path('api/volAutoQuery/',views.volAutoQuery,name='volAutoQuery'),
    path('api/volAutoQuery2/<str:pk>/',views.volAutoQuery2,name='volAutoQuery2'),
    path('api/volBagageAutoQuery/<str:pk>/',views.volBagagesAutoQuery,name='volBagageAutoQuery'),
    path('api/volPassagerAutoQuery/<str:pk>/',views.volPassagerAutoQuery,name='volPassagerAutoQuery')
]

urlpatterns = format_suffix_patterns(urlpatterns)