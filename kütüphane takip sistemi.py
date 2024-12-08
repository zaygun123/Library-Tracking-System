# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 17:28:51 2024

@author: Zeynep_Aygün
"""

import tkinter as tk
from tkinter import messagebox

class Kitap:
    def __init__(self, ad, yazar):
        self.ad = ad
        self.yazar = yazar
        self.odunc_alindi = False

    def __str__(self):
        durum = "Ödünç Alındı" if self.odunc_alindi else "Mevcut"
        return f"Kitap: {self.ad}, Yazar: {self.yazar}, Durum: {durum}"

class Kutuphane:
    def __init__(self):
        self.kitaplar = []
        self.odunc_kitaplar = []

    def kitap_ekle(self, kitap):
        self.kitaplar.append(kitap)

    def kitap_listele(self):
        return [str(kitap) for kitap in self.kitaplar]

    def odunc_ver(self, kitap_ad):
        for kitap in self.kitaplar:
            if kitap.ad == kitap_ad and not kitap.odunc_alindi:
                kitap.odunc_alindi = True
                self.odunc_kitaplar.append(kitap)
                return f"{kitap_ad} kitabı ödünç alındı."
        return f"{kitap_ad} kitabı mevcut değil veya zaten ödünç alındı."

    def geri_al(self, kitap_ad):
        for kitap in self.odunc_kitaplar:
            if kitap.ad == kitap_ad:
                kitap.odunc_alindi = False
                self.odunc_kitaplar.remove(kitap)
                return f"{kitap_ad} kitabı geri alındı."
        return f"{kitap_ad} kitabı ödünç alınmamış."

class KütüphaneGUI:
    def __init__(self, root):
        self.kutuphane = Kutuphane()
        self.root = root
        self.root.title("Kütüphane Yönetim Sistemi")

     
        self.kitap_ad_label = tk.Label(root, text="Kitap Adı:")
        self.kitap_ad_label.pack()
        self.kitap_ad_entry = tk.Entry(root)
        self.kitap_ad_entry.pack()

        self.yazar_ad_label = tk.Label(root, text="Yazar Adı:")
        self.yazar_ad_label.pack()
        self.yazar_ad_entry = tk.Entry(root)
        self.yazar_ad_entry.pack()

        self.kitap_ekle_button = tk.Button(root, text="Kitap Ekle", command=self.kitap_ekle)
        self.kitap_ekle_button.pack()

        
        self.kitap_listele_button = tk.Button(root, text="Kitapları Listele", command=self.kitap_listele)
        self.kitap_listele_button.pack()

        self.kitap_listesi = tk.Listbox(root, height=10, width=50)
        self.kitap_listesi.pack()

        
        self.odunc_kitap_ad_label = tk.Label(root, text="Ödünç Verilecek Kitap Adı:")
        self.odunc_kitap_ad_label.pack()
        self.odunc_kitap_ad_entry = tk.Entry(root)
        self.odunc_kitap_ad_entry.pack()

        self.odunc_ver_button = tk.Button(root, text="Ödünç Ver", command=self.odunc_ver)
        self.odunc_ver_button.pack()

        
        self.geri_al_kitap_ad_label = tk.Label(root, text="Geri Alınacak Kitap Adı:")
        self.geri_al_kitap_ad_label.pack()
        self.geri_al_kitap_ad_entry = tk.Entry(root)
        self.geri_al_kitap_ad_entry.pack()

        self.geri_al_button = tk.Button(root, text="Kitap Geri Al", command=self.geri_al)
        self.geri_al_button.pack()

    def kitap_ekle(self):
        kitap_ad = self.kitap_ad_entry.get()
        yazar_ad = self.yazar_ad_entry.get()
        if kitap_ad and yazar_ad:
            kitap = Kitap(kitap_ad, yazar_ad)
            self.kutuphane.kitap_ekle(kitap)
            self.kitap_ad_entry.delete(0, tk.END)
            self.yazar_ad_entry.delete(0, tk.END)
            messagebox.showinfo("Başarılı", f"{kitap_ad} kitabı başarıyla eklendi.")
        else:
            messagebox.showerror("Hata", "Kitap adı ve yazar adı boş olamaz.")

    def kitap_listele(self):
        self.kitap_listesi.delete(0, tk.END)
        kitaplar = self.kutuphane.kitap_listele()
        for kitap in kitaplar:
            self.kitap_listesi.insert(tk.END, kitap)

    def odunc_ver(self):
        kitap_ad = self.odunc_kitap_ad_entry.get()
        if kitap_ad:
            mesaj = self.kutuphane.odunc_ver(kitap_ad)
            messagebox.showinfo("Sonuç", mesaj)
            self.odunc_kitap_ad_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Hata", "Kitap adı boş olamaz.")

    def geri_al(self):
        kitap_ad = self.geri_al_kitap_ad_entry.get()
        if kitap_ad:
            mesaj = self.kutuphane.geri_al(kitap_ad)
            messagebox.showinfo("Sonuç", mesaj)
            self.geri_al_kitap_ad_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Hata", "Kitap adı boş olamaz.")

if __name__ == "__main__":
    root = tk.Tk()
    gui = KütüphaneGUI(root)
    root.mainloop()
