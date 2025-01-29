run:
	docker compose up
install:
	make collect
	make migrations
	make migrate
	make superuser
collect:
	docker compose exec app bash -c "poetry run python manage.py collectstatic --noinput"
migrations:
	docker compose exec app bash -c "poetry run python manage.py makemigrations"
migrate:
	docker compose exec app bash -c "poetry run python manage.py migrate"
superuser:
	docker compose exec app bash -c "poetry run python manage.py createsuperuser"
load:
	docker compose exec app bash -c "poetry run python manage.py generate"