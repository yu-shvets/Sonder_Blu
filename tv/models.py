from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
from django.core.validators import FileExtensionValidator
from .validators import file_size


class CommonInfo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created']


class Category(MPTTModel):
    slug = models.SlugField(blank=True, null=True)
    title = models.CharField(max_length=256)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children',
                            db_index=True, on_delete=models.CASCADE, verbose_name='parent сategory')

    class Meta(object):
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return "{}".format(self.title)


class Movies(CommonInfo):
    name = models.CharField(max_length=256)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    movie_file = models.FileField(upload_to='movies', blank=True, null=True)
    url_field = models.URLField(blank=True, null=True, verbose_name='URL')
    category = models.ManyToManyField(Category, blank=True)
    likes = models.ManyToManyField(User, related_name="likes", blank=True)
    showtime = models.DateTimeField(blank=True, null=True)
    source = models.CharField(max_length=256, blank=True, default='')

    class Meta(CommonInfo.Meta):
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return "{}".format(self.name)

    @property
    def total_likes(self):
        return self.likes.count()


class Reviews(CommonInfo):
    review = models.TextField()
    video = models.FileField(upload_to='reviews',
                             validators=[FileExtensionValidator(allowed_extensions=['mp4', 'webm', 'mov', 'avi']), file_size],
                             blank=True, null=True)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta(CommonInfo.Meta):
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return "{}-{}".format(self.user, self.created)


class UserProfiles(CommonInfo):

    GENDER_CHOICES = (('Female', 'Female'),
                      ('Male', 'Male'))

    user = models.OneToOneField(User, related_name='profile')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    photo = models.ImageField(upload_to='users/photos', blank=True, null=True)
    friends = models.ManyToManyField('self', blank=True)
    favorites = models.ManyToManyField(Movies, blank=True)
    bio = models.TextField(blank=True, null=True)

    class Meta(CommonInfo.Meta):
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return "{}".format(self.user)


class Groups(CommonInfo):
    name = models.CharField(max_length=256, blank=True, default='')
    movie = models.ForeignKey(Movies)
    author = models.ForeignKey(User, related_name='author')
    invited = models.ManyToManyField(User, blank=True, related_name='group_invited')

    class Meta(CommonInfo.Meta):
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    def __str__(self):
        return "{}".format(self.name)


class Feedback(CommonInfo):
    feedback = models.TextField(verbose_name='feedback')
    video = models.FileField(upload_to='feedbacks',
                             validators=[FileExtensionValidator(allowed_extensions=['mp4', 'webm', 'mov', 'avi']), file_size],
                             blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta(CommonInfo.Meta):
        verbose_name = "Feedback"
        verbose_name_plural = "Feedback"

    def __str__(self):
        return "{}-{}".format(self.user, self.created)

