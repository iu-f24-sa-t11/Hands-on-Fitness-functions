// @ts-ignore
import styles from './input.module.css';
import {FormEvent, useState, KeyboardEvent} from "react";
import {SendIcon} from "../static/SendIcon.tsx";

interface SearchProps {
    placeholder: string;
    onSubmit: (value: string) => void;
}

export const Input = ({placeholder, onSubmit}: SearchProps) => {
    const [inputValue, setInputValue] = useState(""); // Локальное состояние для текста

    const handleSubmit = (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        const trimmedValue = inputValue.trim();
        if (trimmedValue) {
            onSubmit(trimmedValue);
            setInputValue(""); // Очистка поля
        }
    };

    const handleKeyDown = (e: KeyboardEvent<HTMLTextAreaElement>) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSubmit(e as unknown as FormEvent<HTMLFormElement>);
        }
    };

    return (
        <form className={styles.form} onSubmit={handleSubmit}>
            <textarea
                placeholder={placeholder}
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                onKeyDown={handleKeyDown}
                className={styles.input}
                rows={5}
            />
            <button type="submit" className={styles.submit_button}>
                <SendIcon/>
            </button>
        </form>
    );
};
