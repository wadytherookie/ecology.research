from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Enable CORS for mobile/tablet access
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"], 
    allow_methods=["*"], 
    allow_headers=["*"]
)

# Ensure the videos folder exists for local files
if not os.path.exists("videos"):
    os.makedirs("videos")

db = {
    "tundra": {
        "title": "التندرا",
        "temp": "-34°C إلى 12°C",
        "rain": "15-25 سم",
        "plants": "الأشنات، الطحالب، أعشاب قصيرة",
        "animals": "الدببة القطبية، الثعلب القطبي، الرنة",
        "color": "#a5f3fc",
        "video_url": "https://assets.mixkit.co/videos/preview/mixkit-snow-covered-mountain-peaks-under-a-blue-sky-41484-large.mp4"
    },
    "desert": {
        "title": "الصحراء",
        "temp": "2°C إلى 49°C",
        "rain": "أقل من 25 سم",
        "plants": "الصبار، النباتات العصارية، الشجيرات",
        "animals": "الجمال، العقارب، السحالي",
        "color": "#ff9f1c",
        "video_url": "https://assets.mixkit.co/videos/preview/mixkit-sand-dunes-in-the-middle-of-a-desert-42416-large.mp4"
    },
    "rainforest": {
        "title": "الغابات الاستوائية",
        "temp": "24°C إلى 27°C",
        "rain": "200-1000 سم",
        "plants": "أشجار دائمة الخضرة، سرخسيات",
        "animals": "النمر الأمريكي، الطوقان، الكسلان",
        "color": "#2ecc71",
        "video_url": "https://assets.mixkit.co/videos/preview/mixkit-tropical-rainforest-with-a-river-flowing-through-it-41517-large.mp4"
    },
    "grassland": {
        "title": "المراعي المعتدلة",
        "temp": "-40°C إلى 38°C",
        "rain": "50-89 سم",
        "plants": "الأعشاب، الزهور البرية",
        "animals": "البيسون، كلاب المروج",
        "color": "#f4e285",
        "video_url": "https://assets.mixkit.co/videos/preview/mixkit-aerial-view-of-a-green-grass-field-41510-large.mp4"
    },
    "savanna": {
        "title": "السافانا الاستوائية",
        "temp": "20°C إلى 30°C",
        "rain": "50-130 سم",
        "plants": "أعشاب طويلة، أشجار متفرقة",
        "animals": "الأسود، الزرافات، الفيلة",
        "color": "#e67e22",
        "video_url": "https://assets.mixkit.co/videos/preview/mixkit-aerial-view-of-a-dry-savanna-landscape-41512-large.mp4"
    },
    "taiga": {
        "title": "التايغا",
        "temp": "-54°C إلى 21°C",
        "rain": "30-84 سم",
        "plants": "أشجار مخروطية (صنوبر)",
        "animals": "الأيائل، الذئاب، القندس",
        "color": "#16a085",
        "video_url": "https://assets.mixkit.co/videos/preview/mixkit-coniferous-forest-under-a-mountain-range-41497-large.mp4"
    },
    "temperate_forest": {
        "title": "الغابات المعتدلة",
        "temp": "-30°C إلى 30°C",
        "rain": "75-150 سم",
        "plants": "أشجار البلوط، الزان",
        "animals": "السناجب، الثعالب، الغزلان",
        "color": "#27ae60",
        "video_url": "https://assets.mixkit.co/videos/preview/mixkit-sunlight-streaming-through-the-trees-of-a-forest-41514-large.mp4"
    },
    "woodland": {
        "title": "المناطق الحرجية",
        "temp": "10°C إلى 40°C",
        "rain": "38-100 سم",
        "plants": "شجيرات، بلوط أخضر",
        "animals": "الأرانب، الطيور، الزواحف",
        "color": "#95a5a6",
        "video_url": "https://assets.mixkit.co/videos/preview/mixkit-green-hills-and-trees-under-a-cloudy-sky-41503-large.mp4"
    },
    "seasonal_forest": {
        "title": "الغابات الاستوائية الموسمية",
        "temp": "20°C إلى 25°C",
        "rain": "> 200 سم",
        "plants": "أشجار تسقط أوراقها صيفاً",
        "animals": "القردة، الفيلة، النمور",
        "color": "#d35400",
        "video_url": "https://assets.mixkit.co/videos/preview/mixkit-autumn-forest-with-red-and-orange-leaves-41516-large.mp4"
    }
}

@app.get("/data/{biome_name}")
def get_biome(biome_name: str):
    # Standardize name to lowercase to prevent matching errors
    return db.get(biome_name.lower(), {"title": "Unknown Archive", "color": "#ff4d4d", "video_url": ""})

# Mount order is important: Files inside folders first, then the root HTML
app.mount("/videos", StaticFiles(directory="videos"), name="videos")
app.mount("/", StaticFiles(directory="./", html=True), name="static")