# HOW TO RUN

## 1. Create virtual env

```bash
python -m venv venv
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Run manage_db.py

```bash
(venv)python manage_db.py
```

After this steps we initialize sqlite database with data come from <https://gorest.co.in/public/v2/>

Models

* User

| Field Name | Data Type | Constraints |
| --- | --- | --- |
| id | Integer | Primary Key |
| name | Character | Maximum Length: 64 |
| email | Character | Maximum Length: 64 |
| gender | Character | Maximum Length: 10 |
| status | Character | Maximum Length: 10 |

* Posts

| Field Name | Data Type | Constraints |
| --- | --- | --- |
| id | Integer | Primary Key |
| user_id | Integer |  |
| title | Character | Maximum Length: 256 |
| body | Text |  |

* Comments

| Field Name | Data Type | Constraints |
| --- | --- | --- |
| id | Integer | Primary Key |
| post_id | Integer |  |
| name | Character | Maximum Length: 64 |
| email | Character | Maximum Length: 64 |
| body | Text |  |

* Todos

| Field Name | Data Type | Constraints |
| --- | --- | --- |
| id | Integer | Primary Key |
| user_id | Integer |  |
| title | Character | Maximum Length: 256 |
| due_on | Datetime |  |
| status | Character | Maximum Length: 10 |

## Add fast api
