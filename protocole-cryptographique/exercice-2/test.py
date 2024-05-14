import hashlib

def generate_file_hash(file_path, hash_algorithm="sha256"):
    """
    Générer une empreinte hash pour un fichier donné.

    :param file_path: Chemin du fichier.
    :param hash_algorithm: Algorithme de hachage à utiliser (par défaut: SHA-256).
    :return: L'empreinte hash du fichier.
    """
    # Créer un objet de hachage avec l'algorithme spécifié
    hasher = hashlib.new(hash_algorithm)

    # Ouvrir le fichier en mode binaire pour la lecture
    with open(file_path, "rb") as file:
        # Lire le fichier par morceaux et mettre à jour l'empreinte hash
        chunk_size = 8192  # Taille du morceau en octets
        while chunk := file.read(chunk_size):
            hasher.update(chunk)

    # Retourner la représentation hexadécimale de l'empreinte hash
    return hasher.hexdigest()

def save_hash_to_file(hash_result, output_file_path):
    """
    Sauvegarder l'empreinte hash dans un fichier.

    :param hash_result: L'empreinte hash à sauvegarder.
    :param output_file_path: Chemin du fichier de sortie.
    """
    with open(output_file_path, "w") as output_file:
        output_file.write(hash_result)

if __name__ == "__main__":
    # Chemin du fichier à hasher
    file_to_hash = "protocole-cryptographique/exercice-2/test.txt"

    # Algorithme de hachage à utiliser
    hash_algorithm = "sha256"

    # Générer l'empreinte hash du fichier
    hash_result = generate_file_hash(file_to_hash, hash_algorithm)

    # Chemin du fichier de sortie pour sauvegarder l'empreinte hash
    output_file_path = "protocole-cryptographique/exercice-2/data.txt"

    # Sauvegarder l'empreinte hash dans un fichier
    save_hash_to_file(hash_result, output_file_path)

    print(f"L'empreinte hash du fichier a été sauvegardée dans {output_file_path}.")
