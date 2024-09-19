// @ts-ignore
import styles from './chat.module.css';
import {useEffect, useRef, useState} from "react";
import {Input} from './../Input/Input.tsx';
import {ChatItem} from './ChatItem';
import {getAllMessages} from "../api/requests.ts";

import moment from 'moment';
import {domain} from "../config.ts";

interface Message {
    text: string;
    created_at: string;
}

const errorMessages = [
    {"text": "Connection lost.", "created_at": ""},
    {"text": "Page will be reloaded in 5 seconds.", "created_at": ""}
]

export const Chat = () => {
    const [messages, setMessages] = useState<Message[]>([]);
    const messagesEndRef = useRef<HTMLDivElement | null>(null);
    const socketRef = useRef<WebSocket | null>(null);

    const addMessage = (message: Message) => {
        setMessages((prevMessages) => [...prevMessages, message]);
    };

    useEffect(() => {
        const fetchMessages = async () => {
            try {
                const response = await getAllMessages();
                setMessages(response.data);
            } catch (error) {
                console.error("Ошибка при загрузке сообщений:", error);
            }
        };
        fetchMessages();

        socketRef.current = new WebSocket("https://" + domain + "/api/messages/ws");

        socketRef.current.onmessage = (event) => {
            const newMessage: Message = JSON.parse(JSON.parse(event.data));
            addMessage(newMessage);
        };

        socketRef.current.onclose = () => {
            setMessages(errorMessages);
            console.log("Соединение закрыто. Перезагрузка страницы");
            setTimeout(() => {
                window.location.reload();
            }, 5000);
        }

        socketRef.current.onerror = () => {
            setMessages(errorMessages);
            console.log("Ошибка соединения. Перезагрузка страницы");
            setTimeout(() => {
                window.location.reload();
            }, 5000);
        }

        return () => {
            if (socketRef.current) {
                socketRef.current.close();
            }
        };
    }, []);

    const handleSendMessage = (text: string) => {
        if (socketRef.current) {
            socketRef.current.send(text); // Отправляем сообщение в формате JSON
        }
    };

    useEffect(() => {
        if (messagesEndRef.current) {
            messagesEndRef.current.scrollIntoView({behavior: "smooth"});
        }
    }, [messages]);

    return (
        <div className={styles.chat_container}>
            <div className={styles.chat_messages}>
                {messages.map((message, index) => (
                    <ChatItem key={index}
                              text={message.text}
                              date={
                        message.created_at === "" ? "System Message" : (moment.utc(message.created_at).local().format('HH:mm DD.MM.YYYY'))
                    }/>
                ))}
                <div ref={messagesEndRef}/>
            </div>
            <Input placeholder="Message" onSubmit={handleSendMessage}/>
        </div>
    );
};
