# Transcription (SYS125 —-— 2511271015)
## Mouvements à force centrale

### PARTIE 1 : Généralités

**1. Force centrale conservative**

Une force centrale est définie comme étant une force constamment dirigée vers un point fixe d'un référentiel galiléen ($O$) qu'on appelle le centre de force.

La force centrale conservative a pour expression générale :
$$\vec{F}(M) = F(r) \vec{u_r}$$
où $F(r)$ est une fonction scalaire de la distance $r = OM$ et $\vec{u_r}$ est le vecteur unitaire radial pointant de $O$ vers $M$.

En appliquant le principe fondamental de la dynamique (PFD) dans le référentiel galiléen, on obtient :
$$m \frac{d^2 \vec{r}}{dt^2} = \vec{F}(M)$$

Donc le vecteur accélération $\vec{a}$ est donné par :
$$\vec{a} = \frac{\vec{F}(M)}{m}$$

Il est constamment dirigé vers le centre de force $O$.

En ce qui concerne l'aspect "conservatif" de la force, cela signifie que le travail de cette force entre deux points ne dépend pas du chemin suivi, mais uniquement des positions initiale et finale. Par conséquent, il existe une énergie potentielle associée à cette force.

Le travail élémentaire de la force centrale est donné par :
$$\delta W = \vec{F}(M) \cdot d\vec{r} = F(r) dr$$

En intégrant, on peut définir l'énergie potentielle $E_p(r)$ associée à la force centrale :
$$E_p(r) = -\int F(r) dr + C$$
où $C$ est une constante d'intégration.

**Remarque importante :** En général, $\vec{F}$ est une force conservative si et seulement si elle peut être dérivée d'une énergie potentielle, c'est-à-dire si $\vec{F} = -\vec{\nabla} E_p$.

Pour expliquer ce qu'est $\vec{\nabla} E_p$ à partir de zéro (on a jamais vu ça), il s'agit tout simplement du gradient de la fonction scalaire $E_p$. Le gradient est un vecteur qui pointe dans la direction de la plus grande augmentation de la fonction et dont la magnitude est égale au taux de changement maximal de cette fonction. Ainsi, $\vec{\nabla} E_p$ donne la direction et l'intensité du changement de l'énergie potentielle dans l'espace.

On l'exprime de cette manière :
$$\vec{\nabla} = \frac{\partial }{\partial x} \vec{u_x} + \frac{\partial }{\partial y} \vec{u_y} + \frac{\partial }{\partial z} \vec{u_z}$$

Dans notre base polaire, on aura :
$$\vec{\nabla} = \vec{u_r} \frac{\partial }{\partial r} + \vec{u_\theta} \frac{1}{r} \frac{\partial }{\partial \theta} + \vec{u_z} \frac{\partial }{\partial z}$$

On peut donc exprimer $\vec{F}$ en fonction de $E_p$ :
$$\vec{F} = -\vec{\nabla} E_p = -\vec{u_r} \frac{\partial E_p}{\partial r} - \vec{u_\theta} \frac{1}{r} \frac{\partial E_p}{\partial \theta} - \vec{u_z} \frac{\partial E_p}{\partial z}$$

**Quelques exemples :**

- **Force gravitationnelle** : La force gravitationnelle entre deux masses $m_1$ et $m_2$ séparées par une distance $r$ est donnée par :
  $$\vec{F}(M) = -G \frac{m_1 m_2}{r^2} \vec{u_r}$$
  où $G$ est la constante gravitationnelle. L'énergie potentielle associée est :
  $$E_p(r) = -G \frac{m_1 m_2}{r} + C$$

- **Force électrostatique** : La force entre deux charges électriques $q_1$ et $q_2$ séparées par une distance $r$ est donnée par :
  $$\vec{F}(M) = k \frac{q_1 q_2}{r^2} \vec{u_r}$$
  où $k$ est la constante de Coulomb. L'énergie potentielle associée est :
  $$E_p(r) = k \frac{q_1 q_2}{r} + C$$

- **Force de rappel** : La force de rappel dans un ressort est donnée par :
  $$\vec{F}(M) = -k r \vec{u_r}$$
  où $k$ est la constante de raideur du ressort. L'énergie potentielle associée est :
  $$E_p(r) = \frac{1}{2} k r^2 + C$$

Ces exemples illustrent comment différentes forces centrales peuvent être exprimées en termes d'énergie potentielle, confirmant leur nature conservative.

**2. La conservation cinétique**

On rappelle la formule de base du moment cinétique d'un point $M$ par rapport à un point fixe $O$ dans un repère galiléen $R$ :
$$\vec{L_O} = \vec{OM} \times m \vec{v}$$
où $\vec{v}$ est la vitesse de $M$ dans $R$.

