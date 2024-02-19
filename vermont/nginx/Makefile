deploy:
	python3 generate_configs.py
	sudo cp conf/* /etc/nginx/sites-enabled/.
	sudo chown -R root:root /etc/nginx/sites-enabled/
	sudo systemctl restart nginx