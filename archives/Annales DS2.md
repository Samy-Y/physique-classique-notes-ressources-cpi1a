# Annales DS2 Physique

## DS 2 2024

### Boule de Flipper

#### Q0

Système étudié : {Bille}
Bilan des forces :
- Poids : $\vec{P} = -mg\sin(\alpha) \vec{e}_y - mg\cos(\alpha) \vec{e}_z$
- Réaction du plan incliné : $\vec{R} = P\cdot \cos\alpha \vec{e_y}$

Force résultante :
$$\vec{F} = \vec{P} + \vec{R} = -mg\sin(\alpha) \vec{e}_z$$

#### Q1.a

Par PFD, on a :
$$\sum \vec{F}_{ext} = m \vec{a}= \vec{0}$$
$$\implies \dots$$
$$\implies \Delta l_{éq} = \frac{mg\sin(\alpha)}{k} = \frac{mg'}{k}$$

#### Q1.b

$$\ddot{z} + \frac{k}{m} z = g\sin(\alpha)$$

#### Q1.c

$$z(t)=-\Delta l_i \cos(\sqrt{\frac{k}{m}} t) - \Delta l_{éq}$$

#### Q2

$$\Delta l_p \ge \Delta l_{éq}$$
$$\ddot{z}(z_{max})=\Delta l_i \frac{k}{m}$$

#### Q3.a

$$v_1 = \sqrt{\frac km}\sqrt{(\Delta l_i^2 - \Delta l_{eq}^2)}$$

#### Q3.b

$$v(z)=\sqrt{v_1^2 - 2zg\sin(\alpha)}$$

$$\Delta l_D = \sqrt{\frac{2mg'}{k}D+\Delta l_{eq}^2}$$

#### Q4

$$\mu=\tan(\alpha)\left(\frac D{z_{max}} - 1\right)$$

### CORR

Voici la résolution détaillée de la troisième partie de l'exercice.

L'analyse de cette partie est délicate car **la définition de l'angle $\theta$ dans le diagramme est en contradiction avec l'expression de la vitesse angulaire $\dot{\theta}$ donnée dans la question 1.b**.

Pour résoudre le problème, nous devons ignorer l'angle $\theta$ du diagramme et utiliser un angle (que nous appellerons aussi $\theta$, conformément au texte) qui est cohérent avec la formule fournie.

**Convention correcte (basée sur la formule en 1.b) :**
* L'origine est le centre $O_3$.
* L'axe $\vec{e}_x$ est horizontal, dirigé de $O_3$ vers $O_2$.
* L'axe $\vec{e}_z$ est vertical, dirigé de $O_3$ vers le haut.
* L'angle $\theta$ est mesuré depuis l'axe horizontal $\vec{e}_x$, et est **positif vers le haut**.
* Le point $O_2$ (départ) est à $\theta = 0$.
* Le point $O_4$ (opposé) est à $\theta = \pi$.
* La gravité apparente est $\vec{P'} = -mg' \vec{e}_z$ (vers le bas).
* La réaction du guide $\vec{N}$ est dirigée vers le centre $O_3$ (donc $\vec{N} = -N \vec{e}_r$).

---

### III - Trajectoire circulaire

#### 1. (a) Établir les équations différentielles

On applique le Principe Fondamental de la Dynamique (PFD) en coordonnées polaires $\sum \vec{F} = m \vec{a}$.
* **Vecteurs de base :**
    * $\vec{e}_r = \cos\theta \vec{e}_x + \sin\theta \vec{e}_z$
    * $\vec{e}_\theta = -\sin\theta \vec{e}_x + \cos\theta \vec{e}_z$
* **Forces :**
    * $\vec{N} = -N \vec{e}_r$
    * $\vec{P'} = -mg' \vec{e}_z = -mg' (\sin\theta \vec{e}_r + \cos\theta \vec{e}_\theta)$
* **Accélération :**
    * $\vec{a} = (-R \dot{\theta}^2) \vec{e}_r + (R \ddot{\theta}) \vec{e}_\theta$

On projette le PFD :
$\vec{N} + \vec{P'} = m \vec{a}$
$(-N - mg'\sin\theta) \vec{e}_r + (-mg'\cos\theta) \vec{e}_\theta = (-mR\dot{\theta}^2) \vec{e}_r + (mR\ddot{\theta}) \vec{e}_\theta$

En identifiant les composantes :
1.  **Équation radiale (sur $\vec{e}_r$) :**
    $-N - mg'\sin\theta = -mR\dot{\theta}^2 \implies N = mR\dot{\theta}^2 - mg'\sin\theta$
2.  **Équation tangentielle (sur $\vec{e}_\theta$) :**
    $-mg'\cos\theta = mR\ddot{\theta} \implies \ddot{\theta} = -\frac{g'}{R} \cos\theta$

---

#### 1. (b) Vitesse angulaire et Réaction $\vec{N}$

**Vérifier $\dot{\theta}$ :**
On utilise le théorème de l'énergie cinétique entre $O_2$ (où $\theta=0$, $v=v_2$) et un point $M$ (angle $\theta$, vitesse $v=R\dot{\theta}$).
$$\Delta E_c = W(\vec{P'}) + W(\vec{N})$$
$W(\vec{N}) = 0$ (force normale au déplacement).
$$W(\vec{P'}) = \int_{O_2}^M \vec{P'} \cdot d\vec{l} = \int_{0}^{\theta} (-mg'\vec{e}_z) \cdot (R d\theta' \vec{e}_{\theta'})$$
$$W(\vec{P'}) = \int_{0}^{\theta} (-mg'\vec{e}_z) \cdot (-\sin\theta' \vec{e}_x + \cos\theta' \vec{e}_z) R d\theta'$$
$$W(\vec{P'}) = \int_{0}^{\theta} -mg'R \cos\theta' d\theta' = -mg'R [\sin\theta']_0^\theta = -mg'R \sin\theta$$

L'équation de l'énergie est :
$$E_c(M) - E_c(O_2) = W(\vec{P'})$$
$$\frac{1}{2}m(R\dot{\theta})^2 - \frac{1}{2}mv_2^2 = -mg'R \sin\theta$$
$$mR^2\dot{\theta}^2 - mv_2^2 = -2mg'R \sin\theta$$
$$\dot{\theta}^2 = \frac{v_2^2}{R^2} - \frac{2g'}{R} \sin\theta$$
En prenant la racine (pour $\dot{\theta}>0$, la bille monte), on vérifie bien l'expression :
$$\dot{\theta} = \sqrt{\frac{v_2^2}{R^2} - \frac{2g'}{R} \sin\theta}$$

**Expression de $\vec{N}$ :**
On reprend l'équation radiale de 1.(a) : $N = mR\dot{\theta}^2 - mg'\sin\theta$.
On remplace $\dot{\theta}^2$ par l'expression trouvée :
$$N = mR \left( \frac{v_2^2}{R^2} - \frac{2g'}{R} \sin\theta \right) - mg'\sin\theta$$
$$N = \frac{mv_2^2}{R} - 2mg'\sin\theta - mg'\sin\theta$$
**$N(\theta) = \frac{mv_2^2}{R} - 3mg'\sin\theta$**

---

#### 1. (c) Condition pour atteindre $O_4$

Pour que la bille reste au contact du guide, il faut que la force de réaction $N$ soit toujours positive ou nulle ($N \ge 0$). Si $N$ devient négatif, la bille décolle.
$$N(\theta) = \frac{mv_2^2}{R} - 3mg'\sin\theta \ge 0$$
Nous devons trouver la valeur minimale de $N(\theta)$ sur la trajectoire $\theta \in [0, \pi]$.
$N(\theta)$ est minimale lorsque $3mg'\sin\theta$ est maximale.
Sur l'intervalle $[0, \pi]$, $\sin\theta$ est maximal au sommet de la trajectoire, à $\theta = \pi/2$ (où $\sin(\pi/2)=1$).
La force de réaction minimale est donc :
$$N_{min} = N(\pi/2) = \frac{mv_2^2}{R} - 3mg'\sin(\pi/2) = \frac{mv_2^2}{R} - 3mg'$$
La condition pour atteindre $O_4$ (et donc passer le sommet) est $N_{min} \ge 0$.
$$\frac{mv_2^2}{R} - 3mg' \ge 0 \implies v_2^2 \ge 3g'R$$
La vitesse limite $v_{2f}$ est celle qui annule $N$ au sommet :
**$v_{2f}^2 = 3g'R$**

**Valeur de $\Delta l_i$ correspondante :**
On utilise les relations des questions précédentes (Q3.a et Q3.b) :
$v_2^2 = v_1^2 - 2g'D$
$v_1^2 = \frac{k}{m}(\Delta l_i^2 - \Delta l_{eq}^2)$
$v_{2f}^2 = \frac{k}{m}(\Delta l_i^2 - \Delta l_{eq}^2) - 2g'D = 3g'R$
On isole $\Delta l_i$ :
$$\frac{k}{m}(\Delta l_i^2 - \Delta l_{eq}^2) = 3g'R + 2g'D$$
$$\Delta l_i^2 - \Delta l_{eq}^2 = \frac{mg'}{k} (3R + 2D)$$
On sait que $\Delta l_{eq} = mg'/k$ (Q1.a) :
$$\Delta l_i^2 - \Delta l_{eq}^2 = \Delta l_{eq} (3R + 2D)$$
$$\Delta l_i^2 = \Delta l_{eq}^2 + \Delta l_{eq} (3R + 2D)$$
**$\Delta l_i (\text{limite}) = \sqrt{\Delta l_{eq}^2 + \Delta l_{eq} (3R + 2D)}$**

---

### 2. Condition non remplie

#### 2. (a) Angle $\theta_{max}$ et Vitesse $\vec{v}$

Si $v_2 < v_{2f}$, la bille décolle avant le sommet, à un angle $\theta_{max} < \pi/2$ où $N=0$.
**Relation pour $\theta_{max}$ :**
$$N(\theta_{max}) = 0 \implies \frac{mv_2^2}{R} - 3mg'\sin(\theta_{max}) = 0$$
**$\sin(\theta_{max}) = \frac{v_2^2}{3mg'R}$**

**Vitesse à $\theta_{max}$ :**
* **Module $v_{max}$ :** On utilise la conservation de l'énergie $v^2 = R^2\dot{\theta}^2 = v_2^2 - 2g'R \sin\theta$.
    $$v_{max}^2 = v^2(\theta_{max}) = v_2^2 - 2g'R \sin(\theta_{max})$$
    On remplace $\sin(\theta_{max})$ :
    $$v_{max}^2 = v_2^2 - 2g'R \left( \frac{v_2^2}{3mg'R} \right) = v_2^2 - \frac{2}{3} v_2^2 = \frac{1}{3} v_2^2$$
    **$v_{max} = \frac{v_2}{\sqrt{3}}$**
* **Composantes $\vec{v}_{max}$ (en fonction de $v_2$ et $A=3g'R$) :**
    $\vec{v}$ est tangent : $\vec{v}_{max} = v_{max} \vec{e}_\theta(\theta_{max}) = v_{max} (-\sin\theta_{max} \vec{e}_x + \cos\theta_{max} \vec{e}_z)$
    * $\sin(\theta_{max}) = \frac{v_2^2}{3g'R} = \frac{v_2^2}{A}$
    * $\cos(\theta_{max}) = \sqrt{1 - \sin^2\theta_{max}} = \sqrt{1 - (v_2^2/A)^2} = \frac{\sqrt{A^2 - v_2^4}}{A}$
    * **$v_{max, x} = -v_{max} \sin\theta_{max} = -\frac{v_2}{\sqrt{3}} \left( \frac{v_2^2}{A} \right) = -\frac{v_2^3}{A\sqrt{3}}$**
    * **$v_{max, z} = v_{max} \cos\theta_{max} = \frac{v_2}{\sqrt{3}} \left( \frac{\sqrt{A^2 - v_2^4}}{A} \right) = \frac{v_2 \sqrt{A^2 - v_2^4}}{A\sqrt{3}}$**

---

#### 2. (b) Trajectoire ultérieure

Au point de rupture $M$ (à $\theta_{max}$), la bille quitte le guide ($N=0$) et subit uniquement la gravité apparente $\vec{g'}$. Sa trajectoire devient une **parabole** (mouvement de projectile).

**Condition pour passer par $O_3$ :**
La bille part du point $M$ et doit arriver à l'origine $O_3(0, 0)$.
* Position de départ : $M(x_M, z_M)$
    * $x_M = R \cos\theta_{max} = R \frac{\sqrt{A^2 - v_2^4}}{A}$
    * $z_M = R \sin\theta_{max} = R \frac{v_2^2}{A}$
* Vitesse initiale : $v(x_M, z_M) = (v_{max, x}, v_{max, z})$
* Équations du mouvement (pour $t \ge 0$, origine $M$) :
    * $x(t) = x_M + v_{max, x} \cdot t$
    * $z(t) = z_M + v_{max, z} \cdot t - \frac{1}{2} g' t^2$

On cherche $t_{pass}$ tel que $x(t_{pass}) = 0$ :
$t_{pass} = -x_M / v_{max, x}$
On veut qu'à cet instant, $z(t_{pass}) = 0$ :
$$0 = z_M + v_{max, z} \left( \frac{-x_M}{v_{max, x}} \right) - \frac{1}{2} g' \left( \frac{-x_M}{v_{max, x}} \right)^2$$
On multiplie par $v_{max, x}^2$ :
$$0 = z_M v_{max, x}^2 - v_{max, z} x_M v_{max, x} - \frac{1}{2} g' x_M^2$$
Substituons les valeurs :
* $z_M v_{max, x}^2 = \left( R \frac{v_2^2}{A} \right) \left( \frac{v_2^6}{3A^2} \right) = \frac{R v_2^8}{3A^3}$
* $v_{max, z} x_M v_{max, x} = \left( \frac{v_2 \sqrt{A^2 - v_2^4}}{A\sqrt{3}} \right) \left( \frac{R \sqrt{A^2 - v_2^4}}{A} \right) \left( -\frac{v_2^3}{A\sqrt{3}} \right) = -\frac{R v_2^4 (A^2 - v_2^4)}{3A^3}$
* $\frac{1}{2} g' x_M^2 = \frac{1}{2} \left( \frac{A}{3R} \right) \left( \frac{R^2 (A^2 - v_2^4)}{A^2} \right) = \frac{R (A^2 - v_2^4)}{6A}$

L'équation devient :
$$0 = \frac{R v_2^8}{3A^3} - \left( -\frac{R v_2^4 (A^2 - v_2^4)}{3A^3} \right) - \frac{R (A^2 - v_2^4)}{6A}$$
On multiplie tout par $6A^3 / R$ :
$$0 = 2 v_2^8 + 2 v_2^4 (A^2 - v_2^4) - A^2 (A^2 - v_2^4)$$
$$0 = 2 v_2^8 + 2 v_2^4 A^2 - 2 v_2^8 - A^4 + A^2 v_2^4$$
$$0 = 3 v_2^4 A^2 - A^4$$
$$A^4 = 3 v_2^4 A^2$$
Comme $A \ne 0$, on divise par $A^2$ :
**$A^2 = 3 v_2^4 \implies A = \sqrt{3} v_2^2$**

**Jeu de précision :**
Pour que la bille passe par le centre $O_3$, il faut une condition très exacte liant $A$ (qui dépend de $R$ et $g'$) et $v_2$ (la vitesse d'entrée).
$v_2^2 = A / \sqrt{3} = (3g'R) / \sqrt{3} = \sqrt{3} g'R$.
Cette vitesse $v_2$ dépend elle-même très précisément de la compression initiale $\Delta l_i$.
$\Delta l_i = \sqrt{\Delta l_{eq}^2 + \frac{m}{k} (2g'D + \sqrt{3} g'R)}$.
La moindre erreur sur la compression $\Delta l_i$ change $v_2$, ce qui change $A$ et $\theta_{max}$, et la bille manquera $O_3$. C'est donc bien un jeu de précision.

Voici la transcription de l'exercice, suivie de sa résolution complète.

---

## 📝 Transcription de l'exercice

### I. Interception d'une fusée balistique

Une fusée balistique, assimilée à un point matériel $M$ de masse $m$, est mise à feu à l'instant $t = 0$ depuis le point $O$ avec une vitesse $\vec{v}_0$ faisant un angle $\alpha$ avec le plan horizontal $Oxy$. La fusée se déplace uniquement dans le plan vertical $Oxz$. Le référentiel $\mathcal{R}$ est considéré galiléen ; il est rapporté au repère $(O, \vec{u}_x, \vec{u}_y, \vec{u}_z)$. On note $\vec{g} = -g\vec{u}_z$ l'accélération de la pesanteur, et $\vec{r} = (x, y, z)$ le vecteur position de $M$.

**1. Modélisation sans frottement de l'air**

1.  Déterminer les lois horaires du mouvement du point $M$ en fonction des constantes du problème.
2.  En déduire l'équation de la trajectoire du point $M$ sous la forme $z = f(x)$.
3.  En déduire la portée $P$ et l'altitude maximale $h_{max}$ atteintes par la fusée. On définit la portée à partir de l'altitude initiale du tir : $z = 0$.
4.  Pour quelle valeur de $\alpha$ la portée $P$ est-elle maximale ? Que vaut la portée maximale $P_{max}$ ?

On désire maintenant intercepter la fusée pendant le vol. Pour cela, on lâche sans vitesse initiale, à l'instant $t_1$ positif, un obus au point $N_0$ coordonnées $(x_0, z_0)$. Cet obus sera assimilé à un point matériel $N$ de masse $m'$, de vecteur position $\vec{r}' = (x', y', z')$. On cherche à déterminer la date $t_1$ du lâcher et celle de l'interception $T$ en fonction de la position $N_0$ supposée connue.

5.  Déterminer les lois horaires du mouvement de l'obus.
6.  En déduire à quel instant $T$ s'effectue l'interception.
7.  En déduire une équation du second degré en $t_1$ résultant de l'intersection des 2 trajectoires. On l'écrira en fonction des données du problème.
8.  À quelle condition existe-t-il une solution à cette équation ? Où doit se situer le point $N_0$ d'après cette condition ?
9.  Déterminer à quel instant $t_1$ l'obus doit être lâché afin de réussir l'interception. On exprimera le résultat en fonction de $T$ et autres données du problème.
    Montrer que la position de $N_0$ doit vérifier une seconde condition. Laquelle et pourquoi ? Faire un schéma récapitulant la zone de largage possible de l'obus.
10. On suppose que la position initiale $(x_0, z_0)$ de l'obus par rapport à celle de la fusée est connue avec une précision relative de $0,01\%$ près. Quant aux composantes de la vitesse $\vec{v}_0$, elles sont connues à $0,1\%$ près. En déduire l'incertitude relative sur la date $T$. Faire l'application numérique.

---

## 💡 Résolution de l'exercice

### Partie 1 : Mouvement de la fusée (M)

Le système est la fusée $\{M\}$. La seule force est le poids $\vec{P} = m\vec{g} = -mg\vec{u}_z$.
Le PFD (Principe Fondamental de la Dynamique) donne $m\vec{a} = m\vec{g} \implies \vec{a} = \vec{g}$.
$$\vec{a}(t) = \begin{pmatrix} \ddot{x} \\ \ddot{y} \\ \ddot{z} \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ -g \end{pmatrix}$$
Conditions initiales à $t=0$ :
* $\vec{r}(0) = \vec{0}$
* $\vec{v}(0) = (v_0 \cos\alpha) \vec{u}_x + (v_0 \sin\alpha) \vec{u}_z = \begin{pmatrix} v_0 \cos\alpha \\ 0 \\ v_0 \sin\alpha \end{pmatrix}$

#### 1. Lois horaires de la fusée
Par intégrations successives :
* **Vitesse $\vec{v}(t)$ :**
    $\vec{v}(t) = \int \vec{a}(t) dt = \begin{pmatrix} C_1 \\ C_2 \\ -gt + C_3 \end{pmatrix}$
    Avec $\vec{v}(0)$, on trouve $C_1 = v_0 \cos\alpha$, $C_2 = 0$, $C_3 = v_0 \sin\alpha$.
    $$\vec{v}(t) = \begin{pmatrix} v_0 \cos\alpha \\ 0 \\ v_0 \sin\alpha - gt \end{pmatrix}$$
* **Position $\vec{r}(t)$ :**
    $\vec{r}(t) = \int \vec{v}(t) dt = \begin{pmatrix} (v_0 \cos\alpha)t + C_4 \\ C_5 \\ (v_0 \sin\alpha)t - \frac{1}{2}gt^2 + C_6 \end{pmatrix}$
    Avec $\vec{r}(0) = \vec{0}$, on trouve $C_4 = C_5 = C_6 = 0$.

    **Lois horaires :**
    $$x(t) = (v_0 \cos\alpha)t$$
    $$y(t) = 0$$
    $$z(t) = (v_0 \sin\alpha)t - \frac{1}{2}gt^2$$

#### 2. Équation de la trajectoire $z = f(x)$
On isole $t$ de l'équation $x(t)$ : $t = \frac{x}{v_0 \cos\alpha}$.
On substitue $t$ dans $z(t)$ :
$$z(x) = (v_0 \sin\alpha) \left( \frac{x}{v_0 \cos\alpha} \right) - \frac{1}{2}g \left( \frac{x}{v_0 \cos\alpha} \right)^2$$
**$z(x) = (\tan\alpha) x - \left( \frac{g}{2v_0^2 \cos^2\alpha} \right) x^2$** (équation d'une parabole)

#### 3. Portée ($P$) et Altitude maximale ($h_{max}$)
* **Altitude maximale $h_{max}$ :**
    Atteinte lorsque la vitesse verticale est nulle : $\dot{z}(t_{flèche}) = 0$.
    $v_0 \sin\alpha - gt_{flèche} = 0 \implies t_{flèche} = \frac{v_0 \sin\alpha}{g}$.
    $h_{max} = z(t_{flèche}) = (v_0 \sin\alpha)(\frac{v_0 \sin\alpha}{g}) - \frac{1}{2}g(\frac{v_0 \sin\alpha}{g})^2$
    **$h_{max} = \frac{v_0^2 \sin^2\alpha}{2g}$**

* **Portée $P$ :**
    Atteinte lorsque la fusée retombe au sol $z(t_{portée}) = 0$ (pour $t>0$).
    $(v_0 \sin\alpha)t - \frac{1}{2}gt^2 = 0 \implies t \left( v_0 \sin\alpha - \frac{1}{2}gt \right) = 0$.
    $t_{portée} = \frac{2v_0 \sin\alpha}{g}$ (ce qui vaut $2 \times t_{flèche}$).
    $P = x(t_{portée}) = (v_0 \cos\alpha) \left( \frac{2v_0 \sin\alpha}{g} \right) = \frac{v_0^2 (2\sin\alpha \cos\alpha)}{g}$.
    **$P = \frac{v_0^2 \sin(2\alpha)}{g}$**

#### 4. Portée maximale $P_{max}$
La portée $P(\alpha) = \frac{v_0^2}{g} \sin(2\alpha)$ est maximale lorsque $\sin(2\alpha)$ est maximal, c'est-à-dire $\sin(2\alpha) = 1$.
Ceci est obtenu pour $2\alpha = \frac{\pi}{2}$ (ou 90°).
**$\alpha = \frac{\pi}{4}$ (ou 45°)**
La portée maximale vaut alors :
**$P_{max} = \frac{v_0^2}{g}$**

---

### Partie 2 : Interception par l'obus (N)

Le système est l'obus $\{N\}$. Il est en **chute libre** (lâché sans vitesse initiale).
Son PFD est $m'\vec{a}' = m'\vec{g} \implies \vec{a}' = \vec{g}$.
$$\vec{a}'(t) = \begin{pmatrix} 0 \\ 0 \\ -g \end{pmatrix}$$
Conditions initiales (différentes !) : l'obus est lâché à $t=t_1$.
* $\vec{r}'(t_1) = (x_0, 0, z_0)$
* $\vec{v}'(t_1) = \vec{0}$

#### 5. Lois horaires de l'obus
On intègre pour $t \ge t_1$ :
* **Vitesse $\vec{v}'(t)$ :**
    $\vec{v}'(t) = \int_{t_1}^t \vec{a}' du + \vec{v}'(t_1) = \begin{pmatrix} 0 \\ 0 \\ -g(t-t_1) \end{pmatrix} + \vec{0}$
    $$\vec{v}'(t) = \begin{pmatrix} 0 \\ 0 \\ -g(t-t_1) \end{pmatrix}$$
* **Position $\vec{r}'(t)$ :**
    $\vec{r}'(t) = \int_{t_1}^t \vec{v}'(u) du + \vec{r}'(t_1)$
    $\vec{r}'(t) = \begin{pmatrix} 0 \\ 0 \\ \int_{t_1}^t -g(u-t_1) du \end{pmatrix} + \begin{pmatrix} x_0 \\ 0 \\ z_0 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ \left[ -\frac{1}{2}g(u-t_1)^2 \right]_{t_1}^t \end{pmatrix} + \begin{pmatrix} x_0 \\ 0 \\ z_0 \end{pmatrix}$
    $\vec{r}'(t) = \begin{pmatrix} 0 \\ 0 \\ -\frac{1}{2}g(t-t_1)^2 \end{pmatrix} + \begin{pmatrix} x_0 \\ 0 \\ z_0 \end{pmatrix}$

    **Lois horaires :**
    $$x'(t) = x_0$$
    $$y'(t) = 0$$
    $$z'(t) = z_0 - \frac{1}{2}g(t - t_1)^2$$

#### 6. Instant d'interception $T$
L'interception a lieu à l'instant $T$ (avec $T > t_1$) si $\vec{r}(T) = \vec{r}'(T)$.
On égale les composantes :
1.  $x(T) = x'(T) \implies (v_0 \cos\alpha)T = x_0$
2.  $y(T) = y'(T) \implies 0 = 0$
3.  $z(T) = z'(T) \implies (v_0 \sin\alpha)T - \frac{1}{2}gT^2 = z_0 - \frac{1}{2}g(T - t_1)^2$

De l'équation (1), on déduit l'instant $T$. L'interception ne peut avoir lieu qu'au moment où la fusée atteint l'abscisse $x_0$.
**$T = \frac{x_0}{v_0 \cos\alpha}$**

#### 7. Équation du second degré en $t_1$
On reprend l'équation (3) de la question 6 :
$$(v_0 \sin\alpha)T - \frac{1}{2}gT^2 = z_0 - \frac{1}{2}g(T - t_1)^2$$
On développe le terme de droite :
$$(v_0 \sin\alpha)T - \frac{1}{2}gT^2 = z_0 - \frac{1}{2}g(T^2 - 2Tt_1 + t_1^2)$$
$$(v_0 \sin\alpha)T - \frac{1}{2}gT^2 = z_0 - \frac{1}{2}gT^2 + gTt_1 - \frac{1}{2}gt_1^2$$
Les termes en $-\frac{1}{2}gT^2$ s'annulent :
$$(v_0 \sin\alpha)T = z_0 + gTt_1 - \frac{1}{2}gt_1^2$$
On réorganise tout du même côté pour obtenir une équation de la forme $at_1^2 + bt_1 + c = 0$ :
**$\left(\frac{1}{2}g\right) t_1^2 - (gT)t_1 + \left( (v_0 \sin\alpha)T - z_0 \right) = 0$**
(C'est l'équation voulue, où $T = x_0 / (v_0 \cos\alpha)$).

#### 8. Condition d'existence et position de $N_0$
Pour que cette équation du second degré en $t_1$ admette au moins une solution réelle, son discriminant $\Delta$ doit être positif ou nul ($\Delta \ge 0$).
$$a = \frac{g}{2} \quad ; \quad b = -gT \quad ; \quad c = (v_0 \sin\alpha)T - z_0$$
$$\Delta = b^2 - 4ac = (-gT)^2 - 4 \left( \frac{g}{2} \right) \left( (v_0 \sin\alpha)T - z_0 \right) \ge 0$$
$$\Delta = g^2 T^2 - 2g(v_0 \sin\alpha)T + 2gz_0 \ge 0$$
On divise par $2g$ (qui est positif) :
$$\frac{1}{2}gT^2 - (v_0 \sin\alpha)T + z_0 \ge 0$$
$$z_0 \ge (v_0 \sin\alpha)T - \frac{1}{2}gT^2$$
On reconnaît dans le terme de droite $z(T)$, l'altitude de la fusée à l'instant $T$ (voir Q1).
**Condition : $z_0 \ge z(T)$**

* **Où doit se situer $N_0$ ?**
    $z(T)$ est l'altitude de la fusée à l'abscisse $x_0$ (puisque $T$ est le temps pour atteindre $x_0$).
    La condition $z_0 \ge z(x_0)$ signifie que **le point de largage $N_0$ doit être situé à une altitude supérieure ou égale à celle de la trajectoire de la fusée à la même abscisse $x_0$.**
    (Logique : on ne peut pas intercepter la fusée en lâchant l'obus *en dessous* de sa trajectoire).

#### 9. Instant de largage $t_1$ et zone de largage
On résout l'équation pour $t_1$ :
$$t_1 = \frac{-b \pm \sqrt{\Delta}}{2a} = \frac{gT \pm \sqrt{g^2 T^2 - 2g(v_0 \sin\alpha)T + 2gz_0}}{g}$$
En utilisant $\Delta = 2g(z_0 - z(T))$ (simplification de la Q8) :
$$t_1 = \frac{gT \pm \sqrt{2g(z_0 - z(T))}}{g}$$
**$t_1 = T \pm \sqrt{\frac{2(z_0 - z(T))}{g}}$**

* **Choix de la solution :**
    L'interception a lieu à $T$. Le largage a lieu à $t_1$. Pour que la cause (largage) précède l'effet (interception), on doit avoir **$t_1 < T$**.
    La solution $t_1 = T + \sqrt{\dots}$ est donc physiquement impossible.
    On doit choisir la solution avec le signe "moins" :
    **$t_1 = T - \sqrt{\frac{2(z_0 - z(T))}{g}}$**

* **Seconde condition :**
    L'énoncé précise que $t_1$ est **positif** ($t_1 > 0$).
    $$T - \sqrt{\frac{2(z_0 - z(T))}{g}} > 0$$
    $$T > \sqrt{\frac{2(z_0 - z(T))}{g}}$$
    $$T^2 > \frac{2(z_0 - z(T))}{g} \implies \frac{1}{2}gT^2 > z_0 - z(T)$$
    $z_0 < z(T) + \frac{1}{2}gT^2$
    On remplace $z(T) = (v_0 \sin\alpha)T - \frac{1}{2}gT^2$ :
    $z_0 < \left( (v_0 \sin\alpha)T - \frac{1}{2}gT^2 \right) + \frac{1}{2}gT^2$
    $z_0 < (v_0 \sin\alpha)T$
    En remplaçant $T = x_0 / (v_0 \cos\alpha)$ :
    $z_0 < (v_0 \sin\alpha) \left( \frac{x_0}{v_0 \cos\alpha} \right) \implies$ **$z_0 < x_0 \tan\alpha$**
    La ligne $z = x \tan\alpha$ est la tangente à la trajectoire à l'origine (la direction de tir initiale).

* **Schéma récapitulatif (Zone de largage) :**
    Pour pouvoir intercepter la fusée, le point $N_0(x_0, z_0)$ doit respecter deux conditions :
    1.  **$z_0 \ge z(x_0)$** (être *au-dessus* de la parabole de la fusée)
    2.  **$z_0 < x_0 \tan\alpha$** (être *en dessous* de la tangente de tir initiale)
    La zone de largage est la région comprise entre la trajectoire parabolique de la fusée (incluse) et la droite de visée initiale (exclue).
    
#### 10. Incertitude sur $T$
On cherche l'incertitude relative $\frac{\delta T}{T}$.
La relation la plus simple pour $T$ est (Q6) : $T = \frac{x_0}{v_0 \cos\alpha}$.
On note $v_{0x} = v_0 \cos\alpha$ la composante horizontale de la vitesse initiale.
$T = \frac{x_0}{v_{0x}}$

L'instant d'interception $T$ ne dépend **que** de la position horizontale $x_0$ et de la vitesse horizontale $v_{0x}$. Les incertitudes sur $z_0$ et $v_{0z} = v_0 \sin\alpha$ sont des distracteurs pour *cette* question.

On utilise la méthode des incertitudes relatives (différentielle logarithmique) :
$$\ln(T) = \ln(x_0) - \ln(v_{0x})$$
En passant aux incertitudes (en sommant les contributions, cas le plus défavorable) :
$$\frac{\delta T}{T} = \frac{\delta x_0}{x_0} + \frac{\delta v_{0x}}{v_{0x}}$$

* **Données :**
    * $\frac{\delta x_0}{x_0} = 0,01\% = 0,0001$
    * $\frac{\delta v_{0x}}{v_{0x}} = 0,1\% = 0,001$

* **Application numérique :**
    $$\frac{\delta T}{T} = 0,0001 + 0,001 = 0,0011$$

**$\frac{\delta T}{T} = 0,11\%$**

L'incertitude relative sur la date $T$ est de $0,11\%$.

---

Souhaites-tu que je détaille un point en particulier, comme le calcul de l'incertitude sur $t_1$ (qui utiliserait $z_0$ et $v_{0z}$) ?

Voici la résolution pour le reste de l'exercice sur la descente sur une hélice.

---

### 2. Calculer le vecteur accélération

L'expression générale du vecteur accélération en coordonnées cylindriques est :
$$\vec{a} = (\ddot{r} - r\dot{\theta}^2)\vec{u}_r + (r\ddot{\theta} + 2\dot{r}\dot{\theta})\vec{u}_\theta + \ddot{z}\vec{u}_z$$
On utilise les équations de l'hélice pour trouver les dérivées :
* $r = R$ (constant) $\implies \dot{r} = 0$ et $\ddot{r} = 0$
* $\theta = z/R \implies \dot{\theta} = \dot{z}/R$ et $\ddot{\theta} = \ddot{z}/R$

On substitue ces relations dans l'équation de $\vec{a}$ :
$$\vec{a} = (0 - R(\frac{\dot{z}}{R})^2)\vec{u}_r + (R(\frac{\ddot{z}}{R}) + 2(0)\dot{\theta})\vec{u}_\theta + \ddot{z}\vec{u}_z$$
$$\vec{a}(t) = -\frac{\dot{z}(t)^2}{R} \vec{u}_r + \ddot{z}(t) \vec{u}_\theta + \ddot{z}(t) \vec{u}_z$$
On peut factoriser les termes en $\ddot{z}$ :
**$\vec{a}(t) = -\frac{\dot{z}(t)^2}{R} \vec{u}_r + \ddot{z}(t) (\vec{u}_\theta + \vec{u}_z)$**

---

### 3. Projeter le principe fondamental de la dynamique (PFD)

Le PFD s'écrit $m\vec{a} = \sum \vec{F}$.
Les forces sont le poids $\vec{P} = -mg\vec{u}_z$ et la réaction $\vec{R}$ (qui, sans frottement, est $\vec{R} = \vec{N}$).

Nous devons projeter $m\vec{a} = \vec{P} + \vec{R}$ sur la base $(\vec{u}_r, \vec{u}_t, \vec{u}_n)$.

**1. Transformer la base**
D'après la question 1, nous avons les relations :
* $\vec{u}_t = \frac{1}{\sqrt{2}} (\vec{u}_\theta + \vec{u}_z)$
* $\vec{u}_n = \frac{1}{\sqrt{2}} (\vec{u}_z - \vec{u}_\theta)$

En additionnant et soustrayant ces lignes, on peut isoler $\vec{u}_\theta$ et $\vec{u}_z$ :
* $\vec{u}_\theta = \frac{1}{\sqrt{2}} (\vec{u}_t - \vec{u}_n)$
* $\vec{u}_z = \frac{1}{\sqrt{2}} (\vec{u}_t + \vec{u}_n)$

**2. Projeter les vecteurs**
* **Poids $\vec{P}$ :**
    $\vec{P} = -mg \vec{u}_z = -mg \left[ \frac{1}{\sqrt{2}} (\vec{u}_t + \vec{u}_n) \right] = -\frac{mg}{\sqrt{2}} \vec{u}_t - \frac{mg}{\sqrt{2}} \vec{u}_n$

* **Accélération $\vec{a}$ :**
    On utilise le résultat de Q1.a : $(\vec{u}_\theta + \vec{u}_z) = \sqrt{2} \vec{u}_t$.
    $\vec{a} = -\frac{\dot{z}^2}{R} \vec{u}_r + \ddot{z} (\vec{u}_\theta + \vec{u}_z) = -\frac{\dot{z}^2}{R} \vec{u}_r + \ddot{z} (\sqrt{2} \vec{u}_t)$

* **Réaction $\vec{R}$ (sans frottement) :**
    La réaction est normale à la trajectoire (pas de composante sur $\vec{u}_t$). Elle est donc dans le plan $(\vec{u}_r, \vec{u}_n)$.
    $\vec{R} = N_r \vec{u}_r + N_n \vec{u}_n$

**3. Écrire le PFD projeté**
$m\vec{a} = \vec{P} + \vec{R}$

$m\left( -\frac{\dot{z}^2}{R} \vec{u}_r + \sqrt{2}\ddot{z} \vec{u}_t \right) = \left( -\frac{mg}{\sqrt{2}} \vec{u}_t - \frac{mg}{\sqrt{2}} \vec{u}_n \right) + (N_r \vec{u}_r + N_n \vec{u}_n)$

On identifie les composantes :
* **(sur $\vec{u}_r$) :** $m\left(-\frac{\dot{z}^2}{R}\right) = N_r$
* **(sur $\vec{u}_t$) :** $m\sqrt{2}\ddot{z} = -\frac{mg}{\sqrt{2}}$
* **(sur $\vec{u}_n$) :** $0 = -\frac{mg}{\sqrt{2}} + N_n \implies N_n = \frac{mg}{\sqrt{2}}$

---

### 4. Établir l'équation du mouvement et la résoudre (sans frottement)

L'équation du mouvement est l'équation projetée sur la tangente $\vec{u}_t$, car les forces de réaction (normales) n'y apparaissent pas.
$$m\sqrt{2}\ddot{z} = -\frac{mg}{\sqrt{2}}$$
$$\ddot{z} = -\frac{g}{\sqrt{2} \cdot \sqrt{2}} = -\frac{g}{2}$$
**L'équation du mouvement est $\ddot{z} = -g/2$.**

**Résolution :**
On intègre deux fois par rapport au temps :
1.  $\dot{z}(t) = \int -\frac{g}{2} dt = -\frac{g}{2} t + C_1$
    * *Condition initiale :* "abandonné sans vitesse initiale" $\implies \vec{v}(0) = \vec{0}$.
    * Comme $\vec{v} = \dot{z}(\vec{u}_\theta + \vec{u}_z)$, $\vec{v}(0)=\vec{0}$ implique $\dot{z}(0)=0$.
    * $\dot{z}(0) = 0 \implies C_1 = 0$.
    * Donc : $\dot{z}(t) = -\frac{g}{2} t$

2.  $z(t) = \int -\frac{g}{2} t dt = -\frac{g}{4} t^2 + C_2$
    * *Condition initiale :* "depuis le point $M_0$ tel que $(z=0, \theta=0)$" $\implies z(0)=0$.
    * $z(0) = 0 \implies C_2 = 0$.

**La solution est $z(t) = -\frac{g}{4} t^2$.**

---

### 5. En déduire les composantes de la réaction $\vec{R}$

$\vec{R}$ a deux composantes $N_r$ et $N_n$.
* D'après Q3, **$N_n = \frac{mg}{\sqrt{2}}$** (constante).
* D'après Q3, $N_r = -m \frac{\dot{z}^2}{R}$.
* D'après Q4, $\dot{z}(t) = -\frac{g}{2} t$, donc $\dot{z}^2 = \frac{g^2}{4} t^2$.
* En substituant : **$N_r(t) = -\frac{mg^2 t^2}{4R}$**.

(La composante $N_r$ est négative, ce qui signifie que le guide pousse la bille vers l'axe $O_z$, fournissant la force centripète nécessaire à la rotation).

---

### 6. Par une approche énergétique, retrouver l'équation du mouvement

On utilise le théorème de l'énergie mécanique : $\Delta E_m = W_{forces\;non\;conservatives}$.
* Système : {Bille + Terre}
* $E_m = E_c + E_p$
* Force non conservative : Réaction $\vec{R} = \vec{N}$.
* Sans frottement, $\vec{N}$ est perpendiculaire à la vitesse $\vec{v}$. Son travail est nul : $W(\vec{N}) = 0$.
* L'énergie mécanique se conserve : $\frac{dE_m}{dt} = 0$.

**Calcul de $E_m$ :**
* **Énergie potentielle (de pesanteur) :** $E_p = mgz$
* **Énergie cinétique :** $E_c = \frac{1}{2} m v^2$
    * D'après Q1.a, $\vec{v} = \dot{z}(\vec{u}_\theta + \vec{u}_z)$.
    * $v^2 = ||\vec{v}||^2 = \dot{z}^2 \cdot ||\vec{u}_\theta + \vec{u}_z||^2 = \dot{z}^2 (1^2 + 1^2) = 2\dot{z}^2$.
    * $E_c = \frac{1}{2} m (2\dot{z}^2) = m\dot{z}^2$.

**Conservation :**
$$E_m = m\dot{z}^2 + mgz = \text{Constante}$$
On dérive cette expression par rapport au temps :
$$\frac{dE_m}{dt} = \frac{d}{dt} (m\dot{z}^2 + mgz) = 0$$
$$m(2\dot{z}\ddot{z}) + mg\dot{z} = 0$$
$$m\dot{z} (2\ddot{z} + g) = 0$$
Cette équation a deux solutions : $\dot{z}=0$ (la bille reste immobile) ou $2\ddot{z} + g = 0$.
La deuxième solution décrit le mouvement :
**$\ddot{z} = -g/2$**
On retrouve bien l'équation du mouvement.

---

### 7. Établir l'équation du mouvement (avec frottement)

On reprend le PFD de la Q3, mais $\vec{R} = \vec{N} + \vec{T}$.
* $\vec{N} = N_r \vec{u}_r + N_n \vec{u}_n$ (forces normales).
* $\vec{T}$ est la force de frottement solide. Elle s'oppose au mouvement.
    * Le mouvement se fait vers le bas ($\dot{z}<0$), donc $\vec{v}$ est dans la direction $-\vec{u}_t$.
    * $\vec{T}$ est donc dans la direction $+\vec{u}_t$ : $\vec{T} = T \vec{u}_t$.
* La loi de Coulomb dit $T = f ||\vec{N}||$, où $f$ est le coefficient de frottement.
    * $||\vec{N}|| = \sqrt{N_r^2 + N_n^2}$

Le PFD projeté devient :
$m\left( -\frac{\dot{z}^2}{R} \vec{u}_r + \sqrt{2}\ddot{z} \vec{u}_t \right) = (\vec{P}) + (\vec{N}) + (\vec{T})$
$m\left( \dots \right) = \left( -\frac{mg}{\sqrt{2}} \vec{u}_t - \frac{mg}{\sqrt{2}} \vec{u}_n \right) + (N_r \vec{u}_r + N_n \vec{u}_n) + (T \vec{u}_t)$

* (sur $\vec{u}_r$) : $m\left(-\frac{\dot{z}^2}{R}\right) = N_r$ (inchangé)
* (sur $\vec{u}_n$) : $0 = -\frac{mg}{\sqrt{2}} + N_n \implies N_n = \frac{mg}{\sqrt{2}}$ (inchangé)
* **(sur $\vec{u}_t$) :** $m\sqrt{2}\ddot{z} = -\frac{mg}{\sqrt{2}} + T$ (nouvelle équation de mouvement)

On remplace $T = f ||\vec{N}|| = f \sqrt{N_r^2 + N_n^2}$ :
$T = f \sqrt{\left(-m\frac{\dot{z}^2}{R}\right)^2 + \left(\frac{mg}{\sqrt{2}}\right)^2} = f m \sqrt{\frac{\dot{z}^4}{R^2} + \frac{g^2}{2}}$

L'équation du mouvement est :
$m\sqrt{2}\ddot{z} = -\frac{mg}{\sqrt{2}} + f m \sqrt{\frac{\dot{z}^4}{R^2} + \frac{g^2}{2}}$
**$\sqrt{2}\ddot{z} = -\frac{g}{\sqrt{2}} + f \sqrt{\frac{\dot{z}^4}{R^2} + \frac{g^2}{2}}$**

---

### 8. Déterminer la condition sur $f$ pour que le mobile démarre

Le mobile démarre si son accélération initiale $\ddot{z}(0)$ est non nulle (et négative, pour tomber). On évalue l'équation du mouvement (Q7) à $t=0$, où $\dot{z}(0) = 0$ :
$$\sqrt{2}\ddot{z}(0) = -\frac{g}{\sqrt{2}} + f \sqrt{\frac{0^4}{R^2} + \frac{g^2}{2}}$$
$$\sqrt{2}\ddot{z}(0) = -\frac{g}{\sqrt{2}} + f \frac{g}{\sqrt{2}}$$
$$\sqrt{2}\ddot{z}(0) = \frac{g}{\sqrt{2}} (f - 1)$$
$$\ddot{z}(0) = \frac{g}{2} (f - 1)$$
Pour que la bille démarre (c'est-à-dire $\ddot{z}(0) < 0$, car la gravité la tire vers le bas), il faut :
$$\frac{g}{2} (f - 1) < 0 \implies f - 1 < 0$$
**La condition de démarrage est $f < 1$.**
(Si $f \ge 1$, la force de frottement statique maximale est supérieure ou égale à la composante motrice du poids, et la bille reste immobile).

---

### 9. Montrer qu'il existe une vitesse limite de chute

Une vitesse limite $\dot{z}_{lim}$ (constante) est atteinte lorsque l'accélération $\ddot{z}$ devient nulle.
On pose $\ddot{z} = 0$ dans l'équation du mouvement (Q7), en supposant $f < 1$.
$$0 = -\frac{g}{\sqrt{2}} + f \sqrt{\frac{\dot{z}_{lim}^4}{R^2} + \frac{g^2}{2}}$$
$$\frac{g}{\sqrt{2}} = f \sqrt{\frac{\dot{z}_{lim}^4}{R^2} + \frac{g^2}{2}}$$
On élève au carré :
$$\frac{g^2}{2} = f^2 \left( \frac{\dot{z}_{lim}^4}{R^2} + \frac{g^2}{2} \right)$$
$$\frac{g^2}{2f^2} = \frac{\dot{z}_{lim}^4}{R^2} + \frac{g^2}{2}$$
$$\frac{\dot{z}_{lim}^4}{R^2} = \frac{g^2}{2f^2} - \frac{g^2}{2} = \frac{g^2}{2} \left( \frac{1}{f^2} - 1 \right)$$
$$\dot{z}_{lim}^4 = \frac{g^2 R^2 (1 - f^2)}{2f^2}$$
On prend la racine quatrième (et on garde le signe négatif car c'est une chute) :
$|\dot{z}_{lim}| = \sqrt[4]{\frac{g^2 R^2 (1 - f^2)}{2f^2}} = \sqrt{gR} \sqrt[4]{\frac{1-f^2}{2f^2}}$

La vitesse de chute $v_{lim}$ est la norme de $\vec{v}$, $v = \sqrt{2}|\dot{z}|$.
$$v_{lim} = \sqrt{2} |\dot{z}_{lim}| = \sqrt{2} \left[ \frac{g^2 R^2 (1 - f^2)}{2f^2} \right]^{1/4}$$
$$v_{lim} = (2)^{1/2} \frac{(g^2 R^2)^{1/4} (1-f^2)^{1/4}}{(2f^2)^{1/4}} = \frac{2^{1/2}}{2^{1/4}} \frac{\sqrt{gR} \sqrt[4]{1-f^2}}{\sqrt{f}}$$
**$v_{lim} = \sqrt[4]{2} \sqrt{\frac{gR}{f}} \sqrt[4]{1 - f^2}$**