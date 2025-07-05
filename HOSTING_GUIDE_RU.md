# 🇷🇺 Подробная инструкция по развертыванию на российском хостинге

## 📋 Пошаговое руководство

### Шаг 1: Регистрация на хостинге

#### Вариант A: Timeweb (рекомендуется)

1. **Перейдите на [timeweb.com](https://timeweb.com)**
2. **Нажмите "Зарегистрироваться"**
3. **Выберите тариф "Премиум" или выше** (нужны Python + Node.js)
4. **Зарегистрируйтесь и оплатите**
5. **Дождитесь активации аккаунта**

#### Вариант B: Другие хостинги
- **Beget.com** - выберите тариф с поддержкой Python
- **Reg.ru** - VPS или хостинг с Python
- **Любой VPS** с Ubuntu/CentOS

---

### Шаг 2: Подготовка файлов

1. **Скачайте архив** `uroki_islama_deployment.tar.gz` из папки проекта
2. **Извлеките архив** на своем компьютере
3. **Проверьте содержимое:**
   ```
   deployment_package/
   ├── backend/           # Python API сервер
   ├── frontend/          # React приложение  
   ├── deployment_env.txt # Переменные окружения
   └── DEPLOYMENT_INSTRUCTIONS.md
   ```

---

### Шаг 3: Загрузка на хостинг

#### Через панель управления хостинга:

1. **Войдите в панель управления** хостинга
2. **Найдите раздел "Файловый менеджер"** или "Files"
3. **Перейдите в корневую папку** сайта (обычно `public_html/` или `www/`)
4. **Загрузите архив** `uroki_islama_deployment.tar.gz`
5. **Извлеките архив** через панель управления

#### Через FTP/SFTP:

```bash
# Используйте FileZilla или WinSCP
# Подключитесь к хостингу
# Загрузите содержимое deployment_package/ в корень сайта
```

---

### Шаг 4: Настройка переменных окружения

#### На Timeweb:

1. **Зайдите в панель управления**
2. **Выберите "Сайты" → Ваш домен**
3. **Найдите раздел "Переменные окружения"** или "Environment Variables"
4. **Добавьте переменные:**

```env
SUPABASE_URL=https://kykzqxoxgcwqurnceslu.supabase.co
SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imt5a3pxeG94Z2N3cXVybmNlc2x1Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MTQ4NzI0OCwiZXhwIjoyMDY3MDYzMjQ4fQ.wZcC233qDjrIuXn4it1j-YnxHak14v8GqxCCuW6VIb4
SECRET_KEY=uroki-islama-secret-key-2024
USE_POSTGRES=false
```

#### Альтернативно - создайте .env файлы:

**backend/.env:**
```env
SUPABASE_URL=https://kykzqxoxgcwqurnceslu.supabase.co
SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imt5a3pxeG94Z2N3cXVybmNlc2x1Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MTQ4NzI0OCwiZXhwIjoyMDY3MDYzMjQ4fQ.wZcC233qDjrIuXn4it1j-YnxHak14v8GqxCCuW6VIb4
SECRET_KEY=uroki-islama-secret-key-2024
USE_POSTGRES=false
```

**frontend/.env:**
```env
REACT_APP_BACKEND_URL=https://ваш-домен.ru
```

---

### Шаг 5: Установка зависимостей

#### Через SSH (если доступен):

```bash
# Подключитесь по SSH
ssh username@ваш-домен.ru

# Перейдите в папку backend
cd backend

# Установите Python зависимости
pip install -r requirements.txt
# или
pip3 install -r requirements.txt

# Перейдите в папку frontend
cd ../frontend

# Установите Node.js зависимости
npm install
# или
yarn install
```

#### Через панель управления:

1. **Найдите раздел "Python"** или "Node.js" в панели
2. **Включите поддержку Python 3.8+**
3. **Включите поддержку Node.js 16+**
4. **Загрузите requirements.txt** и укажите путь к нему
5. **Запустите установку зависимостей**

---

### Шаг 6: Сборка frontend

#### Через SSH:
```bash
cd frontend
npm run build
# или
yarn build
```

#### Через панель:
1. **Найдите раздел "Node.js приложения"**
2. **Создайте новое приложение**
3. **Укажите папку:** `frontend`
4. **Команда запуска:** `npm run build`
5. **Запустите сборку**

---

### Шаг 7: Настройка веб-сервера

#### Вариант A: Nginx (рекомендуется)

Создайте файл конфигурации `/etc/nginx/sites-available/uroki-islama`:

```nginx
server {
    listen 80;
    server_name ваш-домен.ru www.ваш-домен.ru;
    
    # Frontend (статические файлы React)
    location / {
        root /path/to/frontend/build;
        try_files $uri $uri/ /index.html;
        
        # Кэширование статических файлов
        location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg)$ {
            expires 1y;
            add_header Cache-Control "public";
        }
    }
    
    # Backend API
    location /api/ {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    # Uploads
    location /uploads/ {
        root /path/to/backend;
        expires 1d;
    }
}
```

#### Вариант B: Apache (.htaccess)

В корне сайта создайте `.htaccess`:

```apache
RewriteEngine On

# API перенаправление
RewriteRule ^api/(.*)$ http://127.0.0.1:8000/api/$1 [P,L]

# Frontend маршрутизация
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule . /index.html [L]
```

---

### Шаг 8: Запуск backend

#### Через SSH:
```bash
cd backend

# Простой запуск
python server.py

# Или через Uvicorn (рекомендуется)
uvicorn server:app --host 0.0.0.0 --port 8000

# Для продакшена с автоперезапуском
uvicorn server:app --host 0.0.0.0 --port 8000 --reload
```

#### Через панель управления:
1. **Найдите раздел "Python приложения"**
2. **Создайте новое приложение**
3. **Путь к приложению:** `backend`
4. **Файл запуска:** `server.py`
5. **Или команда:** `uvicorn server:app --host 0.0.0.0 --port 8000`

---

### Шаг 9: Настройка автозапуска

#### Systemd сервис (для VPS):

Создайте файл `/etc/systemd/system/uroki-islama.service`:

```ini
[Unit]
Description=Uroki Islama Backend
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/path/to/backend
Environment=PATH=/usr/bin:/usr/local/bin
ExecStart=/usr/local/bin/uvicorn server:app --host 0.0.0.0 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
```

Активируйте сервис:
```bash
sudo systemctl enable uroki-islama
sudo systemctl start uroki-islama
sudo systemctl status uroki-islama
```

---

### Шаг 10: Настройка SSL (HTTPS)

#### Через панель хостинга:
1. **Найдите раздел "SSL сертификаты"**
2. **Выберите "Let's Encrypt" (бесплатный)**
3. **Укажите домен**
4. **Дождитесь выпуска сертификата**

#### Через Certbot (для VPS):
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d ваш-домен.ru
```

---

### Шаг 11: Проверка работы

1. **Откройте** `https://ваш-домен.ru`
2. **Проверьте главную страницу** - должны загрузиться курсы
3. **Проверьте API:** `https://ваш-домен.ru/api/courses`
4. **Войдите в админку:**
   - Email: `admin@uroki-islama.ru`
   - Пароль: `admin123`

---

## 🔧 Настройка доменного имени

### Если у вас уже есть домен:

1. **Зайдите в панель управления доменом**
2. **Найдите настройки DNS**
3. **Добавьте A-запись:**
   ```
   @ → IP_адрес_хостинга
   www → IP_адрес_хостинга
   ```

### Если нужно купить домен:

1. **На том же хостинге** (Timeweb, Beget, Reg.ru)
2. **Или отдельно:** Nic.ru, 2domains.ru
3. **Выберите .ru или .рф домен**

---

## 🛠️ Возможные проблемы и решения

### Проблема 1: Не устанавливаются Python зависимости

**Решение:**
```bash
# Обновите pip
pip install --upgrade pip

# Установите по одному
pip install fastapi
pip install uvicorn
pip install supabase
pip install python-dotenv

# Или укажите версию Python
pip3.9 install -r requirements.txt
```

### Проблема 2: Не работает Supabase из России

**Решение A:** Используйте VPN на сервере:
```bash
# Установите VPN клиент на сервер
# Настройте подключение к зарубежному серверу
```

**Решение B:** Используйте российскую альтернативу:
- Supabase может работать через российские провайдеры
- Проверьте доступность в браузере

### Проблема 3: Frontend не собирается

**Решение:**
```bash
# Очистите кэш
npm cache clean --force

# Удалите node_modules и переустановите
rm -rf node_modules
npm install

# Увеличьте память для сборки
NODE_OPTIONS="--max-old-space-size=4096" npm run build
```

### Проблема 4: API недоступен

**Проверьте:**
1. Запущен ли backend процесс
2. Правильно ли настроен proxy в nginx/apache
3. Открыт ли порт 8000
4. Корректны ли переменные окружения

### Проблема 5: Ошибки с базой данных

**Решение:**
```bash
# Проверьте подключение к Supabase
cd backend
python -c "
import asyncio
from supabase_client import supabase_client
asyncio.run(supabase_client.get_records('courses', limit=1))
print('База данных работает!')
"
```

---

## 📞 Поддержка

### Техподдержка хостингов:
- **Timeweb:** support@timeweb.ru, онлайн-чат
- **Beget:** support@beget.ru, телефон
- **Reg.ru:** support@reg.ru

### Проверка статуса Supabase:
- [status.supabase.com](https://status.supabase.com)

---

## ✅ Чек-лист развертывания

- [ ] Зарегистрирован аккаунт на хостинге
- [ ] Загружены файлы проекта
- [ ] Настроены переменные окружения
- [ ] Установлены Python зависимости
- [ ] Установлены Node.js зависимости
- [ ] Собран frontend (`npm run build`)
- [ ] Запущен backend сервер
- [ ] Настроен веб-сервер (nginx/apache)
- [ ] Получен SSL сертификат
- [ ] Настроен домен
- [ ] Проверена работа сайта
- [ ] Проверен вход в админку

---

**🎉 После выполнения всех шагов ваш сайт "Уроки Ислама" будет полностью работать на российском хостинге!**

### Админ доступ:
- **Email:** admin@uroki-islama.ru
- **Пароль:** admin123

### Автоматически созданы:
- ✅ 3 курса по Исламу
- ✅ Команда преподавателей
- ✅ Система Q&A
- ✅ Все необходимые данные