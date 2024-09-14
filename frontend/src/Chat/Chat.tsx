// @ts-ignore
import styles from './chat.module.css';
import { useState } from "react";
import { Input } from './../Input/Input.tsx'
import { ChatItem } from './ChatItem';

export const Chat = () => {
  const [messages, setMessages] = useState<string[]>([]); // Используем string[] для массива строк

  const addMessage = (message: string) => {
    setMessages((prevMessages) => [...prevMessages, message]);
  };

  return (
    <div className={styles.chat_container}>
      <div className={styles.chat_messages}>
        {messages.map((message, index) => (
          <ChatItem key={index} text={message} />
        ))}
      </div>
      <Input placeholder="Message" onSubmit={addMessage} />
    </div>
  );
};
