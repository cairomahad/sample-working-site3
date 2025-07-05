#!/bin/bash
# Скрипт для подготовки файлов к развертыванию

echo "🚀 Подготовка файлов для развертывания..."

# Создаем папку для развертывания
mkdir -p deployment_package
cd deployment_package

# Копируем основные файлы приложения
echo "📁 Копирование файлов..."
cp -r ../backend ./
cp -r ../frontend ./
cp ../README_DEPLOYMENT.md ./
cp ../SUPABASE_SETUP_GUIDE.md ./
cp ../HOSTING_GUIDE_RU.md ./
cp ../QUICK_START.md ./

# Создаем файл с переменными окружения для хостинга
echo "🔧 Создание файла переменных окружения..."
cat > deployment_env.txt << 'EOF'
# ПЕРЕМЕННЫЕ ОКРУЖЕНИЯ ДЛЯ ХОСТИНГА

## Backend переменные (.env в папке backend/):
SUPABASE_URL=https://kykzqxoxgcwqurnceslu.supabase.co
SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imt5a3pxeG94Z2N3cXVybmNlc2x1Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MTQ4NzI0OCwiZXhwIjoyMDY3MDYzMjQ4fQ.wZcC233qDjrIuXn4it1j-YnxHak14v8GqxCCuW6VIb4
SECRET_KEY=uroki-islama-secret-key-2024
USE_POSTGRES=false

## Frontend переменные (.env в папке frontend/):
REACT_APP_BACKEND_URL=https://ВАШ_ДОМЕН.ru

## Системные переменные (для панели хостинга):
PYTHON_VERSION=3.11
NODE_VERSION=18
EOF

# Создаем главную инструкцию
cat > README.md << 'EOF'
# 🕌 Исламский образовательный портал "Уроки Ислама"

## 📦 Пакет для развертывания на хостинге

Это готовый пакет для развертывания полнофункционального исламского образовательного портала на российском хостинге.

### 🌟 Что уже настроено:
- ✅ **3 курса** по основам Ислама
- ✅ **Команда преподавателей**
- ✅ **Система тестирования**
- ✅ **Вопросы и ответы имаму**
- ✅ **Админская панель**
- ✅ **Подключение к облачной базе данных**

### 📚 Документация:

1. **QUICK_START.md** - Быстрое развертывание за 15 минут ⚡
2. **HOSTING_GUIDE_RU.md** - Подробная инструкция для российских хостингов 🇷🇺
3. **deployment_env.txt** - Переменные окружения для копирования 🔧
4. **README_DEPLOYMENT.md** - Техническая документация 📖

### 🚀 Быстрый старт:

1. **Загрузите файлы** на хостинг (Timeweb, Beget, Reg.ru)
2. **Скопируйте переменные** из `deployment_env.txt`
3. **Установите зависимости:**
   ```bash
   cd backend && pip install -r requirements.txt
   cd frontend && npm install && npm run build
   ```
4. **Запустите backend:**
   ```bash
   uvicorn server:app --host 0.0.0.0 --port 8000
   ```

### 🔑 Админ доступ:
- **Email:** admin@uroki-islama.ru
- **Пароль:** admin123

### 💾 База данных:
Использует **Supabase** (облачная PostgreSQL) - данные сохраняются постоянно и доступны с любого хостинга.

### 📞 Поддержка:
Если возникли вопросы - читайте `HOSTING_GUIDE_RU.md` с подробными инструкциями.

**🎉 Система автоматически создаст все необходимые данные при первом запуске!**
EOF

# Создаем архив для загрузки
echo "📦 Создание архива для загрузки..."
tar -czf ../uroki_islama_deployment.tar.gz .

cd ..
echo ""
echo "✅ Файлы готовы к развертыванию!"
echo "📦 Архив создан: uroki_islama_deployment.tar.gz"
echo ""
echo "📋 Что делать дальше:"
echo "1. Скачайте архив uroki_islama_deployment.tar.gz"
echo "2. Зарегистрируйтесь на хостинге (Timeweb, Beget, и т.д.)"
echo "3. Загрузите архив на хостинг и извлеките"
echo "4. Следуйте инструкциям в QUICK_START.md (быстро) или HOSTING_GUIDE_RU.md (подробно)"
echo ""
echo "🔑 Админ доступ:"
echo "   Email: admin@uroki-islama.ru"
echo "   Пароль: admin123"