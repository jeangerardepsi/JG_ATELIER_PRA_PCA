# 🛡️ Rapport d'Atelier : Stratégies PRA & PCA sur Kubernetes

**Auteur :** Jean-Gérard  
**École :** EPSI  
**Enseignant :** [Nom de ton Professeur]  
**Date :** 20 Avril 2026  

---

## 📖 Présentation de l'Atelier
Cet atelier met en œuvre un **mini-PRA** (Plan de Reprise d'Activité) sur Kubernetes avec une application Flask et une base SQLite.

---

## 🌐 Accès et Routes de l'Application
* 🏠 [**Accueil**](https://psychic-funicular-4j9jqrxw547jc799v-8080.app.github.dev/)
* 📋 [**Consultation**](https://psychic-funicular-4j9jqrxw547jc799v-8080.app.github.dev/consultation)
* ➕ [**Ajouter un message**](https://psychic-funicular-4j9jqrxw547jc799v-8080.app.github.dev/add?message=test)
* 🔢 [**Compteur**](https://psychic-funicular-4j9jqrxw547jc799v-8080.app.github.dev/count)

---

## 🚀 Séquence 5 : Exercices de Validation

### 📂 Exercice 1 | Perte de données
La perte de données survient si l'on perd le **PVC pra-data** et le **PVC pra-backup**. Le Pod lui-même est stateless.

### 🔄 Exercice 2 | Mécanisme de Résilience
Nous n'avons pas perdu les données grâce au **CronJob** qui réplique la base chaque minute vers un volume de secours indépendant.

### ⏱️ Exercice 3 | Métriques (KPI)
* **RPO** : 1 Minute.
* **RTO** : ~2 à 5 Minutes.

### 🏗️ Exercice 4 & 5 | Évolutions
**Limites :** Stockage local (SPOF).  
**Solution cible :** Backup déporté (S3) et base de données managée.

---

## 🛠️ Séquence 6 : Ateliers Pratiques
1. **Atelier 1** : Route `/status` opérationnelle.
2. **Atelier 2** : Restauration sélective via modification du fichier `50-job-restore.yaml`.