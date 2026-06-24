from dotenv import load_dotenv
load_dotenv()
import os


# from langchain_mistrallAI
# model=chatopenAI(model_name="gpt-4")

# res=model.invoke("Hi chagpt")
# print(res.content)

from langchain_google_genai import ChatGoogleGenerativeAI

# # gemini-2.5-flash
# model = ChatGoogleGenerativeAI(model="gemini-2.5-flash",google_api_key=os.getenv("GOOGLE_API_KEY"))

# res = model.invoke("Hi ChatGPT mujhe 5 countery ka name bataoo aur eoo english me dena and table fromate me ok ")
# print(res.content)




# from langchain_groq import ChatGroq

# model=ChatGroq(model="openai/gpt-oss-120b")
# res=model.invoke("hey write five colors name")
# print(res.content)


# model= init_chat_model("groq:penai/gpt-oss-120b")
# res=model.invoke("hello tell name of five person")
# print(res.content)









# model=chatMistrAI(model="mistral/mistral-large-latest")
# res=model.invoke("hello write a cute poem")
# print(res.content)





