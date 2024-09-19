# Assignment 2 - Hands-on: Fitness Functions

## Course
Innopolis University, Fall 2024, Software Architecture

## Team 11
| Full name       | Group     | Email                           |
|-----------------|-----------|---------------------------------|
| Azamat Bayramov | B22-SD-03 | a.bayramov@innopolis.university |
| Darya Koncheva  | B22-SD-02 | d.koncheva@innopolis.university |
| Matthew Rusakov | B22-SD-03 | m.rusakov@innopolis.university  |
| Egor Valikov    | B22-CBS-01| e.valikov@innopolis.university  |

## Project Structure
#### Backend
FastAPI powers the anonymous chat system, handling message processing and storage. MongoDB is used to store messages while maintaining user anonymity.

#### Frontend
Developed with React, TypeScript, and Vite, providing a user-friendly interface for sending and receiving anonymous messages.

#### Caddy
Functions as a reverse proxy for both frontend and backend services, enabling secure HTTPS connections to protect user anonymity and data integrity.


/project-root
│
├── backend/                 
│   ├── src/
│   │   ├── api/
│   │   │   ├── message/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── routes.py
│   │   │   │   ├── schemas.py
│   │   │   │   ├── service.py
│   │   │   ├── __init__.py
│   │   ├── core/
│   │   │   ├── database/
│   │   │   │   ├── models/
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── message.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├──db.py
│   │   │   ├── websocket/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── manager.py
│   │   │   ├── __init__.py
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── main.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── fitness/                 
│   ├── maintainability.py
│   ├── reliability.py
│   ├── time_behaviour.py
│
├── frontend/                
│   ├── src/
│   │   ├── Chat/
│   │   │   ├── Chat.tsx
│   │   │   ├── ChatItem.tsx
│   │   │   ├── chat.module.css
│   │   ├── Input/
│   │   │   ├── Input.tsx
│   │   │   ├── input.module.css
│   │   ├── api/
│   │   │   └── requests.ts
│   │   ├── static/
│   │   │   ├── SendIcon.tsx
│   │   │   ├── chat.svg
│   │   │   ├── send.svg
│   │   ├── App.tsx
│   │   ├── config.ts
│   │   ├── index.css
│   │   ├── main.tsx
│   ├── .gitignore
│   ├── Dockerfile
│   ├── eslint.config.js
│   ├── index.html
│   ├── package-lock.json
│   ├── package.json
│   ├── tsconfig.app.json
│   ├── tsconfig.json
│   ├── tsconfig.node.json
│   └── vite.config.ts
│
├── .env.sample              
├── .gitignore              
├── Caddyfile                
├── README.md               
├── docker-compose.yml      

