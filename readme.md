# CMS 專案練習

## Settings

### 建立超級使用者
- python manage.py createsuperuser
- username: admin password:Egg790508

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

## 密碼產生器 (APP)

## 帳號管理 (APP): account

### 建立註冊頁面的方法
1. 傳統方法
2. 使用Django 內建 UserCreationForm
    - 不需要再次製作 html頁面
    - 實作功能已包含(檢查重複、登入、登出...)

### 新增使用者至MySQL
- 使用內建 User類別
    - 簡化建立 model 跟 儲存問題

- views.py
```
from django.contrib.auth.models import User
```
- def register
```
User.objects.create_user(username=username, password=password1).save()
```

- 註冊成功後，直接轉向登入頁面

### 登入/出功能製作
- views.py -> user_login/user_logout

## Todo 功能
- model 新增欄位或修改時都需要 makemigrations
- 註冊資料表至後臺: admin.py

### (Foreignkey)一對一關聯
- 範例: Todo models.py
- User <--> Todo
- 引用外部 models: User
```
user = models.ForeignKey(User, on_delete=models.CASCADE)
```
- on_delete=models.CASCADE: 當User 被刪除時，Todo model內容也會被刪除

### 顯示特定使用者資訊
- views.py: 使用 filter
```
todos = Todo.objects.filter(user=request.user)
```

### 顯示單一資料表資訊
- views.py: viewlist

### 建立資料表內容
- forms.py (新增檔案)
```
class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'text', 'important']
        # fields = '__all__' # 全部欄位
```
- views.py: create_todo

### 更新資料表
- views.py

### 刪除

### 使用 login_required 修飾字
- @login_required: 登入後才能操作

- settings.py: 設定使用者若未登入，導回 登入頁面
```
LOGIN_URL = 'login'
```

