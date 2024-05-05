# CMS 專案練習

## Settings

### 設定 Template & Static
- Template:
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates').replace('\\', '/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

- static:
```
STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    ('images', os.path.join(STATIC_ROOT, 'images').replace('\\','/')),
    ('css', os.path.join(STATIC_ROOT, 'css').replace('\\','/')),
    ('js', os.path.join(STATIC_ROOT, 'js').replace('\\','/')),
)

```

### 設定資料庫

#### 開啟新的資料庫
- database:
- 本次使用資料庫名稱為: servercms
```
create database servercms default character set utf8 collate utf8_general_ci;
```
#### 建立使用者
```
create user '(username)'@'%' identified by '(password)';
```
- '%': 任何IP端皆可用該username 登入
- username: 本專案使用 vincent
- password: 本專案使用 987456321

```
grant all privileges on (database).* to '(username)'@'%';
```
- 允許 (username) 使用者使用 (database) 資料庫內容

```
flush privileges;
```
- 立即生效

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'servercms',
        'USER': 'vincent',
        'PASSWORD':'987456321',
        'HOST':'localhost',
        'PORT':'3306',
    }
}
```


### i18n (國際化)

### CMS (App)
