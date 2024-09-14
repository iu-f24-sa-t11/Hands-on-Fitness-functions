// @ts-ignore
import styles from './input.module.css';
import { FormEvent } from "react";

interface SearchProps {
  placeholder: string;
  onSubmit: (value: string) => void; // Изменил тип, чтобы onSubmit принимал текст из инпута
}

export const Input = ({ placeholder, onSubmit }: SearchProps) => {
  const handleSubmit = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault(); // Предотвращаем перезагрузку страницы при отправке формы
    const input = e.currentTarget.elements[0] as HTMLInputElement; // Получаем текст из инпута
    const inputValue = input.value.trim();
    if (inputValue) {
      onSubmit(inputValue); // Вызываем функцию onSubmit с введённым значением
      input.value = ""; // Очищаем поле ввода
    }
  };

  return (
    <form className={styles.form} onSubmit={handleSubmit}>
      <input type="text" placeholder={placeholder} className={styles.input} />
    </form>
  );
};
