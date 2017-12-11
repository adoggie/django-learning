
## django提供 contrib.auth  模块用于用户账户管理和权限管理 

对于每一个 ｀model` 默认都具有三种权限 : `add_model`,`change_model`,`delete_model` 。 
用户权限检查 `user.has_perm( 'core.add_user') ` , 权限参数格式: `<app label>.<permission codename>` 。

## settings.py 设置

```python
AUTHENTICATION_BACKENDS = (
  'django.contrib.auth.backends.ModelBackend',
  'guardian.backends.ObjectPermissionBackend', 对象级控制
)
```

## 用户权限操作： 
* user.get_all_permissions() 列出用户所有权限
* user.get_group_permissions() 列出用户所属group的权限
* user.user_permissions.add( permission,...)  添加用户权限
* user.user_permissions.remove( perm ,.. ) 删除权限
* user.user_permissions.clear() 

## 组权限操作:  
**注意： django.contrib.auth.model.Group 用于权限管理，类似角色的概念**

* group.permission.add() 
* group.permisison.remove()/clear()

```python
group = Group.objects.create(name='employees') 创建用户组
user.groups.add(group) 用户添加进组

```
## model 添加权限
```python
class Task(models.Model):
  class Meta:
    permissions = ( 
      ('view_task','can see available tasks'),
      ...
      )
```

## 装饰器 permission_required 
decorator用于将权限检查和用户业务分离. 

```python
@permission_required('car.driver_car')
def myView(request):
  ... 
  
```

## Template 使用权限
 `perms`保存了当前用户所有权限 ，Template中检查权限方式: 
 
 ` {% if perms.car.add_car %} ` 
 
 (判别当前用户是否具有添加car的权限) 
 
 ## django-guardian 实现对象级的权限控制 
 
[django-guardian](https://github.com/django-guardian/django-guardian) 
[doc reference](https://django-guardian.readthedocs.io/) 

**常用方法**
```python

from guardian.shortcuts import assign_perm, get_perms
from guardian.core import ObjectPermissionChecker
from guardian.decorators import permission_required

assign_perm('myapp.drive_car', request.user, mycar) 分配对象和访问权限到用户
assign_perm('myapp.drive_car', mygroup, mycar) 分配对象和访问权限到用户组  这就是细颗粒度的权限控制了


```
**Object permission**
细粒度的对象权限检查

使用ObjectPermissionChecker检查用户的object permission

```python
assign_perm('main.change_post', request.user, post) 分配对象和访问权限到用户组  这就是细颗粒度的权限控制了
checker = ObjectPermissionChecker(request.user)
checker.has_perm('main.change_post', post)  检查 当前用户是否具有修改post对象的权限


```

