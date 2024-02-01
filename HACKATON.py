#!/usr/bin/env python
# coding: utf-8

# In[114]:

import streamlit as st
from googletrans import Translator, LANGUAGES
import pandas as pd
import requests
import json
from blagues_api import BlaguesAPI, BlagueType, CountJoke, Blague
import matplotlib.pyplot as plt
import seaborn as sns
from random import shuffle
import random
import plotly.graph_objects as go
import time
import graphviz

# In[115]:
# In[116]:
def translate_text(text):
    if pd.isna(text):
        return text
    try:
        return translator.translate(text, src='en', dest='fr').text
    except Exception as e:
        print(f"Erreur lors de la traduction: {e}")
        return text    
    
def chuck_norris():

    api_url = 'https://api.api-ninjas.com/v1/chucknorris'
    response = requests.get(api_url, headers={'X-Api-Key': 'Bb2CN6n47vHRlfERKHe7tg==qGpKlL6XVsTZhcQn'})
    if response.status_code == requests.codes.ok:
        chuck_fr = translate_text(response.text)
        st.write('Original :', response.text)
        st.write('Traduction :', chuck_fr)
    else:
        print("Error:", response.status_code, response.text)

    


def quizz_final():
    url = "https://api.openquizzdb.org/?key=7VG6AGBS25&choice=2&anec=1&wiki=1"
    re = requests.get(url)
    data_fr = json.loads(re.text)
    trivial2 = pd.json_normalize(data_fr['results'])
    question = trivial2['question'][0]
    st.markdown(f"<h5>{question}</h5>", unsafe_allow_html=True)
    
    for index, row in trivial2.iterrows():
        st.write('Choix de réponses possible:')
        value = random.choice(row['autres_choix'])
        st.write(f"- {value}")
        if value == row['autres_choix'][0]:
            value2 = row['autres_choix'][1]
            st.write(f"- {value2}")
        else : 
            value3 = row['autres_choix'][0]
            st.write(f"- {value3}")
    time.sleep(1)
    with st.spinner('La bonne réponse dans 10 secondes'):
            time.sleep(10)
    reponse = trivial2['reponse_correcte'][0]        
    st.write(f"réponse : {reponse}")
    st.write( 'Anecdote : ',trivial2['anecdote'][0])
    st.write('Vous voulez en savoir plus ?')
    lien_wiki = trivial2['wikipedia'][0]
    st.write(f" Notre lien wikipedia : {lien_wiki}")
    
  
            
translator = Translator()

def onglet0():
    st.markdown("<h1 style='text-align: center;'>Festive Fun Crackers</h1>", unsafe_allow_html=True)
    
    
    st.markdown("<h3 style='text-align: center;'>Application pour réchauffer les fêtes de fin d'année</h3>", unsafe_allow_html=True)
    
    st.subheader('Présentation')
    
    "🎄 Bienvenue dans l'appli la plus festive de toutes : 'Festive Fun Crackers' ! 🎅"
    " Vous cherchez à pimenter vos soirées en famille avec des rires garantis ? Vous voulez ajouter une touche d'humour à vos repas de Noël ? Ne cherchez pas plus loin, vous êtes au bon endroit !"
    " 🔔 Pourquoi cette appli est-elle aussi cool que le Père Noël ? 🔔 "
    " ✨ Parce qu'elle vous offre un assortiment infini de blagues rigolotes et de divertissements pour chaque occasion festive,du repas de réveillon à la distribution des cadeaux, on a une blague pour chaque moment de joie (ou de gêne) ! 🎁"    
    " 🤶 'Festive Fun Crackers', c'est quoi le truc en plus ? 🦌 "    
    " 🎉 Des blagues adaptées à toutes les oreilles, des plus jeunes aux plus âgées. On garantit des sourires sur tous les visages, même sur celui du Grincheux de la famille ! 🎅"    
    " 🌟 Nos blagues sont comme des cadeaux de Noël : elles vous feront sourire ! 🌟"
    
    
    
    image = "Pourquoi_.webp"
    st.image(image)
    
    
    st.subheader('Pour plus de fonctionnalités :')
    
    st.write("Festive Fun Crakers Prenium est un abonnement mensuel récurrent. Le montant (4,49 USD) vous sera automatiquement facturé via l'App store à la fin de la période d'essai gratuite de 7jours. L'Abonnement mensuel est automatiquement renouvelé sauf s'il est annulé au moins 24 heures avant la fin de la période en cours. Votre compte sera facturé pour le renouvellemnt dans les 24 heures précédant la fin de la période en cours. Toute partie non utilisée de la période d'essai gratuite sera perdue.Vous pouvez gé gérer votre abonnement surl'App store")
    lien_cond = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    st.write(f"Condition d'utilisation: {lien_cond}")




