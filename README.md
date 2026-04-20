# 🛡️ Rapport d'Atelier : Stratégies PRA & PCA sur Kubernetes

**Auteur :** Jean-Gérard HOUNKANRIN  
**Promotion :** EPSI 2026  
**Encadrant :** Boris STOCKER  
**Date :** 20 Avril 2026  

---

## 📖 Présentation du projet
Cet atelier met en œuvre un **mini-PRA** (Plan de Reprise d'Activité) sur **Kubernetes** en déployant une **application Flask** avec une **base SQLite** stockée sur un **volume persistant (PVC pra-data)** et des **sauvegardes automatiques** réalisées chaque minute vers un second volume (**PVC pra-backup**) via un **CronJob**. 

---

## 🌐 État des Routes et Accès Application

| Route | Résultat Obtenu | Statut |
| :--- | :--- | :--- |
| <a href="https://psychic-funicular-4j9jqrxw547jc799v-8080.app.github.dev/" target="_blank">🏠 Accueil</a> | Affichage de `{"status":"Bonjour tout le monde !"}` | OK ✅ |
| <a href="https://psychic-funicular-4j9jqrxw547jc799v-8080.app.github.dev/health" target="_blank">🏥 /health</a> | Système opérationnel (health check OK) | OK ✅ |
| <a href="https://psychic-funicular-4j9jqrxw547jc799v-8080.app.github.dev/add?message=Message_Initial" target="_blank">➕ /add?message=...</a> | Enregistrement réussi (Message_Initial) | OK ✅ |
| <a href="https://psychic-funicular-4j9jqrxw547jc799v-8080.app.github.dev/count" target="_blank">🔢 /count</a> | Compteur incrémenté à 1 | OK ✅ |
| <a href="https://psychic-funicular-4j9jqrxw547jc799v-8080.app.github.dev/consultation" target="_blank">📋 /consultation</a> | Affichage du JSON avec l'ID 1 et le timestamp | OK ✅ |

---

## 🚀 Expertise Théorique (Séquence 5)

### Q1 : Quels sont les composants dont la perte entraîne une perte de données ?
La perte de données définitive ne survient que si l'on perd la **chaîne de stockage complète** :
* **Le PVC `pra-data`** : Contient la base active. Sa perte efface les données "live".
* **Le PVC `pra-backup`** : Contient les sauvegardes. Si les deux sont perdus, la restauration est impossible.
* **Note :** Le Pod Flask est **stateless**, sa perte n'impacte pas les données.

### Q2 : Pourquoi n'avons-nous pas perdu les données lors de la suppression de `pra-data` ?
Grâce à la **redondance asynchrone** :
1. Un **CronJob** copiait la base chaque minute vers `pra-backup`.
2. Un **Job de restauration** a permis de recharger ces données dans le nouveau volume de production.

### Q3 : Quels sont les RTO et RPO de cette solution ?
* **RPO (Recovery Point Objective)** : **1 Minute** (fréquence du backup).
* **RTO (Recovery Time Objective)** : **~2 à 5 Minutes** (intervention humaine).

### Q4 : Pourquoi cette solution n'est pas adaptée à une production réelle ?
* **SPOF (Point unique de défaillance)** : Tout est sur le même serveur physique.
* **Moteur SQLite** : Pas de gestion de haute disponibilité native.
* **Restauration Manuelle** : Trop lente pour des services critiques.

### Q5 : Proposez une architecture plus robuste
* **Backup Offsite** : Exportation vers **AWS S3 / Azure Blob**.
* **Base de Données Managée (PaaS)** : Amazon RDS Multi-AZ.
* **Observabilité** : Monitoring **Prometheus/Grafana** pour les alertes.

---

## 🛠️ Ateliers de Validation (Séquence 6)
* **Atelier 1 (Route /status)** : Implémentation réussie du JSON d'état des backups.
* **Atelier 2 (Restauration sélective)** : Procédure validée via le fichier `50-job-restore.yaml`.