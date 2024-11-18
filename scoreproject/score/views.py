from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import ScorePostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import ScorePost
from django.views.generic import DetailView
from django.views.generic import DeleteView

class IndexView(ListView):
    '''トップページのビュー
    '''
    # index.htmlをレタリングする
    template_name = 'index.html'

    queryset = ScorePost.objects.order_by('-posted_at')

    # 1ページに表示するレコードの件数
    paginate_by = 9

# デコレーターにより、CreteScoreViewへのアクセスはログインユーザーに限定される
# ログイン状態でなければsettings.pyのLOGIN_URLにリダイレクトされる
@method_decorator(login_required, name='dispatch')
class CreteScoreView(CreateView):
    # forms.pyのScorePostFormをフォームクラスとして登録
    form_class = ScorePostForm
    # レタリングするテンプレート
    template_name = "post_score.html"
    # フォームデータ登録完了後のリダイレクト先
    success_url = reverse_lazy('score:post_done')

    def form_valid(self, form):
        '''CreateViewクラスのform_valid()をオーバーライド
        
        フォームのバリエーションを通過したときに呼ばれる
        フォームデータの登録をここで行う
        '''
        # commit=FalseにしてPOSTされたデータを取得
        postdata = form.save(commit=False)
        # 投稿データのidを取得してモデルのuserフィールドに格納
        postdata.user = self.request.user
        # 投稿データをデータベースに登録
        postdata.save()
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    '''投稿完了ページのビュー
    
    Attributes:
        template_name: レタリングするテンプレート
    '''
    # index.htmlをレタリングする
    template_name = 'post_success.html'

class SubjectView(ListView):
    '''カテゴリページのビュー
    
    Attributes:
        template_name: レタリングするテンプレート
        paginate_by: 1ページに表示するレコードの件数
    '''
    # index.htmlをレタリングする
    template_name = 'index.html'
    # 1ページに表示するレコードの件数
    paginate_by = 9

    def get_queryset(self):
        '''クリエを実行する
        '''
        # self.kwargsでキーワードの辞書を取得し、
        # categoryキーの値(Categorysテーブルのid)を取得
        subject_id = self.kwargs['subject']
        # filtr(フィールド名=id)で絞り込む
        categories = ScorePost.objects.filter(
            subject = subject_id).order_by('-posted_at')
        # クリエによって取得されたレコードを返す
        return categories
    
class UserView(ListView):
    '''ユーザーの投稿ページのビュー
    Attributes:
        template_name: レタリングするテンプレート
        paginate_by: 1ページに表示するレコードの件数
    '''
    # index.htmlをレタリングする
    template_name = 'index.html'
    # 1ページに表示するレコードの件数
    paginate_by = 9

    def get_queryset(self):
        '''クリエを実行する
        '''
        # self.kwargsでキーワードの取得し、
        # userキーの値(ユーザーテーブルのid)を取得
        user_id = self.kwargs['user']
        # filter(フィールド名=id)で絞り込む
        user_list = ScorePost.objects.filter(
            user = user_id).order_by('-posted_at')
        # クリエによって取得されたレコードを返す
        return user_list

class DetailView(DetailView):
    '''詳細ページのビュー
    '''
    # post.htmlをレタリングする
    template_name = 'detail.html'
    # クラス変数modelにモデルScorePostを設定
    model = ScorePost

class MypageView(ListView):
    '''マイページのビュー
    '''
    # mypage.htmlをレタリングする
    template_name = 'mypage.html'
    # 1ページに表示するレコードの件数
    paginate_by = 9

    def get_queryset(self):
        '''クリエを実行する
        '''
        # 現在ログインしているユーザー名はHttpRequest.userに格納されている
        # filter(userフィールド=userオブジェクト)で絞り込む
        queryset = ScorePost.objects.filter(
            user = self.request.user).order_by('-posted_at')
        # クリエによって取得されたレコードを返す
        return queryset
    
class ScoreDeleteView(DeleteView):
    '''レコードの削除を行うビュー
    '''
    # 操作の対象はScorePostモデル
    model = ScorePost
    # score_delete.htmlをレタリングする
    template_name = 'score_delete.html'
    # 処理完了後にマイページにリダイレクト
    success_url = reverse_lazy('score:mypage')

    def delete(self, request, *args, **kwargs):
        '''レコードの削除を行う
        '''
        # スーパークラスのdelite()を実行
        return super().delete(request, *args, **kwargs)