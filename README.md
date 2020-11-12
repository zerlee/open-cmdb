Django rest framework + vue 的 CMDB 项目

## 后端开发调试

1、linux 下安装 python3 和一些依赖

```
yum install python3 gcc python36-devel python-ldap  openldap openldap24-libs openldap-clients openldap-devel openssl-devel
```

2、 创建虚拟环境

在 open-cmdb 项目根目录下

```
python3 -m venv venv
```

开启虚拟环境

```
. venv/bin/active
```

3、 在虚拟环境开启的情况下，在 backend 目录下 安装后端 python 项目依赖的库

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U

pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

pip install -r requirements.txt
```

4、在 linux 上创建用户 lqs

```
useradd lqs
```

切换到 lqs 用户下，创建用户密钥

```
su lqs
ssh-keygen -t rsa，按三次回车
```

5、修改 setting 文件中的用户名 usera 为 lqs

6、修改 setting 文件中的 ldap 服务器 IP（非必须）

7、修改数据库为 mysql，更改其中的连接信息

使用 mysql 的原因是，对 mysql 的使用更熟悉

8、连接 mysql 创建数据库 cmdb

9、执行数据库迁移

```
python manage.py makemigrations
python manage.py migrate
```

10、创建后台 admin 管理界面的登录账号

```
python manage.py createsuperuser
```

11、启动服务器

```
python manage.py runserver 0.0.0.0:8000
```

12、打开浏览器,登录，查看效果

```
ip:8000/admin
```

13、如果你修改后端代码的话，不用重新运行，改动效果会立即显示

## 前端开发调试

1、安装 node 和 npm

```
cd /opt/software
wget https://nodejs.org/dist/v10.9.0/node-v10.9.0-linux-x64.tar.xz
tar xf  node-v10.9.0-linux-x64.tar.xz
mv /opt/software/node-v10.9.0-linux-x64   /usr/local/node
echo "export PATH=$PATH:/usr/local/node/bin" >> /etc/profile
source /etc/profile
```

2、配置 npm 源

```
npm config set registry https://registry.npm.taobao.org
```

3、安装前端依赖的库，在 frontend 目录下执行

```
npm install
```

如果报错`Error: EACCES: permission denied, open`,
检查 node 安装路径所属用户，如果是 500，则改为 root

```
chown -R root:root /usr/local/node/
```

4、修改/root/open-cmdb/frontend/src/config/index.js 中的 baseurl 为下

```
  baseUrl: {
    dev: 'http://192.168.2.74:8000', //服务器的IP，端口是python后端的端口
    pro: 'http://192.168.2.74:8000'
  },
```

5、启动前端

在 frontend 目录下执行

```
npm run dev
```

6、打开浏览器，登录，查看效果

7、如果你修改前端代码的话，不用重新运行，改动效果会立即显示
