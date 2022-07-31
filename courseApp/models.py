from django.db import models
from django.urls import reverse
from datetime import datetime

class Category(models.Model):
    categoryName = models.CharField("Category name", max_length=255)
    slug = models.SlugField("URL category", unique=True)

    def __str__(self):
        return self.categoryName

    def get_absolute_url(self):
        return reverse("courseListByCategory", args=[self.slug])

    class Meta:
        verbose_name_plural = "Categories"

class Course(models.Model):
    courseName = models.CharField("Course name", max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category")
    courseDescription = models.TextField("Course description")
    courseCover = models.ImageField("Course cover")
    postDate = models.DateTimeField(default=datetime.now)
    slug = models.SlugField("URL course", unique=True)
    published = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("themeList", args=[self.slug])

    def __str__(self):
        return self.courseName

    class Meta:
        verbose_name_plural = "Courses"


class Theme(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Course")
    themeName = models.CharField("Theme name", max_length=255)
    themeDescription = models.TextField("Theme description")
    themeVideo = models.FileField("Video file")

    def __str__(self):
        return self.themeName

    def get_absolute_url(self):
        return reverse("themeDetail", args=[self.pk])

    class Meta:
        verbose_name_plural = "Themes"