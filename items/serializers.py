from rest_framework import serializers
from items.models import Item
from django.contrib.auth.models import User



class ItemSerializer(serializers.HyperlinkedModelSerializer):
    """
    Creating an Item Serialzier, will contain a hyperlink to Item Instance (Item Detail)
    """
   
    class Meta:
        """
        Inner class, defining the model and fields for the Item Serializer
        """
        model = Item
        fields = ['url', 'id', 'name']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Creating an User Serialzier, will contain a hyperlink to User Instance (User Detail)
    """

   
    class Meta:
        """
        Inner class, defining the model and fields for the User Serializer
        """
        model = User
        fields = ['url', 'id', 'username']








# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Snippet.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance







# from django.contrib.auth.models import User, Group
# from rest_framework import serializers


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']