Le théorème du moment cinétique s'écrit :
$$\frac{d \vec{L_O}}{dt} = \vec{\Gamma_O}$$
où $\vec{\Gamma_O}$ est le moment de la force par rapport à $O$ :
$$\vec{\Gamma_O} = \vec{OM} \times \vec{F(M)}$$
Dans le cas d'une force centrale, $\vec{F(M)}$ est colinéaire à $\vec{OM}$, donc le produit vectoriel est nul :
$$\vec{\Gamma_O} = \vec{0}$$
Ainsi, on a :
$$\frac{d \vec{L_O}}{dt} = \vec{0}$$
Ce qui implique que le moment cinétique $\vec{L_O}$ est constant dans le temps :
$$\vec{L_O} = \text{constante}$$

**3. Mouvements plans**

Le fait que le moment cinétique soit constant implique que le mouvement du point $M$ se déroule dans un plan perpendiculaire à $\vec{L_O}$. En effet, puisque $\vec{L_O}$ est constant en direction et en magnitude, le vecteur position $\vec{OM}$ doit rester dans un plan fixe.

On peut choisir un repère polaire $(O, \vec{u_r}, \vec{u_\theta})$ dans ce plan, où $\vec{u_r}$ est dirigé de $O$ vers $M$ et $\vec{u_\theta}$ est perpendiculaire à $\vec{u_r}$ dans le plan du mouvement.

On exprime alors $\vec{L}_{O/R}(M)$ dans ce repère :
$$\vec{L}_{O/R}(M) = \vec{OM} \times m \vec{v} = m r^2 \dot{\theta} \vec{u_z} = \text{constante}$$
où $\vec{u_z}$ est perpendiculaire au plan du mouvement.

Cela montre que le produit $m r^2 \dot{\theta}$ est constant, ce qui est une expression de la conservation du moment cinétique dans le mouvement plan sous l'influence d'une force centrale conservative.

En posant $C= r^2 \dot{\theta}$, on obtient la deuxième loi de Kepler, qui stipule que le rayon vecteur balaie des aires égales en des temps égaux :
$$\frac{dA}{dt} = \frac{1}{2} r^2 \dot{\theta} = \frac{C}{2} = \text{constante}$$

**4. Visualisation de la loi des aires**

<iframe 
  src="kepler.html" 
  width="100%" 
  height="500px"
  style="border:none; border-radius: 8px; background: #0f172a;">
</iframe>

**5. Conservation de l'énergie mécanique**

Comme la force centrale est conservative, l'énergie mécanique totale $E_m$ du système est conservée. L'énergie mécanique est la somme de l'énergie cinétique $E_c$ et de l'énergie potentielle $E_p$ :
$$E_m = E_c + E_p = \text{constante}$$

On exprime l'énergie cinétique dans le repère polaire :
$$E_c = \frac{1}{2} m v^2 = \frac{1}{2} m (\dot{r}^2 + r^2 \dot{\theta}^2)$$

On exprime alors l'énergie mécanique totale :
$$E_m = \frac{1}{2} m (\dot{r}^2 + r^2 \dot{\theta}^2) + E_p(r) = \text{constante}$$

En utilisant la conservation du moment cinétique $C = r^2 \dot{\theta}$, on peut réécrire l'énergie mécanique totale en fonction de $r$ et $\dot{r}$ uniquement :
$$E_m = \frac{1}{2} m \dot{r}^2 + \frac{mC^2}{2 r^2} + E_p(r) = \text{constante}$$

On définit l'énergie potentielle effective $E_{p,eff}(r)$ comme :
$$E_{p,eff}(r) = \frac{mC^2}{2r^2} + E_p(r)$$

Il s'agit de la somme de l'énergie potentielle due à la force centrale et d'un terme supplémentaire lié au moment cinétique. Pour vulgariser et faire simple, on peut dire que ce terme supplémentaire agit comme une barrière centrifuge qui empêche le point $M$ de s'approcher trop près du centre de force $O$.

On peut exprimer $\frac12 m \dot{r}^2$ en fonction de l'énergie mécanique totale et de l'énergie potentielle effective :
$$\frac{1}{2} m \dot{r}^2 = E_m - E_{p,eff}(r) \ge 0$$

Cette inégalité impose des contraintes sur les valeurs possibles de $r$. En effet, pour que $\dot{r}^2$ soit non négatif, l'énergie mécanique totale doit être supérieure ou égale à l'énergie potentielle effective :
$$E_m \ge E_{p,eff}(r)$$

