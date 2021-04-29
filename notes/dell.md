# Dell

- [Initial E-Mail](#initial-e-mail)


---

## Questions

- Code needed?
  - prefered language? Python ok?
- Wann anmelden?
  - Welche Vorarbeit notwendig
  - Welche Vorarbeit empfehlenswert
- Prefered language?
  - Eng vs Ger
- Sachen / Präferenzen, die ich nicht wissen kann? (bin flexibel)
- Weitere Paper
  - Empfehlungen vs eigen Recherche


---

## Initial E-Mail

Hallo Julian,

ich habe mal überlegt, ob mir eine Frage für eine Masterarbeit einfällt.

Kürzlich habe ich das tolle Paper [1] gelesen, wo es um das
Homomorphismenpolynom geht und seine Komplexität bezüglich monotoner
Schaltkreise.

Das Paper hat mich an eins meiner eigenen Paper erinnert [2] und ich
habe mir die folgenden Fragen gestellt:

a) Stimmt es, dass der Color Refinement Algorithmus zwei Graphen G,G'
genau dann unterscheidet, wenn die zugehörigen Homomorphismenpolynome
bezüglich des Patterns H nicht identisch sind? (Hier setze ich H auf den
Baum, wo jedes Blatt in Tiefe n ist und jeder innere Knoten Tiefe n hat,
oder vielleicht auf einen Pfad?)? Wenn nein, welche Gegenbeispiele gibt
es? Wenn es stimmt:
- gibt es eine ähnliche Charakterisierung für k-Weisfeiler-Leman?
- kann man diese Tatsache nutzen, um einen möglichst schnellen,
randomisierten Algorithmus für Color Refinement zu entwerfen? Kann man
diesen Algorithmus derandomisieren?

b) In [2] wird diskutiert, wie Graphen G,G' aussehen, die die gleiche
Anzahl an Homormorphismen von Pattern kleiner Baumweite oder kleiner
Pfadweite haben. Wie kann man Paare G,G' charakterisieren, die die
gleichen Homomorphismenzahlen von allen Graphen kleiner Baumtiefe haben?
Außerdem, gibt es einen Algorithmus, der letzteres in Zeit O(n^{td(H)})
entscheidet?

Diese Fragen sind explorativ, das heißt, ich weiß nicht, ob es machbar
ist, die überhaupt zu lösen, und was raus kommt. Also anspruchsvoll.
Außerdem müsstest du noch lernen was Baumweite und so sind. Aber
vielleicht interessiert dich diese thematische Richtung?

Viele Grüße,
Holger



[1]
Graph Homomorphism Polynomials: Algorithms and Complexity
https://arxiv.org/pdf/2011.04778

[2]
https://arxiv.org/abs/1802.08876
