# DevFiles

Этот проект представляет собой веб-приложение на базе Django, с фронтендом и интеграцией с Telegram ботом. Проект разработан для демонстрации основных функциональных возможностей Django в сочетании с интерфейсом пользователя и взаимодействием через мессенджер Telegram.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/humoyunxujaev/devfiles.git
   
  1. Create a virtual environment:
     ```bash
     python -m venv venv
     ```

  2.Activate the virtual environment:
      For Windows:
         ```bash
         venv\Scripts\activate
         ```
      For Unix/Mac:
      ```bash
      source venv/bin/activate
      ```
  3.Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
  4.Apply migrations:
    ```bash
    python manage.py migrate
    ```
  5. Run the development server:
    ```bash
    python manage.py runserver
    ```
  6. Create a Telegram bot and obtain the token from BotFather. Set the token in the settings.py file:
  ```bash
  BOT_TOKEN = 'your_telegram_bot_token'
  ```
  7. Run the bot
      ```bash
      python bot.py
      ```
      

Usage
1.Start the development server:
  ```bash
python manage.py runserver
```
2.Open a web browser and go to http://localhost:8000/.
3.Interact with the web application and the Telegram messenger to demonstrate integration.

Project Structure 
mysite/: main Django application.
templates/: HTML templates.
static/: static files (CSS, JavaScript).
bot.py/: telegram bot script
manage.py: main Django management script.


Authors
humoyunxujaev 
    

    

