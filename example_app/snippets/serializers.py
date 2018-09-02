from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    created = serializers.DateTimeField(read_only=True,
        help_text="La fecha de creacion del snippet, autogenerada")

    class Meta:
        model = Snippet
        fields = ('url', 'highlight', 'owner', 'created',
                  'title', 'code', 'linenos', 'language', 'style')
        extra_kwargs = {'code': {'help_text': 'Codigo a resaltar'},
                        'title': {'help_text': 'El título del snippet'}}
                  
class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(queryset=Snippet.objects.all(), view_name='snippet-detail', many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'snippets')
