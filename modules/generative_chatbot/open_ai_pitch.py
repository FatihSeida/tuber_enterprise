import os
import openai
from openai import OpenAI

# Documentation about the Tokopedih E-commerce Platform
project_doc = """
Chatbot ini diperuntukan hanya untuk menjawab pertanyaan-pertanyaan yang berkaitan dengan pembuatan pitch deck.
'Maaf chatbot ini diperuntukan untuk menjawab hal yang berkaitan dengan pembuatan pitch deck'
Service yang dapat disediakan perusahaan Sosofwerhausan:

Backend Developer: Cara mudah mendapatkan tenaga kerja outsourcing Java Developer, .Net Developer, Golang Developer, NodeJS Developer, dan PHP Developer

Frontend Developer: Cara mudah mendapatkan tenaga kerja outsourcing React.JS, Vue.JS,dan Angular.JS Developer

Mobile App Developer: Cara mudah mendapatkan tenaga kerja outsourcing React Native, Flutter, Native Android, iOS Developer

Business Analyst: Cara mudah mendapatkan tenaga kerja outsourcing IT Business Analyst, IT System Analyst, dan Technical Writer

DevOps Engineer: Cara mudah mendapatkan tenaga kerja outsourcing DevOps Engineer Profesional

Project Manager: Cara mudah mendapatkan tenaga kerja outsourcing Project Manager

IT Security Specialist: Cara mudah mendapatkan tenaga kerja outsourcing IT Security Engineer

Software QA: Cara mudah mendapatkan tenaga kerja outsourcing Software Quality Assurance Automation Tester & Software Quality Assurance Manual Tester

UI/UX Designer: Cara mudah mendapatkan tenaga kerja outsourcing UI / UX Designer Profesional

Sebagai informasi, saat ini perusahaan tidak dapat melayani pengiriman tenaga kerja IT di luar pengembangan software seperti
IT Support, IT Help-desk, Network Engineer, dll


Mengapa Harus Menggunakan Layanan dari Sosofwerhausan?
Sosofwerhausan memiliki tim tech recruiter berpengalaman untuk mencari talenta berbakat di bidang IT.
Sebagai perusahaan berbasis teknologi, Sosofwerhausan memiliki tim tech recruiter berpengalaman untuk mencari talenta berbakat di bidang IT. Kami juga didukung tenaga IT (engineer) yang kompeten dalam melakukan technical assessment untuk menilai keterampilan yang dimiliki kandidat sehingga kualitas tenaga kerja terjamin dan sesuai kebutuhan proyek Anda. Kami juga berpengalaman dalam melakukan seleksi tenaga IT, baik itu penilaian kemampuan fundamental ataupun technical kandidat sehingga tenaga IT yang akan kami sediakan akan sesuai dengan kebutuhan perusahaan Anda.
Sosofwerhausan memiliki akses ke lebih dari 50.000 database untuk berbagai keterampilan IT
Sosofwerhausan memiliki akses ke lebih dari 50.000 database untuk berbagai keterampilan IT dari level junior hingga senior sehingga penyaluran tenaga kerja outsource IT bisa dilakukan dalam waktu yang cepat. Kami dapat mengirimkan tenaga outsourcing yang sesuai dengan kebutuhan Anda dalam kurun waktu maksimal 3 hari kerja sejak kerjasama disepakati oleh kedua belah pihak.
Kami dapat memberi masukan ataupun saran terkait resource planning yang Anda butuhkan tanpa biaya tambahan
Tidak mengetahui keterampilan apa saja yang dibutuhkan untuk proyek digital Anda? Tidak perlu khawatir! Kami dapat memberi masukan ataupun saran terkait resource planning yang Anda butuhkan tanpa biaya tambahan (GRATIS). Silakan hubungi kami untuk berkonsultasi dengan tim profesional dari Sosofwerhausan.
Perusahaan Anda akan menghemat waktu dan beban rekrutmen, tanpa harus mengeluarkan biaya pelatihan
Dengan layanan penyaluran tenaga IT dari Sosofwerhausan, perusahaan Anda akan menghemat waktu dan beban rekrutmen. Layanan ini juga dapat membantu perusahaan IT developer Anda untuk menemukan tenaga kerja IT yang sudah berpengalaman tanpa harus mengeluarkan biaya pelatihan.
Sosofwerhausan memprioritaskan keamanan IT serta memiliki kebijakan keamanan yang ketat
Sosofwerhausan adalah perusahaan outsourcing yang memprioritaskan keamanan IT serta memiliki kebijakan keamanan yang ketat. Tenaga kerja yang kami kirimkan akan turut serta menjaga kerahasiaan data perusahaan Anda.
"""

def chat_with_gpt_pitch(prompt, model="gpt-4-turbo"):
    full_prompt = f"{project_doc}\n\nQuestion: {prompt}"
    client = OpenAI(
        api_key=str(os.getenv("OPENAI_API_KEY")),
    )
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant familiar with creating a good pitching deck to client for starting a new software project in Sosofwerhausan software house."},
                {"role": "user", "content": full_prompt}
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"