Il existe donc une valeur critique de l'énergie mécanique totale, notée $E_{m,crit}$, telle que pour $E_m < E_{m,crit}$, le mouvement de $M$ est confiné entre deux distances minimales et maximales par rapport à $O$. Ces distances correspondent aux points où l'énergie mécanique totale égale l'énergie potentielle effective :
$$E_m = E_{p,eff}(r_{min}) = E_{p,eff}(r_{max})$$

On peut tracer un graphe représentant l'évolution de $E_{p,eff}(r)$ en fonction de $r$ pour visualiser ces concepts.

<!-- graphe html -->
<iframe 
    src="energie_potentielle_effective.html" 
    width="100%" 
    height="500px" 
    style="border:none; border-radius: 8px; background: #0f172a;">
</iframe>

Ce graphe montre comment l'énergie potentielle effective varie avec la distance $r$. Les points où la ligne horizontale représentant l'énergie mécanique totale intersecte la courbe de l'énergie potentielle effective déterminent les distances minimales et maximales accessibles au point $M$.

Dans le cas où $r$ évolue entre $r_{min}$ et $r_{max}$, le mouvement de $M$ est dit "lié", car il reste confiné dans une région finie de l'espace. Si l'énergie mécanique totale est suffisamment élevée pour que $M$ puisse s'échapper à l'infini, le mouvement est dit "non lié" ou "libre".

### PARTIE 2 : Force newtonienne et potentiel newtonien

**1. Définition d'une force newtonienne**

Une force newtonienne est une force centrale conservative qui suit la loi de l'inverse du carré de la distance. Elle est donnée par l'expression :
$$\vec{F}(M) = \frac{k}{r^2} \vec{u_r}$$
où $k$ est une constante qui peut être positive ou négative selon la nature de la force (attractive ou répulsive).

**2. Énergie potentielle associée**

L'énergie potentielle associée à cette force est :
$$E_p(r) = -\frac{k}{r} + C$$
où $C$ est une constante d'intégration. On peut s'en affranchir en choisissant $C=0$.

**Démonstration :**

On part de l'expression de la force :
$$\vec{F}(M) = F(r) \vec{u_r} = \frac{k}{r^2} \vec{u_r}$$
Le travail élémentaire de la force est donné par :
$$\delta W = \vec{F}(M) \cdot d\vec{r} = F(r) dr = \frac{k}{r^2} dr$$
En intégrant, on obtient l'énergie potentielle :
$$E_p(r) = -\int F(r) dr + C = -\int \frac{k}{r^2} dr + C = -\left(-\frac{k}{r}\right) + C = \frac{k}{r} + C$$

On peut s'en affranchir en choisissant $C=0$.

**Exemple :**

Le potentiel gravitationnel est un exemple classique de potentiel newtonien. La force gravitationnelle entre deux masses $m_1$ et $m_2$ séparées par une distance $r$ est donnée par :
$$\vec{F}(M) = -G \frac{m_1 m_2}{r^2} \vec{u_r}$$
où $G$ est la constante gravitationnelle. L'énergie potentielle associée est :
$$E_p(r) = -G \frac{m_1 m_2}{r}$$

Le potentiel électrostatique est un autre exemple de potentiel newtonien. La force entre deux charges électriques $q_1$ et $q_2$ séparées par une distance $r$ est donnée par :
$$\vec{F}(M) = k \frac{q_1 q_2}{r^2} \vec{u_r}$$
où $k$ est la constante de Coulomb. L'énergie potentielle associée est :
$$E_p(r) = k \frac{q_1 q_2}{r}$$

**3. Discussion énergétique qualitative du mouvement**

L'énergie potentielle effective pour une force newtonienne est donnée par :
$$E_{p,eff}(r) = \frac12\frac{mC^2}{r^2} + \frac{k}{r}$$
où $C$ est la constante liée au moment cinétique.

Nous allons essayer de déterminer l'allure de la courbe de $E_{p,eff}(r)$ en fonction de la valeur de $k$.

- Si $k > 0$ (force attractive) :
  - Lorsque $r \to 0$, le terme $\frac12\frac{mC^2}{r^2}$ domine, donc $E_{p,eff}(r) \to +\infty$.
  - Lorsque $r \to +\infty$, le terme $-\frac{k}{r}$ domine, donc $E_{p,eff}(r) \to 0^-$.
  - Il existe un minimum de $E_{p,eff}(r)$ à une certaine distance $r_0$, où la force centrifuge équilibre la force attractive.
