invoice = """
0.....6.................................40........52...55........
1909 Pimoroni PiBrella $17.50 3 $52.50
1489 6mm Tactile Switch x20 $4.95 2 $9.90
1510 Panavise Jr. - PV-201 $28.00 1 $28.00
1601 PiTFT Mini Kit 320x240 $34.95 1 $34.95
"""
sku = slice(0, 6)
description = slice(6, 40)
unit_price = slice(52, 55)
quantity = slice(52, 55)
item_total = slice(55, None)

line_items = invoice.split("\n")[2:]

for item in line_items:
        print(item[unit_price], item[description])
