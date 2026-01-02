from rest_framework import viewsets
from pokedex.models import Pokemon
from pokedex.models import Trainer
from .serializers import PokemonSerializer
from .serializers import TrainersSerializer
from oauth2_provider.contrib.rest_framework import TokenHasScope, OAuth2Authentication
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.
class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    
    authentication_classes = [OAuth2Authentication]
    required_scopes = ['write']
    
    def get_permissions(self):
        if self.request.method in ['POST', 'GET', 'DELETE', 'PUT']:
            return [AllowAny()]
        return [TokenHasScope(), IsAuthenticated()]

class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainersSerializer
    
    authentication_classes = [OAuth2Authentication]
    required_scopes = ['write']
    
    def get_permissions(self):
        if self.request.method in ['POST', 'GET', 'DELETE', 'PUT']:
            return [AllowAny()]
        return [TokenHasScope(), IsAuthenticated()]
        
    
    
    