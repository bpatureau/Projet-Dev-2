# Format JSON des Aventures

Ce document explique comment créer vos propres aventures au format JSON.

## Structure générale

```json
{
  "nom": "Nom de l'aventure",
  "description": "Description courte de l'aventure",
  "or_depart": 0,
  "node_depart": "id_du_premier_node",
  "pnj": [...],
  "nodes": [...]
}
```

## Champs principaux

### nom (string, requis)
Le nom de l'aventure qui sera affiché dans le menu.

### description (string, requis)
Une courte description de l'aventure pour aider le joueur à choisir.

### or_depart (number, optionnel, défaut: 0)
La quantité d'or que le héros possède au début de l'aventure.

**Exemples:**
- `"or_depart": 0` - Pas d'or au départ (aventures simples)
- `"or_depart": 50` - 50 pièces d'or (pour aventures avec économie)
- `"or_depart": 100` - 100 pièces d'or (aventures riches)

### node_depart (string, requis)
L'ID du node par lequel commence l'aventure.

### pnj (array, optionnel)
Liste des PNJ (Personnages Non-Joueurs) présents dans l'aventure.

Exemple:
```json
"pnj": [
  {
    "nom": "Nom du PNJ",
    "affinite_initiale": 50
  }
]
```

L'affinité va de 0 (aucune affinité) à 100 (affinité maximale).

### nodes (array, requis)
Liste de tous les nodes (étapes) de l'aventure.

## Structure d'un Node

```json
{
  "id": "identifiant_unique",
  "description": "Description de la situation",
  "propositions": [...]
}
```

### id (string, requis)
Identifiant unique du node. Utilisé pour la navigation entre nodes.

### description (string, requis)
Le texte narratif décrivant la situation actuelle.

### propositions (array, requis)
Liste des choix disponibles pour le joueur dans ce node.

## Structure d'une Proposition

```json
{
  "texte": "Texte du choix affiché au joueur",
  "consequence": "Texte décrivant ce qui se passe après ce choix",
  "suivant": "id_du_prochain_node",
  "defaite": false,
  "prerequis": null
}
```

### texte (string, requis)
Le texte du choix qui sera affiché au joueur.

### consequence (string, requis)
Le texte décrivant ce qui se passe lorsque le joueur fait ce choix.

### suivant (string ou null, optionnel)
L'ID du node suivant. Si `null`, c'est une fin (défaite ou victoire selon `defaite`).
Utilisez `"victoire"` pour déclencher un écran de victoire.

### defaite (boolean, optionnel, défaut: false)
Si `true`, ce choix mène à une défaite (Game Over).

### prerequis (object ou null, optionnel)
Conditions requises pour que ce choix soit disponible.

## Types de Prérequis

### Prérequis sur un objet
Le joueur doit posséder un objet spécifique:
```json
"prerequis": {
  "objet": "nom_de_lobjet"
}
```

### Prérequis sur une caractéristique
Le joueur doit avoir une caractéristique minimale:
```json
"prerequis": {
  "caracteristique": "force",
  "valeur_min": 12
}
```

Caractéristiques disponibles: `force`, `intelligence`, `charisme`

### Prérequis sur une affinité PNJ
Le joueur doit avoir une affinité minimale avec un PNJ:
```json
"prerequis": {
  "pnj": "Nom du PNJ",
  "affinite_min": 50
}
```

### Prérequis sur l'or
Le joueur doit avoir une quantité minimale d'or:
```json
"prerequis": {
  "or_min": 100
}
```

### Pas de prérequis
```json
"prerequis": null
```

## Exemple Complet d'Aventure Simple

```json
{
  "nom": "La Caverne Sombre",
  "description": "Explorez une caverne mystérieuse",
  "or_depart": 0,
  "node_depart": "entree",
  "pnj": [],
  "nodes": [
    {
      "id": "entree",
      "description": "Vous êtes à l'entrée d'une caverne sombre. Vous entendez des bruits étranges.",
      "propositions": [
        {
          "texte": "Entrer sans préparation",
          "consequence": "Une créature vous attaque dans l'obscurité! GAME OVER",
          "suivant": null,
          "defaite": true
        },
        {
          "texte": "Allumer une torche et entrer prudemment",
          "consequence": "La lumière révèle un passage sûr. Vous progressez dans la caverne.",
          "suivant": "tresor"
        }
      ]
    },
    {
      "id": "tresor",
      "description": "Vous découvrez un coffre au trésor!",
      "propositions": [
        {
          "texte": "Ouvrir le coffre",
          "consequence": "Le coffre contient 1000 pièces d'or! Vous êtes riche!",
          "suivant": "victoire"
        }
      ]
    },
    {
      "id": "victoire",
      "description": "Félicitations! Vous avez trouvé le trésor!\n\n*** VICTOIRE ***",
      "propositions": []
    }
  ]
}
```

## Conseils pour créer une bonne aventure

1. **Commencez simple**: 3-5 nodes suffisent pour une première aventure
2. **Variez les chemins**: Offrez plusieurs façons d'atteindre la victoire
3. **Équilibrez difficulté**: Mettez quelques défaites possibles mais pas trop
4. **Utilisez les prérequis**: Ils rendent l'aventure plus intéressante
5. **Testez**: Jouez votre aventure pour vérifier qu'elle fonctionne bien
6. **Soignez la narration**: Des descriptions immersives rendent le jeu plus captivant

## Placement des fichiers

Placez vos fichiers JSON dans le dossier `aventures/` à la racine du jeu.
Le nom du fichier peut être différent du nom de l'aventure (ex: `mon_aventure.json`).