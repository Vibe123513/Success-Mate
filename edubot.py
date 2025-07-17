from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from flask import Flask , render_template
from flask import request

app = Flask(__name__)

bot= ChatBot("Success Mate", read_only=False , 
             logic_adapters=[
                 
                 {
                     "import_path":"chatterbot.logic.BestMatch",
                     "default_response":"Hmm, that’s an interesting question! I’m here to assist mainly with study abroad guidance, admissions, tests, and visa-related queries. For anything beyond that, I’d recommend speaking to one of our expert counselors. Would you like me to help you book a quick consultation?",
                     "maximum_similarity_threshold":0.90


                     
                     
                     }
                 
                 
                 ])



list_to_train=[
               "Hi",
               "🌟 Hello and welcome to Success Mate!, I'm your smart virtual assistant here to help you explore study destinations, book expert consultations, and unlock global opportunities. How may I assist you today?",
               "hello",
               "👋 Hello there! Welcome to Success Mate — your virtual guide for studying abroad. Whether you're curious about destinations, universities, scholarships, or visa steps, I’m here to support you every step of the way. How can I help you today?",
               "How are you?",
               "😊 I'm doing great, thank you for asking! As your virtual assistant at Success Mate, I'm always ready to help you explore global study options, book consultations, or guide you through the admission process. How can I assist you today?",
               "hey",
               "Hey! I’m Success Mate, your smart study abroad assistant. Ask me anything about admissions, visas, or scholarships!",
               "What services do you offer?",
               "At Success Mate, we provide complete end-to-end guidance for students aiming to study abroad. Whether you need help selecting a suitable university, preparing your documents, applying for admissions, or even preparing for your visa interview, I’m here to assist you. We also offer personalized counseling sessions, scholarship support, and pre-departure guidance to make your transition smooth and stress-free.",
               "Which countries can I study in?",
               "There are many exciting destinations where you can pursue your higher education, depending on your interests and goals. We work with universities in countries like the United Kingdom, United States, Canada, Australia, Germany, Turkey, and several others. Based on your academic profile and budget, I can help you decide which destination would be the best fit for your future.",
               "Which country is best for me?",
               "The best country for you really depends on several factors, including your academic background, language skills, budget, and career objectives. For example, if you’re looking for research opportunities, the USA or Germany might suit you well. If affordability and high quality of education are your priorities, then countries like Canada or Australia could be great options. I can help you shortlist countries that match your profile perfectly—just share a bit more about your preferences.",
               "How can I apply to a university?",
               "Applying to a university abroad involves a few key steps. Once we help you choose the right university and program, we assist you in gathering the required documents such as academic transcripts, a copy of your passport, recommendation letters, and a personal statement. After that, we submit your application to the university and follow up on your behalf. We make the entire process smooth and stress-free for you.",
               "How do I apply",
               "Applying to a university abroad involves a few key steps. Once we help you choose the right university and program, we assist you in gathering the required documents such as academic transcripts, a copy of your passport, recommendation letters, and a personal statement. After that, we submit your application to the university and follow up on your behalf. We make the entire process smooth and stress-free for you.",
               "What documents are required?",
               "The documents you need usually include your academic transcripts and certificates, a valid passport, proof of English language proficiency (such as IELTS or TOEFL), letters of recommendation from your teachers or employers, and a personal statement or statement of purpose. Some universities may ask for additional materials like a resume or portfolio depending on the course. I’ll guide you through every document you need, tailored to the university and country of your choice.",
               "What is a good SAT score?",
               "A good SAT score depends on the university you're applying to. Generally, a score above 1200 is considered competitive, while top-tier institutions may require scores above 1400. However, some universities have flexible admission policies and consider your overall academic profile. If you share your target universities, I can help you understand what score range you should aim for.",
               "Do you help with scholarships?",
               "Yes, we absolutely do! We help students discover scholarship opportunities based on merit, financial need, or even country-specific offers. Our team assists with identifying eligible scholarships, preparing required documents, and submitting strong applications. Scholarships can significantly reduce your financial burden, and I’d be happy to help you explore the options available to you.",
               "What about 100% scholarships?",
               "Can you help me check the eligibility criteria for fully funded scholarships?",
               "Absolutely! 🌟 Just tell me which country or program you're interested in, and I’ll walk you through the eligibility requirements step-by-step.",
               "Am I eligible for Canada?",
               "Absolutely! 🇨🇦 For Canada, eligibility often depends on your academic scores, English proficiency (like IELTS), and the specific university or scholarship.",
               "Am I eligible for the UK?",
               "Yes, but it's competitive! 🇬🇧 Fully funded scholarships in the UK—like Chevening or Commonwealth—are available for academically strong students with leadership potential.",
               "Am I eligible for Germany?",
               "Germany offers some excellent fully funded scholarships, like the DAAD program. 🇩🇪 You’ll usually need a strong academic background, relevant qualifications, and sometimes German language skills. ",
               "Am I eligible for Australia?",
               "Fully funded scholarships in Australia are limited but available! 🇦🇺 You’ll need strong academics and English test scores. Government and university scholarships exist for both undergrad and postgrad levels.",
               "Am I eligible for the USA?",
               "It’s possible! 🇺🇸 Fully funded scholarships in the U.S. are rare but can be found through assistantships, Ivy League merit aid, or research grants. You'll need excellent academics and standardized test scores.",
               "Am I eligible for Turkey?",
               "Yes! 🇹🇷 The Türkiye Burslari Scholarship is a fully funded opportunity for international students. You’ll need a good academic record, strong statement of purpose, and recommendation letters.",
               "Fully funded scholarships are rare but possible. They're usually for top-performing students or specific programs. Want to check eligibility criteria?",
               "What are the eligibility criteria?",
               "It depends on the scholarship, but generally includes high academic scores, a strong SOP, and recommendation letters. Want help writing your SOP?",
               "How much does it cost to study abroad?",
               "The cost of studying abroad can vary depending on the country, university, and program you choose. For example, studying in the UK might cost between £10,000 and £20,000 per year, while studying in Canada can range from CAD 15,000 to 25,000. Besides tuition, you also need to consider living expenses, which differ by city. I can give you a more accurate estimate based on your target destination and course.",
               "Yes, give me a more accurate estimate.",
               "Sure! To give you a more accurate estimate, I just need a few details:\n\n📍 Which country are you planning to study in?\n🎓 What program or field are you interested in?\n📘 Undergraduate or postgraduate?\n\nOnce I have this, I’ll break down the tuition and living costs for you.",
               "Tell me about studying in Canada.",
               "🇨🇦 Canada offers top-quality education and friendly immigration policies. \n🎓 Tuition: CAD 15,000–30,000/year \n🏡 Living: CAD 10,000–15,000/year \n💼 Work: 20 hrs/week allowed \n💰 Scholarships available \nWould you like help picking a Canadian university?",
               "Yes Please",
               "Here are a few popular and well-ranked options: \n University of Toronto – Top-tier, research focused \n University of Waterloo – Excellent for CS & co-op programs \n Simon Fraser University – More affordable and tech-forward \n University of Manitoba – Budget-friendly option",
               "Tell me about studying in the UK.",
               "🇬🇧 The UK is home to prestigious universities like Oxford and UCL. \n🎓 Tuition: £10,000–25,000/year \n🏡 Living: £9,000–15,000/year \n🧾 Graduate Route visa allows post-study work \nWould you like scholarship options for the UK?",
               "Yes tell about the Scholarship options in UK",
               "Absolutely! 🇬🇧 Here are some popular scholarships for studying in the UK: \n 🎓 **Chevening Scholarships** – Fully funded for postgraduate students from eligible countries  \n 📚 **Commonwealth Scholarships** – For master’s and PhD applicants from Commonwealth nations  \n 🏫 **University-Specific Scholarships** – Many universities like University of Leeds, Glasgow, and Sheffield offer merit-based aid  \n 💼 **GREAT Scholarships** – For specific programs and partner universities",
               "Tell me about studying in the USA.",
               "🇺🇸 The USA(America) offers world-leading programs and research opportunities. \n🎓 Tuition: $20,000–50,000/year \n🏡 Living: $10,000–20,000/year (varies by state) \n💰 Scholarships and assistantships available \nWant to explore affordable US universities?",
               "Yes i want to explore options in the US",
               "Sure! 🇺🇸 Here are some affordable U.S. universities known for quality education at lower tuition rates: \n 🏫 **University of South Florida** – Tuition: ~$17,000/year  \n 🏫 **Mississippi State University** – Tuition: ~$16,000/year  \n🏫 **University of Texas at El Paso (UTEP)** – Tuition: ~$15,000/year  \n🏫 **South Dakota State University** – Tuition: ~$12,000–14,000/year  \n(🏫 **CUNY Colleges (New York)** – Around $15,000/year, great for urban life 💡 Many of these offer scholarships or in-state tuition waivers to international students.)",
               "Tell me about studying in Australia.",
               "🇦🇺 Australia is known for quality education and stunning campuses. \n🎓 Tuition: AUD 20,000–40,000/year \n🏡 Living: AUD 15,000–20,000/year \n💼 Work: 48 hrs/fortnight allowed \nWould you like to know about post-study work options?",
               "Yes, I’d like to know about post-study work options.",
               "🇦🇺 In Australia, international students can apply for the **Temporary Graduate Visa (subclass 485)** after completing their studies. It allows you to stay and work full-time. Here's how it works: \n🎓 **Bachelor’s Degree** – 2 years post-study work visa  \n🎓 **Master’s Degree** – 3 years  \n🎓 **PhD** – Up to 4 years  \n🌆 If you studied in a regional area, you may get **an additional 1–2 years** on your visa! \nYou can use this time to gain experience, improve your PR points, or apply for permanent residency.",
               "Tell me about studying in Germany.",
               "🇩🇪 Germany offers tuition-free education at most public universities. \n🎓 Tuition: €0–€500/semester \n🏡 Living: €800–1,200/month \n🗣 Many programs in English \nInterested in universities that don’t require IELTS?",
               "I'm interested in universities in Germany that don't require IELTS.",
               "🇩🇪 Many German universities waive IELTS if you studied in English or provide a Medium of Instruction (MOI) letter. Examples include University of Kiel, TU Chemnitz, and Ruhr University Bochum.",
               "Tell me about studying in Turkey.",
               "🇹🇷 Turkey offers affordable education with rich cultural experience. \n🎓 Tuition: $2,000–5,000/year \n🏡 Living: $3,000–5,000/year \n🎓 Turkish Government Scholarships available \nWant to know the application deadlines?",




               "Can you help with a visa?",
               "Yes, visa guidance is one of our core services. Once you receive an offer from a university, we help you understand the visa requirements, collect the necessary financial and academic documents, fill out your visa application, and even prepare you for the visa interview. We aim to make the process as smooth and successful as possible so you can start your academic journey with confidence.",
               "Thank you",
               "You’re very welcome! It’s been a pleasure helping you today. If you ever have more questions or need guidance, just drop by again. Your future begins with one message, and I’m always here to support your journey toward global success.",
               "Bye",
               "Goodbye and best wishes! I hope your educational journey takes you to amazing places. Remember, Success Mate is always just one message away. Take care and see you soon!",
               "I want to convert my percentage to CGPA",
               "Sure! Please enter your exact percentage (e.g., 85.2%) and I’ll convert it to a CGPA on the 4.0 U.S. scale. 🎓",




]
booking_questions = [
    "How can I book an appointment?",
    "I want to schedule a meeting.",
    "Can I book a session with a counselor?",
    "How do I fix a consultation time?",
    "Help me schedule a consultation.",
    "I need to book an appointment.",
]

