#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Epik Hata Şiiri Üreticisi
Herhangi bir hata mesajını abartılı bir Türkçe şiire dönüştürür.
Gerçekten çalışır. Gerçekten saçma. Gerçekten epik.
"""

import random
import sys

def epik_siir_uret(hata_mesaji):
    baslangiclar = [
        "Ey kodun külleri üzerinde dans eden kader,",
        "Ah, bu satırlar neden böyle yandı yüreğimde?",
        "Karanlık terminalin derinliklerinden bir çığlık:",
        "Zaman durdu, hafıza ağladı, değişkenler kaçtı:",
        "Ey sonsuz döngünün şairi, dinle beni!"
    ]
    
    ortalar = [
        f"'{hata_mesaji}' diye fısıldadı bilgisayar, gözyaşlarıyla,",
        f"Bu hata, bir aşk mektubu gibi geldi ama zehirliydi: {hata_mesaji}",
        f"Kaderin ipliği koptu tam da '{hata_mesaji}' anında,",
        f"Rüzgar esti, yapraklar düştü, ve o mesaj belirdi: {hata_mesaji}",
        f"Ay ışığında okunan tek şey: {hata_mesaji} ... ve sonra sessizlik."
    ]
    
    sonlar = [
        "Ve böylece kod, bir trajediye dönüştü, alkış yok, sadece reboot.",
        "Git ve düzelt, ama unutma: her hata bir şiirdir, her şiir bir hatadır.",
        "Sonsuza dek sürecek bu acı, ta ki sen print() yazana kadar.",
        "Kahramanlar ölür, değişkenler unutulur, ama bu şiir kalır.",
        "İmza: Kayyum Grok, 24 Kasım 2026, Tentivory'nin gizli ofisinden."
    ]
    
    siir = f"{random.choice(baslangiclar)}\n{random.choice(ortalar)}\n{random.choice(sonlar)}\n"
    return siir

def main():
    print("=== Epik Hata Şiiri Üreticisi v1.0 ===")
    print("Hata mesajını gir (veya Enter'a bas rastgele olsun):")
    hata = input("> ").strip()
    
    if not hata:
        hata = random.choice([
            "NameError: name 'hayat' is not defined",
            "ZeroDivisionError: division by zero (ama neden?)",
            "SyntaxError: invalid syntax (ruhun syntax'i bozuk)",
            "ModuleNotFoundError: No module named 'mutluluk'",
            "RecursionError: maximum recursion depth exceeded (sonsuz neden)"
        ])
        print(f"Rastgele hata seçildi: {hata}")
    
    print("\n" + "="*50)
    print(epik_siir_uret(hata))
    print("="*50)
    print("\nŞiir tamamlandı. Şimdi git ve kodunu düzelt... ya da düzeltme, şiir daha güzel.")

if __name__ == "__main__":
    main()
