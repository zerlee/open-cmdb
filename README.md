Django rest framework + vue 的CMDB项目

## 开发步骤

### linux下安装python3和一些依赖
yum install python3 gcc python36-devel python-ldap  openldap openldap24-libs openldap-clients openldap-devel openssl-devel

### 安装node和npm
cd /opt/software
wget https://nodejs.org/dist/v10.9.0/node-v10.9.0-linux-x64.tar.xz 
tar xf  node-v10.9.0-linux-x64.tar.xz      
ln -s /opt/software/node-v10.9.0-linux-x64/bin/npm   /usr/local/bin/ 
ln -s /opt/software/node-v10.9.0-linux-x64/bin/node   /usr/local/bin/

### 创建虚拟环境
在open-cmdb目录下
python3 -m venv venv
开启虚拟环境
. venv/bin/active

### 后端调试

1、 在虚拟环境开启的情况下，在backend目录下 安装后端python项目依赖的库
```
pip install -r requirements.txt
```
2、在linux上创建用户lqs
```
useradd lqs
```
切换到lqs用户下，创建用户密钥
```
su lqs
ssh-keygen -t rsa，按三次回车
```

3、修改setting文件中的用户名usera为lqs

4、修改setting文件中的ldap服务器IP

5、执行数据库迁移
```
python manage.py makemigrations
python manage.py migrate
```
6、创建后台admin管理界面的登录账号
```
python manage.py createsuperuser
```
7、启动服务器
```
python manage.py runserver 0.0.0.0:8000
```
8、打开浏览器查看效果

### 在frontend目录下 安装前端vue项目依赖的库





## 部署
- 推荐容器化部署
```bash
docker pull myide/opencmdb:v1
docker run -itd --name op1 --network host opencmdb:v1
```




