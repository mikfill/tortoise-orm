# HOW TO RUN

## 1. Create virtual env

```bash
python -m venv venv
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Run app

```bash
(venv)python uvicorn main:app --reload
```

### If you run app first time you need to initialize database

Go to endpoint <http://localhost:8000/init-db>

After this  we initialize sqlite database with data come from <https://gorest.co.in/public/v2/> and all ready to work.
