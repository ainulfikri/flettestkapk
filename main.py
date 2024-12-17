import tkinter as tk

# Membuat jendela aplikasi
root = tk.Tk()
root.title("Hello World App")

# Fungsi yang akan dipanggil saat tombol ditekan
def on_success_button_click():
    print("Success button clicked!")

# Menambahkan label untuk menampilkan "Hello World"
label = tk.Label(root, text="Hello World", font=("Arial", 16))
label.pack(pady=20)

# Menambahkan tombol "Success"
success_button = tk.Button(root, text="Success", command=on_success_button_click, font=("Arial", 12))
success_button.pack(pady=20)

# Menjalankan aplikasi
root.mainloop()
