from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage

class SignUpView(CreateView):
    ''''サインアップページのビュー
    
    '''
    # forms.pyで定義したフォームのクラス
    form_class = CustomUserCreationForm
    # レタリングするテンプレート
    template_name = "signup.html"
    # サインアップ完了後のリダイレクト先のURLパターン
    success_url = reverse_lazy('accounts:signup_success')

    def form_valid(self, form):

        # formオブジェクトのフィールドの値をデータベースに保存
        user = form.save()
        self.object = user
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)
    
class SignUpSuccessView(TemplateView):
    '''サインアップ完了ページのビュー
    
    '''
    # レタリングするテンプレート
    template_name = "signup_success.html"

class ContactView(FormView):
    '''問い合わせページを表示するビュー
    
    フォームで入力されたデータを取得し、メールの作成と送信を行う
    '''
    # contact.htmlをレタリングする
    template_name = 'contact.html'
    # クラス変数form_classにforms.pyで定義したContactFormを設定
    form_class = ContactForm
    # 送信完了後にリダイレクトするページ
    success_url = reverse_lazy('accounts:contact')

    def form_valid(self, form):

        # フォームに入力されたデータをフィールド名を指定して取得
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        # メールのタイトルの書式設定
        subject = 'お問い合わせ: {}'.format(title)
        # フォームの入力データの書式設定
        message = \
            '送信者名: {0}\nメールアドレス: {1}\n タイトル:{2}\n メッセージ:\n{3}' \
            .format(name, email, title, message)
        # メールの送信元のアドレス
        from_email = 'kmm2459381@stu.o-hara.ac.jp'
        # 送信先のメールアドレス
        to_list = ['kmm2459381@stu.o-hara.ac.jp']
        # EmailMessageオブジェクトを生成
        message = EmailMessage(subject=subject,
                               body=message,
                               from_email=from_email,
                               to=to_list,
                               )
        # EmailMessageクラスのsend()でメールサーバーからメールを送信
        message.send()
        # 送信完了後に表示するメッセージ
        messages.success(self.request, 'お問い合わせは正常に送信されました。')
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)