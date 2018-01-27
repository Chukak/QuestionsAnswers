upstream django {
        # your socket
		server unix:/tmp/QuestionsAnswers.sock;
	}

server {
	listen 8000;
	server_name localhost;

	location / {
		uwsgi_pass django;
		include {your_path_to_app}/QuestionsAnswers/uwsgi_params;
	}

	location /static/ {
		alias {your_path_to_app}/QuestionsAnswers/static/;
	}

	location /media/ {
		alias {your_path_to_app}/QuestionsAnswers/media/;
	}

}
