from django.urls import path
from . import views

#名前つける
app_name = 'score'

#urlパターン
urlpatterns = [
    #index
    path('', views.IndexView.as_view(), name = 'index'),

    #記録
    path('post/', views.CreteScoreView.as_view(), name='post'),

    #記録完了
    path('post_done/',
         views.PostSuccessView.as_view(),
         name='post_done'),

    #科目
    path('scores/<int:subject>',
         views.SubjectView.as_view(),
         name='scores_cat'),

    #ユーザー記録
    path('user-list/<int:user>',
         views.UserView.as_view(),
         name='user_list'),

    #詳細ページ
    path('score-detail/<int:pk>',
         views.DetailView.as_view(),
         name='score_detail'),

    #マイページ
    path('mypage/', views.MypageView.as_view(), name = 'mypage'),

    #削除
    path('score/<int:pk>/delete/',
         views.ScoreDeleteView.as_view(),
         name='score_delete'),
]