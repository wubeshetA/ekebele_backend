# build_files.sh
# pip install pipenv

# pipenv install
pip3 install --upgrade pip
pip3 install -r requirements.txt

# make migrations
python3 manage.py migrate 
python3 manage.py collectstatic
