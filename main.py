import tkinter
from tkinter import messagebox, StringVar, Text

# Pencere ayarları
window = tkinter.Tk()
window.title('BMI KÜTLE ENDEKSİ')
window.config(padx=20, pady=20, bg='#eaeaea')  # Arka plan rengi

history = []  # Hesaplama tarihçesi için liste

# Ölçüm birimleri için değişkenler
unit_var = StringVar(value='kg/cm')  # Varsayılan birim kg ve cm

def calculate():
    height = height_input.get()
    weight = weight_input.get()

    if not height.isdigit() or not weight.isdigit():
        messagebox.showerror("Giriş Hatası", "Lütfen geçerli bir boy ve kilo girin.")
        return

    height = float(height)
    weight = float(weight)

    # Birim dönüşümleri
    if unit_var.get() == 'lbs/inch':
        height *= 2.54  # inç'ten cm'ye çevir
        weight *= 0.453592  # lbs'den kg'ye çevir

    if weight == 0 or height == 0:
        result_label.config(text="Boy ve kilo sıfırdan büyük olmalıdır.")
    else:
        bmi = weight / (height / 100) ** 2
        result_string = write_result(bmi)
        result_label.config(text=result_string)
        history.append(result_string)  # Sonucu tarihçeye ekle
        update_history()  # Tarihçeyi güncelle

def write_result(bmi):
    result_string = f"Your BMI is {bmi:.2f}. You are "
    if bmi <= 16:
        result_string += "severely thin"
        result_label.config(fg='blue')
    elif 16 < bmi <= 17:
        result_string += "moderately thin"
        result_label.config(fg='lightblue')
    elif 17 < bmi <= 18.5:
        result_string += "mildly thin"
        result_label.config(fg='lightgreen')
    elif 18.5 < bmi <= 25:
        result_string += "normal"
        result_label.config(fg='green')
    elif 25 < bmi <= 30:
        result_string += "overweight"
        result_label.config(fg='orange')
    elif 30 < bmi <= 35:
        result_string += "obese class 1"
        result_label.config(fg='red')
    elif 35 < bmi <= 40:
        result_string += "obese class 2"
        result_label.config(fg='darkred')
    else:
        result_string += "obese class 3"
        result_label.config(fg='purple')
    return result_string

def update_history():
    history_text.delete(1.0, tkinter.END)  # Önceki metni temizle
    for record in history:
        history_text.insert(tkinter.END, record + '\n')  # Her kaydı ekle

def reset():
    weight_input.delete(0, tkinter.END)
    height_input.delete(0, tkinter.END)
    result_label.config(text="Result:")
    history.clear()  # Tarihçeyi sıfırla
    update_history()

# Label ve input alanları
weight_label = tkinter.Label(text="Enter your weight (kg or lbs):", bg='#eaeaea', font=('Arial', 12))
weight_label.pack()

weight_input = tkinter.Entry()
weight_input.pack()

height_input_label = tkinter.Label(text="Enter your height (cm or inch):", bg='#eaeaea', font=('Arial', 12))
height_input_label.pack()

height_input = tkinter.Entry()
height_input.pack()

# Ölçü birimi seçimi
unit_frame = tkinter.Frame(window, bg='#eaeaea')
unit_frame.pack()

unit_label = tkinter.Label(unit_frame, text="Select units:", bg='#eaeaea', font=('Arial', 12))
unit_label.pack(side=tkinter.LEFT)

kg_cm_radio = tkinter.Radiobutton(unit_frame, text="kg/cm", variable=unit_var, value='kg/cm', bg='#eaeaea')
kg_cm_radio.pack(side=tkinter.LEFT)

lbs_inch_radio = tkinter.Radiobutton(unit_frame, text="lbs/inch", variable=unit_var, value='lbs/inch', bg='#eaeaea')
lbs_inch_radio.pack(side=tkinter.LEFT)

calculate_button = tkinter.Button(text="Calculate", command=calculate, bg='#4CAF50', fg='white', font=('Arial', 12))
calculate_button.pack(pady=5)

reset_button = tkinter.Button(text="Reset", command=reset, bg='#f44336', fg='white', font=('Arial', 12))
reset_button.pack(pady=5)

result_label = tkinter.Label(text="Result:", bg='#eaeaea', font=('Arial', 12))
result_label.pack()

# Hesaplama tarihçesi alanı
history_label = tkinter.Label(text="Calculation History:", bg='#eaeaea', font=('Arial', 12))
history_label.pack()

history_text = Text(window, height=10, width=50, bg='#f9f9f9')
history_text.pack()

window.mainloop()
