import streamlit as st

st.title(" A Reflection of Myself 👦")



st.title("The Portait of Myself")


image_paths = ["./my_pict/myself2.jpg", "./my_pict/myself3.jpg", "./my_pict/myself.jpg"]


cols = st.columns(len(image_paths))

for col, image_path in zip(cols, image_paths):
    col.image(image_path)


st.header(" ANGEL MAE LACIDA LAMIS")

st.markdown("""
##### 👨‍👩‍👧‍👦Family Members👨‍👩‍👧‍👦 

* 👩‍👦 Mother's Name: Ruby L. Lamis 
* 👨‍👧‍👧 Father's Name: Rafael A Lamis 
* 👭🏻 Sister's Name: Rufa L. Lamis and Cristine L. Lamis        

### 🔎 Overview
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #ff6347;'>Personal Information 🌟</h1>", unsafe_allow_html=True)

st.write("👩‍💻 Name: Angel Mae Lamis")
st.write("✨ Age:  21 years old")
st.write("🎓 Education: Currently studying at CARLOS HILADO MEMORIAL STATE UNIVERSITY")
st.write("📘 Year: 3rd year Bachelor of Science in Information Systems Student")
st.write("📍  Location: So. Dapdap Brgy Lantad Silay City")

with st.expander("Get to Know Me More🤔"):
    st.markdown("""
    
   Hey there! I'm someone who finds joy in simple pleasures. 
   I'm absolutely crazy about dogs - their loyalty and boundless energy always bring a smile to my face. 
   Music is my daily companion; whether it's upbeat tunes or soulful melodies, it's the soundtrack to my life.
   And when it comes to the finer things, I adore savoring a great cup of coffee and delicious food, especially when shared with friends.
   But above all, my heart belongs to my family. They're my rock, my cheerleaders, and my greatest source of happiness. 
   
     """, unsafe_allow_html=True)


st.header("My Treasured Quotes from Different Writers 📚✨")
st.write("1. 🙏 *\"Trust in the Lord with all your heart and lean not on your own understanding; in all your ways submit to him, and he will make your paths straight.\"* - Proverbs 3:5-6")
st.write("2. 🦅 *\"But those who hope in the Lord will renew their strength. They will soar on wings like eagles; they will run and not grow weary, they will walk and not be faint.\"* - Isaiah 40:31")
st.write("3. 🌟 *\"The only person you are destined to become is the person you decide to be.\"* - Ralph Waldo Emerson")


import streamlit as st


images = [
    {"path": "./my_pict/fr2.JPG", "caption":"I cherish my classmates deeply for the joy and comfort they bring into my life. Their laughter and encouragement uplift my spirits in ways that words can't express. Celebrating our successes together and supporting each other through challenges creates a bond that fills me with happiness. Their friendship and diverse viewpoints enrich my journey of learning, making every moment shared with them meaningful and unforgettable."},
    {"path": "./my_pict/fr3.JPG", "caption": "Gathering for study sessions, chatting during breaks, or simply hanging out creates a sense of camaraderie that makes us feel connected and supported. Sharing memories of our time together strengthens our bond, reminding us that we're part of a community where everyone's experiences and contributions matter. In times of challenge, their presence and understanding make me feel reassured and not alone."},
    {"path": "./my_pict/fr1.jpg", "caption": "Having close friends is a blessing that makes life better in many ways. They give unwavering support, encouragement, and understanding through all the ups and downs. Their belief in me motivates me to do my best, and their friendship turns everyday moments into cherished memories. Together, we have adventures that bring us closer and create lifelong connections. I am really thankful for their presence in my life because they bring happiness, comfort, and a feeling of belonging that is priceless."}

]


st.title("🖼️Gallery")


for image in images:
    st.image(image["path"], caption=image["caption"])



st.markdown(
    """
    <style>
    .stApp {
        background-color: white;
        padding: 2em;
    }
    h1, h2 {
        color: black;
    }
    .stText {
        font-size: 1.5em;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Footer or additional sections (optional)
st.write("### ✿ ❀ ❁  Thank you for visiting my profile! ❃ ❋ ❊ ")
