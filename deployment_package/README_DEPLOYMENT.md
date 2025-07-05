# 🕌 Исламский образовательный портал "Уроки Ислама"

## 📋 О системе

Это полнофункциональная образовательная платформа для изучения основ Ислама, созданная с использованием современных технологий:

- **Frontend**: React.js с Tailwind CSS
- **Backend**: FastAPI (Python)
- **База данных**: Supabase (PostgreSQL)
- **Аутентификация**: JWT токены
- **Файловое хранилище**: Локальное с возможностью загрузки

## 🌟 Основные функции

### Для учеников:
- 📚 Просмотр курсов и уроков
- 🎯 Прохождение тестов
- 🏆 Система баллов и лидерборд
- ❓ Раздел вопросов и ответов имама
- 👥 Информация о команде преподавателей

### Для администраторов:
- 🔧 Управление курсами и уроками
- 📝 Создание и редактирование тестов
- 👥 Управление командой
- 📊 Система Q&A
- 📈 Статистика и аналитика

## 🔗 Подключение к Supabase

### Текущие настройки:
```bash
SUPABASE_URL=https://kykzqxoxgcwqurnceslu.supabase.co
SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
USE_POSTGRES=false
```

### Автоматическая инициализация:
Система автоматически создает качественные демо-данные при запуске:
- ✅ 3 основных курса по Исламу
- ✅ Команда преподавателей
- ✅ Админский аккаунт (admin@uroki-islama.ru / admin123)

## 🚀 Развертывание на хостинге

### 1. Переменные окружения:

#### Backend:
```env
SUPABASE_URL=https://kykzqxoxgcwqurnceslu.supabase.co
SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imt5a3pxeG94Z2N3cXVybmNlc2x1Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MTQ4NzI0OCwiZXhwIjoyMDY3MDYzMjQ4fQ.wZcC233qDjrIuXn4it1j-YnxHak14v8GqxCCuW6VIb4
SECRET_KEY=uroki-islama-secret-key-2024
USE_POSTGRES=false
```

#### Frontend:
```env
REACT_APP_BACKEND_URL=https://ваш-домен.com
```

### 2. Критически важные файлы:

- `/backend/supabase_client.py` - Клиент базы данных
- `/backend/server.py` - Основной API сервер
- `/backend/models.py` - Модели данных
- `/backend/autostart_supabase.py` - Автоинициализация
- `/frontend/.env` и `/backend/.env` - Конфигурация

### 3. Проверка работоспособности:

```bash
# Запуск проверки всех компонентов
python setup_supabase.py

# Ручная проверка API
curl https://ваш-домен.com/api/courses

# Проверка админки
# Логин: admin@uroki-islama.ru
# Пароль: admin123
```

## 📚 Демо-контент

Система автоматически создает следующие курсы:

1. **"Основы Ислама"** - Базовый курс (8 уроков, 32 часа)
2. **"Очищение и молитва"** - Практические навыки (6 уроков, 24 часа)
3. **"Изучение Корана"** - Углубленное изучение (12 уроков, 48 часов)

## 👥 Команда преподавателей

- **Имам Али Евтеев** - Основы веры и этика
- **Устаз Абдуль-Басит** - Коран и хадисы
- **Хафиз Микаиль** - История Ислама

## 🔐 Доступы

### Администратор:
- Email: `admin@uroki-islama.ru`
- Пароль: `admin123`

### Тестовые студенты:
Регистрируются автоматически при входе через любой email

## 🛠️ Скрипты для обслуживания

### Автоматическая настройка:
```bash
python setup_supabase.py
```

### Проверка подключения:
```bash
cd backend && python -c "
import asyncio
from supabase_client import supabase_client
asyncio.run(supabase_client.get_records('courses', limit=1))
print('✅ Supabase работает!')
"
```

### Ручная инициализация данных:
```bash
cd backend && python autostart_supabase.py
```

## 🌐 URL структура

### Публичные страницы:
- `/` - Главная страница
- `/lessons` - Каталог курсов
- `/lessons/{course-slug}` - Уроки курса
- `/lessons/{course-slug}/{lesson-slug}` - Страница урока
- `/qa` - Вопросы и ответы
- `/leaderboard` - Лидерборд
- `/about` - О проекте

### API эндпоинты:
- `GET /api/courses` - Список курсов
- `GET /api/team` - Команда
- `POST /api/auth/login` - Авторизация
- `GET /api/admin/*` - Админские функции

## 📊 База данных Supabase

### Основные таблицы:
- `courses` - Курсы
- `lessons` - Уроки
- `tests` - Тесты
- `admin_users` - Администраторы
- `students` - Студенты
- `team_members` - Команда
- `qa_questions` - Вопросы имаму

### Доступ к Supabase Dashboard:
1. Перейдите на https://app.supabase.com
2. Найдите проект: `kykzqxoxgcwqurnceslu`
3. Просматривайте данные, таблицы, статистику

## 🔄 Автоматическое обновление

При каждом запуске сервера:
1. Проверяется подключение к Supabase
2. Удаляются тестовые/некачественные данные
3. Создаются качественные демо-курсы (если нужно)
4. Обеспечивается наличие админа и команды

## 🆘 Поддержка

### При проблемах:
1. Проверьте переменные окружения
2. Убедитесь в доступности интернета к supabase.co
3. Запустите `python setup_supabase.py`
4. Проверьте логи сервера

### Backup конфигурации:
Система автоматически создает резервные копии важных файлов в `supabase_backup_*.tar.gz`

## 📖 Документация

- **SUPABASE_SETUP_GUIDE.md** - Подробное руководство по Supabase
- **test_result.md** - История тестирования и изменений
- **backend/autostart_supabase.py** - Автоинициализация данных
- **setup_supabase.py** - Полная проверка системы

---

**🚀 Система готова к развертыванию и будет автоматически работать с Supabase базой данных на любом хостинге!**