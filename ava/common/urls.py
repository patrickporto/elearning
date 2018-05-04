from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import Usuario


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'nome', 'email', 'foto', 'papel')


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
