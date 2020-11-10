# kafka_python_test
Ec2에서 Python3 설치 및 Boto3 설치 <br>
[ec2-user@ip-xxx-xxx-xxx-xxx ~]$ yum list installed | grep -i python3<br>
[ec2-user@ip-xxx-xxx-xxx-xxx ~]$ sudo yum install python3 -y<br>
<br><br>
python3 가상환경 만들기 <br>
[ec2-user@ip-xxx-xxx-xxx-xxx ~]$ pthon3 -m venv my_app/env<br>
[ec2-user@ip-xxx-xxx-xxx-xxx ~]$ source ~/my_app/env/bin/activate<br>
<br><br>
boot3 설치하기 <br>
(env) [ec2-user@ip-xxx-xxx-xxx-xxx ~]$ pip install boto3<br>
<br><br>
가상환경 deactivate<br>
(env) [ec2-user@ip-xxx-xxx-xxx-xxx ~]$ deactivate<br>

