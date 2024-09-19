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

#### Structure tree

/project-root
│
├── backend/                 
│   ├── src/
│   │   ├── api/
│   │   │   ├── message/
│   │   ├── core/
│   │   │   ├── database/  // Database which contains all messages
│   │   │   │   ├── models/
│   │   │   │   ├──db.py
│   │   │   ├── websocket/ // Logic for handling websockets
│   │   ├── config.py
│   │   ├── main.py        // Base python file
│   ├── Dockerfile
│   └── requirements.txt
│
├── fitness/               // fitness functions for testing quality attributes
│   ├── maintainability.py
│   ├── reliability.py
│   ├── time_behaviour.py
│
├── frontend/                
│   ├── src/
│   │   ├── Chat/          // Chat component for all messages
│   │   ├── Input/         // Component for creating new message
│   │   ├── api/
│   │   ├── static/        // static files, icons, images
│   │   ├── App.tsx
│   │   ├── config.ts
│   │   ├── index.css
│   │   ├── main.tsx
│   ├── Dockerfile
│   ├── basic config files
│   ├── index.html         // base html file
│           
├── Caddyfile                
├── README.md               
├── docker-compose.yml      
