# 🛡️ Rapport d'Atelier : Stratégies PRA & PCA sur Kubernetes

**Auteur :** Jean-Gérard  
**École :** EPSI  
**Enseignant :** [Nom de ton Professeur]  
**Date :** 20 Avril 2026  

---

## 📖 Présentation de l'Atelier
Cet atelier met en œuvre un **mini-PRA** (Plan de Reprise d'Activité) sur **Kubernetes** en déployant une **application Flask** avec une **base SQLite** stockée sur un **volume persistant (PVC pra-data)** et des **sauvegardes automatiques réalisées chaque minute vers un second volume (PVC pra-backup)** via un **CronJob**.

---

## 🌐 État des Routes et Tests Applicatifs

| Route | Résultat Obtenu | Statut |
| :--- | :--- | :--- |
| [Accueil (/)](https://psychic-funicular-4j9jqrxw547jc799v-8080.app.github.dev/) | Affichage de 'Bonjour tout le monde !' | OK ✅ |
| [/health](https://psychic-funicular-4j9jqrxw547jc799v-8080.app.github.dev/health) | Système opérationnel | OK ✅ |
| [/add?message=...](https://psychic-funicular-4j9jqrxw547jc799v-8080.app.github.dev/add?message=Message_Initial) | Enregistrement réussi | OK ✅ |
| [/count](https://psychic-funicular-4j9jqrxw547jc799v-8080.app.github.dev/count) | Compteur incrémenté | OK ✅ |
| [/consultation](https://psychic-funicular-4j9jqrxw547jc799v-8080.app.github.dev/consultation) | Affichage du JSON complet | OK ✅ |

---

## 🚀 Séquence 5 : Exercices de Validation

### 📂 Exercice 1 | Analyse des Risques
La perte de données ne survient que si l'on perd simultanément le **PVC pra-data** et le **PVC pra-backup**. Le Pod Flask est stateless.

### 🔄 Exercice 2 | Mécanisme de Résilience
Les données n'ont pas été perdues car un **CronJob** copiait la base chaque minute vers le volume de secours. Un **Job de restauration** a permis la reprise.

### ⏱️ Exercice 3 | Métriques (KPI)
* **RPO** : 1 Minute.
* **RTO** : ~2 à 5 Minutes.

### 🏗️ Exercice 4 & 5 | Limites et Évolutions
**Limites :** Stockage local (SPOF). **Architecture robuste :** Backups déportés (S3) et DB managée (RDS).

---

## 🛠️ Séquence 6 : Ateliers Pratiques
1. **Atelier 1** : Route /status ajoutée.
2. **Atelier 2** : Choix du point de restauration via job YAML.
