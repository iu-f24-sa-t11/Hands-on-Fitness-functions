// @ts-ignore
import styles from './chat.module.css';
import {useEffect, useRef, useState} from "react";
import {Input} from './../Input/Input.tsx';
import {ChatItem} from './ChatItem';
import {getAllMessages} from "../api/requests.ts";

import moment from 'moment';

interface Message {
    text: string;
    created_at: string;
}

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

        socketRef.current = new WebSocket("ws://localhost/api/messages/ws");

        socketRef.current.onmessage = (event) => {
            const newMessage: Message = JSON.parse(JSON.parse(event.data));
            addMessage(newMessage);
        };

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
                              date={moment(message.created_at).format('HH:mm DD.MM.YYYY')}/>
                ))}
                <div ref={messagesEndRef}/>
            </div>
            <Input placeholder="Message" onSubmit={handleSendMessage}/>
        </div>
    );
};