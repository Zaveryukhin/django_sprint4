from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import SET_NULL

User = get_user_model()


class Location(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название места')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(
        unique=True, verbose_name='Идентификатор',
        help_text='Идентификатор страницы для URL; разрешены символы'
                  ' латиницы, цифры, дефис и подчёркивание.'
    )
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Добавлено')
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text='Если установить дату и время в будущем — можно делать'
                  ' отложенные публикации.'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Автор публикации',
        related_name='author_posts'
    )
    location = models.ForeignKey(
        Location, null=True, on_delete=models.SET_NULL,
        blank=True, verbose_name='Местоположение',
        related_name='location_posts'
    )
    # category = models.ManyToManyField(Category, through='PostCategory',
    #                                   related_name='category_posts')
    category = models.ForeignKey(
        Category, null=True, on_delete=SET_NULL,
        verbose_name='Категория',
        related_name='category_posts'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено'
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title

    # class PostCategory(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.SET_NULL)
#     category = models.ForeignKey(Category, on_delete=models.SET_NULL)
