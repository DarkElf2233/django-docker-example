FROM nginx:latest
COPY conf /etc/nginx/conf.d/default.conf

# create folder for storing staticfiles
ENV APP_HOME=/home/app/web
RUN mkdir -p ${APP_HOME}
RUN mkdir -p ${APP_HOME}/staticfiles