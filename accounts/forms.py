from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse
from django import forms


# 회원정보 수정 폼
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "password" in self.fields:
            # 비밀번호 변경 문구 추가
            self.fields["password"].help_text = (
                '<a href="{}">여기</a>에서 비밀번호를 변경할 수 있어요.'.format(
                    reverse("accounts:change_password")
                )
            )
            # CSS를 활용해 필드 자체는 숨기지만 help_text는 남김
            self.fields["password"].widget.attrs["style"] = "display: none;"
            self.fields["password"].label = "비밀번호 변경"


# 회원가입 폼
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ()
