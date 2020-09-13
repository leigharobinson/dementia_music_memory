"""musicmemory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from musicmemoryapi.views import CaretakerView, UserView, FacilityView, SongView, MoodView
from musicmemoryapi.views import EyeContactView, MovementView, TalkativenessView, VocalizationView
from musicmemoryapi.views import LikedSongView, PatientView, FacilityCaretakerView
from musicmemoryapi.views import CaretakerPatientView
from musicmemoryapi.views import register_user, login_user

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'caretakers', CaretakerView, 'caretaker')
router.register(r'users', UserView, 'user')
router.register(r'facilities', FacilityView, 'facility')
router.register(r'songs', SongView, 'song')
router.register(r'moods', MoodView, 'mood')
router.register(r'eyecontacts', EyeContactView, 'eyecontact')
router.register(r'movements', MovementView, 'movement')
router.register(r'talkativeness', TalkativenessView, 'talkativeness')
router.register(r'vocalizations', VocalizationView, 'vocalization')
router.register(r'likedsongs', LikedSongView, 'likedsong')
router.register(r'patients', PatientView, 'patient')
router.register(r'facilitiescaretakers',
                FacilityCaretakerView, 'facilitycaretaker')
router.register(r'caretakerspatients',
                CaretakerPatientView, 'caretakerpatient')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('register/', register_user),
    path('login/', login_user),
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
