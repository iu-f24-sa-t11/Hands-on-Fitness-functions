// @ts-ignore
import styles from './input.module.css';
import {FormEvent, useState} from "react";
import sendSvg from "../static/send.svg";

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

    return (
        <form className={styles.form} onSubmit={handleSubmit}>
            <textarea
                placeholder={placeholder}
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                className={styles.input}
                rows={5}
            />
            <button type="submit" className={styles.submit_button}>
                <img src={sendSvg} alt="send" style={{width: 30, height: 30}}/>
            </button>
        </form>
    );
};