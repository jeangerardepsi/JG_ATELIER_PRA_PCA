# 🛡️ Rapport d'Atelier : Stratégies PRA & PCA sur Kubernetes

**Auteur :** Jean-Gérard HOUNKANRIN  
**Promotion :** EPSI 2026  
**Encadrant :** Boris STOCKER  
**Date :** 20 Avril 2026  

---

## 📖 Présentation du projet
Cet atelier met en œuvre un **mini-PRA** (Plan de Reprise d'Activité) sur **Kubernetes**. Il simule la perte d'un volume de données et sa restauration via un système de sauvegarde automatisé par **CronJob**.

---

## 🌐 Accès à l'Application (Liens Directs)
*Cliquez sur les liens ci-dessous pour tester l'application (Port 8080 public) :*

* 🏠 **Accueil** : https://psychic-funicular-4j9jqrxw547jc799v-8080.app.github.dev/
* 🏥 **Santé** : https://psychic-funicular-4j9jqrxw547jc799v-8080.app.github.dev/health
* ➕ **Ajouter** : https://psychic-funicular-4j9jqrxw547jc799v-8080.app.github.dev/add?message=Test_EPSI
* 🔢 **Compteur** : https://psychic-funicular-4j9jqrxw547jc799v-8080.app.github.dev/count
* 📋 **Consultation** : https://psychic-funicular-4j9jqrxw547jc799v-8080.app.github.dev/consultation

---

## ✅ État de Validation des Services

| Service | Fonctionnalité | État |
| :--- | :--- | :--- |
| API Flask | Réponse JSON /status | Opérationnel ✅ |
| Base de données | SQLite Persistante | Opérationnel ✅ |
| Sauvegarde | CronJob (1 min) | Opérationnel ✅ |
| Restauration | Job Ansible/K8s | Testé et Validé ✅ |

---

## 🚀 Expertise Théorique (Séquence 5)

### Q1 : Quels sont les composants dont la perte entraîne une perte de données ?
La perte est définitive si l'on perd le **PVC pra-data** (données live) ET le **PVC pra-backup** (sauvegardes). Le Pod Flask est **stateless**, sa perte n'impacte pas les données.

### Q2 : Pourquoi n'avons-nous pas perdu les données lors de la suppression de `pra-data` ?
Grâce à la **redondance asynchrone** : le CronJob a sauvegardé la base sur un volume indépendant (`pra-backup`) avant la suppression.

### Q3 : Quels sont les RTO et RPO de cette solution ?
* **RPO** : 1 Minute.
* **RTO** : ~2 à 5 Minutes.

### Q4 : Pourquoi cette solution n'est pas adaptée à une production réelle ?
À cause du **SPOF** (Single Point of Failure) : les sauvegardes sont sur le même cluster. Il manque également un monitoring (alerting) et un stockage déporté.

### Q5 : Architecture cible plus robuste
Utilisation d'un stockage objet distant (**S3**) et d'une base de données managée (**PaaS**) pour garantir une haute disponibilité géographique.

---

## 🛠️ Ateliers de Validation (Séquence 6)
* **Atelier 1** : Route `/status` ajoutée (JSON).
* **Atelier 2** : Restauration granulaire validée.