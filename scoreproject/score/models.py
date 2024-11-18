from django.db import models
# accountsアプリのmodelsモジュールからCustomUserをインポート
from accounts.models import CustomUser

class Subject(models.Model):
    '''科目を管理するモデル
    '''
    # 科目名のフィールド
    subject = models.CharField(
        verbose_name='科目',
        max_length=20)
    
    def __str__(self):
        '''オブジェクトを文字列に変換して返す
        
        Returns(str):科目名
        '''
    def __str__(self):
        return str(self.subject)
    
class ScorePost(models.Model):
    '''入力された点数を管理するモデル
    '''

    user = models.ForeignKey(
        CustomUser,
        # フィールドのタイトル
        verbose_name='学生',
        # ユーザーを削除する場合はそのユーザーの投稿データもすべて削除する
        on_delete=models.CASCADE
    )
    # Categoryモデル(のtitle)とPhotoPostモデルを
    # 1対多の関係で結びつける
    # Categoryが親でPhotoPostが子の関係となる
    subject = models.ForeignKey(
        Subject,
        # フィールドのタイトル
        verbose_name='科目',
        # カテゴリに関係付けられた投稿データが存在する場合は
        # そのカテゴリを削除できないようにする
        on_delete=models.PROTECT
    )
    # 点数用のフィールド
    score = models.IntegerField(
        verbose_name='点数'
    )
    # memoフィールド
    memo = models.TextField(
        verbose_name='memo',
        blank=True,
        null=True
    )
    # 投稿日時のフィールド
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
    )

    def __str__(self):
        '''オブジェクトを文字列に変換して返す
        
        Returns(str):投稿記事のタイトル
        '''
    def __str__(self):
        return str(self.subject)