# Guide d'Utilisation - Jeu d'Aventure Textuel

## 🎮 Comment jouer

### Lancement du jeu
```bash
python aventure_textuelle.py
```

### Menu principal
1. **Nouvelle Partie** : Choisir une aventure et commencer à jouer
2. **Quitter** : Fermer le jeu

### Choix d'aventure
Le jeu vous présentera toutes les aventures disponibles dans le dossier `aventures/`.
Choisissez celle qui vous intéresse en entrant son numéro.

### Pendant le jeu
- **Chiffres (1-9)** : Faire un choix parmi les propositions affichées
- **I** : Afficher l'inventaire (or et objets)
- **H** : Afficher l'historique des nodes explorés
- **Q** : Quitter l'aventure en cours

## 📁 Structure des fichiers

```
aventure_textuelle.py          # Le jeu principal
aventures/                     # Dossier contenant les aventures
├── README.md                  # Documentation du format JSON
├── TEMPLATE.json              # Template pour créer vos aventures
├── ascension_heros.json       # Aventure 1: L'Ascension du Héros
├── tresor_maudit.json         # Aventure 2: Le Trésor Maudit
└── foret_enchantee.json       # Aventure 3: La Forêt Enchantée
```

## ✨ Caractéristiques du jeu

### Le Héros
Chaque héros possède :
- **Nom** : Choisi par le joueur
- **Caractéristiques** : Force (10), Intelligence (10), Charisme (10)
- **Inventaire** : Or et objets collectés

### Système de prérequis
Certains choix peuvent être verrouillés et nécessiter :
- Un **objet spécifique** dans l'inventaire
- Une **caractéristique minimale** (ex: Intelligence ≥ 8)
- Une **affinité minimale** avec un PNJ
- Une **quantité d'or minimale**

Les choix verrouillés ne sont pas affichés au joueur.

### Système d'affinités
Vous pouvez développer des relations avec les PNJ (0-100).
Une affinité élevée peut débloquer des choix spéciaux.

## 🎯 Les 3 aventures incluses

### 1. L'Ascension du Héros
**Difficulté** : Facile
**Durée** : Courte (3 nodes)
**Thème** : Fantasy/Dragon

Affrontez un dragon au sommet d'une montagne. Utilisez la sagesse plutôt que la force brute pour triompher.

### 2. Le Trésor Maudit
**Difficulté** : Moyenne
**Durée** : Courte (3 nodes)
**Thème** : Temple/Énigme

Explorez un temple ancien gardé par un mystérieux gardien. Votre intelligence sera mise à l'épreuve.

**Note** : Un choix nécessite Intelligence ≥ 8

### 3. La Forêt Enchantée
**Difficulté** : Moyenne-Difficile
**Durée** : Moyenne (4 nodes)
**Thème** : Magie/Sauvetage

Sauvez une princesse des griffes d'une sorcière. Faites-vous des alliés et utilisez la diplomatie.

**Note** : Plusieurs chemins possibles avec prérequis variés (charisme, affinités PNJ)

## 🛠️ Créer vos propres aventures

### Étape 1 : Copier le template
```bash
cp aventures/TEMPLATE.json aventures/mon_aventure.json
```

### Étape 2 : Éditer avec votre éditeur favori
Ouvrez `mon_aventure.json` et modifiez :
- Le nom et la description
- Les nodes et leur contenu
- Les choix et leurs conséquences

### Étape 3 : Tester
Lancez le jeu et sélectionnez votre aventure pour la tester.

### Conseils de création
1. **Planifiez d'abord** : Dessinez votre arbre de décision sur papier
2. **Commencez petit** : 3-5 nodes sont parfaits pour débuter
3. **Testez régulièrement** : Vérifiez que tous les chemins fonctionnent
4. **Variez les fins** : Proposez plusieurs chemins vers la victoire
5. **Utilisez les prérequis** : Ils ajoutent de la profondeur

