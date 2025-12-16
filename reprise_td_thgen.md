## Force élastique/Stabilité d'un équilibre

**Expression de $\vec{O'P}$ dans la base polaire en fonction de $a,\theta$**

$$\vec{O'P}=\vec{O'O}+\vec{OP}
\\
=a\vec{e}_x+a\vec{e}_r
\\
=a(\vec{e}_x+\vec{e}_r)
\\
=a((\cos\theta \vec{e}_r-\sin\theta \vec{e}_\theta)+\vec{e}_r)
\\
= a(1+\cos\theta)\vec{e}_r - a\sin\theta \vec{e}_\theta$$

**Expression du module $O'P$ en fonction de $a,\theta$**

$$||\vec{O'P}||=O'P=a\sqrt{2}\sqrt{1+\cos\theta}$$

$$O'P=2a\cos\frac\theta2$$

**Expression de la tension $\vec{T}$ du ressort en fonction de $a,k,l_O,\theta$**

On sait que $\vec{T}$ est colinéaire avec $\vec{O'P}$, donc $\vec{T}=T\cdot ((1+\cos\theta) \vec{e}_r - \sin\theta\vec{e}_\theta)$ et $T=k(l_0-O'P)$.

Donc $\vec{T}=k(l_0-2a\cos\frac\theta2)((1+\cos\theta) \vec{e}_r - \sin\theta\vec{e}_\theta)$

**Expression de la vitesse de $P$ dans $R_g$**

Le vecteur vitesse est colinéaire au vecteur unitaire $\vec{e}_\theta$, donc $\vec{v}=v\vec{e}_\theta$ ou encore $\vec{v}=a\dot{\theta}\vec{e}_\theta$.

**Expression de la puissance de la résultante des forces $\vec{F}$**

$$\vec{F}=\vec{P}+\vec{T}+\vec{R}$$

comme $R=-T\cdot \vec{e}_r - P\cdot \vec{e}_r$, alors $\vec{F}=C\cdot\vec{e}_\theta$

$$F=\vec{P}\cdot \vec{e}_\theta + \vec{T}\cdot\vec{e}_\theta$$

$$F=mg\vec{e}_x \cdot \vec{e}_\theta + k(2a\cos\frac\theta2-l_0)\sin\theta$$

On sait que $\vec{e}_x=\cos\theta\vec{e}_r-\sin\theta\vec{e}_\theta$

On obtient donc l'expression suivante :

$$F=-mg\sin\theta+k(2a\cos\frac\theta2-l_0)\sin\theta$$

La puissance de F est donc :

$$P(\vec{F})=\vec{F}\cdot\vec{v}=F\cdot a\dot{\theta}$$

$$P(\vec{F})=-mga\dot{\theta}\sin\theta+ka(2a\cos\frac\theta2-l_0)\dot{\theta}\sin\theta$$

**Expression de l'énergie potentielle dont dérive la résultante**

$$\varepsilon_p=\int P(\vec{F})~dt$$

$$\varepsilon_p=-mga\cos\theta+ka\left(-\int l_0\dot{\theta}\sin\theta~dt+\int 2a\cos\frac\theta2\dot{\theta}\sin\theta~dt\right)$$

$$\varepsilon_p=mga\cos\theta + ka\left(l_0\cos\theta+2a\int\dot{\theta}\cos\frac\theta2\sin\theta~dt\right)$$

$$\varepsilon_p=mga\cos\theta+kal_0\cos\theta+2ka^2\int\dot{\theta}\cos\frac\theta2\sin\theta~dt$$

(erreur quelque part ici j'imagine)

**Positions d'équilibre**

On remplacera dans l'expression de $\varepsilon_p(\theta)=0$ pour trouver deux solutions.

**Stabilité des équilibres**

On vérifiera si $\varepsilon_p(\theta_i)>0$ ou non.

**Période $T$ des petites oscillations de $P$**

On sait que l'énergie mécanique se conserve, donc $\frac{dE_m}{dt}=0=\frac{dE_c}{dt}+\frac{d\varepsilon_p}{dt}=\frac{dE_c}{dt}+P(\vec{F})$

On sait que $E_c=\frac12Mv^2=\frac12Ma^2\dot{\theta}^2$

En remplaçant dans l'expression, on trouvera une équation différentielle d'un oscillateur harmonique, ce qui nous permettra de déterminer la période demandée.

## Force de gravitation et tunnel terrestre

**Énergie potentielle de $M$**

On a $\vec{F}=mg_0\frac rR \vec{e}_r=C\cdot r\vec{e}_r$ avec $C=\frac{mg_0}{R}$

$$P(\vec{F})=F\cdot\dot{r}=C\cdot r\cdot \dot{r}$$

En intégrant on trouve que :

$$E_p(r)=\frac12 Cr^2+A$$

avec $A$ une constante à déterminer.

On sait que $E_p(r=0)=0$ (énoncé)

Donc $A=0$

$$\boxed{E_p(r)=\frac12 \frac{mg_0}R r^2}$$

**Vitesse maximal $v_m$ au cours du mouvement**

$$E_m(r)=cte=E_c(r)+E_p(r)$$

$$E_m(r=R)=0+\frac12 mg_0 R$$

$$\implies \boxed{E_m=\frac12 mg_0 R}$$

On a $E_p(r)=E_{p,\min}\iff r=d$ ($r$ ne peut pas être inférieur à $d$ dans les conditions fixées)

Donc $E_c(r)=E_{c,\max} \iff r=d$

$$E_m(r=d)=\frac12mv_m^2 +\frac12\frac{mg_0 d^2}R$$

$$\implies \frac12(mg_0R-\frac{mg_0 d^2}R)=\frac12 mv_m^2$$

$$\implies v_m^2=g_0R-\frac{g_0d^2}R$$

$$\implies \boxed{v_m=\sqrt{g_0R-\frac{g_0d^2}R}}$$

**Expression de $\overline{HM}=x$ en fonction du temps par méthode énergétique**

On sait que $r^2=d^2+x^2$

On a $v=\dot{x}$

On sait que $E_m=cte \implies \frac{dE_m}{dt}=0$

On a $E_m=\frac12 m v^2 + \frac12 \frac{mg_0}R r^2$

Donc $E_m(x)=\frac12 m \dot{x}^2 + \frac12 \frac{mg_0}R (d^2+x^2)$

Donc $E_m(x)=\frac12 m \left(\dot{x}^2+\frac{g_0}R x^2\right) + \frac12 \frac{mg_0}R d^2$

$$\frac{dE_m}{dt}=0$$

$$\dot{x}\ddot{x}+\frac{g_0}R\dot{x}x=0$$

$$\dot{x}\left(\ddot{x}+\frac{g_0}R x\right)=0$$

$$\ddot{x}+\frac{g_0}Rx=0$$

D'où $x(t)=A\cos(\sqrt{\frac{g_0}R}t+\varphi)$

avec $A$ et $\varphi$ deux constantes à déterminer en fonction des conditions initiales.

À $t=0$ on a $R^2=x^2(0)+d^2$ donc $x(t=0)=\sqrt{R^2-d^2}$

On a aussi : $\dot{x}(0)=0$ donc $-A\sqrt{\frac{g_0}R}\sin(\varphi)=0$

Donc $\sin\varphi=0$ et $A\cos\varphi=\sqrt{R^2-d^2}$

Donc $\varphi \equiv 0[\pi]$ et $A=\pm\sqrt{R^2-d^2}$ (dépend de $\varphi$)

On sait que $x$ est croissante au début, donc $x(t)=-\sqrt{R^2-d^2}\cos(\sqrt{\frac{g_0}R}t)$

$$\boxed{x(t)=-\sqrt{R^2-d^2}\cos(\sqrt{\frac{g_0}R}t)}$$

**Représentation de l'énergie potentielle**

$$E_p(r)=\frac12 \frac{mg_0}R r^2$$

$$E_p(x)=\frac12 \frac{mg_0}R (x^2 + d^2)$$
(parabole)

$$E_p(t)=\frac12 \frac{mg_0 d^2}R + \frac12 \frac{(R^2-d^2)mg_0}R\cos^2(\sqrt{\frac{g_0}R}t)$$
(fonction périodique sinusoïdale)

$M$ va suivre un mouvement périodique entre $A$ et $B$, représenté par $x(t)$ (fonction sinusoïdale de paramètre $t$)

## Planeur

**Travail des forces de frottement $W_0$**

On sait que $E_c=\frac12 m v^2$ et comme la vitesse est constante alors $E_c=cte$

On sait que $E_m=E_c+E_{pp}$ et que $\Delta E_m= W_0$

$$\Delta E_m = E_{m,f}-E_{m,i}$$

$$\Delta E_m = mg(z_f-z_i)$$

$$\implies \boxed{W_0 = mg(z_f-z_i)} < 0$$

(on effectue après une application numérique pour trouver la valeur de $W_0$)

**Calcul de l'intensité de la force de frottements**

$$W_0=\int \vec{f}\cdot d\vec{l}=\int -\lambda\vec{v}d\vec{x}=-\frac12 \lambda x^2$$

Lors de la descente : $\Delta z = 2200 - 700 = 1500 = 1,5$ Km

Le planeur aura donc parcouru $x_h=57$ Km horizontalement.

Et on a $x=\sqrt{x_h^2+(\Delta z)^2}$

On obtient donc : $W_0 = - \frac12 \lambda (x_h^2+(\Delta z)^2)$

$$\implies mg\Delta z = \frac12 \lambda (x_h^2+(\Delta z)^2)$$
$$\implies \lambda = \frac{2mg\Delta z}{x_h^2+(\Delta z)^2}$$

$$\implies \lambda = \frac{\frac{2mg}{\Delta z}}{(\frac{x_h}{\Delta z})^2+1}=\frac{1}{39}\frac{2mg}{\Delta z}$$

(on effectue une application numérique pour trouver la valeur de $\lambda$)

## Toboggan

**Expression de $v_m$ la norme de la vitesse du point $M$**

À l'intérieur du demi-cercle, on a $E_m = cte$

Et on a $E_{pp}=mga(1-\cos\theta)$ et $E_c=\frac12 m v_m^2$ (constantes nulles)

On a donc $E_{pp}(\theta=0)=0$ et $E_c=\frac12 m v_0^2$

On a donc $E_m=\frac12 m v_0^2$

Donc $mga(1-\cos\theta)+\frac12 m v_m^2=\frac12 m v_0^2$

Donc $ga(1-\cos\theta)+\frac12 v_m^2=\frac12 v_0^2$

Donc $v_m^2=v_0^2-2ga(1-\cos\theta)$

$$\boxed{v_m(\theta)=\sqrt{v_0^2-2ga(1-\cos\theta)}}$$

**Détermination de la hauteur $h_{\min}$**

Nous allons limiter notre étude au trajet avant l'entrée de le cercle.

On a $E_m=cte$, avec $E_{pp}=m g h(t)$ et $E_c=\frac12 m v^2$

On a donc $mg h(t) + \frac12 m v^2(t)=cte$

Au début du trajet, on a $E_m=mgh$

A la fin du trajet, on a $E_m=\frac 12 m v_0^2$

Donc $\frac{v_0^2}{2}=gh$

Donc $h(v_0)=\frac{v_0^2}{2g}$

On a donc exprimé $h$ en fonction de $v_0$.

Pour que le point matériel arrive au point le plus haut du demi-circle, il faut que sa vitesse à ce point soit strictement positive.

Donc $v_m(\theta=\pi)>0$

Donc $v_0^2-2ga(1-\cos\pi)>0$

Donc $v_0^2>2ga(1-cos\pi)$

On prend $v_{0,\min}^2=4ga$, soit $v_{0,\min}=\sqrt{4ga}=2\sqrt{ga}$

Donc $h_{\min}=\frac{2ga}{2g}=a$

faux faux faux triplement faux

**Expression de la réaction du support**

On a $\sum F_{ext} = m\cdot \alpha$ avec $\alpha=\frac{v_m^2}a$

Donc $R-mg=m\frac{v_m^2}a$

Donc $R=m(g+\frac{v_m^2}a)$

À $\theta = 0$ on a $R=mg+m\frac{v_0^2}a$

## Enroulement d'un pendule autour d'un clou

**Détermination de la condition sur $d$ et $l$ pour que le pendule s'enroule tout en restant tendu**

Le pendule est lâché sans vitesse initiale depuis la position $\alpha_0=\frac12\pi$.

(La position est fixée à $\alpha_0$ et non pas $\alpha$ comme indiqué dans l'énoncé afin de faciliter l'étude, $\alpha$ étant considérée comme la variable d'angle variable entre la position de départ et le début de l'enroulement par rapport au clou)

Toutes les forces mises en jeu sont conservatives, l'énergie mécanique est donc constante.

On a donc $E_m(\alpha)=E_c(\alpha)+E_{pp}(\alpha)$

On a $E_c(\alpha)=\frac12 m v^2=\frac12 m l^2 \dot{\alpha}^2$ (on prend $E_c=0\iff \dot{\alpha}=0$)

On a $E_{pp}(\alpha)=mgl(1-\cos\alpha)$ (on prend $E_{pp}(\alpha=0)=0$)

On a $E_c(\alpha_0)=0$ et $E_{pp}(\alpha=\frac12 \pi)=mgl$

Et on a $E_{pp}(\alpha=0)=0$

On a $E_m=cte=E_{pp}(\alpha=\frac12 pi)=mgl$

Or $E_m=E_c(\alpha=0)$

Donc $\frac12 m v_{\max}^2 = mgl$

Donc $v_{\max}^2=2gl$

$v_{\max}=l\dot{\alpha}_{\max}=\sqrt{2gl}$

Pour que le pendule s'enroule tout en restant tendu, il faut qu'il atteigne la position $\theta = \pi$ avec une force de tension (liée au fil) strictement positive et une vitesse strictement positive (selon le sens utilisé).

Comme le mouvement est circulaire, on a, par PFD :

$$T+mg=m\frac{v^2(\theta=\pi)}{l-d}$$

<!-- j'ai eu BEAUCOUP de mal à faire l'application du PFD ici, j'ai juste tatonné jusqu'à ce que ça ait l'air correct, mais j'aimerais plus d'indications (sur un truc aussi simple... oui...) -->

$$T=m(\frac{v^2(\theta=\pi)}{l-d}-g)$$

Après application de la condition, on obtient :
$$\frac{v^2(\theta=\pi)}{l-d} -g > 0$$

$$v^2(\theta=\pi)>g(l-d)$$

$$\frac12 m v^2(\theta=\pi) > \frac12mg(l-d)$$

$$E_c(\theta=\pi) > \frac12mg(l-d)$$

$$\implies \boxed{E_{c,\min}(\theta=\pi) = \frac12mg(l-d)}$$

On sait que l'énergie mécanique se conserve.

On a $E_m(\theta=0)=\frac12 m v_{\max}^2=mgl$

Donc $E_m(\theta=\pi)=E_c(\theta=\pi)+2mg(l-d)=mgl$

Donc $\frac12 mg(l-d)+2mg(l-d)=mgl$

Donc $\frac12(l-d)+2(l-d)=l$

Donc $\frac52 (l-d) = l$

Donc $5l-5d=2l$

Donc $\boxed{5d=3l}$