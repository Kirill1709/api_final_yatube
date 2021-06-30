from rest_framework import serializers

from .models import Comment, Post, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    # author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('title',)
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        required=False,
        default=serializers.CurrentUserDefault())
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all())

    class Meta:
        fields = ('user', 'following')
        model = Follow

    def validate(self, data):
        if data['following'] == data['user']:
            raise serializers.ValidationError(
                'Нельзя подписаться самому на себя')
        follow = Follow.objects.filter(
            user=self.context['request'].user, following=data['following'])
        if follow.exists():
            raise serializers.ValidationError(
                'Ошибка Unique')
        return data
