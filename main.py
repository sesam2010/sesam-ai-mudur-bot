from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Merhaba Volkan Bey.\n\nBen Sesam AI Müdür.\nHazırım."
    )

async def plan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """📋 Bugünün Planı

1- Hepsiburada Buybox kontrol
2- Trendyol sipariş kontrol
3- Instagram paylaşımı
4- Personel görüşmeleri
5- Depo düzeni

🚀 Hedef: Satışı artırmak
"""
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("plan", plan))

app.run_polling()
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import os
from datetime import datetime

TOKEN = os.getenv("BOT_TOKEN")

GUNLUK_PLAN = """
🧠 Selim Volkan Operasyon Müdürü

GÜNÜN ANA HEDEFİ:
Satışı artır, dağınıklığı azalt, ekibi kontrol et.

1️⃣ E-TİCARET
• Hepsiburada Buybox kayıplarını kontrol et
• Trendyol siparişleri kontrol et
• Amazon kurulum adımlarını ilerlet
• Entegra ürün/stok/fiyat hatalarına bak

2️⃣ DEPO
• Günlük sevkiyat listesi kontrol
• Geciken kargo var mı?
• Ağır yük / paketleme alanı düzeni
• İade gelen ürün kontrolü

3️⃣ PERSONEL
• Eksik pozisyonlar: depo, e-ticaret, ön muhasebe
• Bugün en az 3 aday aranacak
• Mevcut ekipten aksayan iş sorulacak

4️⃣ INSTAGRAM
• 1 reels fikri
• 1 story
• 1 ürün güven vurgusu
• AI gibi değil, gerçek firma dili

5️⃣ PARA
• Bugünkü hedef: gereksiz işi kes, para getiren işe odaklan
• Öncelik: teklif, sipariş, tahsilat
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Merhaba Volkan Bey.\n\nBen Selim Volkan'ın Operasyon Müdürüyüm.\nBugünden itibaren işi, ekibi, satışı ve günlük planı takip ederim.\n\nKomutlar:\n/bugun\n/plan\n/instagram\n/personel\n/depo\n/eticaret\n/hedef\n/rapor"
    )

async def bugun(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(GUNLUK_PLAN)

async def plan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(GUNLUK_PLAN)

async def instagram(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """📱 Bugünkü Instagram Planı

Reels:
"İş güvenliği ekipmanı sadece ürün değil, işçinin hayat sigortasıdır."

Story:
• Depodan ürün hazırlık görüntüsü
• Üzerine: “Bugün Türkiye geneli sevkiyat devam ediyor.”

Post fikri:
SSM iş elbiseleri + iş ayakkabısı kombin paylaşımı

Dil:
Kurumsal, sade, güven veren.
AI gibi değil, gerçek Sesam Grup dili."""
    )

async def personel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """👷 Personel Takip Planı

Bugün aranacak pozisyonlar:
1. Depo-sevkiyat ağır yük
2. E-ticaret uzmanı
3. Ön muhasebe + mağaza satış

Adaylara sor:
• Daha önce depo/e-ticaret tecrüben var mı?
• Ankara/İvedik ulaşım uygun mu?
• Uzun vadeli çalışır mısın?
• Maaş beklentin nedir?

Bugünün hedefi:
En az 3 kişiyle görüşme."""
    )

async def depo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """📦 Depo Kontrol Listesi

1. Geciken kargo var mı?
2. Yanlış çıkan ürün var mı?
3. İade gelen ürünler kontrol edildi mi?
4. Ağır ürünler ayrı alanda mı?
5. Paketleme alanı düzenli mi?
6. Bugün çıkan sipariş sayısı kaç?

Kural:
Depo dağınıksa satış büyümez."""
    )

async def eticaret(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """🛒 E-Ticaret Kontrol

Hepsiburada:
• Buybox kaybedilen ürünleri kontrol et
• Premium fiyatları kontrol et
• Kargo desi hatalarına bak

Trendyol:
• Sipariş gecikmesi var mı?
• Fiyat rekabeti bozuldu mu?

Amazon:
• Mağaza kurulum adımı ilerlet
• FBA mantığını netleştir

Entegra:
• Stok/fiyat eşleşmesi kontrol."""
    )

async def hedef(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """🎯 Bugünün Hedefi

Ana hedef:
Satış + düzen + takip.

Para getiren işler:
1. Teklif gönder
2. Siparişleri hızlandır
3. Buybox kontrol et
4. Personel eksiklerini kapat
5. Instagram güven algısını büyüt

Bugünün net cümlesi:
Volkan Bey bugün düşünmeyecek, sistem takip edecek."""
    )

async def rapor(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.now().strftime("%d.%m.%Y %H:%M")
    await update.message.reply_text(
        f"""📊 Günlük Rapor Şablonu
Tarih: {now}

Ciro:
Sipariş sayısı:
Geciken kargo:
Aranan aday:
Görüşülen aday:
Instagram paylaşımı:
Buybox kontrol:
Acil sorun:

Akşam bana bu bilgileri yaz, ben sana patron raporu çıkarayım."""
    )

async def mesaj_yakala(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "ne yapayım" in text or "bugün" in text:
        await update.message.reply_text(GUNLUK_PLAN)
    elif "instagram" in text:
        await instagram(update, context)
    elif "personel" in text or "eleman" in text:
        await personel(update, context)
    elif "depo" in text:
        await depo(update, context)
    elif "hedef" in text:
        await hedef(update, context)
    else:
        await update.message.reply_text(
            "Anladım Volkan Bey. Bunu operasyon notu olarak düşüyorum.\n\nHızlı komutlar:\n/bugun /instagram /personel /depo /eticaret /hedef /rapor"
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("bugun", bugun))
app.add_handler(CommandHandler("plan", plan))
app.add_handler(CommandHandler("instagram", instagram))
app.add_handler(CommandHandler("personel", personel))
app.add_handler(CommandHandler("depo", depo))
app.add_handler(CommandHandler("eticaret", eticaret))
app.add_handler(CommandHandler("hedef", hedef))
app.add_handler(CommandHandler("rapor", rapor))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mesaj_yakala))

app.run_polling()
