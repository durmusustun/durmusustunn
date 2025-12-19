import os
from huggingface_hub import HfApi, create_repo

# --- AYARLAR ---
# 1. Hugging Face Kullanıcı Adın ve Dataset Adın
REPO_ID = "durmus04/noisy_voice_dataset"  # <-- Kendi kullanıcı adını yaz!

# 2. Bilgisayarında yüklemek istediğin klasörün yolu
# Örnek: "/home/durmusustun/project/after/911_fixed"
YUKLENECEK_KLASOR = "/home/durmusustun/project"

def main():
    api = HfApi()

    if not os.path.exists(YUKLENECEK_KLASOR):
        print(f"❌ HATA: '{YUKLENECEK_KLASOR}' klasörü bulunamadı!")
        return

    print(f"🚀 '{REPO_ID}' deposuna bağlanılıyor...")

    # 1. Depoyu Oluştur (Eğer zaten varsa hata vermez, devam eder)
    try:
        create_repo(repo_id=REPO_ID, repo_type="dataset", exist_ok=True)
        print("✅ Depo hazır (veya oluşturuldu).")
    except Exception as e:
        print(f"⚠️ Depo uyarısı: {e}")

    # 2. Klasörü Yükle
    print(f"📦 Dosyalar yükleniyor... Lütfen bekleyin.")
    
    api.upload_folder(
        folder_path=YUKLENECEK_KLASOR,
        repo_id=REPO_ID,
        repo_type="dataset",
        path_in_repo=".",  # "." demek: Dosyaları direkt ana sayfaya at (Klasör içine değil)
        commit_message="Veri seti yüklendi"
    )

    print(f"\n🎉 İŞLEM TAMAM! Verilerine şuradan bakabilirsin:\nhttps://huggingface.co/datasets/{REPO_ID}")

if __name__ == "__main__":
    main()