# Kitten

## Чтобы запустить бота нужно:

1. Установить [Python 3.10+](https://www.python.org/downloads/)
2. Установить [Poetry](https://python-poetry.org/docs/#installation)
3. Установить зависимости командой `poetry install` в корневой папке проекта
4. Перейти к [BotFather](https://t.me/BotFather) в Telegram и создать бота, получить токен
5. Запустить бота командой `poetry run python main.py` в корневой папке проекта
    - При первом запуске бота будет создан файл `config.json` в корневой папке проекта, в котором нужно будет указать
      токен бота, полученный в пункте 4
6. Перейти к боту в Telegram и написать `/start`
7. А теперь развлекайтесь!
    - перво-наперво, нужно разобраться как это всё работает, поэтому рекомендую
      прочитать [документацию](https://docs.aiogram.dev/en/dev-3.x/)
    - по-хорошему нужно добавить комментарии к коду, максимально подробные и красивые...
8. Также можно расширить функционал бота
    - Оформить бота в BotFather (иконки, описание, команды)
    - добавить новые подписи к котикам — генерируемые с помощью марковских
      цепей на наборе кошачьих звуков; или прицепить какой-нибудь общедоступный ИИ
    - добавить новые команды, например, с другими животными, или мемами, или историями, или с музыкой, что угодно,
      серьёзно...
9. Поизучать дополнительно
    - [aiogram](https://docs.aiogram.dev/en/dev-3.x/)
    - [aiogram-dialog](https://aiogram-dialog.readthedocs.io/en/latest/) — более красивые диалоги (реально крутые и
      гибкие)
    - [fastapi](https://fastapi.tiangolo.com/) — для создания более сложных ботов (например, с веб-интерфейсом)
    - [sqlalchemy](https://docs.sqlalchemy.org/en/14/) — для работы с базами данных