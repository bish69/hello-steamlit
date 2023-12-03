import streamlit as st

# Titre de l'application
st.title("Epydemie - Simulateur de contagion en temps réel")

# Description du projet
st.write(
    "Bienvenue sur Epydemie, un simulateur en temps réel de la contagion d'un virus "
    "par rapport aux populations. Ce projet vise à fournir une compréhension visuelle "
    "de la propagation des maladies infectieuses et de l'impact de différentes "
    "mesures préventives."
)

# Ajouter des images
image_path = "https://www.gircor.fr/wp-content/uploads/2022/07/corona-5174671_1920-2-1024x683.jpg"
image = st.image(image_path, caption="bla bla bla", use_column_width=True)


col1, col2 = st.columns(2)
# Boutons interactifs
if col1.button("En savoir plus sur Epydemie"):
    st.write("Epydemie est un projet innovant qui utilise des modèles de simulation pour "
             "prédire la propagation d'une maladie dans différentes populations. La plateforme "
             "permet aux utilisateurs de tester différents scénarios en ajustant des paramètres "
             "tels que le taux de transmission, la durée d'incubation, etc.")

if col2.button("Démarrer la simulation"):
    st.write("Cliquez sur le bouton pour lancer la simulation en temps réel. "
             "Explorez les résultats et visualisez l'impact des différentes mesures de prévention.")

# Pied de page
st.write(
    "Contactez-nous pour plus d'informations sur Epydemie. "
    "© 2023 Epydemie. Tous droits réservés."
)