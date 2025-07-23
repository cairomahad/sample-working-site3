#!/usr/bin/env python3
import requests
import json

# Configuration
BASE_URL = "https://35f9d4a8-c03f-45bb-8150-a7498528d472.preview.emergentagent.com/api"
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

def get_admin_token():
    """Get admin authentication token"""
    login_url = f"{BASE_URL}/admin/login"
    login_data = {
        "username": ADMIN_USERNAME,
        "password": ADMIN_PASSWORD
    }
    
    response = requests.post(login_url, json=login_data)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception(f"Failed to login: {response.text}")

def add_questions_to_test():
    """Add 30 questions to the test"""
    token = get_admin_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    test_id = "e6e13fab-9b00-4026-b00c-0d067d2207bd"
    
    # 30 questions about fasting
    questions = [
        {
            "question_text": "Сколько основных условий обязательности поста?",
            "question_type": "single_choice",
            "options": [
                {"text": "3", "is_correct": False},
                {"text": "4", "is_correct": True},
                {"text": "5", "is_correct": False},
                {"text": "6", "is_correct": False}
            ],
            "explanation": "Есть 4 основных условия: ислам, совершеннолетие, разумность, физическая способность",
            "points": 1
        },
        {
            "question_text": "Что является первым условием обязательности поста?",
            "question_type": "single_choice",
            "options": [
                {"text": "Ислам", "is_correct": True},
                {"text": "Совершеннолетие", "is_correct": False},
                {"text": "Разумность", "is_correct": False},
                {"text": "Здоровье", "is_correct": False}
            ],
            "explanation": "Человек должен быть мусульманином",
            "points": 1
        },
        {
            "question_text": "Обязан ли соблюдать пост душевнобольной?",
            "question_type": "single_choice",
            "options": [
                {"text": "Да, обязан", "is_correct": False},
                {"text": "Нет, не обязан", "is_correct": True},
                {"text": "Только в определенные дни", "is_correct": False},
                {"text": "По желанию", "is_correct": False}
            ],
            "explanation": "Разумность - одно из условий обязательности поста",
            "points": 1
        },
        {
            "question_text": "Должна ли женщина поститься во время менструации?",
            "question_type": "single_choice",
            "options": [
                {"text": "Да, должна", "is_correct": False},
                {"text": "Нет, но должна возместить позже", "is_correct": True},
                {"text": "Нет, и возмещать не нужно", "is_correct": False},
                {"text": "По желанию", "is_correct": False}
            ],
            "explanation": "В период хайда пост не обязателен, но пропущенные дни нужно возместить",
            "points": 1
        },
        {
            "question_text": "Что означает 'хайд'?",
            "question_type": "single_choice",
            "options": [
                {"text": "Болезнь", "is_correct": False},
                {"text": "Менструация", "is_correct": True},
                {"text": "Беременность", "is_correct": False},
                {"text": "Путешествие", "is_correct": False}
            ],
            "explanation": "Хайд - это менструация",
            "points": 1
        },
        {
            "question_text": "Что означает 'нифас'?",
            "question_type": "single_choice",
            "options": [
                {"text": "Менструация", "is_correct": False},
                {"text": "Послеродовое кровотечение", "is_correct": True},
                {"text": "Болезнь", "is_correct": False},
                {"text": "Путешествие", "is_correct": False}
            ],
            "explanation": "Нифас - это послеродовое кровотечение",
            "points": 1
        },
        {
            "question_text": "Обязан ли поститься немусульманин?",
            "question_type": "single_choice",
            "options": [
                {"text": "Да, обязан", "is_correct": False},
                {"text": "Нет, сначала нужно принять ислам", "is_correct": True},
                {"text": "Только в Рамадан", "is_correct": False},
                {"text": "По желанию", "is_correct": False}
            ],
            "explanation": "Ислам - первое условие обязательности поста",
            "points": 1
        },
        {
            "question_text": "С какого возраста становится обязательным пост?",
            "question_type": "single_choice",
            "options": [
                {"text": "С 7 лет", "is_correct": False},
                {"text": "С 15 лет", "is_correct": False},
                {"text": "С достижения половой зрелости", "is_correct": True},
                {"text": "С 18 лет", "is_correct": False}
            ],
            "explanation": "Совершеннолетие определяется достижением половой зрелости",
            "points": 1
        },
        {
            "question_text": "Можно ли больному человеку не поститься?",
            "question_type": "single_choice",
            "options": [
                {"text": "Нет, должен поститься", "is_correct": False},
                {"text": "Да, если пост может навредить здоровью", "is_correct": True},
                {"text": "Только при высокой температуре", "is_correct": False},
                {"text": "Только по разрешению врача", "is_correct": False}
            ],
            "explanation": "Физическая способность - условие обязательности поста",
            "points": 1
        },
        {
            "question_text": "Что означает 'совершеннолетие' в исламе?",
            "question_type": "single_choice",
            "options": [
                {"text": "18 лет", "is_correct": False},
                {"text": "Достижение половой зрелости", "is_correct": True},
                {"text": "21 год", "is_correct": False},
                {"text": "16 лет", "is_correct": False}
            ],
            "explanation": "В исламе совершеннолетие определяется достижением половой зрелости",
            "points": 1
        },
        {
            "question_text": "Как называется глава о посте?",
            "question_type": "single_choice",
            "options": [
                {"text": "Китабус-салят", "is_correct": False},
                {"text": "Китабус-сиям", "is_correct": True},
                {"text": "Китабус-закят", "is_correct": False},
                {"text": "Китабус-хадж", "is_correct": False}
            ],
            "explanation": "Китабус-сиям - глава о посте",
            "points": 1
        },
        {
            "question_text": "Сколько условий должно выполняться для женщин дополнительно?",
            "question_type": "single_choice",
            "options": [
                {"text": "0", "is_correct": False},
                {"text": "1", "is_correct": True},
                {"text": "2", "is_correct": False},
                {"text": "3", "is_correct": False}
            ],
            "explanation": "Дополнительно для женщин - отсутствие хайда или нифаса",
            "points": 1
        },
        {
            "question_text": "Должен ли ребенок соблюдать пост?",
            "question_type": "single_choice",
            "options": [
                {"text": "Да, обязательно", "is_correct": False},
                {"text": "Нет, до совершеннолетия", "is_correct": True},
                {"text": "Только половину дня", "is_correct": False},
                {"text": "По желанию родителей", "is_correct": False}
            ],
            "explanation": "Совершеннолетие - условие обязательности поста",
            "points": 1
        },
        {
            "question_text": "Что нужно сделать женщине после окончания менструации?",
            "question_type": "single_choice",
            "options": [
                {"text": "Ничего не делать", "is_correct": False},
                {"text": "Возместить пропущенные дни поста", "is_correct": True},
                {"text": "Заплатить фидью", "is_correct": False},
                {"text": "Поститься двойное количество дней", "is_correct": False}
            ],
            "explanation": "Пропущенные дни поста нужно возместить",
            "points": 1
        },
        {
            "question_text": "Является ли здоровье условием поста?",
            "question_type": "single_choice",
            "options": [
                {"text": "Нет", "is_correct": False},
                {"text": "Да, физическая способность", "is_correct": True},
                {"text": "Только для пожилых", "is_correct": False},
                {"text": "Только при хронических болезнях", "is_correct": False}
            ],
            "explanation": "Физическая способность - одно из основных условий",
            "points": 1
        },
        {
            "question_text": "Обязательно ли соблюдать пост путешественнику?",
            "question_type": "single_choice",
            "options": [
                {"text": "Да, всегда", "is_correct": False},
                {"text": "Нет, может не поститься и возместить позже", "is_correct": True},
                {"text": "Только в дальних поездках", "is_correct": False},
                {"text": "По желанию", "is_correct": False}
            ],
            "explanation": "Путешественник может не поститься, но должен возместить",
            "points": 1
        },
        {
            "question_text": "Что означает слово 'сиям'?",
            "question_type": "single_choice",
            "options": [
                {"text": "Молитва", "is_correct": False},
                {"text": "Пост", "is_correct": True},
                {"text": "Закят", "is_correct": False},
                {"text": "Паломничество", "is_correct": False}
            ],
            "explanation": "Сиям означает пост",
            "points": 1
        },
        {
            "question_text": "В каком месяце обязательно соблюдать пост?",
            "question_type": "single_choice",
            "options": [
                {"text": "Шаваль", "is_correct": False},
                {"text": "Рамадан", "is_correct": True},
                {"text": "Мухаррам", "is_correct": False},
                {"text": "Раджаб", "is_correct": False}
            ],
            "explanation": "Обязательный пост соблюдается в месяц Рамадан",
            "points": 1
        },
        {
            "question_text": "Может ли беременная женщина не поститься?",
            "question_type": "single_choice",
            "options": [
                {"text": "Нет, должна поститься", "is_correct": False},
                {"text": "Да, если есть опасность для здоровья", "is_correct": True},
                {"text": "Только в последние месяцы", "is_correct": False},
                {"text": "По желанию", "is_correct": False}
            ],
            "explanation": "Если пост может навредить здоровью матери или ребенка",
            "points": 1
        },
        {
            "question_text": "Что такое 'фидья'?",
            "question_type": "single_choice",
            "options": [
                {"text": "Дополнительная молитва", "is_correct": False},
                {"text": "Компенсация за пропущенный пост", "is_correct": True},
                {"text": "Вид закята", "is_correct": False},
                {"text": "Дополнительный пост", "is_correct": False}
            ],
            "explanation": "Фидья - компенсация для тех, кто не может поститься",
            "points": 1
        },
        {
            "question_text": "Обязан ли пожилой человек поститься?",
            "question_type": "single_choice",
            "options": [
                {"text": "Да, всегда", "is_correct": False},
                {"text": "Нет, если не способен физически", "is_correct": True},
                {"text": "Только половину дня", "is_correct": False},
                {"text": "Только по желанию", "is_correct": False}
            ],
            "explanation": "Если нет физической способности, пост не обязателен",
            "points": 1
        },
        {
            "question_text": "Когда женщина должна возместить пост?",
            "question_type": "single_choice",
            "options": [
                {"text": "Сразу после окончания менструации", "is_correct": False},
                {"text": "До следующего Рамадана", "is_correct": True},
                {"text": "В течение месяца", "is_correct": False},
                {"text": "Когда захочет", "is_correct": False}
            ],
            "explanation": "Возмещение должно быть до следующего Рамадана",
            "points": 1
        },
        {
            "question_text": "Что нужно для соблюдения поста кроме условий?",
            "question_type": "single_choice",
            "options": [
                {"text": "Только условия", "is_correct": False},
                {"text": "Намерение (ния)", "is_correct": True},
                {"text": "Разрешение имама", "is_correct": False},
                {"text": "Специальная одежда", "is_correct": False}
            ],
            "explanation": "Намерение (ния) обязательно для поста",
            "points": 1
        },
        {
            "question_text": "Можно ли принимать лекарства во время поста?",
            "question_type": "single_choice",
            "options": [
                {"text": "Нет, никогда", "is_correct": False},
                {"text": "Да, если необходимо для здоровья", "is_correct": True},
                {"text": "Только в форме инъекций", "is_correct": False},
                {"text": "Только витамины", "is_correct": False}
            ],
            "explanation": "При необходимости лечения можно принимать лекарства",
            "points": 1
        },
        {
            "question_text": "Что происходит с постом при болезни?",
            "question_type": "single_choice",
            "options": [
                {"text": "Должен продолжать поститься", "is_correct": False},
                {"text": "Может прервать и возместить позже", "is_correct": True},
                {"text": "Пост становится недействительным", "is_correct": False},
                {"text": "Должен заплатить фидью", "is_correct": False}
            ],
            "explanation": "Больной может прервать пост и возместить после выздоровления",
            "points": 1
        },
        {
            "question_text": "Кто освобождается от возмещения поста?",
            "question_type": "single_choice",
            "options": [
                {"text": "Никто", "is_correct": False},
                {"text": "Те, кто не может поститься постоянно", "is_correct": True},
                {"text": "Все больные", "is_correct": False},
                {"text": "Все пожилые", "is_correct": False}
            ],
            "explanation": "При постоянной неспособности поститься платят фидью",
            "points": 1
        },
        {
            "question_text": "Когда начинается время поста?",
            "question_type": "single_choice",
            "options": [
                {"text": "С восходом солнца", "is_correct": False},
                {"text": "С рассветом (фаджр)", "is_correct": True},
                {"text": "В полночь", "is_correct": False},
                {"text": "После утренней молитвы", "is_correct": False}
            ],
            "explanation": "Пост начинается с наступлением времени фаджра",
            "points": 1
        },
        {
            "question_text": "Когда заканчивается время поста?",
            "question_type": "single_choice",
            "options": [
                {"text": "На закате (магриб)", "is_correct": True},
                {"text": "После вечерней молитвы", "is_correct": False},
                {"text": "В полночь", "is_correct": False},
                {"text": "Когда станет темно", "is_correct": False}
            ],
            "explanation": "Пост заканчивается с наступлением времени магриба",
            "points": 1
        },
        {
            "question_text": "Что нарушает пост?",
            "question_type": "single_choice",
            "options": [
                {"text": "Только еда и питье", "is_correct": False},
                {"text": "Еда, питье и интимная близость", "is_correct": True},
                {"text": "Только еда", "is_correct": False},
                {"text": "Разговор", "is_correct": False}
            ],
            "explanation": "Основные нарушители поста: еда, питье и интимная близость",
            "points": 1
        },
        {
            "question_text": "Нарушает ли пост случайный прием пищи?",
            "question_type": "single_choice",
            "options": [
                {"text": "Да, всегда", "is_correct": False},
                {"text": "Нет, если по забывчивости", "is_correct": True},
                {"text": "Только если съел много", "is_correct": False},
                {"text": "Зависит от времени дня", "is_correct": False}
            ],
            "explanation": "Случайный прием пищи по забывчивости не нарушает пост",
            "points": 1
        }
    ]
    
    success_count = 0
    total_questions = len(questions)
    
    print(f"🚀 Добавление {total_questions} вопросов в тест...")
    
    for i, question_data in enumerate(questions, 1):
        # Create question
        create_url = f"{BASE_URL}/admin/tests/{test_id}/questions"
        response = requests.post(create_url, headers=headers, json=question_data)
        
        if response.status_code == 200:
            success_count += 1
            print(f"✅ Вопрос {i}/{total_questions} добавлен")
        else:
            print(f"❌ Ошибка добавления вопроса {i}: {response.text}")
    
    print(f"\n📊 Результат: {success_count}/{total_questions} вопросов успешно добавлено")
    
    return success_count == total_questions

def main():
    print("📝 Добавление вопросов в тест 'Китабус-сиям'...")
    
    success = add_questions_to_test()
    
    if success:
        print("\n✅ Все вопросы успешно добавлены!")
        print("\n🎯 Особенности теста:")
        print("• Всего вопросов в банке: 30")
        print("• Показывается студенту: 10 случайных вопросов")
        print("• Время прохождения: 15 минут")
        print("• Проходной балл: 70%")
        print("• Максимум попыток: 3")
        print("\n🔄 Система рандомизации настроена автоматически - при каждом запуске теста будет выбираться 10 случайных вопросов из 30 доступных.")
    else:
        print("\n❌ Не все вопросы были добавлены. Проверьте ошибки выше.")

if __name__ == "__main__":
    main()