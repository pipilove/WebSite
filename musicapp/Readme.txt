 修改你的模型（在models.py中）。
    运行python manage.py makemigrations命令为这些改动创建迁移文件。
    运行python manage.py migrate命令将这些改动应用到数据库中。
superuser lml lml


pythonmanage.py shell 进入交互式命令行
from music.models import User,Item1,Login

Item1.objects.all()

python manage.py runserver
http://127.0.0.1:8000/music

python manage.py runserver 0.0.0.0:8000
http://192.168.31.213:8000/