def onglet1():
    
    st.markdown("<h1 style='text-align: center;'>La carte des entrées</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Quiz de culture générale</h3>", unsafe_allow_html=True)
    url1 = "quiz-dans-style-bande-dessinee-pop-art_175838-505.avif"
    st.image(url1, width = 700)
    if st.button("Lancer le quizz"):
        quizz_final()
        
        
        





def onglet2():

    st.markdown("<h1 style='text-align: center;'>Plat de resistance</h1>", unsafe_allow_html=True)
    #url3 =
    chemin_fichier_json = "/Users/aloisbrault/Documents/wildcodeschool/HACKATON/blagues.json"
    with open(chemin_fichier_json, 'r') as fichier:
        donnees_json = json.load(fichier)


    df = pd.json_normalize(donnees_json[0])
    
    nb_blagues_par_genre = df['type'].value_counts()
    st.subheader('Blagues')
    categorie = [""] + list(df["type"].unique())
    st.write('! Attention la catégorie limit est réservé à un public averti 🔞')
    category_user = st.selectbox("Sélectionnez le genre de blagues",categorie)
    if category_user == "dev":
            df_cat = df[df['type']== 'dev']
            blague_au_hasard = df_cat.sample().iloc[0]
            st.write('Blague: ', blague_au_hasard['joke'])
            with st.spinner('...'):
                time.sleep(3)
            st.write('Réponse: ', blague_au_hasard['answer'])
    elif category_user == "beauf":
            df_cat = df[df['type']== 'beauf']
            blague_au_hasard = df_cat.sample().iloc[0]
            st.write('Blague: ', blague_au_hasard['joke'])
            with st.spinner('...'):
                time.sleep(3)
            st.write('Réponse: ', blague_au_hasard['answer'])
    elif category_user == "limit":
            df_cat = df[df['type']== 'limit']
            blague_au_hasard = df_cat.sample().iloc[0]
            st.write('Blague: ', blague_au_hasard['joke'])
            with st.spinner('...'):
                time.sleep(3)
            st.write('Réponse: ', blague_au_hasard['answer'])
    elif category_user == "global":
            df_cat = df[df['type']== 'global']
            blague_au_hasard = df_cat.sample().iloc[0]
            st.write('Blague: ', blague_au_hasard['joke'])
            with st.spinner('...'):
                time.sleep(3)
            st.write('Réponse: ', blague_au_hasard['answer'])
    elif category_user == "blondes":
            df_cat = df[df['type']== 'blondes']
            blague_au_hasard = df_cat.sample().iloc[0]
            st.write('Blague: ', blague_au_hasard['joke'])
            with st.spinner('...'):
                time.sleep(3)
            st.write('Réponse: ', blague_au_hasard['answer'])
 
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.subheader('Graphique')
    fig = go.Figure(data=[go.Histogram(x=df['type'], marker_color='#D00F0F')])
    fig.update_layout(
        title='Nombre de blagues par genre',
        xaxis_title='Genre',
        yaxis_title='Nombre de blagues',
        xaxis_categoryorder='total descending',
        bargap=0.1  # Espacement entre les barres
    )
    
    st.plotly_chart(fig)
    
    
    
def onglet3():
    
    st.markdown("<h1 style='text-align: center;'>Dessert gourmand</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Chuck Norris vous offre une petite gourmandise</h3>", unsafe_allow_html=True)
    url2 = 'https://youtu.be/fmflXUbfPn0?si=8q0uzJHHz4fgR7Xt'

   
    if st.button("Qui est Chuck Norris?"):
        chuck_norris()
        
    st.markdown("<h3 style='text-align: center;'>Vidéo</h3>", unsafe_allow_html=True)
       
    st.video(url2)

    
    
    
    
def onglet4():
    
    st.markdown("<h1 style='text-align: center;'>Et un petit digestif ?</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>Ici sera bientôt disponible LE 'BLIND TEST' tant attendu !!</h4>", unsafe_allow_html=True)
    
    url6 = "https://drive.google.com/uc?export=view&id=1NuahitKx56DvSHAp-oYCY7DZJKFtU6Nb"
    st.image(url6)
    
   

    
    
def main():
    
    url5 = "https://drive.google.com/uc?export=view&id=1uFSSTvQTEpU7XIxuvVDhfmnhu2ifsisI"
    st.sidebar.image(url5)
    st.sidebar.title("Navigation")

    onglet_selectionne = st.sidebar.selectbox("Etape du menu", ["Festive Fun Crackers", "La carte des entrées", "Plat de resistance", "Dessert gourmand", "Et un petit digestif ?"])

    if onglet_selectionne == "Festive Fun Crackers":
        onglet0()
    elif onglet_selectionne == "La carte des entrées":
        onglet1()
    elif onglet_selectionne == "Plat de resistance":
        onglet2()
    elif onglet_selectionne == "Dessert gourmand":
        onglet3()
    elif onglet_selectionne == "Et un petit digestif ?":
        onglet4()

if __name__ == "__main__":
    main()










    
    
    