Consultez `aventures/README.md` pour la documentation complète du format JSON.

## 🏗️ Architecture du code

### Classes principales
- **Inventaire** : Gère l'or et les objets du héros
- **Hero** : Représente le héros avec ses caractéristiques
- **ListeDeChoix** : Un node de l'histoire avec ses choix
- **Aventure** : Gère une partie complète avec historique

### Séparation interface/logique
L'interface CLI (`InterfaceCLI`) est totalement séparée de la logique métier.
Cela facilite l'ajout d'une interface graphique future (Tkinter, PyQt, etc.)

### Extensibilité
- Ajoutez facilement de nouvelles aventures (fichiers JSON)
- Les classes sont modulaires et réutilisables
- Le système de prérequis est extensible

## 🔧 Personnalisation avancée

### Modifier les caractéristiques de base
Dans `Hero.__init__()`, changez les valeurs initiales :
```python
self.caracteristiques: Dict[str, int] = {
    "force": 12,        # Au lieu de 10
    "intelligence": 8,  # Au lieu de 10
    "charisme": 15      # Au lieu de 10
}
```

### Ajouter de nouvelles caractéristiques
1. Modifiez `Hero.__init__()` pour ajouter la caractéristique
2. Utilisez-la dans vos prérequis JSON :
```json
"prerequis": {
  "caracteristique": "nouvelle_stat",
  "valeur_min": 10
}
```

### Personnaliser l'affichage
Toutes les méthodes d'affichage retournent des strings.
Modifiez-les dans les classes pour changer l'apparence du jeu.

## 🐛 Résolution de problèmes

### "Aucune aventure disponible"
- Vérifiez que le dossier `aventures/` existe
- Vérifiez qu'il contient des fichiers `.json`
- Vérifiez que les fichiers JSON sont valides

### "Erreur de format JSON"
- Utilisez un validateur JSON en ligne
- Vérifiez les virgules, guillemets, et accolades
- Consultez le TEMPLATE.json pour la structure correcte

### Un choix avec prérequis ne s'affiche pas
- Vérifiez que le héros remplit les conditions
- Testez en modifiant temporairement les caractéristiques de base
- Vérifiez l'orthographe des noms de caractéristiques/objets/PNJ

### Le jeu se bloque après un choix
- Vérifiez que le node `"suivant"` existe dans votre fichier JSON
- Pour une fin, utilisez `"suivant": "victoire"` ou `"suivant": null` avec `"defaite": true`

## 📝 Format JSON - Résumé rapide

```json
{
  "nom": "Titre",
  "description": "Description",
  "node_depart": "id_debut",
  "pnj": [{"nom": "NPC", "affinite_initiale": 50}],
  "nodes": [
    {
      "id": "unique_id",
      "description": "Texte narratif",
      "propositions": [
        {
          "texte": "Option",
          "consequence": "Résultat",
          "suivant": "next_id",
          "defaite": false,
          "prerequis": null
        }
      ]
    }
  ]
}
```

## 🎓 Exemples de prérequis

```json
// Objet requis
"prerequis": {"objet": "cle_magique"}

// Caractéristique minimale
"prerequis": {"caracteristique": "force", "valeur_min": 15}

// Affinité PNJ minimale
"prerequis": {"pnj": "Elfe", "affinite_min": 60}

// Or minimum
"prerequis": {"or_min": 500}

// Pas de prérequis
"prerequis": null
```

## 📚 Ressources

- `aventures/README.md` : Documentation complète du format JSON
- `aventures/TEMPLATE.json` : Template vide pour créer une aventure
- Les 3 aventures incluses : Exemples de complexité croissante

## 🚀 Prochaines améliorations possibles

- Interface graphique (Tkinter/PyQt)
- Système de sauvegarde/chargement
- Effets sonores et musique
- Images pour les nodes
- Combat avec système de dés
- Inventaire graphique
- Éditeur d'aventures intégré

Amusez-vous bien à créer vos propres aventures ! 🎮