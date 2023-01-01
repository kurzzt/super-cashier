# SUPER CASHIER PROJECT

\>///<

## LATAR BELAKANG
---

Andi adalah seorang pemilik supermarket besar di salah satu kota di Indonesia. Andi akan membuat sistem kasir yang self-service di supermarket miliknya. Sehingga customer bisa langsung memasukkan item yang dibeli, jumlah item yang dibeli, dan harga item yang dibeli dan fitur yang lain.

## REQUIREMENTS / OBJECTIVES
---

1. Costumer membuat ID transaksi customer dengan membuat object dari class. Sebagai contoh, `trnsct_123 = Transaction()`
2. Customer meng-input nama item, jumlah item, dan harga barang dengan method `add_item()`
3. Jika ternyata ada kesalahan dalam meng-input nama item atau jumlah item atau harga item tetapi tidak ingin menghapus itemnya, customer bisa melakukan:
   - Update nama item dengan method `update_item_name()`
   - Update jumlah item dengan method `update_item_qty()`
   - Update harga item dengan method `update_item_price()`
4. Jika batal membeli item belanjaan, Customer bisa melakukan:
   - Menghapus salah satu item dari nama item dengan method `delete_item()`
   - Langsung menghapus semua transaksi atau reset transaksi dengan method `reset_transaction()`
5. Customer bisa melakukan pengecekan pada status pemesanan sebelum membayar dengan method `check_order()` yang akan mengeluarkan output yaitu:
   - Akan mengeluarkan pesan **"Order is correct"** jika tidak ada kesalahan input.
   - Akan mengeluarkan pesan **"There is a data input error"** jika terjadi kesalahan input.
   - Keluaran output transaksi atau pemesanan apa saja yang sudah dibeli.
6. Setelah melakukan checkout, Customer bisa menghitung total belanja dengan method `total_price`. Pada supermarket terdapat ketentuan:
    - Jika total belanja diatas Rp 200.000 maka akan mendapatkan diskon 5%
    - Jika total belanja diatas Rp 300.000 maka akan mendapatkan diskon 8%
    - Jika total belanja diatas Rp 500.000 maka akan mendapatkan diskon 10%

## FLOWCHART
---

![flowchart](/img/Untitled.png)

## Funcions Explanation
---
1. init() : 
   
   menginisialiasasi class Transaction()
   
2. add_item(name, qty, price)
   
   Menambahkan item ke list transaksi

3. update_item_name(name, update_name)

   Melakukan perubahan nama item pada item yang ada di list transaksi

4. update_item_qty(name, update_qty)
   
   Melakukan perubahan jumlah item pada item yang ada di list transaksi

5. update_item_price(name, update_price)

   Melakukan perubahan harga item pada item yang ada di list transaksi

6. delete_item(name)
   
   Menghapus atau membatalkan pembelian sebuah item pada list transaksi

7. reset_transaction()

   Membatalkan pembelian seluruh item yang ada di list transaksi

8. check_order()

   Melakukan pengecekan apakah seluruh item yang akan dibeli pada list transaksi sudah benar atau belum

9.  total_price()

   Menghitung total belanja dari seluruh item yang ada di list transaksi

## Guide
---
1. Clone repo ini
2. Install **tabulate** dan **pandas**
   ```
   pip install tabulate
   pip install pandas
   ```
3. Run the jupyter notebook file

## TEST CASE
---

### Test Case 1:

```py
trnsct_123 = s.Transaction()
trnsct_123.add_item("Nasi goreng", 1, 10000)
trnsct_123.add_item("Sate Kelinci", 3, 15000)
trnsct_123.add_item("Sendok", 7, 3000)
trnsct_123.add_item("Permen Miksu", 1, 500)
trnsct_123.add_item("Miksu", 1, 8000)

print('\n')
trnsct_123.update_item_name('Nasi goreng', 'Mie Goyeng')
trnsct_123.update_item_price('Sate Kelinci', 17000)
trnsct_123.update_item_qty('Sendok', 2)
trnsct_123.delete_item('Permen Miksu')

print('\n')
trnsct_123.check_order()
trnsct_123.total_price()
```

