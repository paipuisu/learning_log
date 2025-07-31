from django.contrib import admin

from .models import Topic, Entry # admin.pyと同じフォルダで探すように指示「.」

# Register your models here.
admin.site.register(Topic) # 管理サイトでモデルを操作できるようにDjangoに指示
admin.site.register(Entry)
