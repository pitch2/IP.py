#172.168.255.4/22

import tkinter as tk
from tkinter import messagebox

def init():
    global partie_1
    global partie_2
    global partie_2_sans_cro

    #ip = "172.168.255.4/22"
    ip= input("Votre IP: ")

    partie_ip = ip.split("/")
    partie_2 = partie_ip[1]
    partie_2_sans_cro = partie_ip[0]
    partie_1 = partie_ip[0].split(".")

def masque():
    global liste_masque

    mask = [0] * 32
    for i in range(int(partie_2)):
        mask[i] = 1
    masque_bin = []

    for i in range(0, 32, 8):
        masque_bin.append(sum([mask[j] * (2**(7-j%8)) for j in range(i, i+8)]))
    masque = ".".join(str(octet) for octet in masque_bin)

    liste_masque = masque.split(".")
    liste_masque = [int(part) for part in liste_masque]
    print("Le masque est: ",masque)
    

def adresse_reseau():
    print("L'adresse de sous réseau est: ", end='')
    adresse_reseau_1= int(partie_1[0]) & liste_masque[0]
    adresse_reseau_2=int(partie_1[1]) & liste_masque[1]
    adresse_reseau_3=int(partie_1[2]) & liste_masque[2]
    adresse_reseau_4=(int(partie_1[3]) & liste_masque[3]) 
    print(adresse_reseau_1,".", adresse_reseau_2,".", adresse_reseau_3,".", adresse_reseau_4)


def adresse_diffusion():
    ip = partie_2_sans_cro
    ip_binary = ''.join([bin(int(x)+256)[3:] for x in ip.split('.')])
    subnet_mask = partie_2
    subnet_mask_binary = ('1' * int(subnet_mask)).ljust(32, '0')
    network_address_binary = ''.join([str(int(ip_binary[i]) & int(subnet_mask_binary[i])) for i in range(32)])
    inversement = ''.join(['0' if x == '1' else '1' for x in subnet_mask_binary])
    bin_diffusion = ''.join([str(int(network_address_binary[i]) | int(inversement[i])) for i in range(32)])

    print("L'adresse de diffusion: ", end='')

    partie_1_dec = int(str("".join(str(bit) for bit in list(str(bin_diffusion))[0:8])), 2)
    partie_2_dec = int(str("".join(str(bit) for bit in list(str(bin_diffusion))[8:16])), 2)
    partie_3_dec = int(str("".join(str(bit) for bit in list(str(bin_diffusion))[16:24])), 2)
    partie_4_dec = int(str("".join(str(bit) for bit in list(str(bin_diffusion))[24:32])), 2)
    print(partie_1_dec,".", partie_2_dec,".", partie_3_dec,".", partie_4_dec)


def nombre_clients():
    
    nbr = 2**(32 - int(partie_2))-2
    print("Le nombre de clients possible est: ", nbr)






init()
masque()
adresse_reseau()
adresse_diffusion()
nombre_clients()
input('\nAppuyer sur entrée ...')