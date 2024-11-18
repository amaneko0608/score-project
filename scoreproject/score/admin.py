from django.contrib import admin
# CustomUserをインポート
from .models import Subject, ScorePost

class SubjectAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカラムを設定するクラス
    
    '''
    # レコード一覧にidとtitleを表示
    list_display = ('id', 'subject')
    # 表示するカラムにリンクを設定
    list_display_links = ('id', 'subject')

class ScorePostAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカラムを設定するクラス
    
    '''
    # レコード一覧にidとtitleを表示
    list_display = ('id', 'subject')
    # 表示するカラムにリンクを設定
    list_display_links = ('id', 'subject')

# Django管理サイトにCategory、CategoryAdminを登録する
admin.site.register(Subject, SubjectAdmin)

# Django管理サイトにPhotoPost、PhotoPostAdminを登録する
admin.site.register(ScorePost, ScorePostAdmin)