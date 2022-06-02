import threading
import time
import random
import os

class Queue:
    #first in first out
    def __init__(self, size=1000):
        self.queue = []
        self.size = size

    def size(self):
        return len(self.queue)

    #checks if queue is full
    def isFull(self):
        return len(self.queue) == self.size

    #checks if queue is empty
    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    #puts the item in the queue
    def enqueue(self,item):
        if self.isFull() == False:
            self.queue.insert(0, item)

    #takes an item in the front of the queue
    def dequeue(self):
        if self.isEmpty() == False:
            self.queue.pop()

    def display(self):
        print(self.queue)
    
    def checkQueue(self):
        count = 0
        for i in range(0, self.size):
            if self.size[i] != None:
                count += 1

        return count


dataRekening = [
    {
        "Nomor Rekening": "132465798",
        "Pengguna": "Mehmed",
        "PIN": "3564",
        "Saldo": 13000000,
        "antrian_transfer" : Queue(3)
    },
    {
        "Nomor Rekening": "918273645",
        "Pengguna": "faruqy",
        "PIN": "8290",
        "Saldo": 25000000,
        "antrian_transfer" : Queue(3)
    }
]


def main():
    running = True
    while (running):
        os.system('cls')
        print('1. Login')
        print('2. Register')
        print('3. Keluar')
        print('---------------------')
        

        opsi = int(input())

        if opsi == 1:
            #bagian login
            username = input('Inputkan Username Anda : ')
            login = input('Inputkan Password : ')

            success = False;
            for i in range(0, len(dataRekening)):
                if username == dataRekening[i]['Pengguna'] and login == dataRekening[i]['PIN']:
                    user = dataRekening[i]
                    print('login berhasil')
                    success = True

                    def dequeueAuto():
                        time.sleep(40) #bisa diubah tergantung berapa lama
                        user['antrian_transfer'].dequeue()

                    while(success):
                        os.system('cls')
                        print('1. Cek Saldo')
                        print('2. Transfer')
                        print('3. Deposit Saldo')
                        print('4. Tarik Tunai')
                        print('5. Data User')
                        print('6. Cek Kuota Transaksi')
                        print('7. Logout')
                        print('------------------')

                        chosen = int(input())

                        if chosen == 1:
                            os.system('cls')
                            print(f'Saldo Anda adalah : {user["Saldo"]}')
                            time.sleep(5)

                        elif chosen == 2:
                            os.system('cls')
                            print('Transfer')
                            print('1. Lanjut Transfer')
                            print('2. Kembali')
                            print('---------------------')

                            transferchosen = int(input())

                            if transferchosen == 1:
                                if (user["antrian_transfer"].isFull()):
                                    print('Maximal Transaksi Anda Sudah Melebihi Maksimum, silahkan tunggu beberapa saat lagi')
                                
                                else:
                                    print('Transfer')
                                    
                                    rekDituju = input('Inputkan Rekening yang dituju : ')
                                    saldoDikirim = int(input('Inputkan Saldo yang ditransfer : '))
                                    userDituju = ''


                                    for i in range(0, len(dataRekening)):
                                        if rekDituju == dataRekening[i]['Nomor Rekening']:
                                            userDituju = dataRekening[i]
                                        
                                    
                                    if userDituju == '':
                                        print('User tidak ditemukan, silahkan input dengan benar')

                                    if userDituju == user:
                                        print('User yang dituju tidak boleh sama dengan punya anda')
                                    
                                    else:
                                        os.system('cls')
                                        print('Data Rekening yang dituju')
                                        print(f' Atas Nama : {userDituju["Pengguna"]}')
                                        print(f' Nomor Rekening : {userDituju["Nomor Rekening"]}')
                                        print(f' Nominal Transfer : {saldoDikirim}')
                                        print('-------------------------------------------------')
                                        print('Apakah sudah yakin?')
                                        print('(0: tidak, 1: iya)')

                                        decideTransfer = int(input())

                                        if decideTransfer == 1:
                                            print('Transfer Berhasil')

                                            user['antrian_transfer'].enqueue('transfer')
                                            user['Saldo'] -= saldoDikirim
                                            userDituju['Saldo'] += saldoDikirim
                                            #asynchoronous function 
                                            transferTask = threading.Thread(target = dequeueAuto)
                                            transferTask.start()

                                        else:
                                            pass  

                            elif transferchosen == 2:
                                pass



                        elif chosen == 3:
                            os.system('cls')
                            print('Tambah Saldo')
                            print('Inputkan 0 apabila tidak jadi')
                            saldoDitambahkan = int(input('Inputkan Saldo yang akan ditambahkan : '))

                            if (user["antrian_transfer"].isFull()):
                                os.system('cls')
                                print('Kuota transaksi anda sudah penuh, harap tunggu beberapa saat lagi.')
                                time.sleep(2)

                            elif saldoDitambahkan >= 1 :
                                print('Deposit saldo berhasil!')
                                user['antrian_transfer'].enqueue('tambahsaldo')
                                #asynchoronous functtion
                                user['Saldo'] += saldoDitambahkan
                                tambahTask = threading.Thread(target = dequeueAuto)
                                tambahTask.start()

                            else:
                                pass
                        

                        elif chosen == 4:
                            os.system('cls')
                            print('Tarik Tunai')
                            print('Inputkan 0 apabila tidak jadi')

                            saldoDitarik = int(input('Inputkan Saldo yang akan ditarik : '))

                            if (user["antrian_transfer"].isFull()):
                                os.system('cls')
                                print('Kuota transaksi anda sudah penuh, harap tunggu beberapa saat lagi.')
                                time.sleep(2)

                            elif saldoDitarik >= 1 and saldoDitarik <= user['Saldo']:
                                print('Penarikan tunai berhasil')
                                user['antrian_transfer'].enqueue('tariktunai')
                                user['Saldo'] -= saldoDitarik
                                # asynchoronous function
                                tarikTask = threading.Thread(target = dequeueAuto)
                                tarikTask.start()

                            else:
                                pass

                        elif chosen == 5:
                            os.system('cls')
                            print('Data Anda')
                            print(f'Nomor Rekening Anda : {user["Nomor Rekening"]}')
                            print(f'Username Anda : {user["Pengguna"]}')
                            time.sleep(5)


                        elif chosen == 6:
                            os.system('cls')
                            print('Cek Kuota Transaksi')
                            user['antrian_transfer'].display()
                            print(f'Kuota transfer yang tersedia {user["antrian_transfer"].size - len(user["antrian_transfer"].queue)}')
                            time.sleep(5)


                        elif chosen == 7:
                            print('Anda akan logout')
                            success = False;

                        else:
                            print('Input invalid, mohon input dengan benar')
                            time.sleep(1)
        elif opsi == 2:
            #bagian register
            os.system('cls')
            print('Registrasi Pengguna Baru')
            pengguna = input('Inputkan Nama Username Anda : ')
            pinpenggunabaru = input('Inputkan PIN yang ingin anda gunakan : ')
            saldo = int(input('Inputkan Saldo Awal : '))
            norekbaru = ''
            #pembuatan nomor rekening otomatis
            pilihan = ['0','1','2','3','4','5','6','7','8','9']
            
            for i in range(0, 9):
                pilihanangka = random.choice(pilihan)
                norekbaru += pilihanangka

            dataRekening.append({
                "Nomor Rekening": norekbaru,
                "Pengguna": pengguna,
                "PIN": pinpenggunabaru,
                "Saldo": saldo,
                "antrian_transfer" : Queue(3)
            })

            print(f'Registrasi Berhasil dengan username : {pengguna},  pin : {pinpenggunabaru}, nomor rekening : {norekbaru}')
            time.sleep(30)
        
        elif opsi == 3:
            running = False
            quit()
        
        else:
            print('input invalid, silahkan input dengan benar')
            time.sleep(1)

main()
