import pandas as pd
from tabulate import tabulate

class Transaction:
    '''Membuat class Transaction'''
    def __init__(self):
        self.items = dict()

    def add_item(self, name, qty, price):
        '''
        Menambahkan item ke dalam transaksi
        '''
        self.items.update({name: [qty, price]})
        return print(f'Item purchased : {self.items}')

    def update_item_name(self, name, update_name):
        '''
        Update nama item ke nama baru
        '''
        temp = self.items[name]
        self.items.pop(name)
        self.items.update({update_name: temp})
        return print(f'Updated transaction list, Item purchased is {self.items}')

    def update_item_qty(self, name, update_qty):
        '''
        Update jumlah pembelian suatu item
        '''
        self.items[name][0] =  update_qty
        return print(f'Updated transaction list, Item purchased is {self.items}')

    def update_item_price(self, name, update_price):
        '''
        Update harga dari suatu item
        '''
        self.items[name][1] =  update_price
        return print(f'Updated transaction list, Item purchased is {self.items}')

    def delete_item(self, name):
        '''
        Menghapus suatu item dari list item
        '''
        self.items.pop(name)
        return print(f'Item deleted, Item purchased is {self.items}')

    def reset_transaction(self):
        '''
        Menghapus semua item 
        '''
        self.items.clear()
        return print(f'All items have been removed')


    def check_order(self):
        '''
        Melakukan pengecekan terhadap seluruh item, apakah terdapat nilai 0
        '''
        tabel = pd.DataFrame(self.items).T
        total_prices = list()
        for key in self.items:
            total_prices.append(self.items[key][0]*self.items[key][1])
        tabel['total'] = total_prices
        header = ["Item", "Quantity", "Price", "Total Price"]
        print(tabulate(tabel, header, tablefmt='github'))
        
        check = True
        for item in tabel['total']:
            if item<= 0:
                check = False
        if check:
            print("Order is correct")
        else:
            print("There is a data input error")

    def total_price(self):
        '''
        Menghitung total belanja dari transaksi, jika pembelian
        - lebih dari 200_000 maka mendapat diskon 5%
        - lebih dari 300_000 maka mendapat diskon 8%
        - lebih dari 500_000 maka mendapat diskon 10%
        '''
        tabel = pd.DataFrame(self.items).T
        total_prices = list()
        for key in self.items:
            total_prices.append(self.items[key][0]*self.items[key][1])
        tabel['total'] = total_prices
        sum = tabel['total'].sum()
        
        if sum<200000:
            pass
        elif sum<300000:
            sum = sum*0.95
        elif sum<500000:
            sum = sum*0.92
        else:
            sum = sum*0.9
        
        return print(f'Total price : {sum}')