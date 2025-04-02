import socket 
from escpos.printer import Network
from PIL import Image

# Printer IP Address
PRINTER_IP = "192.168.1.100" # Replace with actual IP
PORT = 9100 # Standard raw printing port

# Open connection to printer
p = Network(PRINTER_IP, port=PORT)

# Load and process image
image = Image.open("test.png") # Replace with your image file
image = image.convert("1") # Convert to monochrome

# Send image to printer
p.image(image)
p.cut() # Cut the receipt (if supported)
p.close()