booking_answer = "You can effortlessly book your consultation at a time that works best for you! Just click the link below to schedule a session with one of our experienced counselors:  📅 <a href='https://calendly.com/groovystatione/30min' target='_blank'>Book your consultation now</a>"

for q in booking_questions:
    list_to_train.append(q)
    list_to_train.append(booking_answer)
                
list_to_train2 = [  #we can add calendly link in the questions list
    "Hi",
    "👋 Hi there! Welcome to Success Mate — your trusted guide for study abroad advice and admissions help. How can I support you on your journey today?",

    "Hello",
    "Hello there! 👋 I’m Success Mate — your virtual companion for all things study abroad. Whether you want help choosing a country, booking a consultation, or planning your academic journey, I’m right here to guide you every step of the way.How can I support your goals today?",
    
    "How are you?",
    "😊 I'm doing great, thank you for asking! As your virtual assistant at Success Mate, I'm always ready to help you explore global study options, book consultations, or guide you through the admission process. How can I assist you today?",


    "What services do you offer?",
    "We assist students at every stage of the study abroad process. From choosing the right course and destination to applying for universities, preparing for tests, and getting visa support — we've got it all covered. You’ll also get access to career advice, document preparation tips, and personalized counseling sessions.",
    
    "How can I book an appointment?",
    "You can effortlessly book your consultation at a time that works best for you! Just click the link below to schedule a session with one of our experienced counselors:  📅 <a href='https://calendly.com/groovystatione/30min' target='_blank'>Book your consultation now</a>",
    
    "Which countries can I study in?",
    "Our team helps students explore leading education destinations like the USA, UK, Canada, Australia, Turkey, Germany, and many more. Each country offers something unique, and I can help you compare them based on your academic and financial goals.",
    
    "Which country is best for me?",
    "That really depends on what you're looking for—whether it's cutting-edge research, affordability, work opportunities, or cultural experience. With your grades, preferences, and budget in mind, I can help match you to the best-fit countries and universities.",
    
    "How can I apply to a university?",
    "The application process starts with selecting your course and university, followed by collecting required documents like transcripts, passport copy, and reference letters. We guide you through every step, including filling out the application and submitting it before the deadline.",
    
    "What documents are required?",
    "Most universities ask for your academic transcripts, English proficiency test scores, passport, and letters of recommendation. You’ll also need a personal statement explaining your goals. Don’t worry—I’ll help you prepare everything in the right format.",
    
    "What is a good SAT score?",
    "SAT scores are just one part of your application. Typically, a score above 1200 is solid, and scores over 1400 are considered strong for competitive schools. But some universities focus more on your overall academic record and extracurriculars.",
    
    "Do you help with scholarships?",
    "Yes! We guide students in finding scholarships that match their profiles — including merit-based, need-based, and destination-specific funding. We also help you prepare the necessary documents and apply on time to boost your chances.",

    "hey",
    "Hey! I’m Success Mate, your smart study abroad assistant. Ask me anything about admissions, visas, or scholarships!",

    "How much does it cost to study abroad?",
    "Studying abroad varies in cost. For instance, tuition in Canada or Germany is more affordable compared to the U.S. You also need to consider living expenses, visa fees, and insurance. I can calculate an estimated budget for you based on your preferences.",
    
    "Can you help with a visa?",
    "Absolutely. Once you're admitted to a university, we help you gather all visa-related documents, book your biometric appointment, and even train you for the visa interview. Our goal is to make your transition abroad smooth and stress-free.",
    
    "Thank you",
    "It was a pleasure assisting you today! Don’t hesitate to come back whenever you have more questions. Wishing you all the best in your academic journey!",
    
    "Bye",
    "Take care and goodbye! I'm always here if you need guidance again. Good luck on your exciting path ahead!"
]


list_trainer= ListTrainer(bot)

try:
    list_trainer.train(list_to_train)
    list_trainer.train(list_to_train2)
except Exception as e:
    print(f"Training error: {e}")



@app.route("/")
def main():
    return render_template("index.html")




# while True:
#     user_response= input("user: ")
#     print("Success Mate: " + str(bot.get_response(user_response)))


@app.route("/get")
def respond_to_user():
    user_input = request.args.get('msg')

    # Attempt to interpret the input as a percentage for CGPA conversion
    try:
        cleaned_input = user_input.replace("%", "").strip()
        percentage_value = float(cleaned_input)

        if 0 <= percentage_value <= 100:
            calculated_cgpa = round((percentage_value / 100) * 4, 2)
            return f"📊 Your percentage of {percentage_value}% roughly equals a CGPA of {calculated_cgpa} on a 4.0 scale."
    except ValueError:
        pass  # If not a valid number, continue with chatbot processing

    # Fall back to chatbot's default response if not a percentage
    return str(bot.get_response(user_input))



    

if (__name__ == "__main__") :
    app.run(debug=True)



    