- Si $k < 0$ (force répulsive) :
  - Lorsque $r \to 0$, le terme $\frac12\frac{mC^2}{r^2}$ domine, donc $E_{p,eff}(r) \to +\infty$.
  - Lorsque $r \to +\infty$, le terme $-\frac{k}{r}$ domine, donc $E_{p,eff}(r) \to 0^+$.
  - La courbe de $E_{p,eff}(r)$ est monotone décroissante.

En ce qui concerne les extrêmes de $E_{p,eff}(r)$, on peut les trouver en dérivant $E_{p,eff}(r)$ par rapport à $r$ et en cherchant les points où la dérivée s'annule :
$$\frac{dE_{p,eff}}{dr} = -\frac{mC^2}{r^3} - \frac{k}{r^2} = 0$$
$$\implies \frac1{r^2}\left[-\frac{mC^2}{r} + k\right] = 0$$
$$\implies -\frac{mC^2}{r} + k = 0$$
$$\implies r = \frac{mC^2}{k}$$

On constate que cet extrême n'existe que si $k < 0$ (force attractive). Dans ce cas, $r_0 = -\frac{mC^2}{k}$ est un minimum de $E_{p,eff}(r)$.

Si $k > 0$, il n'y a pas d'extrême, mais un minimum.

### PARTIE 3 : Détermination de l'expression de la trajectoire

Nous allons établir la trajectoire en utilisant les formules de Binet.

Nous allons d'abord établir l'accélération dans le repère polaire :
$$\vec{a} = (\ddot{r} - r \dot{\theta}^2) \vec{u_r} + (r \ddot{\theta} + 2 \dot{r} \dot{\theta}) \vec{u_\theta}$$

Or, on sait que la force est centrée, donc la composante en $\vec{u_\theta}$ de l'accélération est nulle :
$$r \ddot{\theta} + 2 \dot{r} \dot{\theta} = 0$$

On obtient ainsi l'expression de l'accélération suivante :

$$\vec{a} = (\ddot{r} - r \dot{\theta}^2) \vec{u_r}$$

En effectuant le changement de variable $u = \frac1{r}$, on peut linéariser l'équation différentielle du mouvement. On pose $C=r^2 \dot{\theta} = \text{constante}$. On obtient ainsi l'équation de Binet :

$$\boxed{\vec{a} = -{C^2}u^2 \left(\frac{d^2 u}{d\theta^2} + u\right) \vec{u_r}}$$

On intègre pour trouver l'expression de la vitesse $\vec{v}_{(M/R)}$ :

$$\vec{v}_{(M/R)} = \int \vec{a}~dt = C^2\left(\frac{du}{d\theta}\right)^2+C^2 u^2 + \text{constante}$$

En appliquant le PFD, on a :
$$m \vec{a} = \vec{F}(M)$$

