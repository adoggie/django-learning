
nginx -t 测试配置

nginx -s reload 重新加载

```
        autoindex_exact_size off;  显示M大小
        charset utf-8,gbk;      显示中文
        
        location /share {       文件目录
          autoindex on;
          alias /home/share;
        }
```
