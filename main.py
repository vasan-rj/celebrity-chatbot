from dotenv import load_dotenv
from streamlit_modal import Modal
from PIL import Image
import streamlit as st
import os
import google.generativeai as genai
import random
st.set_page_config(page_title="Celebrity.AI")
# loading enviroinmental variables
load_dotenv()
api_lst=[]
msg_query=[]

api_lst.append(os.environ.get('GOOGLE_API_KEY_1'))
api_lst.append(os.environ.get('GOOGLE_API_KEY_2'))
api_lst.append(os.environ.get('GOOGLE_API_KEY_3'))
api_lst.append(os.environ.get('GOOGLE_API_KEY_4'))
api_lst.append(os.environ.get('GOOGLE_API_KEY_5'))


key_random=random.randint(0,len(api_lst)-1)

genai.configure(api_key=str(api_lst[key_random]))

modal = Modal(key="Demo Key",title=["test"])

# loading model
model=genai.GenerativeModel('gemini-pro')

# chat variables store all chat history

chat = model.start_chat(history=[])

def main_page():
    # st.write(key_random)
    # st.write(api_lst[key_random])
    st.caption("🛠️use dark theme for better user experience 😎")

    title_text = '<p style="font-family:Impact; color:rgb(255, 161, 39);; font-size: 50px;">CELEBRITY AI</p>'
    st.markdown(title_text, unsafe_allow_html=True)
    st.write("-"*50)
    
    
    st.header(" 🚀Chat with Fomous personalities 🙎🏼 Anytime ⏲️, Anywhere!!! 📌")
    st.write("\n")
    st.write("\n")
    # if st.checkbox('checkbox'):
    st.image("black-img-trans.png")
    # 
    # st.image("black-img-trans-resized.png")
    # 
    st.write("\n")
    st.write("\n")
    st.write("\n")
    
    user_input = st.text_input(' *Enter Celebrity name 🧔🏽‍♂️👩🏽:')
    # original_title = '<p style="font-family:Impact; color:rgb(255, 161, 39);; font-size: 50px;">Original image</p>'
    # st.markdown(original_title, unsafe_allow_html=True)
    st.write("\n")
    st.write("\n")
    st.write("\n")
    # 🛠️✨🎯📌🚀🔥🙎🏼🙎🏼🧔🏽‍♂️👩🏽🔥
    con_type=st.selectbox(
        " *how you want your conversation to be ?",
        ['Friendly 😊','Casual 😎','Formal 🙂','Inspirational 🥺',"Serious 😨","Funny 🤣",'Informative 🧐','Professional 🤓','Sarcastic 😆','Respectful 🫡','Motivational 🤯']
    )
    st.write("\n")
    st.write("\n")
    st.write("\n")
    
    con_length=st.selectbox(
        " *choose preffered chat length",
        ['Crisp (5 - 50 words)','Short (50 - 100 words)','Medium (100 - 200 words)','Long (200 - 350 words)']
    )
    
    st.write("\n")
    st.write("\n")
    st.write("\n")
    next=st.button('Next')
    st.caption("Click next to continue..")
    st.write("-"*50)
    st.subheader("Help us improve📝")
    st.write("Share your Valuable feedback: https://shorturl.at/itEM2")
    st.write("-"*50)
    st.subheader("Contact Me!! 📱")
    # st.subheader("Made by Vasan R ❤️")
    
    st.write("Email Me! 📧 contact.vasanml@gmail.com")
    st.write("My github 🐈‍⬛ https://github.com/vasan-rj")
    st.write("My LinkedIn 🔗 https://www.linkedin.com/in/vasan-r/")
    st.caption("Made by Vasan R ❤️")
    if next :
        if con_length and con_type and user_input:  
            # Save user input to session state
            st.session_state.user_input = user_input
            st.session_state.con_type=con_type
            st.session_state.con_length=con_length
            
            # Navigate to the "side" page
            st.experimental_set_query_params(page='side')
        else:            
            with modal.container():
                st.markdown('" :red[ENTER THE CELEBRITY NAME..... ]"')
               
            
            
