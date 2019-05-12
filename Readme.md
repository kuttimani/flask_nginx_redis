-----------------
simple flask redis nginx app
at start set counter to 0
and for every hit conter increaded and displayed

to start app:
1. cd to /Users/kuttimani/workspace/redis_nginx/myproj
2. source ../env/bin/activate
3. start the startApp.sh  - which is "nohup gunicorn -b 0.0.0.0:5556 wsgi:app &"
   to kill the process use the following command 
   kill $(ps -ef | grep 'gunicorn' | awk '{print $2}')
4. nginx confirgured to reverse proxy aoo to 8000/flask
  configuration added to
  /usr/local/etc/nginx/nginx.conf  
  location /flask {
       rewrite ^/flask(.*) /$1 break;
       proxy_pass  http://0.0.0.0:5556;
      }
5. nginx started by command #nginx
6. stop nginx by command #nginx -s stop
7. initiate virtual environment by running
   virtualenv <projectname>
   cd <projectname>
   source ./bin/activate
8. to deactivate type #deactivate
9. redis location
   /Users/kuttimani/apps/redis-5.0.4/
  start uaing nohup ./src/redis-server redis.conf &
