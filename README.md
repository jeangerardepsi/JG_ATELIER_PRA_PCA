cat << 'EOF' > README.md
# 🛡️ Rapport d'Atelier : Stratégies PRA & PCA sur Kubernetes

**Auteur :** Jean-Gérard  
**École :** EPSI  
**Enseignant :** [Nom de ton Professeur]  
**Date :** 20 Avril 2026  

---

## 📖 Présentation de l'Atelier
Cet atelier met en œuvre un **mini-PRA** (Plan de Reprise d'Activité) sur **Kubernetes** en déployant une **application Flask** avec une **base SQLite** stockée sur un **volume persistant (PVC pra-data)** et des **sauvegardes automatiques réalisées chaque minute vers un second volume (PVC pra-backup)** via un **CronJob**.

L’objectif est de maîtriser les concepts de **PCA** (Continuité d'Activité via la résilience des Pods) et de **PRA** (Reprise après sinistre via la restauration de données).

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

## 🚀 Séquence 5 : Exercices de Validation

### 📂 Exercice 1 | Analyse des Risques
La perte de données ne survient que si l'on perd simultanément le **PVC pra-data** (données live) et le **PVC pra-backup** (sauvegardes). Le Pod Flask est "stateless" et n'entraîne aucune perte en cas de crash.

### 🔄 Exercice 2 | Mécanisme de Résilience
Nous n'avons pas perdu les données lors de la suppression de `pra-data` car un **CronJob** copiait la base de données chaque minute vers `pra-backup`. Nous avons utilisé un **Job de restauration** pour réinjecter ces données depuis le volume de secours.

### ⏱️ Exercice 3 | Métriques de Reprise (KPI)
* **RPO (Recovery Point Objective)** : 1 Minute (fréquence des backups).
* **RTO (Recovery Time Objective)** : ~2 à 5 Minutes (temps d'intervention manuelle).

### 🏗️ Exercice 4 & 5 | Limites et Architecture Cible
**Limites :** Stockage local (SPOF), restauration manuelle et absence d'alerting.  
**Architecture robuste :** Backups déportés sur un stockage objet (**S3**), utilisation d'une base de données managée (**RDS**) et monitoring avec **Prometheus/Grafana**.

---

## 🛠️ Séquence 6 : Ateliers Pratiques
1. **Atelier 1** : Route `/status` opérationnelle affichant les métriques de backup.
2. **Atelier 2** : Capacité de choisir un point de restauration en modifiant le fichier `50-job-restore.yaml`.

---

## 🚀 Publication
```bash
git add README.md
git commit -m "docs: Rapport complet fusionné avec tableau des routes pour EPSI"
git push origin main