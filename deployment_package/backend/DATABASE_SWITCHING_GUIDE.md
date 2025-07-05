# 🗄️ Инструкция по переключению между Supabase API и прямым PostgreSQL

## 📋 **Текущее состояние**

Ваше приложение настроено для работы с двумя типами подключения к базе данных:
1. **Supabase API** (по умолчанию) - рекомендуется
2. **Прямое PostgreSQL подключение** - альтернативный вариант

## 🔄 **Переключение режимов**

### **Режим 1: Supabase API (по умолчанию)**
```bash
# В файле /app/backend/.env
USE_POSTGRES=false
```

**Преимущества:**
- ✅ Безопасность (автоматическая аутентификация)
- ✅ Встроенные RLS (Row Level Security) политики
- ✅ Real-time обновления
- ✅ Автоматическое управление соединениями
- ✅ Мониторинг через Supabase Dashboard
- ✅ Простота в развертывании

### **Режим 2: Прямое PostgreSQL подключение**
```bash
# В файле /app/backend/.env
USE_POSTGRES=true
```

**Преимущества:**
- ✅ Полный контроль над запросами
- ✅ Возможность использования сложных SQL операций
- ✅ Прямой доступ к PostgreSQL функциям
- ✅ Меньше абстракций

## 🛠️ **Как переключиться**

### **Способ 1: Изменить переменную среды**
```bash
cd /app/backend
# Для Supabase API
echo "USE_POSTGRES=false" >> .env

# Для прямого PostgreSQL
echo "USE_POSTGRES=true" >> .env

# Перезапустить сервер
sudo supervisorctl restart backend
```

### **Способ 2: Автоматическое переключение**
Создан скрипт для легкого переключения:

```bash
# Переключиться на Supabase API
cd /app/backend && python switch_db.py supabase

# Переключиться на PostgreSQL
cd /app/backend && python switch_db.py postgres
```

## 📊 **Connection strings**

**Supabase API:**
- URL: `https://kykzqxoxgcwqurnceslu.supabase.co`
- Использует анонимный ключ для аутентификации

**Прямой PostgreSQL:**
- URL: `postgresql://postgres:jsjsjdhsivdusbdis267263733673@db.kykzqxoxgcwqurnceslu.supabase.co:5432/postgres`
- Прямое подключение к PostgreSQL серверу

## 🎯 **Рекомендации**

1. **Для продакшена:** Используйте Supabase API (USE_POSTGRES=false)
2. **Для разработки:** Можете экспериментировать с прямым PostgreSQL
3. **Для миграций:** Используйте прямое PostgreSQL подключение

## 🔧 **Устранение неполадок**

Если возникают проблемы с прямым PostgreSQL:
```bash
# Проверить соединение
cd /app/backend && python -c "
import psycopg2
try:
    conn = psycopg2.connect('postgresql://postgres:jsjsjdhsivdusbdis267263733673@db.kykzqxoxgcwqurnceslu.supabase.co:5432/postgres', sslmode='require')
    print('✅ PostgreSQL подключение работает')
    conn.close()
except Exception as e:
    print(f'❌ Ошибка PostgreSQL: {e}')
"
```

## 📝 **Заметки**

- Обе версии используют одну и ту же базу данных Supabase
- Данные остаются одинаковыми независимо от способа подключения
- Переключение не влияет на существующие данные
- При проблемах всегда можно вернуться к Supabase API