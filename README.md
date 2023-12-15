# LoLDrafter
Un projet utilisant le Machine Learning et le Deep Learning pour prédire l'équipe gagnante d'un match de League of Legends avant le début de cette dernière, en Python (Scikit-Learn et Tensorflow).

Les modèles ne se basent que sur la liste des champions et leurs rôles pour effectuer les prédictions; ce sont de toute manière les seules informations dont disposent les joueurs avant le début des matchs, étant donné qu'il n'est pas possible de voir les pseudonymes des autres joueurs de la partie (et donc pas possible non plus de récupérer les stats des joueurs).

Les features utilisées par ces modèles sont donc assez pauvres et expliquent que nos modèles obtiennent des validation et test accuracies d'environ 60%. Il serait possible d'obtenir de meilleures performances en utilisant des features plus riches (performance des joueurs dans les parties précédentes, ...).

Les modèles obtenant les meilleures performances sont le Random Forest classifier et un RNN à base de deux couches de LSTM.
