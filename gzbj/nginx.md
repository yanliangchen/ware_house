```
server {
   client_max_body_size 100m;
   listen 80 default_server;
   # listen [::]:80 default_server;


   root /webapp/build;

   # Add index.php to the list if you are using PHP
   index index.html index.htm index.nginx-debian.html;

   server_name _;

   location / {
    # First attempt to serve request as file, then
    # as directory, then fall back to displaying a 404.
    try_files $uri $uri/ =404;
   }

   location /api {
        proxy_pass http://100.98.97.83:8000/api;
   }
}

```

