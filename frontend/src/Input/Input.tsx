// @ts-ignore
import styles from './input.module.css';
import {FormEvent, useState, useRef, useEffect, KeyboardEvent} from "react";
import {SendIcon} from "../static/SendIcon.tsx";

interface SearchProps {
    placeholder: string;
    onSubmit: (value: string) => void;
}

export const Input = ({placeholder, onSubmit}: SearchProps) => {
    const [inputValue, setInputValue] = useState(""); // Локальное состояние для текста
    const textareaRef = useRef<HTMLTextAreaElement>(null); // Реф для textarea
    const isMobile = /Mobi|windows phone|android|iPad|iPhone|iPod/i.test(navigator.userAgent || navigator.vendor);

    // Устанавливаем фокус на textarea при каждом рендере
    useEffect(() => {
        const savedValue = sessionStorage.getItem('textareaValue');
        if (savedValue) {
            setInputValue(savedValue);
        }

        if (textareaRef.current) {
            textareaRef.current.focus();
        }
    }, []);

    // Обновляем sessionStorage при каждом изменении inputValue
    useEffect(() => {
        sessionStorage.setItem('textareaValue', inputValue);
    }, [inputValue]);

    // Обработчик отправки формы
    const handleSubmit = (e: FormEvent<HTMLFormElement> | KeyboardEvent) => {
        e.preventDefault();
        const trimmedValue = inputValue.trim();
        if (trimmedValue) {
            onSubmit(trimmedValue);
            setInputValue(""); // Очистка поля
            sessionStorage.removeItem('textareaValue'); // Удаляем сохраненное значение после отправки
        }
    };

    // Обработчик нажатия клавиш в textarea
    const handleKeyDown = (e: KeyboardEvent<HTMLTextAreaElement>) => {
        if (!isMobile) {
            // Shift + Enter для новой строки, иначе отправляем форму
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault(); // Предотвращаем переход на новую строку
                handleSubmit(e); // Отправляем форму
            }
        }
        // На мобильных устройствах Enter просто добавляет новую строку
    };

    // Глобальный обработчик нажатий клавиш
    useEffect(() => {
        const handleGlobalKeyPress = () => {
            // Если textarea существует и не в фокусе — фокусируемся на ней
            if (textareaRef.current && document.activeElement !== textareaRef.current) {
                textareaRef.current.focus();
            }
        };

        // Вешаем обработчик на нажатие клавиш по всему документу
        document.addEventListener("keydown", handleGlobalKeyPress);

        // Очищаем обработчик при размонтировании компонента
        return () => {
            document.removeEventListener("keydown", handleGlobalKeyPress);
        };
    }, []);

    return (
        <form className={styles.form} onSubmit={handleSubmit}>
            <textarea
                ref={textareaRef} // Присваиваем реф к textarea
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
