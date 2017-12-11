
django提供 contrib.auth  模块用于用户账户管理和权限管理 

对于每一个 ｀model` 默认都具有三种权限 : `add_model`,`change_model`,`delete_model` 。 
用户权限检查 `user.has_perm( 'core.add_user') ` , 权限参数格式: `<app label>.<permission codename>` 。

用户权限操作： 
* user.get_all_permissions() 列出用户所有权限
* user.get_group_permissions() 列出用户所属group的权限
* user.user_permissions.add( permission,...)  添加用户权限
* user.user_permissions.remove( perm ,.. ) 删除权限
* user.user_permissions.clear() 

组权限操作: 

* group.permission.add() 
* group.permisison.remove()/clear()

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
 `perms`保存了当前用户所有权限 ，Template中检查权限方式: ` {% if perms.car.add_car %} ` (判别当前用户是否具有添加car的权限) 
 
 
 

