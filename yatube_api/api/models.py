from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    text = models.TextField(verbose_name="Текст")
    pub_date = models.DateTimeField(
        "Дата публикации", auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts",
        verbose_name="Автор"
    )
    group = models.ForeignKey(
        "Group", on_delete=models.SET_NULL,
        related_name="groups",
        blank=True,
        null=True,
        verbose_name="Группа")

    def __str__(self):
        return self.text[:50]


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments",
        verbose_name="Автор"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments",
        verbose_name="Статья"
    )
    text = models.TextField(verbose_name="Текст")
    created = models.DateTimeField(
        "Дата добавления", auto_now_add=True, db_index=True
    )

    def __str__(self):
        return self.text[:50]


class Group(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="follower",
        verbose_name="Подписчик")
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blogger",
        verbose_name="Блогер")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "following"], name="unique_follow"),
            models.CheckConstraint(
                check=~models.Q(user=models.F('following')),
                name='user!=following'
            )
        ]
