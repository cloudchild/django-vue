django- vue 前后端分离

## 做什么

使用django vue 来实现前后端分离的web项目，以博客crud为例子

## 技术栈

### 后端backends

- django
- django rest framework
- django cors headers

### 前端 fronteds

- vue
- bootstrap
- fontawesome

## 步骤



![image-20201023020451739](C:\Users\asus\AppData\Roaming\Typora\typora-user-images\image-20201023020451739.png)

## 实操

### 后端

#### 1、新建项目文件夹，django-vue

#### 2、创建django项目 

django-admin startproject backend

#### 3、运行项目

cd backend  

python manage.py  runserver

#### 4、创建app

django-admin startapp blog

#### 5、应用配置

#### 6、创建模型

#### 7、数据迁移

#### 8、手动添加数据

python manage.py shell?

![image-20201023191154017](C:\Users\asus\AppData\Roaming\Typora\typora-user-images\image-20201023191154017.png)

![image-20201023191243651](C:\Users\asus\AppData\Roaming\Typora\typora-user-images\image-20201023191243651.png)

#### 9、framework

搜索 django rest framework

- 在项目文件目录下 pip install djangorestframework

- 应用配置 ：'rest_framework',

#### 10、创建serializers

在app目录下新建serializers.py

指定序列化的model和fields

#### 11、views

创建viewset

#### 12、配置路由

在主路由 添加router

from rest_framework import routers

router = routers.DefaultRouter()

views 注册到总路由router.register(...)

router注册到总路由

#### 13、运行程序测试

#### 14、处理前后端cors跨域请求

搜索django cors header

- pip install django-cors-headers

- 配置应用 'corsheaders'

- 添加中间件：

  ![image-20201023193127168](C:\Users\asus\AppData\Roaming\Typora\typora-user-images\image-20201023193127168.png)

- CORS_ORIGIN_ALLOW_ALL = True 粗暴允许所有

## 前端

## 1、安装vue -cli

- 下载node，搜索nodejs

- 安装在d盘需要对环境变量进行配置   

  - 创建node_global 和node_cache 文件夹

  - cmd 中定义两句

    ```
    npm config set prefix “node_global绝对路径”
    npm config set cache "node_cache 绝对路径"
    ```

    --报错的话，在c盘用户文件搜索.npmrc文件。用记事本打开，手动修改

  - 配置环境变量

    系统变量 NODE_PATH : D:\python_learn\nodejs\node_global\node_models

    用户变量：path 添加 D:\python_learn\nodejs\node_global

- 配置淘宝镜像

  npm config set registry https://registry.npm.taobao.org

  检验 ：npm config get registry  

  输出： https://registry.npm.taobao.org

## 2、安装vue/cli

在cmd命令行操作下

`npm install @vue/cli -g`

### 报错npm报错：

npm ERR! request to https://registry.nom.taobao.org/@vue%2fcli failed, reason: 

解决办法:

- 1、通过以下代码查看代理设置，如果返回null那就不需要清理

`npm config get https-proxy`

`npm config get proxy`

- 2，如果返回不是null
  npm config set proxy null

  npm config set https-proxy null

- 重新配置淘宝镜像。不行的话，卸载nodejs ，从第一步安装nodejs 开始

## 3、创建前端项目

在项目根目录下创建vue create frontend

## 4、运行项目

**在cmd 命令操作下**

cd frontend

#### 在前端目录下npm run serve

- 报错

  ![image-20201027233639186](C:\Users\asus\AppData\Roaming\Typora\typora-user-images\image-20201027233639186.png)

  解决办法：

  - 去项目的绝对路径去找node_models文件夹，手动删除

  - 在cmd 项目目录下，npm install

  - 安装完毕之后，再次在终端里面输入命令行：npm run serve 回车

    ![image-20201028001235010](C:\Users\asus\AppData\Roaming\Typora\typora-user-images\image-20201028001235010.png)

    

#### 安装npm install 报错

由于有些npm有些资源被屏蔽或者是国外资源的原因，经常会导致用npm安装依赖包的时候失败，所有我还需要npm的国内镜像---cnpm。

解决办法：

-  安装cnpm

  `npm install -g cnpm --registry=http://registry.npm.taobao.org`

  **注意，在cmd 命令行操作**

## 5、开始修改前端页面index.html

### 注意三个文件

index.html主页 --APP.vue---HelloWorld.vue

![image-20201028001850927](C:\Users\asus\AppData\Roaming\Typora\typora-user-images\image-20201028001850927.png)

![image-20201028001756405](C:\Users\asus\AppData\Roaming\Typora\typora-user-images\image-20201028001756405.png)

![image-20201028001948849](C:\Users\asus\AppData\Roaming\Typora\typora-user-images\image-20201028001948849.png)

### 添加Bootsrtap 美化页面

搜索Bootsrtap

复制模板代码 整个代替index.html

修改<title>\<body>里内容



##### 最基本的模板

请确保你的页面遵循了最新的设计和开发标准。也就是说，使用 HTML5 doctype 并包含 viewport meta 标签以实现正确的响应式行为。把这些东西攒在一起，你的页面应该是这样的：

### fontawesome 字体美化

搜索Font Awesome 图标

### 编写container.vue

页面样式

![image-20201028013550865](C:\Users\asus\AppData\Roaming\Typora\typora-user-images\image-20201028013550865.png)

### 通过bootstrap 添加导航栏

## 6、安装axios

在cmd 命令行窗口 frontend 目录下

npm install axios --save