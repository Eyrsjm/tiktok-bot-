import google.generativeai as genai
import os

# مفتاح Gemini الخاص بك
API_KEY = "AIzaSyDm54DuLRPXB-PIHvqYaBrRM-k8mA5Ff80"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

def generate_tiktok_script():
    """توليد نص فيديو تيك توك"""
    prompt = "اكتب نصاً قصيراً ومشوقاً لفيديو تيك توك (4 جمل)"
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    print("🤖 بوت تيك توك شغال!")
    script = generate_tiktok_script()
    print("\n📝 نص الفيديو:")
    print(script)
    print("\n✅ تم بنجاح!")
