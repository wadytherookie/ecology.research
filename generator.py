import qrcode
import os

# Create a place for the images
if not os.path.exists('barcodes'): 
    os.makedirs('barcodes')

biomes = ["tundra", "taiga", "temperate_forest", "woodland", "grassland", "desert", "savanna", "seasonal_forest", "rainforest"]

print("Starting generation...")

for biome in biomes:
    # IMPORTANT: These lines MUST be indented to stay inside the loop
    url = f"http://192.168.100.26:8000/biome_view.html?type={biome}"
    
    qr = qrcode.QRCode(version=1, box_size=20, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"barcodes/{biome}_qr.png")
    print(f"Generated QR for: {biome}")

print("\n✅ 9 High-Res barcodes generated in /barcodes")
#uvicorn server:app --host 0.0.0.0 --port 8000