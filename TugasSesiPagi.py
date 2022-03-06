#!/usr/bin/env python
# coding: utf-8

# In[ ]:


loop = 100
for i in range(loop):
    print(f"Halo Hai")


# In[22]:


import pandas as pd

df = pd.DataFrame({
        'pemain 1':['batu','gunting','kertas','batu','gunting','kertas','batu','gunting','kertas'],
        'pemain 2':['batu','gunting','kertas','kertas','batu','gunting','gunting','kertas','batu'],
        'pemenang':['seri', 'seri', 'seri', 'pemain 2', 'pemain 2', 'pemain 2', 'pemain 1', 'pemain 1', 'pemain 1']
     })
df


# In[ ]:


print('''Please pick one:
            rock
            scissors
            paper''')

while True:
    game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
    player_a = str(input("Player a: "))
    player_b = str(input("Player b: "))
    a = game_dict.get(player_a)
    b = game_dict.get(player_b)
    dif = a - b

    if dif in [-1, 2]:
        print('player a wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif dif in [-2, 1]:
        print('player b wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    else:
        print('Draw.Please continue.')
        print('')


# In[ ]:


pilihan="y"
while pilihan=="y":
    print("""
    ==============================
    
    MENU JAJANAN PASAR INDAH
 
    ==============================
    1. Donat : Rp 1.250
    2. Bakwan : Rp 1.000
    3. Onde-onde : Rp 800
    4. Lemper : Rp 1.250
    5. Risol : Rp 1.500
    ==============================
    """)
    pesan=str(input("Masukan menu yang ingin kamu beli ="))
    jumlahpesan=int(input("Masukkan berapa banyak kamu ingin beli? ="))
    if pesan == "1":
        listnama= "Donat"
        harga=(1250*jumlahpesan)
        totalharga=int(harga)
    elif pesan == "2":
        listnama= "Bakwan"
        harga = (1000*jumlahpesan)
        totalharga=int(harga)
    elif pesan == "3":
        listnama= "Onde-onde"
        harga = (800*jumlahpesan)
        totalharga=int(harga)
    elif pesan == "4":
        listnama= "Lemper"
        harga = (1250*jumlahpesan)
        totalharga=int(harga)
    elif pesan == "5":
        listnama= "Risol"
        harga = (1500*jumlahpesan)
        totalharga=int(harga)
    else:
        listnama = "-"
        harga = "-"
        totalharga = "-"
        pilihan=input("menu tidak tersedia, silahkan masukkan menu yang tersedia silahkan ulangi kembali Y/N =")
 
    print("--------------------------")
    print("JAJANAN PASAR INDAH")
    print("--------------------------")
    print("Menu :",listnama)
    print("Jumlah Pesan :", jumlahpesan)
    print("Harga :", harga)
    print("--------------------------")
    print("Jumlah Bayar :", totalharga)
    print("--------------------------")
    pilihan=input("apakah anda ingin order kembali Y/N =")


# In[ ]:




