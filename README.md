## Запуск
  1. Активируйте виртуальную среду
  2. Установите зависимости: `pip install -r requirements.txt` <br/>Если версия Python выше 3.8 то отредактируйте `requirements.txt`. 
  3. Нужно заменить: `backports.zoneinfo==0.2.1` на `backports.zoneinfo;python_version<"3.9"`
  4. Запуск сервера разработки: `python manage.py runserver`

## Получение доступа к API
Зарегистрируйтесь по ссылке http://localhost:8000/app/register

Далее перейдите на http://localhost:8000/api/adds и авторизуйтесь, вы увидете список всех объяевлений из БД
Чтобы отправить запрос на конкретное объявление нужно указать http://localhost:8000/api/adds/<add_id>. `add_id` указан по ссылке http://localhost:8000/api/adds для кажого объявления. Например: http://localhost:8000/api/adds/103794726

Можно просмотреть все таблицы БД по ссылке http://localhost:8000/admin (логин:admin, пароль:1234)

### **_Важно!_**
В результате нормализации из модели Add была выделена новая модель Author. Поле Author в модели Add - внешний ключ. В json(при запросе к api) в поле author показывается первичный ключ из таблицы Author.
Имена авторов объявлений можно посмотреть в панели администратора http://localhost:8000/admin
