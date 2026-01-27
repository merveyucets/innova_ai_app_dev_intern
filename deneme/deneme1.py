from google import genai

# API Key'ini buraya yapıştır
MY_API_KEY = "AIzaSyCbJreugXAa1XXRGYNheWUODv_7g5IEy7g" 

client = genai.Client(api_key=MY_API_KEY)

print("Mevcut modeller listeleniyor...")

try:
    # Filtreleme yapmadan sadece isimleri yazdırıyoruz
    for model in client.models.list():
        print(model.name)
        
except Exception as e:
    print(f"Hata detayı: {e}")