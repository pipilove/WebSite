 �޸����ģ�ͣ���models.py�У���
    ����python manage.py makemigrations����Ϊ��Щ�Ķ�����Ǩ���ļ���
    ����python manage.py migrate�����Щ�Ķ�Ӧ�õ����ݿ��С�
superuser lml lml


pythonmanage.py shell ���뽻��ʽ������
from music.models import User,Item1,Login

Item1.objects.all()

python manage.py runserver
http://127.0.0.1:8000/music

python manage.py runserver 0.0.0.0:8000
http://192.168.31.213:8000/