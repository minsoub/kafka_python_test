# kafka_python_test
Ec2에서 Python3 설치 및 Boto3 설치 
[ec2-user@ip-xxx-xxx-xxx-xxx ~]$ yum list installed | grep -i python3
[ec2-user@ip-xxx-xxx-xxx-xxx ~]$ sudo yum install python3 -y

python3 가상환경 만들기 
[ec2-user@ip-xxx-xxx-xxx-xxx ~]$ pthon3 -m venv my_app/env
[ec2-user@ip-xxx-xxx-xxx-xxx ~]$ source ~/my_app/env/bin/activate

boot3 설치하기 
(env) [ec2-user@ip-xxx-xxx-xxx-xxx ~]$ pip install boto3

가상환경 deactivate
(env) [ec2-user@ip-xxx-xxx-xxx-xxx ~]$ deactivate

