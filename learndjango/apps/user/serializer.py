from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(label='明确密码',
                                             write_only=True,
                                             min_length=6,
                                             max_length=20,
                                             help_text='确认密码',
                                             error_messages={
                                                 'min_length': '仅允许6-20个字符串',
                                                 'max_length': '仅允许6-20个字符串'
                                             })
    token = serializers.CharField(label='生成字段', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'password_confirm')
        extra_kwargs = {
            'username': {
                'label': '用户名',
                'help_test': '确认密码'             
            }
        }
