from io import BytesIO
from barcode import Code128
from barcode.writer import ImageWriter

# Write to a file-like object:
rv = BytesIO()
Code128("CH2210-Chandan-WBL", writer=ImageWriter()).write(rv)

# Saving to a file:
with open("barcode.png", "wb") as f:
    Code128("CH2210-Chandan-WBL", writer=ImageWriter()).write(f)
