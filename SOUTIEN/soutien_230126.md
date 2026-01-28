# CDS 23 janvier 2026

*transcription approximative*

**Question 1**

$$\vec{v} = r\vec{e}_r+r\dot\theta\vec{e}_\theta$$

**Question 2**

On a $E_p(\vec{f})$. $\vec{f}$ étant conservative, on peut directement écrire

$$\vec f = -\overrightarrow{grad}~E_p$$

En faisant les calculs, on trouve $\vec f = $

**Question 3**

Le moment cinétique.

Son expression est :

$$\vec L_0 = \dots = mr^2\dot\theta \vec{e}_z$$

Il est constant parce que sa dérivée est nulle (produit vectoriel de $\vec r$ et $\vec f$, colinéaires).

Cela implique $r^2\dot\theta = const$. On l'appelle la constante des aires.

La vecteur $\vec{OM}$ balaye des aires égales en des temps égaux. C'est un conséquence immédiate de la conservation de l'énergie mécanique.

**Question 4**

$\vec v = r\dot\theta \vec e_\theta = v\vec e_\theta$

$\vec a = \dot v \vec e\theta - v\dot\theta \vec e_r = -\dfrac{v^2}{r}\vec e_r+\dot v \vec e_\theta$

**Question 5**

En appliquant le principe fondamental à $\Sigma = \{\text{satellite}\}$, on trouve :

$$m\vec a = \vec f$$

On trouve $\dot v = 0$ et $-\dfrac{mv^2}{r} = -\dfrac{g_0Mm}{r^2}$

D'où $v^2 = \dfrac{g_0R_T^2}{r}$

**Question 6**

$$E_m = E_c + E_p$$

$$E_p = -\frac{g_0mR_T^2}r$$

$$E_c = \frac 12 mv^2 = \frac 12 m\frac{g_0R_T^2}{r}$$

$$E_m = -\frac 12 \frac{g_0mR_T^2}r \le 0$$

**Question 7 : Application numérique (skipped)**

**Question 8**

Seules des forces conservatives (gravitationnelles) agissent sur le satellite. Donc son énergie mécanique est conservée.

$$E_m = \frac12 m v^2 + E_p = const$$

$$E_m = \frac12 m\dot r^2 + \underbrace{\frac12 mr^2\dot\theta^2 - \frac{g_0mR_T^2}r}_{=E_{p,eff}(r)}$$

On utilise l'expression de $\vec L_0$ pour écrire $\dot\theta = \dfrac{L_0}{mr^2}$.

On a donc

$$E_{p,eff}(r) = \frac{L_0^2}{2mr^2} - \frac{g_0mR_T^2}r$$

Donc $E_m= \frac12 m\dot r^2 + \dfrac {L_0^2}{2mr^2} - \dfrac{g_0mR_T^2}r$

**Question 9**

Les orbites permises physiquement doivent vérifier $E_m \ge E_{p,eff,min}$.

**Question 10**

a) $E_{m1}$ : hyperbolique.

$E_{m2}$ : elliptique.

b) Pour la valeur $E_m = E_{p,eff,min}$, l'orbite est circulaire.

**Question 11**

$$\dot r = 0$$

(extremums de l'orbite elliptique, périhélie et aphélie)

$$a=\dfrac{r_{b}+r_{h}}{2}$$

**Question 12**

Trivial, on utilise l'expression trouvée précédemment et on remplace $r$ par $r_b$ et $r_h$.

$\alpha = -mg_0R_T^2$

$\beta = -\frac{L_0^2}{2m}$

**Question 13**

Trivial, on utilise les propriétés des racines et des coefficients des équations du second degré, on remplace dans l'équation initiale pour retrouver l'expression de $E_m$ souhaitée en fonction de $a$.

**Question 14**

Environ -39 GJ.

**Question 15**

Trivial.

**Question 16**

$$\Delta E_m = E_{m,trans} - E_{m,basse}$$

Application numérique à faire.

Deuxième partie simple.

$$\Delta E_m / M_c = m_c$$

avec $m_c$ la masse de carburant nécessaire et $M_c$ le pouvoir calorifique du carburant.

**Question 17**

C'est un mélange de dioxygène et d'hydrogène liquide.

**Question 18**

$T=\frac{2\pi r}v = 2\pi \sqrt{\dfrac{r^3}{g_0R_T^2}}$

On trouve $T\approx$ 1h30 pour une orbite basse.

**Question 19**

On dérive $E_m$ et on retrouve le résultat souhaité (on n'oublie pas les frottements et l'expression de $\vec v$...).