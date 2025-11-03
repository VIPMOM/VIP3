import telebot
import requests
import os

# محاولة الحصول على التوكن من متغير البيئة أولاً
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '')

# إذا لم يكن موجوداً، اطلبه من المستخدم
if not TOKEN:
    print("=" * 50)
    print("مرحباً بك في بوت تيليجرام")
    print("=" * 50)
    TOKEN = input("الرجاء إدخال توكن البوت الخاص بك: ").strip()
    
    if not TOKEN:
        print("❌ خطأ: لم يتم إدخال التوكن!")
        exit(1)
    
    print("✅ تم تعيين التوكن بنجاح!")
    print("=" * 50)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text
    
    # يمكنك تخزين هذه البيانات في متغيرات البيئة أيضاً
    cookies = {
        'sessionId': '01410e57-fd4c-469a-a568-0869638f496b',
        '__Host-authjs.csrf-token': 'f5e66df52e2e90a27f41aab0e3445ec1dcb388537b7ce4533d8e9be9b21b0572%7Cf7846468427f3f36904cd8b64b564e1ed7b43d9d2f62f3b1a2272164db0d81e4',
        '__Secure-authjs.callback-url': 'https%3A%2F%2Fwww.blackbox.ai%2Fchat%2Fexpert-python',
        '__Secure-authjs.session-token': 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..JTr0sPTzb4mYF4I2.EGWDMlnswBbg7gqEN5nt_fYRMUhncJ01YHPQXbPr0RFObk3nv6T_AEESkXeXNB5BrRgz_3g7DweBue4GcX9AR5DEpo2ResC5dhmHVLmeStd2JdaiMKhrVEBgplL0w9-f0swbhRDl15DuZHJreKHG5i-eFlrq6Zl7QHAXN6yQLIVF2DgtPsZWO8B2FcjiUk4AY0mDOpFJAtA7EsT4OaLEb42V5L1Vd2ykdiVjErK8mMIl3g5_R_Kb_m51OS7D0QFxx7pOMme2obzwEAPCnr1WoJVtI673cs_EBw4GBUvkGYkgP4cmW1zcoTKSlaHPgf9Bokir5Vet0VI0zsQR6_01jQV9Io2w8eTf3jSx53OGgQVUZoxj3G6j2bq88Jb25JTzGFCprI1EEh5zLNztnyCY8U7TNUMfkzNrckS_xuESHit0LDF7AK6qAcJ-u_Kezy5eFmYNZFveM_ZteUgwasa_BMODjr7rbl0Jk3WZMtv8QeFzLRdCWHmsXLJPONyhDO16c8z4.gjTzngC1N1YT0c6WYZqhDg',
    }
    
    headers = {
        'authority': 'www.blackbox.ai',
        'accept': '*/*',
        'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://www.blackbox.ai',
        'referer': 'https://www.blackbox.ai/chat',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }
    
    json_data = {
        'messages': [
            {
                'id': 'mpdSNYS',
                'content': user_input,
                'role': 'user',
            },
        ],
        'previewToken': None,
        'userId': None,
        'codeModelMode': True,
        'agentMode': {},
        'trendingAgentMode': {
            'mode': True,
            'id': 'python',
        },
        'isMicMode': False,
        'userSystemPrompt': None,  # تم إزالة المحتوى غير المناسب
        'maxTokens': 8096,
        'playgroundTopP': None,
        'playgroundTemperature': None,
        'isChromeExt': False,
        'githubToken': '',
        'clickedAnswer2': False,
        'clickedAnswer3': False,
        'clickedForceWebSearch': False,
        'visitFromDelta': False,
        'mobileClient': False,
        'userSelectedModel': 'gpt-4o',
        'validated': '00f37b34-a166-4efb-bce5-1312d87f2f94',
        'imageGenerationMode': False,
        'webSearchModePrompt': False,
        'deepSearchMode': False,
    }
    
    try:
        # إرسال رسالة "جاري الكتابة..." للمستخدم
        bot.send_chat_action(message.chat.id, 'typing')
        
        response = requests.post(
            'https://www.blackbox.ai/api/chat',
            cookies=cookies,
            headers=headers,
            json=json_data,
            timeout=30
        )
        
        if response.status_code == 200:
            alresponse = response.text
            
            # تقسيم الرسالة إذا كانت طويلة (حد تيليجرام 4096 حرف)
            if len(alresponse) > 4096:
                for i in range(0, len(alresponse), 4096):
                    bot.send_message(message.chat.id, alresponse[i:i+4096])
            else:
                bot.send_message(message.chat.id, alresponse)
        else:
            bot.send_message(
                message.chat.id, 
                f"حدث خطأ أثناء جلب البيانات. رمز الخطأ: {response.status_code}"
            )
    
    except requests.exceptions.Timeout:
        bot.send_message(message.chat.id, "انتهت مهلة الطلب. حاول مرة أخرى لاحقاً")
    
    except requests.exceptions.RequestException as e:
        bot.send_message(message.chat.id, f"حدث خطأ في الاتصال: {str(e)}")
    
    except Exception as e:
        bot.send_message(message.chat.id, f"حدث خطأ غير متوقع: {str(e)}")
        print(f"Error: {e}")

if __name__ == "__main__":
    print("البوت يعمل الآن...")
    bot.polling(none_stop=True)
