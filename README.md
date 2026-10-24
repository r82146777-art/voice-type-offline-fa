# آفلاین تایپ (نسخه اصلاح‌شده)

## تغییرات اعمال‌شده

1. **چینش کلیدها چپ‌چین (LTR)**  
   همهٔ صفحات صفحه‌کلید (فارسی، انگلیسی، اعداد و ...) چپ‌به‌راست چیده می‌شوند.

2. **افزایش اندازه صفحه‌کلید**  
   ارتفاع ردیف کلیدها ۵۶dp و فونت کمی بزرگ‌تر.

3. **نام برنامه**  
   نام اپ و صفحه‌کلید به **آفلاین تایپ** تغییر کرد.

4. **نام در بخش درباره ما**  
   مدیریت: امیرحسین بابایی، رضا ایمانزاده

5. **رفع مشکل مجوز میکروفون**  
   درخواست زودهنگام مجوز در شروع برنامه.

## ساخت APK

مدل `model-fa.zip` را از سورس اصلی در `app/src/main/assets/` قرار دهید و با Android Studio یا `./gradlew assembleRelease` بسازید.


## APK inspection/build pipeline

GitHub Actions workflow: `.github/workflows/apk-inspect.yml`. It downloads the shared APK, decodes it with apktool, attempts a baseline rebuild/signing, and publishes inspection artifacts. This is a tooling/bootstrap step only; it does not yet implement the requested speech-recognition, duplicate-input, keyboard-switching, or bundled natural TTS changes.
