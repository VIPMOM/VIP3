# Telegram Bot - Blackbox AI Integration

## التحسينات التي تم إجراؤها:

### 1. إصلاح الأخطاء البرمجية:
- ✅ إصلاح خطأ المسافة قبل `@bot.message_handler`
- ✅ تصحيح البنية العامة للكود

### 2. تحسينات الأمان:
- ✅ استخدام متغيرات البيئة للتوكن بدلاً من كتابته مباشرة
- ✅ إزالة المحتوى غير المناسب من `userSystemPrompt`

### 3. معالجة الأخطاء:
- ✅ إضافة `try-except` blocks
- ✅ معالجة timeout errors
- ✅ معالجة connection errors
- ✅ رسائل خطأ واضحة بالعربية

### 4. تحسينات إضافية:
- ✅ إضافة timeout للطلبات (30 ثانية)
- ✅ تقسيم الرسائل الطويلة (حد تيليجرام 4096 حرف)
- ✅ إضافة "جاري الكتابة..." للمستخدم
- ✅ إضافة `none_stop=True` للـ polling

## كيفية الاستخدام:

### 1. تثبيت المكتبات المطلوبة:
```bash
pip install -r requirements.txt
```

### 2. تعيين توكن البوت:
```bash
export TELEGRAM_BOT_TOKEN="your_bot_token_here"
```

أو في Windows:
```cmd
set TELEGRAM_BOT_TOKEN=your_bot_token_here
```

### 3. تشغيل البوت:
```bash
python telegram_bot.py
```

## ملاحظات مهمة:

⚠️ **التوكن والجلسات**: 
- احصل على توكن البوت من [@BotFather](https://t.me/botfather)
- الـ session tokens في الكود قد تنتهي صلاحيتها، قد تحتاج لتحديثها

⚠️ **الاستخدام الأخلاقي**:
- تم إزالة المحتوى غير المناسب من الكود الأصلي
- استخدم البوت بشكل مسؤول وأخلاقي

⚠️ **الأداء**:
- البوت يستخدم polling، للإنتاج يُفضل استخدام webhooks
- قد تحتاج لإضافة rate limiting لتجنب الحظر
