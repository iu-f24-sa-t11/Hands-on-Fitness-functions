# Используем базовый образ Node.js для сборки
FROM node:20 AS build

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем package.json и package-lock.json
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем весь проект в рабочую директорию
COPY . .

ARG DOMAIN

RUN sed -i "s/{domain-here}/$DOMAIN/g" ./src/config.ts

# Собираем приложение
RUN npm run build

# Используем образ NGINX для продакшн-сервера
FROM nginx

# Копируем сгенерированные файлы сборки в папку, которая обслуживается NGINX
COPY --from=build /app/dist /usr/share/nginx/html

# Экспонируем порт
EXPOSE 80

# Стартуем NGINX
CMD ["nginx", "-g", "daemon off;"]
