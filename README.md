# Keylogger - Documentation

## Prérequis

Assurez-vous d'installer les bibliothèques Python suivantes avant d'utiliser ce programme :

- **DateTime** : `5.5`
- **psutil** : `6.0.0`
- **pynput** : `1.7.7`

Pour installer les dépendances, vous pouvez utiliser `pip` :

```bash
pip install DateTime==5.5 psutil==6.0.0 pynput==1.7.7
```

## Utilisation

### 1. Lancer le programme

Pour démarrer le keylogger, exécutez le fichier batch suivant :

```bash
keyloggerOn.bat
```

Le programme enregistrera toutes les frappes de touches dans des fichiers texte dans le dossier **`keyloggerLog/`**.

### 2. Arrêter le programme

Pour arrêter le keylogger, exécutez le fichier batch suivant :

```bash
keyloggerOff.bat
```

Ce script arrêtera le processus en cours.

### 3. Nettoyer les logs

Si vous souhaitez supprimer les fichiers de logs, exécutez le fichier batch suivant :

```bash
cleanKeyloggerLog.bat
```

Cela supprimera tous les fichiers enregistrés dans le dossier **`keyloggerLog/`**.

---

### Notes

- **Processus de fermeture** : Le fichier **`keyloggerOff.bat`** doit être utilisé pour fermer le programme proprement en s'assurant que tous les processus associés sont terminés.

---

