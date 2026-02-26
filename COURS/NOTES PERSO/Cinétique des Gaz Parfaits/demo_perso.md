# Distribution des vitesses d'un gaz parfait (Maxwell-Boltzmann)

**Objectif :** Établir le lien entre les grandeurs microscopiques (vitesse des particules $\vec{v}$) et macroscopiques (température $T$) pour un gaz parfait à l'équilibre thermique, où la densité de particules $n^*$ est uniforme.

## 1. Définitions préalables

> [!WARNING]Distinction entre probabilité et densité de probabilité
> Il est impératif de distinguer la probabilité, qui s'applique à un intervalle, de la densité de probabilité, qui s'évalue en un point.

L'étude requiert la définition de trois fonctions de densité de probabilité distinctes :
* $f(v_x)$ : Densité de probabilité pour une composante unidimensionnelle de la vitesse.
* $f(\vec{v})$ : Densité de probabilité pour le vecteur vitesse en trois dimensions.
* $F(v)$ : Densité de probabilité pour la norme de la vitesse (la rapidité).
* $P$ : Probabilité que la vitesse d'une particule soit comprise entre $v_1$ et $v_2$.
$$P(v_1 \leq v \leq v_2) = \int_{v_1}^{v_2} F(v) dv$$

## 2. Distribution unidimensionnelle et normalisation

Selon la statistique de Maxwell-Boltzmann, la probabilité de trouver une particule dans un état d'énergie cinétique $E_c$ est proportionnelle à $e^{-\frac{E_c}{k_B T}}$. Pour la composante $v_x$, l'énergie cinétique associée est $\frac{1}{2} m v_x^2$. La densité de probabilité s'écrit :

$$f(v_x) = A e^{-\frac{m v_x^2}{2 k_B T}}$$

La constante de normalisation $A$ se détermine en imposant que l'intégrale sur toutes les vitesses possibles soit unitaire :

$$\int_{-\infty}^{+\infty} f(v_x) dv_x = 1 \implies A \int_{-\infty}^{+\infty} e^{-\frac{m v_x^2}{2 k_B T}} dv_x = 1$$

> [!TIP]Intégrale de Gauss
> La résolution fait appel à l'intégrale de Gauss $\int_{-\infty}^{+\infty} e^{-\alpha x^2} dx = \sqrt{\frac{\pi}{\alpha}}$, en posant $\alpha = \frac{m}{2 k_B T}$.

Le calcul donne $A \sqrt{\frac{2 \pi k_B T}{m}} = 1$, d'où $A = \sqrt{\frac{m}{2 \pi k_B T}}$. L'expression unidimensionnelle rigoureuse est :

$$f(v_x) = \sqrt{\frac{m}{2 \pi k_B T}} e^{-\frac{m v_x^2}{2 k_B T}}$$

## 3. Distribution du vecteur vitesse en 3D

L'espace est isotrope et les composantes du vecteur vitesse sont indépendantes. La probabilité combinée de trouver le vecteur vitesse $\vec{v}$ dans l'élément de volume de l'espace des vitesses $d^3v = dv_x dv_y dv_z$ correspond au produit des probabilités unidimensionnelles :

$$f(\vec{v}) d^3v = f(v_x) f(v_y) f(v_z) dv_x dv_y dv_z$$

> [!IMPORTANT]
> La normalisation de la distribution tridimensionnelle nécessite la constante $A^3$, puisqu'elle résulte du produit de trois distributions unidimensionnelles.

En effectuant le produit, les arguments des exponentielles s'additionnent de sorte que $v_x^2 + v_y^2 + v_z^2 = v^2$ :

$$f(\vec{v}) = \left( \frac{m}{2 \pi k_B T} \right)^{\frac{3}{2}} e^{-\frac{m v^2}{2 k_B T}}$$

## 4. Distribution de la norme de la vitesse

L'objectif est d'obtenir la probabilité $F(v)dv$ qu'une particule possède une vitesse de norme comprise entre $v$ et $v+dv$, indépendamment de sa direction. Cela requiert l'intégration de $f(\vec{v})$ sur l'ensemble des directions de l'espace des vitesses. Le passage en coordonnées sphériques donne l'élément de volume $d^3v = v^2 \sin\theta dv d\theta d\phi$.

$$F(v) dv = \int_{\theta=0}^{\pi} \int_{\phi=0}^{2\pi} f(\vec{v}) v^2 \sin\theta dv d\theta d\phi$$

Les variables se séparent de la manière suivante :

$$F(v) dv = f(\vec{v}) v^2 dv \left( \int_{0}^{\pi} \sin\theta d\theta \right) \left( \int_{0}^{2\pi} d\phi \right)$$

L'intégration de la partie angulaire donne le facteur $4\pi$, correspondant à l'angle solide total de la sphère. L'expression $4\pi v^2 dv$ représente le volume infinitésimal d'une coquille sphérique d'épaisseur $dv$ et de rayon $v$ dans l'espace des vitesses.

$$F(v) dv = 4\pi v^2 f(\vec{v}) dv$$

La substitution de $f(\vec{v})$ par son expression fournit la fonction de distribution de Maxwell-Boltzmann pour la norme de la vitesse :

$$F(v) = 4\pi \left( \frac{m}{2 \pi k_B T} \right)^{\frac{3}{2}} v^2 e^{-\frac{m v^2}{2 k_B T}}$$