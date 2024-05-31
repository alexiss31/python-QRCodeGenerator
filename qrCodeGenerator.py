import qrcode  # Importation du module qrcode pour créer des QR codes
import image   # Importation du module image pour manipuler les images (nécessaire si vous utilisez certaines fonctionnalités de qrcode)

# Création d'une instance de QRCode avec des paramètres spécifiques
qr = qrcode.QRCode(
    version=15,      # Version du QR code. Plus le numéro de version est élevé, plus le QR code peut contenir d'informations.
    box_size=10,     # Cela détermine la taille de l'image finale.
    border=5         # Largeur de la bordure blanche autour du QR code, en boîtes (pixels).
)

# Demande à l'utilisateur de saisir une URL ou un lien qui sera encodé dans le QR code
data = str(input("Veuillez entrer le lien qui sera généré via le QR Code : "))

# Ajout des données (lien) au QR code
qr.add_data(data)

# Génération du QR code. Le paramètre 'fit=True' ajuste automatiquement la taille du QR code pour s'adapter aux données fournies.
qr.make(fit=True)

# Création de l'image du QR code avec des paramètres de couleur personnalisés
# 'fill' détermine la couleur des pixels du QR code, ici en noir
# 'back_color' détermine la couleur de fond, ici en blanc
img = qr.make_image(fill="black", back_color="white") #Création de l'image, 'fill' correspond à la couleur des pixels, back_color à la couleur de fond

#Demande le nom du fichier à sauvegarder à l'utilisateur
filename = str(input("Veuillez entrer le nom du fichier à enregistrer : "))

# Sauvegarde de l'image du QR code dans un fichier PNG
img.save(filename + ".png")
