# positive
test for positive technologies

python3 -m venv env &&
source env/bin/activate &&
pip install -U pip &&
pip install -r requirements.txt

#### run tests
pytest -v --tb=short