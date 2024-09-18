// @ts-ignore
import styles from './chat.module.css';

interface ChatItemProps {
    text: string;
    date: string;
}

export const ChatItem = ({text, date}: ChatItemProps) => {
    return (
        <div className={styles.chat_item}>
            <p className={styles.chat_text}>{text}</p>
            <p className={styles.chat_date}>{date}</p>
        </div>
    );
};
