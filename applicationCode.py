import tkinter as tk
from tkinter import messagebox

class EventCostCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор стоимости мероприятия")

        # Текст и текстовые поля
        tk.Label(root, text="Количество участников:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.participants_entry = tk.Entry(root)
        self.participants_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Стоимость на одного участника (руб):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.cost_per_person_entry = tk.Entry(root)
        self.cost_per_person_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Дополнительные расходы (руб):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.additional_costs_entry = tk.Entry(root)
        self.additional_costs_entry.grid(row=2, column=1, padx=10, pady=5)

        # Кнопки
        calculate_button = tk.Button(root, text="Рассчитать", command=self.calculate)
        calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Output
        self.result_label = tk.Label(root, text="Общая стоимость: 0 руб", font=("Arial", 12, "bold"))
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def calculate(self):
        try:
           # Получение значений из текстовых полей и их преобразование в нужные числовые типы
            participants = int(self.participants_entry.get())
            cost_per_person = float(self.cost_per_person_entry.get())
            additional_costs = float(self.additional_costs_entry.get())
          # Расчет общей стоимости мероприятия
            total_cost = (participants * cost_per_person) + additional_costs
           # Обновление текстового поля с результатами
            self.result_label.config(text=f"Общая стоимость: {total_cost:.2f} руб")
          # Обработка исключений, если ввод пользователя некорректен
        except ValueError:
            messagebox.showerror("Ошибка ввода", "Пожалуйста, введите корректные числовые значения.")

# Проверка, является ли скрипт основным модулем
if __name__ == "__main__":
    root = tk.Tk()
    app = EventCostCalculator(root)
    root.mainloop()