On sait que $\vec{F}(M)=K u^2 \vec{u_r}$, (c'est normalement $\vec{F}(M)=K\frac1{r^2} \vec{u_r}$, on fait le changement de variable) donc on obtient l'équation différentielle suivante :
$$\frac{d^2 u}{d\theta^2} + u = -\frac{K}{mC^2}$$

La solution générale de cette équation différentielle est donnée par :
$$\boxed{u(\theta) = A \cos(\theta - \theta_0) - \frac{K}{mC^2}}$$
où $A$ et $\theta_0$ sont des constantes déterminées par les conditions initiales.

Il s'agit en réalité de l'équation d'une conique en coordonnées polaires, avec le centre de force $O$ situé à un des foyers de la conique. Le paramètre de la conique est donné par :
$$p = \frac{mC^2}{|K|}$$

Une conique peut être une ellipse, une parabole ou une hyperbole, selon la valeur de l'énergie mécanique totale $E_m$ et du paramètre $e$ (excentricité) défini par :
$$e = A \frac{mC^2}{|K|}$$

On peut donc écrire l'équation de la trajectoire sous la forme :
$$r(\theta) = \frac{p}{\varepsilon + e \cos(\theta - \theta_0)}$$

avec $\varepsilon = 1$ si $K < 0$ (force attractive) et $\varepsilon = -1$ si $K > 0$ (force répulsive).

<!--  brah the teacher just coming and assuming we know conics -->

**Explication bien plus détaillée et intuitive des coniques**

#### 1. Introduction : Qu'est-ce qu'une conique ?

Historiquement, les coniques sont les courbes obtenues par l'intersection d'un **cône** de révolution et d'un **plan**. Selon l'angle de coupe, on obtient différentes formes.

Il existe trois types principaux (non dégénérés) :
1.  **L'Ellipse** (coupe fermée, cercle inclus).
2.  **La Parabole** (coupe parallèle à une génératrice du cône).
3.  **L'Hyperbole** (coupe qui tranche les deux nappes du cône).

---

#### 2. La Définition Monofocale (La plus puissante)

C'est souvent la définition la plus utile pour résoudre des problèmes dynamiques (comme les orbites).

Une conique est l'ensemble des points $M$ du plan tels que le rapport de la distance au foyer $F$ sur la distance à la directrice $D$ est constant. Ce rapport est appelé **l'excentricité ($e$)**.

$$\frac{MF}{MH} = e$$

*Où $H$ est la projection orthogonale de $M$ sur la directrice $D$.*

##### Classification par l'excentricité ($e$)
| Excentricité | Type de Conique | Forme |
| :--- | :--- | :--- |
| $e = 0$ | **Cercle** | Cas particulier de l'ellipse. |
| $0 < e < 1$ | **Ellipse** | Fermée. |
| $e = 1$ | **Parabole** | Ouverte (limite). |
| $e > 1$ | **Hyperbole** | Ouverte (deux branches). |

---

#### 3. Équations Réduites (Cartésiennes)

On se place dans un repère adapté où le centre (ou le sommet) de la conique est à l'origine $(0,0)$.

##### A. L'Ellipse
**Équation :**
$$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$$

* **$a$** : Demi-grand axe.
* **$b$** : Demi-petit axe.
* **Relation importante :** $c^2 = a^2 - b^2$ (avec $c$ la distance du centre au foyer).
* **Foyers :** $(\pm c, 0)$.

##### B. L'Hyperbole
**Équation :**
$$\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$$

* **Relation importante :** $c^2 = a^2 + b^2$.
* **Asymptotes :** Les droites d'équation $y = \pm \frac{b}{a}x$.
* **Foyers :** $(\pm c, 0)$.

##### C. La Parabole
**Équation :**
$$y^2 = 2px$$

* **$p$** : Le paramètre de la parabole (distance foyer-directrice).
* **Foyer :** $(p/2, 0)$.
* **Directrice :** $x = -p/2$.

---

#### 4. La Définition Bifocale (Celle du jardinier)

Pour l'ellipse et l'hyperbole, on peut les définir par rapport à deux foyers $F$ et $F'$.

* **Ellipse :** L'ensemble des points $M$ tels que la **somme** des distances aux foyers est constante.
    $$MF + MF' = 2a$$
    *(C'est comme cela qu'on trace une ellipse avec une corde et deux piquets).*

* **Hyperbole :** L'ensemble des points $M$ tels que la **différence** (en valeur absolue) des distances aux foyers est constante.
    $$|MF - MF'| = 2a$$

---

#### 5. L'Équation Polaire (Indispensable en Physique)

Si on place le pôle (origine) sur **un foyer** (et non au centre), l'équation devient unique pour toutes les coniques. C'est la forme utilisée pour les lois de Kepler.

$$r(\theta) = \frac{p}{1 + e \cos(\theta)}$$

* **$r$** : Distance Foyer-Point.
* **$p$** : Paramètre (le "latus rectum" semi-latéral).
    * Pour une ellipse/hyperbole : $p = \frac{b^2}{a} = a(1-e^2)$.
* **$e$** : Excentricité.

##### Résumé visuel des paramètres
* Si $\theta = 0$, le point est au **périastre** (point le plus proche du foyer).
* Si $\theta = \pi$, le point est à l'**apoastre** (point le plus éloigné, existe si $e < 1$).

---

#### 6. L'Équation Générale (Quadratique)

Toute conique est représentée par une équation du second degré à deux variables :

$$Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0$$

Le discriminant $\Delta = B^2 - 4AC$ nous dit tout :
* $\Delta < 0$ : Genre **Ellipse**.
* $\Delta = 0$ : Genre **Parabole**.
* $\Delta > 0$ : Genre **Hyperbole**.

**Site web intéressant pour visualiser les coniques :** [https://www.geogebra.org/m/nqcfbzms](Conic Sections in 3D Space - GeoGebra)

---

**Continuation :**

On retourne au cours sur les forces centrales.

Nous allons lier les coniques aux trajectoires des corps sous l'influence d'une force newtonienne, et aussi à leurs propriétés dynamiques (énergie, moment cinétique, etc.).

On rappelle que l'expression de l'énergie mécanique totale est donnée par : 
$$E = \frac{1}{2}mv^2 - \frac{GMm}{r}$$

En faisant le changement de variable $u = \frac1{r}$, on peut réécrire l'énergie mécanique de la manière suivante :

$$\boxed{E_m = \frac{K^2}{2mC^2}\left(e^2-1\right)}$$

$$\boxed{E_m = \frac12\frac{mC^2}{p}\left(e^2-1\right)}$$