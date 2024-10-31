# build_files.sh
# pip install pipenv

# pipenv install
pip install -r requirements.txt

# make migrations
python manage.py migrate 
python manage.py collectstatic