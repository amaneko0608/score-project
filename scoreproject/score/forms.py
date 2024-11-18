from django.forms import ModelForm
from .models import ScorePost

class ScorePostForm(ModelForm):
    '''ModelFormのクラス
    '''
    class Meta:
        '''ModelFormのインナークラス
        
        Attributes:
            model: モデルのクラス
            fields: フォームで使用するモデルのフィールドを指定
            '''
        model = ScorePost
        fields = ['subject', 'score', 'memo']