from django.urls import path
# from films.views import FilmListApiView, FilmDetailAPIView
from films.views import FilmViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('films', FilmViewSet, basename='films')
urlpatterns = router.urls


# urlpatterns = [
#      path('films/', FilmListApiView.as_view()), # /api/films
#      path('films/<int:pk>/', FilmDetailAPIView.as_view())
# ]
