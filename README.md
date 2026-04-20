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
* 🏠 [**Accueil**](https://psychic-funicular-4j9jqrxw547jc799v-8080.app.github.dev/) : *"Bonjour tout le monde !"*.
* 🏥 [**Health Check**](https://psychic-funicular-4j9jqrxw547jc799v-8080.app.github.dev/health) : État de santé.
* ➕ [**Ajouter un message**](https://psychic-funicular-4j9jqrxw547jc799v-8080.app.github.dev/add?message=test).
* 🔢 [**Compteur**](https://psychic-funicular-4j9jqrxw547jc799v-8080.app.github.dev/count).
* 📋 [**Consultation**](https://psychic-funicular-4j9jqrxw547jc799v-8080.app.github.dev/consultation).

---

## 🚀 Séquence 5 : Exercices de Validation

### 📂 Exercice 1 | Perte de données
La perte de données survient si l'on perd le **PVC pra-data** et le **PVC pra-backup**.

### 🔄 Exercice 2 | Pourquoi pas de perte ?
Les données sont répliquées chaque minute par un **CronJob** vers un volume de secours.

### ⏱️ Exercice 3 | KPI
* **RPO** : 1 Minute.
* **RTO** : ~2 à 5 Minutes.

### 🏗️ Exercice 4 & 5 | Évolutions
**Limites :** Stockage local. **Solution :** Cloud S3, DB managée et Monitoring.

---

## 🛠️ Séquence 6 : Ateliers Pratiques
1. **Atelier 1** : Route /status ajoutée.
2. **Atelier 2** : Restauration sélective via modification du job YAML.

