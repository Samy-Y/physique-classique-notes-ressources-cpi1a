# Cheatsheet : Mouvement d’une particule chargée (Champs $\vec{E}$ et $\vec{B}$)

## 1. Principes Fondamentaux
* **Force de Lorentz** : Force subie par une particule de charge $q$ et vitesse $\vec{v}$.
    $$\vec{F} = q(\vec{E} + \vec{v} \wedge \vec{B})$$
* **PFD (Équation du mouvement)** :
    $$\frac{d\vec{v}}{dt} = \frac{q}{m}(\vec{E} + \vec{v} \wedge \vec{B})$$

---

## 2. Champ Électrique Uniforme ($\vec{E}$ constant, $\vec{B}=\vec{0}$)
* **Force** : $\vec{F}_E = q\vec{E}$. Force **conservative**.
* **Accélération** : $\vec{a} = \frac{q}{m}\vec{E}$.
* **Théorème de l'Énergie Cinétique (TEC)** :
    $$\Delta E_c = W_{AB}(\vec{F}_E) = qU_{AB}$$
    *(La particule accélère ou décélère selon le signe de $q$ et $\vec{E}$)*.
* **Trajectoire** :
    * **Rectiligne** si $\vec{v}_0 \parallel \vec{E}$.
    * **Parabolique** si $\vec{v}_0$ fait un angle $\alpha$ avec $\vec{E}$ (déviation parabolique).
* **Équations horaires** (avec $\vec{E} \parallel Ox$) :
    $$x(t) = \frac{qE}{2m}t^2 + v_{0x}t + x_0$$

---

## 3. Champ Magnétique Uniforme ($\vec{B}$ constant, $\vec{E}=\vec{0}$)
* **Force** : $\vec{F}_B = q(\vec{v} \wedge \vec{B})$. Toujours $\perp$ à $\vec{v}$.
* **Énergétique** :
    * La force magnétique **ne travaille pas** ($W = 0$).
    * L'énergie cinétique $E_c$ et la norme de la vitesse $\|\vec{v}\|$ sont **constantes** (mouvement uniforme).
* **Pulsation cyclotron** :
    $$\omega_c = \frac{|q|B}{m}$$ 
* **Trajectoire** :
    * **Circulaire** si $\vec{v}_0 \perp \vec{B}$. Rayon de Larmor :
        $$R = \frac{mv_0}{|q|B}$$ 
    * **Hélicoïdale** si $\vec{v}_0$ a une composante parallèle à $\vec{B}$.

---

## 4. Champs Croisés ($\vec{E} \perp \vec{B}$)
* **Configuration** : Champs orthogonaux (ex: $\vec{E}$ selon $y$, $\vec{B}$ selon $z$).
* **Trajectoire** : **Cycloïde** (combinaison d'un mouvement circulaire et d'une dérive).
* **Vitesse de dérive** (moyenne) :
    $$\langle \vec{v} \rangle = \frac{\vec{E} \wedge \vec{B}}{B^2} \implies v_{drift} = \frac{E}{B}$$ 

---

## 5. Application : Le Cyclotron
* **Principe** : Accélérateur utilisant un champ $\vec{B}$ pour guider et un champ $\vec{E}$ alternatif pour accélérer.
* **Condition de synchronisme** : La fréquence de la tension accélératrice doit égaler la fréquence cyclotron :
    $$f = f_c = \frac{\omega_c}{2\pi} = \frac{|q|B}{2\pi m}$$ 
* **Vitesse maximale** (en sortie, rayon $R_{max}$) :
    $$v_{max} = \frac{|q|B R_{max}}{m}$$ 
    *(Indépendant de la tension accélératrice, dépend du rayon et du champ B)*.