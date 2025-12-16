## Deux oscillateurs

**Longueur à l'équilibre**

Système étudié : $\{Masse (M)\}$

Bilan des forces :

* Poids $\vec{P}$
* Tension $\vec{T}_1$ du premier ressort $(k_1,l_0)$ 
* Tension $\vec{T}_2$ du deuxième ressort $(k_2,l_0)$

Par application du PFD, on a $k_1(l_0-x)-k_2(l_0-d+x)=m\ddot{x}$

On a donc $k_1l_0-k_1x-k_2l_0-k_2x+k_2d=m\ddot{x}$

Donc $m\ddot{x}+x(k_1+k_2)=l_0(k_1-k_2)+k_2d$

Donc $\ddot{x}+\frac{k_1+k_2}m(x-(\frac{k_1-k_2}{k_1+k_2}l_0+\frac{k_2}{k_1+k_2}d))=0$

Donc $x_{eq}=\frac{k_1-k_2}{k_1+k_2}l_0+\frac{k_2}{k_1+k_2}d$

**Équation différentielle avec position d'équilibre comme origine des abscisses**

On va recycler la formule trouvée ci-dessus, mais en remplaçant $x-x_{eq}$ par $x_1$, et on aura $\ddot{x}=\ddot{x}_1$

On obtient donc :

$$\ddot{x}_1+\frac{k_1+k_2}mx_1=0$$

Donc $x_1(t)$ s'écrit sous la forme :

$$x_1(t)=A\cos(\sqrt{\frac{k_1+k_2}m}t+\varphi)$$

avec $A$ et $\varphi$ deux constantes à déterminer

On sait que $\begin{cases} x_1(0)=\alpha_0\\\dot{x}_1(0)=0\end{cases}$

Donc $\begin{cases}A\cos\varphi=\alpha_0\\-A\sqrt{\frac{k_1+k_2}m}\sin\varphi = 0\end{cases}$

Donc $\sin\varphi = 0$, donc $\varphi=0$ ou $\varphi=\pi$, donc $A=\pm\alpha_0$ (ça dépend de $\varphi$)

Si $\alpha_0$ est positive, alors $x_1$ sera décroissante, et $\dot{x}_1$ sera croissante et négative. Ces conditions ne sont vérifiées que si $A=-\alpha_0$ et $\varphi=\pi$

<!-- J'aimerais une manière plus optimisée de déduire ça parce que c'est clairement de la merde là :sob: -->

On a donc :

$$\boxed{x_1(t)=-\alpha_0\cos(\sqrt{\frac{k_1+k_2}m}t+\pi)}$$

**Période des oscillations**

$$T=2\pi\cdot\sqrt{\frac{m}{k_1+k_2}}$$

**Expression de l'énergie mécanique de la masse**

$$E_m=E_c+E_{pe}$$

(On utilise un ressort équivalent de longueur à vide $l_0$ et de raideur $k_1+k_2$)

$$E_m=\frac12m\dot{x}_1^2+\frac12(k_1+k_2)(l_0-x_1)^2$$

On remplace $\dot{x}_1$ et $x_1$ par leurs expressions pour trouver une expression de l'énergie mécanique de la masse. On peut ensuite utiliser leurs points particuliers pour trouver une expression constante (l'énergie mécanique est constante donc...)

**Mêmes questions mais avec plan incliné**

Par PFD dans la nouvelle situation :

(on considère que l'origine passe par l'extrémité de l'axe, pas par la position d'équilibre, comme dans les questions précédentes ;) )

$$-mg\sin\alpha +k_1(l_0-x)-k_2(l_0-d+x)=m\ddot{x}$$

$$m\ddot{x}=-k_1x-k_2x+k_1l_0-k_2l_0+k_2d-mg\sin\alpha$$

$$m\ddot{x}=-x(k_2+k_1)+l_0(k_1-k_2)+k_2d-mg\sin\alpha$$

$$m\ddot{x}+x(k_1+k_2)-l_0(k_1-k_2)-k_2d+mg\sin\alpha=0$$

$$\ddot{x}+\frac{k_1+k_2}m(x-\frac{k_1-k_2}{k_1+k_2}l_0-\frac{k_2}{k_1+k_2}d+\frac{g}{k_1+k_2}\sin\alpha)=0$$

Nouvelle position d'équilibre : $\frac{k_1-k_2}{k_1+k_2}l_0+\frac{k_2}{k_1+k_2}d-\frac{g}{k_1+k_2}\sin\alpha$

On répète les mêmes opérations... pas grand chose ne change !

## Portrait de phase d'un oscillateur harmonique amorti

**Régime de l'oscillateur**

Il s'agit d'un régime pseudo-périodique car son portrait de phase est une spirale.

**Lecture graphique**

* $x_0=3$ cm
* $x_f=0$ cm
* $T_a=315$ ms
* $\delta = \ln(\frac{A(t)}{A(t+T_a)})=\ln(3/1,5)=\ln(2)$

**Facteur de qualité de l'oscillateur**

$$T=\frac{2\pi}\Omega$$

$$\Omega=\frac{2\pi}T$$


$$\omega_0=\sqrt{\Omega^2+\xi^2}$$

$$\xi = \delta / T$$

$$Q=\frac{\omega_0}{2\xi}$$

## Oscillateur harmonique spatial isotrope

**Energie potentielle $E_p$ de $\vec{F}$ en fct de $m,r,\omega_0$**

On sait que $\delta W(\vec{F})=\vec{F}\cdot d\vec{OM}$

$$\delta W(\vec{F})=-k\cdot \vec{OM}\cdot d\vec{OM}$$

$$\delta W(\vec{F})=-k\cdot r \cdot dr$$

On a $\delta W(\vec{F})=-dE_p$

Donc $E_p=\int k\cdot r \cdot dr$

Donc $E_p=\frac12 k r^2 + \cancel{C}$ 

Donc $W(\vec{F})=\frac12 k r_1^2-\frac12 k r_2^2$

Donc $W(\vec{F})=\frac12 k (r_1^2-r_2^2)$

**Equations paramétriques de $x(t)$ et $y(t)$**

On sait que $\vec{F}=m\cdot \vec{a}$

Donc $-k\cdot \vec{OM}=m \cdot \frac{d^2\vec{OM}}{dt^2}$

En projetant sur $\vec{u}_x$ on a :

$$-kx=m\ddot{x}$$
$$-ky=m\ddot{y}$$

$$x=A\cos(\sqrt{\frac km}t+\varphi_1)$$
$$y=B\cos(\sqrt{\frac km}t+\varphi_2)$$

On a

$$x(t=0)=x_0$$
$$\dot{x}(t=0)=0$$
$$y(t=0)=0$$
$$\dot{x}(t=0)=v_0$$

Donc

$$A\cos\varphi_1=x_0$$
$$\sin\varphi_1=0$$
$$B\cos\varphi_2=0$$
$$-B\sqrt{\frac km}\sin\varphi_2=v_0$$

On prend donc $\varphi_1=0$ et $\varphi_2=-\frac12 \pi$
et $A=x_0$ et $B=v_0