# Programme de test pour le Premier TP
## Comment lancer les tests:

1 - Copier les dossiers contenant les projets des étudiants dans le dossier `projects`

2 - double click sur le fichier ``testerTP1.bat``

## Comment cela fonctionne:

- Le programme compile les classes Java de chaque étudiant
- copie les classes compilés vers le dossier `javaClasses`
    - Le dossier contient les classes compilés de test, affichage et notes
- Execute la classe principale de teste `TestTP1.main()` avec comme parametre le nom du dossier
    - le nom du dossier représente le nom de l'étudiant.
- enregistre le résultat dans un fichiers ``résultat.json`` (fichier temporaire)
- supprime les fichiers compilés et refait la chose pour un autre étudiant

- Crée et ouvre le fichier de résultat finale `résultat.json`
