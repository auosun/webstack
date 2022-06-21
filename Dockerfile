FROM node:13.12.0-alpine as node
WORKDIR /app/frontend
COPY ./frontend ./
RUN npm install
RUN npm run build

FROM python:3.8
ENV PYTHONUNBUFFERED 1
COPY --from=node /app/frontend/build /app/web
WORKDIR /app/api
COPY . .
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
RUN python manage.py collectstatic --noinput
RUN cp -r ./static /app/web/
EXPOSE 8000
CMD ["sh", "-c", "cp -r /app/web/* /app/www/ && python manage.py runserver 0.0.0.0:8000"]