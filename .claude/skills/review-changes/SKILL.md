---
name: review-changes
description: Review der aktuellen uncommitted Git-Änderungen (git status + git diff HEAD) - fasst zusammen, nennt Risiken/Bugs, fehlende Tests, sachfremde Änderungen und Commit-Bereitschaft. Berücksichtigt auch untracked Dateien. Rein lesend, keine Änderungen, kein Commit, kein Push.
---

# Review Changes

Dieser Skill überprüft die aktuellen uncommitted Änderungen im Arbeitsverzeichnis.

## Aktueller Status

!`git status --short`

## Aktueller Diff

!`git diff HEAD`

## Aufgabe

Werte Status und Diff **gemeinsam** aus:

- `git status --short` zeigt den vollständigen Überblick, inklusive **untracked Dateien** (Markierung `??`), die im Diff nicht auftauchen.
- `git diff HEAD` zeigt die eigentlichen inhaltlichen Änderungen an bereits getrackten Dateien.

Liefere darauf basierend ein kurzes, klar strukturiertes Review mit folgenden Abschnitten:

1. **Zusammenfassung** – Was wurde geändert, in wenigen Sätzen (inkl. neuer untracked Dateien laut Status).
2. **Mögliche Bugs / Risiken** – Logikfehler, Edge Cases, unklares Verhalten, riskante Änderungen.
3. **Tests** – Fehlende oder anzupassende Tests für die geänderten Codeteile.
4. **Sachfremde Änderungen** – Änderungen oder neue Dateien (auch untracked), die nichts mit dem eigentlichen Zweck der Änderung zu tun scheinen, oder gegen Projektregeln (z. B. CLAUDE.md) verstoßen.
5. **Commit-Bereitschaft** – Kurze Einschätzung, ob die Änderungen so committet werden könnten oder was vorher noch zu tun ist.

Wichtige Regeln für die Bewertung untracked Dateien:

- Eine untracked Datei blockiert die Commit-Bereitschaft **nicht automatisch**, solange sie nicht Teil des geplanten Commits ist. Untracked heißt: Git würde sie ohnehin nicht mit committen, es sei denn, sie wird explizit hinzugefügt (`git add`).
- Wenn eine Projektregel (z. B. in CLAUDE.md) lediglich besagt, dass eine bestimmte Datei **nicht hinzugefügt oder committet** werden soll, ist das kein Hinweis darauf, dass die lokale Datei gelöscht werden muss. Schlage in diesem Fall **nicht** vor, die Datei zu löschen.
- Empfehle stattdessen, eine solche Datei einfach untracked und außerhalb des Commits zu lassen (z. B. nicht per `git add` hinzufügen, ggf. in `.gitignore` aufnehmen, falls sinnvoll).
- Weise nur dann auf ein tatsächliches Risiko hin, wenn konkrete Anzeichen bestehen, dass die Datei versehentlich mitcommittet werden könnte (z. B. durch `git add .` oder `git add -A`).

Falls sowohl Status als auch Diff leer sind, weise darauf hin, dass keine uncommitted Änderungen vorhanden sind, und beende das Review an dieser Stelle.

## Einschränkungen

- Keine Dateien verändern.
- Nichts committen.
- Nichts pushen.
- Nur lesen und bewerten (git diff, ggf. weitere lesende Befehle wie `git status` oder das Lesen einzelner Dateien zur Einordnung des Kontexts sind erlaubt).
