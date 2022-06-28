# Django_WebStack

> 一款基于 Django 和 [WebStackPage](https://github.com/WebStackPage/WebStackPage.github.io) 网站导航系统

![](https://aupicgo.oss-cn-shanghai.aliyuncs.com/img/202206261902482.png)  

[Project Management Kanban](https://wekan.jzy.pub/b/xGTmLaEDTF9p3axAr/webstack)

## 特性

1. WebStack页面，可配置  
2. 前后端分离，便于协作开发更多新功能
3. 网站导航增加环境变量，能够根据不同环境自动转换网络地址

## 待发布版本 1.0 

版本 1.0 开发周期为 3个月  
开发时间：  
2022.06.23 - 2022.09.23

### 前端

- [x] 拆分前端界面，使用React进行简单重建，能够使用导航站基础功能 2022.06.24
- [x] 增加环境切换按钮，并使用该按钮能够快速切换导航站收录站点的网络地址 2022.6.26
- [ ] 设计开发快速录入页面
- [ ] 将WebStack使用React重新构建以支撑后期新功能的开发
- [ ] 开发管理界面替代django-admin

### 后端

- [x] 使用 django + django-rest-framework 构建站点导航功能 2022.06.23
- [x] 开发环境功能，能够在查询站点列表时通过环境参数获取不同的网站链接 2022.06.24
- [ ] 开发快速录入功能，能够快速录入站点
- [ ] 使用jwt替代django用户认证系统
- [ ] 构建后台管理系统 替代django-admin

## 版本 2.0

### 特性

1. 使用无障碍重新开发前端界面 能够帮助阅读障碍人群通过导航获取到自己想要的信息

## Thanks
前端设计：[**WebStackPage**](https://github.com/WebStackPage/WebStackPage.github.io)

Web框架：[**Django**](https://github.com/django/django) 后台使用 Django-Admin 
