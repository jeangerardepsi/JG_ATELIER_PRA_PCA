# 🛡️ Rapport d'Atelier : Stratégies PRA & PCA sur Kubernetes

**Auteur :** Jean-Gérard HOUNKANRIN  
**Promotion :** EPSI 2026  
**Encadrant :** Boris STOCKER  
**Environnement :** GitHub Codespaces (Ubuntu)  

---

## 📖 Présentation du projet
Cet atelier met en œuvre un **mini-PRA** (Plan de Reprise d'Activité) sur **Kubernetes** en déployant une **application Flask** avec une **base SQLite** stockée sur un **volume persistant (PVC pra-data)** et des **sauvegardes automatiques** réalisées chaque minute vers un second volume (**PVC pra-backup**) via un **CronJob**. 

L'image applicative est construite avec **Packer** et le déploiement est orchestré avec **Ansible**. Cet atelier illustre la différence fondamentale entre la **Haute Disponibilité** (PCA) et la **Reprise après sinistre** (PRA).

---

## 🌐 État des Routes et Tests Applicatifs

| Route | Résultat Obtenu | Statut |
| :--- | :--- | :--- |
| [Accueil (/)](https://psychic-funicular-4j9jqrxw547jc799v-8080.app.github.dev/) | Affichage de `{"status":"Bonjour tout le monde !"}` | OK ✅ |
| [/health](https://psychic-funicular-4j9jqrxw547jc799v-8080.app.github.dev/health) | Système opérationnel (health check OK) | OK ✅ |
| [/add?message=...](https://psychic-funicular-4j9jqrxw547jc799v-8080.app.github.dev/add?message=Message_Initial) | Enregistrement réussi (Message_Initial) | OK ✅ |
| [/count](https://psychic-funicular-4j9jqrxw547jc799v-8080.app.github.dev/count) | Compteur incrémenté à 1 | OK ✅ |
| [/consultation](https://psychic-funicular-4j9jqrxw547jc799v-8080.app.github.dev/consultation) | Affichage du JSON avec l'ID 1 et le timestamp | OK ✅ |

---

## 🚀 Expertise Théorique (Séquence 5)

### Q1 : Quels sont les composants dont la perte entraîne une perte de données ?
La perte de données définitive ne survient que si l'on perd la **chaîne de stockage complète** :
* **Le PVC `pra-data`** : Contient la base SQLite active. Sa perte supprime les données en cours.
* **Le PVC `pra-backup`** : Contient l'historique. Si les deux sont perdus, aucune restauration n'est possible.
* *Note :* Le Pod Flask est **stateless**, sa perte n'impacte pas les données.

### Q2 : Pourquoi n'avons-nous pas perdu les données lors de la suppression de `pra-data` ?
Grâce à la stratégie de **redondance asynchrone** :
1. Un **CronJob** copiait la base chaque minute vers le volume de secours (`pra-backup`).
2. Un **Job de restauration** a permis de copier le dernier backup valide vers le nouveau volume de production.

### Q3 : Quels sont les RTO et RPO de cette solution ?
* **RPO (Recovery Point Objective)** : **1 Minute** (perte de données maximale définie par la fréquence du CronJob).
* **RTO (Recovery Time Objective)** : **~2 à 5 Minutes** (temps d'intervention pour lancer le script de restauration).

### Q4 : Pourquoi cette solution n'est pas adaptée à une production réelle ?
* **SPOF (Point de défaillance unique)** : Les backups sont sur le même cluster/serveur physique.
* **Moteur SQLite** : Pas conçu pour la haute disponibilité ou les accès concurrents massifs.
* **Restauration Manuelle** : Nécessite une action humaine, ce qui ralentit la reprise.

### Q5 : Proposez une architecture plus robuste
1. **Backup Offsite** : Exporter les données vers un stockage cloud (**AWS S3 / Azure Blob**).
2. **Base de Données Managée (PaaS)** : Utiliser **Amazon RDS** ou un cluster PostgreSQL Multi-AZ.
3. **Observabilité** : Monitoring avec **Prometheus/Grafana** pour alerter en cas d'échec de sauvegarde.

---

## 🛠️ Ateliers de Validation
* **Atelier 1 (Route /status)** : Implémentation réussie affichant l'état des backups.
* **Atelier 2 (Restauration sélective)** : Procédure documentée via modification du fichier `50-job-restore.yaml`.