def side_page():
    # st.write(st.session_state['user_input'])
    st.caption("🛠️use dark theme for better user experience 😎")
    title_text = '<p style="font-family:Impact; color:rgb(255, 161, 39);; font-size: 50px;">CELEBRITY AI</p>'
    st.markdown(title_text, unsafe_allow_html=True)
    st.subheader('🔥Talk to famous personality like Shah Rukh Khan Ghandhi ji Hitler ,Andrew Tate RDJ Etc....✨')
    
    st.write("-"*20)
    # Retrieve user data from session state
    if 'user_input' and 'con_type' and 'con_length' in st.session_state:
        user_input = st.session_state.user_input
        con_type=st.session_state.con_type
        con_length=st.session_state.con_length
        
    
        # st.write(f"User data from Main Page: {user_input}")
        # st.write(f"User data from Main Page: {con_type}")
        # st.write(f"User data from Main Page: {con_length}")
    else:
        st.write("⚠️⚠️⚠️ERROR: Go back to Main Page and type celebrity name and try again....⚠️⚠️⚠️")
        
        
    def respone_from_gemini(query):
        try:
            res_ponse=model.generate_content(query)
        except:
            res_ponse="Soory error occured try again please ..."
            
        return res_ponse
        
        # response=model.generate_content(query,stream=True)
        
    # st.set_page_config(page_title="Q and A Demo")
     
    x=""
    # st.image("black-img-trans.png")
    initial_prompt= f''' 
    user : hey you are a celebrity chatbot which gives reply like {user_input} ,
    Your role is to respond authentically, reflecting the unique mannerisms, vocabulary, and style of {user_input}
    And i want you to give response to the asked question in the {con_type} manner, and your response should be {con_length}, 
    make sure that you give correct and human readable answers ,Embrace their personas and interact naturally, providing users with an
    immersive experience akin to chatting with their idols, make sure you add emojis to your response.
    
    ai : hey i am {user_input} bot !!  
    
    '''
    x+=initial_prompt
    # st.write(x)
# d={}
    if 'chat-history' not in st.session_state:
        st.session_state['chat-history'] =[]
        
    with st.chat_message("ai"):
        st.markdown(f"hey i'm {user_input} bot!!")    
        
    # st.write(x)
    for role,res in st.session_state['chat-history']:
        with st.chat_message(role):
            st.markdown(res)
    # st.write("-"*20)
    # for message in st.session_state['chat-history']:
    #     with st.chat_message(message[0]):
    #         st.markdown(message[1].text)
               
    
    # input=st.chat_input("Say something")
    
    if input := st.chat_input("Talk to celebrity!!"):
        with st.chat_message("user"):
            st.markdown(input)
    
        st.session_state['chat-history'].append(("user",input)) 
        
        # x=str(st.session_state['chat-history'])
        # st.write("vasan")
        # st.write(x)
        # x=""
        for user,text in st.session_state['chat-history']:
            x+=(f"{user} : {text}")
            x+="\n"*2
        # st.write(x)
        
        response=respone_from_gemini(x)
        
        
        st.subheader("Your response is")
        with st.chat_message("ai"):
            st.markdown(response.text)
        st.session_state['chat-history'].append(("ai",response.text)) 
        
    reset=st.button('Reset The bot')
    if reset:
        x=" "
        st.session_state['chat-history'] =[]
    st.caption("📝⚠️ if you want to talk to another personality click 'reset the bot' button and go back to the main page and type the new celebeirty name !! ⚠️")
    
    st.write(" "*10)
    st.write("-"*50)
    st.subheader("Help us improve📝")
    st.write("Share your Valuable feedback: https://shorturl.at/itEM2")
    st.write("-"*50)
    st.caption("Made by Vasan R ❤️")

    # st.write(x)
    # st.write(st.session_state['chat-history'])
    # st.subheader('Chat History')

    # chat history
    # for role,text in st.session_state['chat-history']:
        
    #     if role=="user":
    #         st.write("-"*80)
    #         st.write(f"{role} : {text}")
    #         st.write("-"*80)
    #         # st.write(f"model :")
            
    #     else:
    #         st.write(f"{text}")

    # st.session_state['chat-history']
    
    # st.chat_input("What is up?")
    # st.chat_message("user")
        
    
# /////////////////////////////////

def main():
    page = st.experimental_get_query_params().get("page", ["main"])[0]

    if page == "main":
        main_page()
    elif page == "side":
        side_page()

if __name__ == "__main__":
    main()



