from rest_framework import viewsets
from pokedex.models import Pokemon
from .serializers import PokemonSerializer
from oauth2_provider.contrib.rest_framework import TokenHasScope, OAuth2Authentication
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.
class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    
    authentication_classes = [OAuth2Authentication]
    required_scopes = ['write']
    
    def get_permissions(self):
        if self.request.method in ['POST', 'GET', 'DELETE']:
            return [AllowAny()]
        return [TokenHasScope(), IsAuthenticated()]
        
    
    
    