<details>
<summary>Result</summary>
<br>

```
Item purchased : {'Nasi goreng': [1, 10000]}
Item purchased : {'Nasi goreng': [1, 10000], 'Sate Kelinci': [3, 15000]}
Item purchased : {'Nasi goreng': [1, 10000], 'Sate Kelinci': [3, 15000], 'Sendok': [7, 3000]}
Item purchased : {'Nasi goreng': [1, 10000], 'Sate Kelinci': [3, 15000], 'Sendok': [7, 3000], 'Permen Miksu': [1, 500]}
Item purchased : {'Nasi goreng': [1, 10000], 'Sate Kelinci': [3, 15000], 'Sendok': [7, 3000], 'Permen Miksu': [1, 500], 'Miksu': [1, 8000]}


Updated transaction list, Item purchased is {'Sate Kelinci': [3, 15000], 'Sendok': [7, 3000], 'Permen Miksu': [1, 500], 'Miksu': [1, 8000], 'Mie Goyeng': [1, 10000]}
Updated transaction list, Item purchased is {'Sate Kelinci': [3, 17000], 'Sendok': [7, 3000], 'Permen Miksu': [1, 500], 'Miksu': [1, 8000], 'Mie Goyeng': [1, 10000]}
Updated transaction list, Item purchased is {'Sate Kelinci': [3, 17000], 'Sendok': [2, 3000], 'Permen Miksu': [1, 500], 'Miksu': [1, 8000], 'Mie Goyeng': [1, 10000]}
Item deleted, Item purchased is {'Sate Kelinci': [3, 17000], 'Sendok': [2, 3000], 'Miksu': [1, 8000], 'Mie Goyeng': [1, 10000]}


| Item         |   Quantity |   Price |   Total Price |
|--------------|------------|---------|---------------|
| Sate Kelinci |          3 |   17000 |         51000 |
| Sendok       |          2 |    3000 |          6000 |
| Miksu        |          1 |    8000 |          8000 |
| Mie Goyeng   |          1 |   10000 |         10000 |
Order is correct
Total price : 75000
```
</details>

### Test Case 2:

```py
trnsct_333 = s.Transaction()
trnsct_333.add_item("Nasi goreng", 1, 10000)
trnsct_333.add_item("Sate Kelinci", 3, 15000)
trnsct_333.add_item("Sendok", 7, 3000)

trnsct_333.reset_transaction()
trnsct_333.check_order()
trnsct_333.total_price()
```
<details>
<summary>Result</summary>
<br>

```
Item purchased : {'Nasi goreng': [1, 10000]}
Item purchased : {'Nasi goreng': [1, 10000], 'Sate Kelinci': [3, 15000]}
Item purchased : {'Nasi goreng': [1, 10000], 'Sate Kelinci': [3, 15000], 'Sendok': [7, 3000]}
All items have been removed
| Item   | Quantity   | Price   | Total Price   |
|--------|------------|---------|---------------|
Order is correct
Total price : 0.0
```

</details>

### Test Case 3:

```py
trnsct_124 = s.Transaction()
trnsct_124.add_item("Nasi goreng", 1, 10000)
trnsct_124.add_item("Sate Kelinci", 3, 15000)
trnsct_124.add_item("Sendok", 7, 0000)

print('\n')
trnsct_124.check_order()
trnsct_124.total_price()
```
<details>
<summary>Result</summary>
<br>

```
Item purchased : {'Nasi goreng': [1, 10000]}
Item purchased : {'Nasi goreng': [1, 10000], 'Sate Kelinci': [3, 15000]}
Item purchased : {'Nasi goreng': [1, 10000], 'Sate Kelinci': [3, 15000], 'Sendok': [7, 0]}


| Item         |   Quantity |   Price |   Total Price |
|--------------|------------|---------|---------------|
| Nasi goreng  |          1 |   10000 |         10000 |
| Sate Kelinci |          3 |   15000 |         45000 |
| Sendok       |          7 |       0 |             0 |
There is a data input error
Total price : 55000
```

</details>