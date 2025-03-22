from google_auth_oauthlib.flow import InstalledAppFlow

# Charger les credentials depuis le fichier JSON
flow = InstalledAppFlow.from_client_secrets_file(
    "credentials.json",  # Assure-toi que ce fichier est bien dans ton dossier
    scopes=["https://www.googleapis.com/auth/gmail.send"]  # Permission pour envoyer des mails
)

# Lancer l'authentification
creds = flow.run_local_server(port=8000)

# Sauvegarder le token pour éviter de réauthentifier à chaque fois
with open("token.json", "w") as token:
    token.write(creds.to_json())

print("✅ Authentification réussie ! Token enregistré.")
