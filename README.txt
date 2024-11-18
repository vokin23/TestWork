Для запуска проекта необходимо:
1. Клонировать репозиторий
2. В корне проекта создать файл .env и заполнить его данными, пример:
DB_HOST=postgres
DB_PORT=5432
DB_USER=test
DB_PASS=test
DB_NAME=test
MODE=DEV
3. Создать сеть командой docker network create TestNetwork
4. Запустить проект командой docker-compose up --build
5. После запуска проекта можно перейти на адрес http://localhost:8000/docs и потыкать СВАГЕР :)
