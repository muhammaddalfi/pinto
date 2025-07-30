# `Pintö` - Role-Based Access Control (RBAC) dengan FastAPI + JWT + MariaDB

**`Pintö`** *(dalam bahasa Aceh, pintu)* adalah API otentikasi dan manajemen user berbasis JWT + Role + Permission.  

---

## 🔧 Tech Stack

- ✅ FastAPI
- ✅ SQLAlchemy ORM
- ✅ JWT
- ✅ MariaDB
- ✅ Modular Router & Dependency Injection

---

## 📁 Struktur Project

```
fastapi_rbac/
├── app/
│   ├── __init__.py
│   ├── main.py                  # Entry point FastAPI
│   ├── core/
│   │   ├── config.py            # Konfigurasi (env, secret, DB_URL, dll)
│   │   └── security.py          # JWT encode/decode & password hash
│   ├── db/
│   │   ├── database.py          # Engine, session, Base ORM
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── role.py
│   │   │   ├── permission.py
│   │   │   └── association.py   # user_roles, role_permissions, user_permissions
│   ├── schemas/
│   │   ├── user.py
│   │   ├── role.py
│   │   └── permission.py
│   ├── services/
│   │   ├── auth_service.py      # Login, register, token builder
│   │   └── user_service.py      # Assign role/permission ke user
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes_auth.py
│   │   ├── routes_user.py
│   │   ├── routes_role.py
│   │   ├── routes_permission.py
│   │   └── routes_dashboard.py  # Protected endpoint
│   ├── dependencies/
│   │   ├── auth.py              # get_current_user (JWT decoding)
│   │   ├── permission.py        # permission_required
│   │   └── role.py              # role_required
│   └── utils/
│       └── response.py          # (optional) helper
├── .env                         # Konfigurasi environment
├── requirements.txt             # Daftar dependensi
```

---

## 🔐 Endpoint List

| Method | Endpoint                          | Deskripsi                                                  |
|--------|-----------------------------------|------------------------------------------------------------|
| POST   | `/auth/register`                  | Register user baru                                         |
| POST   | `/auth/login`                     | Login dan dapatkan JWT                                     |
| POST   | `/users/assign-role`              | Assign role ke user                                        |
| POST   | `/users/assign-permission`        | Assign permission langsung ke user                         |
| POST   | `/roles/`                         | Buat role baru                                             |
| GET    | `/roles/`                         | List seluruh role                                          |
| POST   | `/roles/assign-permission`        | Berikan permission ke role                                 |
| POST   | `/permissions/`                   | Buat permission baru                                       |
| GET    | `/dashboard/`                     | 🔒 Hanya untuk user dengan permission `view_dashboard`     |

---

## 🔑 Contoh JWT Payload

```json
{
  "sub": "admin",
  "roles": ["admin"],
  "permissions": ["view_dashboard", "manage_user"],
  "exp": 1753866055
}
```

---

## ⚙️ Environment `.env`

```env
DATABASE_URL=mysql+pymysql://username:password@host:port/dbname
SECRET_KEY=super-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 🚀 Menjalankan Server

```bash
uvicorn app.main:app --reload
```

---

## 📘 Docs API via Browser
```
http://127.0.0.1:8000/docs
```
---

## 🧪 Testing via HTTP Client

Contoh:

```http
GET /dashboard/
Authorization: Bearer <JWT_TOKEN>
```

---