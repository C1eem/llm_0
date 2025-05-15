from tokenizer import TechnicalTokenizer

text = """
Пример описания RESTful API для работы с пользователями. 
Для аутентификации используется OAuth2 токен. Пример запроса:
GET /v1/users/{id} возвращает JSON-объект пользователя.
Максимальное время ответа - 500ms. Для микрокода (мкд) 
используется специальный формат. Конфигурация хранится в 
/etc/api/config.json. UUID сессии: 550e8400-e29b-41d4-a716-446655440000.
"""

tokenizer = TechnicalTokenizer()

a = tokenizer.tokenize(text)

for i in a:
    print(i)