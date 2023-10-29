from rest_framework.serializers import *
from apps.app.models import *

#user
class UserSerializer(ModelSerializer):
    class Meta:
        model = ModelsUser
        fields = '__all__'

#post
class PostSerializer(ModelSerializer):
    class Meta:
        models = ModelsPost
        fields = '__all__'

        