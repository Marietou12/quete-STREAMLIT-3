import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Nos données utilisateurs doivent respecter ce format

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)
authenticator.login()


# Définition des fonctions pour les différentes pages
def accueil():
    """Page d'accueil."""
    st.title("Bienvenue sur ma page")
    st.image('giphy.gif', caption="Bienvenue 🎉")

def photos():
    """Page pour afficher des photos."""
    st.title("Bienvenue sur mon album photo")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("a photo")
        st.image("charge1.jpg")

    with col2:
        st.header("it's loading")
        st.image("charge1.jpg")

    with col3:
        st.header("HAHA NOPE")
        st.image("giphy2.gif", caption=" j'ai pas de photos 😜")
        
    
if st.session_state["authentication_status"]:
    # Si l'utilisateur est authentifié
    with st.sidebar:
        authenticator.logout("Déconnexion", "sidebar")  # Bouton de déconnexion
        st.markdown("Bienvenue root")       # Message de bienvenue

        # Menu de navigation
        selection = option_menu(
            menu_title="Menu", 
            options=["Accueil", "Photos"], 
            icons=["house", "camera"], 
            menu_icon="menu-down",
            default_index=0,
        )
    
    # Affichage de la page en fonction de la sélection
    if selection == "Accueil":
        accueil()
    elif selection == "Photos":
        photos()

elif st.session_state["authentication_status"] is False:
    # Si l'authentification a échoué
    st.error("Le nom d'utilisateur ou le mot de passe est incorrect.")

elif st.session_state["authentication_status"] is None:
    # Si les champs sont vides
    st.warning("Veuillez saisir votre nom d'utilisateur et votre mot de passe.")
