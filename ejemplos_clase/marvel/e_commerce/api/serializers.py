
# Primero importamos los modelos que queremos serializar:
from e_commerce.models import Comic,WishList
from django.contrib.auth.models import User

# Luego importamos todos los serializadores de django rest framework.
from rest_framework import serializers

class ComicSerializer(serializers.ModelSerializer):
    # data =  serializers.SerializerMethodField()
    
    class Meta:
        model = Comic
        fields = ('marvel_id','title', 'description', 'price', 'stock_qty', 'picture')
        # fields = ('marvel_id', 'title', 'data')

    # def get_data(self, obj):
    #     print('obj: ', obj.title)

    #     return {
    #         'titulo': obj.title,
    #         'description': obj.description,
    #         'imagen': obj.picture,
    #         'precio': obj.price,
    #         'stock_qty': obj.stock_qty,
    #         'total': obj.stock_qty * obj.price
    #     }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ("__all__")

# TODO: Realizar el serializador para el modelo de WishList
