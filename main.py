from converter import Converter
import tkinter as tk
from tkinter import ttk, messagebox

class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Конвертер единиц")
        
        self.converter = Converter()
        self.SMALL_NUMBER_THRESHOLD = 1e-10  # Порог для определения "слишком маленького" числа
        
        # Переменные для хранения выбора
        self.mode_var = tk.StringVar(value="length")
        self.from_value_var = tk.DoubleVar(value=1.0)
        self.to_value_var = tk.StringVar()  # Теперь StringVar для вывода сообщений
        self.from_unit_var = tk.StringVar()
        self.to_unit_var = tk.StringVar()
        
        # Создаем интерфейс
        self.create_widgets()
        
    def create_widgets(self):
        # Фрейм для выбора режима
        mode_frame = tk.LabelFrame(self.root, text="Режим", padx=5, pady=5)
        mode_frame.pack(padx=10, pady=5, fill=tk.X)
        
        tk.Radiobutton(
            mode_frame, text="Длина", variable=self.mode_var, 
            value="length", command=self.update_units
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Radiobutton(
            mode_frame, text="Время", variable=self.mode_var,
            value="time", command=self.update_units
        ).pack(side=tk.LEFT, padx=5)
        
        # Фрейм для ввода значения и выбора единиц
        convert_frame = tk.Frame(self.root)
        convert_frame.pack(padx=10, pady=5, fill=tk.X)
        
        # Поле ввода
        tk.Entry(
            convert_frame, textvariable=self.from_value_var,
            width=15
        ).pack(side=tk.LEFT, padx=5)
        
        # Выпадающий список для исходных единиц
        self.from_units = ttk.Combobox(
            convert_frame, textvariable=self.from_unit_var,
            width=15, state="readonly"
        )
        self.from_units.pack(side=tk.LEFT, padx=5)
        
        # Кнопка конвертации
        tk.Button(
            convert_frame, text="→", command=self.convert,
            width=3
        ).pack(side=tk.LEFT, padx=5)
        
        # Поле вывода (теперь может содержать текст)
        tk.Entry(
            convert_frame, textvariable=self.to_value_var,
            width=15, state="readonly"
        ).pack(side=tk.LEFT, padx=5)
        
        # Выпадающий список для целевых единиц
        self.to_units = ttk.Combobox(
            convert_frame, textvariable=self.to_unit_var,
            width=15, state="readonly"
        )
        self.to_units.pack(side=tk.LEFT, padx=5)
        
        # Инициализируем списки единиц
        self.update_units()
        
    def update_units(self):
        """Обновляет доступные единицы измерения в зависимости от выбранного режима"""
        mode = self.mode_var.get()
        
        if mode == "length":
            units = list(self.converter.LENGTH_COEFFS.keys())
        else:
            units = list(self.converter.TIME_COEFFS.keys())
            
        self.from_units["values"] = units
        self.to_units["values"] = units
        
        if units:
            self.from_unit_var.set(units[0])
            self.to_unit_var.set(units[1] if len(units) > 1 else units[0])
            
    def convert(self):
        """Выполняет конвертацию с проверкой на слишком маленькие числа"""
        try:
            value = self.from_value_var.get()
            from_unit = self.from_unit_var.get()
            to_unit = self.to_unit_var.get()
            
            if self.mode_var.get() == "length":
                result = self.converter.convert_length(value, from_unit, to_unit)
            else:
                result = self.converter.convert_time(value, from_unit, to_unit)
            
            # Проверяем, не слишком ли маленькое число
            if abs(result) < self.SMALL_NUMBER_THRESHOLD and result != 0:
                self.to_value_var.set("Слишком маленькое значение")
                # Дополнительно показываем сообщение
                messagebox.showinfo(
                    "Очень маленькое значение",
                    f"Результат конвертации ({result:.2e}) слишком мал для отображения.\n"
                    "Попробуйте выбрать другие единицы измерения."
                )
            else:
                # Форматируем результат: если число целое - без десятичной части, иначе до 8 знаков
                if result.is_integer():
                    self.to_value_var.set(int(result))
                else:
                    self.to_value_var.set(round(result, 8))
                    
        except Exception as e:
            self.to_value_var.set("Ошибка")
            messagebox.showerror("Ошибка", f"Произошла ошибка при конвертации: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()