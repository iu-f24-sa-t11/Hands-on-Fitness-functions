// @ts-ignore
import styles from './chat.module.css';

interface ChatItemProps {
  text: string;
}

export const ChatItem = ({text}: ChatItemProps) => {
  return (
      <div className={styles.chat_item}>
          <p>{text}</p>
      </div>
  );
};