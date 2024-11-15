# Create your models here.

from django.db import models
import os

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    hook_text = models.CharField(max_length=100, blank=True)

    head_image = models.ImageField(upload_to="blog/images/%y/%m/%d", blank=True)
    file_upload = models.FileField(upload_to="blog/images/%Y/%m/%d", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # author = models.ForeignKey(User, on_deletd=models.CACADE)
    # category = models. Foreignkey category, on_delete=modeLs.CASCADE)
    # tags = models.ManyToManyField(Tag)
    def __str__(self):
        return f"[{self.pk}] {self.title}"

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    # 첨부 파일명과 확장자 아이콘 나타내기
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)
    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]