# build_files.sh
# pip install pipenv

# pipenv install
pip3 install --upgrade pip
pip3 install -r requirements.txt

# make migrations
python3.11 manage.py migrate 
python3.11 manage.py collectstatic