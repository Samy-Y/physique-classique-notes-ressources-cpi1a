# Notes de cours
## Physique classique D251030-V1

**Exemples d'application (énergie potentielle et position d'équilibre)**

**Diapo 40: Application 2**

Afin de s'assurer de la stabilité d'une position d'équilibre, on peut analyser la concavité du graphe de l'énergie potentielle $E_p(x)$ autour de cette position.

* À $x=2$, la position d'équilibre est instable.
* À $x=0$, la position d'équilibre est stable.

On admet que l'énergie mécanique totale $E_m$ est constante et égale à 2 J. On a alors :

$$E_m = E_c + E_p = \text{constante} = 2 \text{ J}$$
$$\implies E_c = E_m - E_p = 2 - E_p$$

Graphiquement, on voit que l'énergie cinétique $E_c$ est nulle lorsque $x\approx -0,75$ et $x=1$ et $x\approx 2,7$.

On peut aussi représenter graphiquement $E_c(x)$ en traçant la droite horizontale $E_m = 2$ J et en soustrayant la courbe de $E_p(x)$. Il faut par contre faire attention aux valeurs interdites où $E_p > E_m$, car l'énergie cinétique ne peut pas être négative.

Le point matériel étudié pourra donc se déplacer uniquement dans les intervalles où $E_p(x) \leq E_m$, c'est-à-dire entre $x\approx -0,75$ et $x=1$, ainsi qu'entre $x\approx 2,7$ et l'infini.

* Si $x_0 \in [-0,75; 1]$, le point matériel oscillera entre les positions $x\approx -0,75$ et $x=1$. Sa vitesse sera aussi bornée, avec une vitesse maximale au point d'équilibre stable $x=0$. Le mouvement sera (peut-être, ça dépend des conditions initiales et du système étudié) périodique, mais pas forcément sinusoïdal.
* Si $x_0 \ge 2,7$, le point matériel s'éloignera indéfiniment vers l'infini, sa vitesse augmentant continuellement.

Les conditions initiales vont jouer un rôle crucial dans la détermination du comportement du système. Par exemple, si le point matériel est initialement placé à $x_0=0$, il faudra absolument lui communiquer une vitesse initiale afin d'atteindre l'énergie mécanique totale $E_m = 2$ J. Sinon, il restera au repos à cette position d'équilibre stable (l'énergie potentielle est nulle et $\frac{dE_p}{dx}=0$).

**Oscillateurs harmoniques :**

**Diapo 1 : Vulgarisation :')**

Un oscillateur harmonique est un système physique qui décrit un comportement oscillant à cause d'une nature intrinsèque de restauration ou de rappel autour d'une position d'équilibre.

L'équation caractéristique d'un mouvement harmonique est la suivante :

$$\boxed{\ddot{x}+\omega_0^2 x = 0}$$

**Exemples de systèmes oscillants :**
* Un circuit électrique LC (inductance-capacité) où l'énergie oscille entre le champ magnétique de l'inductance et le champ électrique du condensateur.
  * Dans ce cas, l'analogue de l'énergie cinétique est l'énergie magnétique stockée dans l'inductance, tandis que l'analogue de l'énergie potentielle est l'énergie électrique stockée dans le condensateur.
  * L'énergie magnétique s'écrit sous la forme $E_m = \frac{1}{2} L I^2$ et l'énergie électrique sous la forme $E_e = \frac{1}{2} C V^2$. L'énergie électromagnétique totale du circuit est donc $E_{em} = E_m + E_e = \text{constante}$.
  * L'équation différentielle régissant le comportement du circuit LC est similaire à celle d'un oscillateur harmonique mécanique, avec une fréquence propre donnée par $\omega_0 = \frac{1}{\sqrt{LC}}$. On trouve $\ddot{Q} + \frac{1}{LC} Q = 0$, où $Q$ est la charge sur le condensateur.

La solution de l'équation différentielle trouvée (avant l'exemple) est de la forme :
$$x(t) = Acos(\omega_0 t) + Bsin(\omega_0 t)$$
où $A$ et $B$ sont des constantes déterminées par les conditions initiales du système (position et vitesse initiales) et $\omega_0$ est la fréquence/pulsation propre.

On peut aussi l'écrire sous la forme :
$$x(t) = X_m cos(\omega_0 t + \varphi)$$
où $X_m$ est l'amplitude maximale des oscillations et $\varphi$ est la phase initiale ($X_m=\sqrt{A^2 + B^2}$ et $\varphi = arctan(-\frac{B}{A})$).

Le mouvement est périodique de période $T_0 = \frac{2\pi}{\omega_0}$, elle est indépendante de l'amplitude des oscillations (propriété d'isochronisme des oscillations). Le rythme des oscillations est donc constant, et ne dépend pas des conditions initiales.

**Diapo 7 : Aspect énergétique**

L'énergie potentielle du système est donnée par :
$$E_p = \frac{1}{2} k x^2=\frac{1}{2} k X_m^2\cos^2(\omega_0 t + \varphi)$$
L'énergie cinétique du système est donnée par :
$$E_c = \frac{1}{2} m \dot{x}^2 = \frac{1}{2} m \omega_0^2 X_m^2 \sin^2(\omega_0 t + \varphi)$$
L'énergie mécanique totale du système est donc constante et égale à :
$$E_m = E_c + E_p = \frac{1}{2} k X_m^2$$
(Sachant que $\omega_0^2 = \frac{k}{m}$)

**Diapo 8 : Valeurs moyennes des énergies**

Les valeurs moyennes de l'énergie potentielle et de l'énergie cinétique sur une période sont égales :
$$\langle E_p \rangle = \langle E_c \rangle \\= \frac{1}{T_0} \int_0^{T_0} E_p(t) dt = \frac{1}{T_0} \int_0^{T_0}E_c(t)dt \\= \frac{1}{4} k X_m^2\\=\frac12E_m$$

La représentation graphique communique aussi cette idée d'alternance entre énergie potentielle et énergie cinétique, avec une énergie mécanique totale constante.

**Diapo 9 : Portrait de phase**

Le portrait de phase d'un oscillateur harmonique est une ellipse centrée à l'origine du plan $(x, \dot{x})$. Chaque point de cette ellipse représente un état possible du système à un instant donné, avec une position $x$ et une vitesse $\dot{x}$.

Un point possède une abscisse $x$ (position) et une ordonnée $\dot{x}$ (vitesse). La trajectoire dans le portrait de phase est périodique, reflétant la nature oscillatoire du mouvement. Le point renseigne sur l'*état de phase du mouvement*, c'est-à-dire la combinaison de la position et de la vitesse à un instant donné ($\varepsilon(x, \dot{x})$), et donc l'**énergie potentielle et cinétique** du système à cet instant.

On peut déterminer l'équation caractéristique de l'ellipse en utilisant l'équation différentielle qu'on avait obtenue au début, en combinaison avec la solution de celle-ci.

On a : $\ddot{x} + \omega_0^2 x = 0$ et $\dot{x} = -\omega_0 X_m \sin(\omega_0 t + \varphi)$.

En isolant le temps $t$ dans les deux équations, on peut exprimer $\sin(\omega_0 t + \varphi)$ et $\cos(\omega_0 t + \varphi)$ en fonction de $x$ et $\dot{x}$ :
$$\cos(\omega_0 t + \varphi) = \frac{x}{X_m}$$
$$\sin(\omega_0 t + \varphi) = -\frac{\dot{x}}{\omega_0 X_m}$$

On peut alors utiliser l'identité trigonométrique $\sin^2 + \cos^2 = 1$ pour obtenir l'équation de l'ellipse :
$$\left(\frac{x}{X_m}\right)^2 + \left(-\frac{\dot{x}}{\omega_0 X_m}\right)^2 = 1$$
Ce qui donne finalement :
$$\frac{x^2}{X_m^2} + \frac{\dot{x}^2}{\omega_0^2 X_m^2} = 1$$
ou, en multipliant par $X_m^2$ :
$$x^2 + \frac{\dot{x}^2}{\omega_0^2} = X_m^2$$

**Diapo 11 : Oscillateurs amortis**

On va s'intéresser ici uniquement à l'amortissement visqueux, qui est proportionnel à la vitesse du point matériel. La force d'amortissement s'écrit donc :
$$\vec{f} = -\lambda \vec{v}$$

L'équation différentielle régissant le mouvement de l'oscillateur amorti est alors :
$$\ddot{x} + \frac{\lambda}{m} \dot{x} + \frac{k}{m} x = 0$$

On a l'habitude mettre cette équation sous une forme dite canonique en définissant le coefficient d'amortissement $\xi = \frac{\lambda}{2m}$ (ou n'importe quelle autre lettre...). On obtient alors :
$$\ddot{x} + 2\xi \dot{x} + \omega_0^2 x = 0$$

La dimension de $\xi$ est en $s^{-1}$ (fréquence). Il s'agit d'un temps caractéristique lié à l'amortissement du système.

La forme générale de la solution est $x(t)=Ae^{rt}$. En injectant cette forme dans l'équation différentielle, on obtient le polynôme caractéristique suivant :
$$r^2 + 2\xi r + \omega_0^2 = 0$$

Les solutions de l'équation caractéristique sont données par la formule quadratique :
$$r_{1,2} = -\xi \pm \sqrt{\xi^2 - \omega_0^2}$$

***Attention : Il faut que $\Delta \geq 0$ pour avoir des solutions réelles.***

On utilise un discriminant réduit $\Delta' = \xi^2 - \omega_0^2$ pour analyser les différentes solutions possibles.

**Diapo 14 : Régime pseudo-périodique**

Le régime pseudo-périodique se produit lorsque $\Delta' < 0$, c'est-à-dire lorsque $\xi < \omega_0$. En pratique, cela signifie que l'amortissement est faible par rapport à la fréquence propre du système.

Les racines de l'équation caractéristique sont alors complexes conjuguées :
$$r_{1,2} = -\xi \pm i\omega_1$$

On notera $\Omega^2=-\Delta'$. Ainsi, $r_{1,2} = -\xi \pm i\Omega$.

Les solutions de l'équation différentielle sont donc de la forme :
$$x(t) = e^{-\xi t}(A \cos(\Omega t) + B \sin(\Omega t))$$

On peut aussi écrire la solution sous la forme :
$$x(t) = X_m e^{-\xi t} \cos(\Omega t + \varphi)$$

On peut aussi la mettre sous une forme encore plus simplifiée :
$$x(t)=A(t) \cos(\Omega t + \varphi)$$
où l'amplitude $A(t) = X_m e^{-\xi t}$ décroît exponentiellement avec le temps à cause de l'amortissement.

**Diapo 17 : Pseudo-période et décrément logarithmique**

En revanche, les "sommets" des oscillations sont atteints exactement chaque pseudo-période $T_1 = \frac{2\pi}{\Omega}$.

La pseudo-période et la période propre sont différentes, car l'amortissement modifie la fréquence des oscillations. Celle-ci dépend directement de l'amortissement. 
$$T=\frac{T_0}{\sqrt{1 - \left(\frac{\xi}{\omega_0}\right)^2}}$$

Donc $T > T_0$.

La représentation graphique présente dans le support PPTX aide à mieux assimiler cette décroissance de l'amplitude.

On définit aussi le décrément logarithmique $\delta$ comme étant le logarithme du rapport des amplitudes de deux oscillations successives :
$$\delta = \ln\left(\frac{A(t)}{A(t+T)}\right)=\ln\left(\frac{A(t)}{A(t)e^{-\xi T}}\right)=\ln\left(\frac{1}{e^{-\xi T}}\right)=\xi T$$

**Diapo 18 : Approximation de la pseudo-période**

On approxime $T$ sachant que $\xi \ll \omega_0$ donc $\frac{\xi}{\omega_0} \ll 1$.

On a alors : $T=T_0 \left(1 - \left(\frac{\xi}{\omega_0}\right)^2\right)^{-\frac12} \approx T_0 \left(1 + \frac{1}{2}\left(\frac{\xi}{\omega_0}\right)^2\right) = T_0 + \frac{T_0}{2}\left(\frac{\xi}{\omega_0}\right)^2$.

**Diapo 19 : Régime apériodique**

Ce régime correspond au cas où $\Delta' > 0$, c'est-à-dire lorsque $\xi > \omega_0$. L'amortissement est alors suffisamment fort pour empêcher toute oscillation.

Les racines de l'équation caractéristique sont réelles et distinctes :
$$\begin{cases}r_1 = -\xi + \sqrt{\Delta'}\\r_2 = -\xi - \sqrt{\Delta'}\end{cases}$$

Comme $\xi > \omega_0$, on a $-\xi + \sqrt{\Delta'} < 0$ et $-\xi - \sqrt{\Delta'} < 0$. Les deux racines sont donc négatives.

La solution générale de l'équation différentielle est donc :
$$x(t) = A e^{r_1 t} + B e^{r_2 t}$$
où $A$ et $B$ sont des constantes déterminées par les conditions initiales.

L'amplitude diminue au cours du temps sans oscillations, le système revenant lentement à la position d'équilibre.

**Diapo 20 : Cas critique**

Ce régime correspond au cas où $\Delta' = 0$, c'est-à-dire lorsque $\xi = \omega_0$. L'amortissement est alors juste suffisant pour empêcher les oscillations.

Les racines de l'équation caractéristique sont alors :
$$r_1 = r_2 = -\xi$$

La solution générale de l'équation différentielle est donc :
$$x(t) = (A + Bt)e^{-\xi t}$$
où $A$ et $B$ sont des constantes déterminées par les conditions initiales.

L'amplitude diminue au cours du temps sans oscillations, le système revenant rapidement à la position d'équilibre.

Dans le régime critique, la tendance est de revenir à l'équilibre le plus rapidement possible sans osciller autour de cette position.

En pratique, ce régime n'est jamais parfaitement atteint, mais on peut s'en approcher en ajustant l'amortissement du système.

**Diapo 21 : Aspect énergétique de l'oscillateur amorti**

On limite l'étude au régime pseudo-périodique.
$$x(t) = X_m e^{-\xi t} \cos(\Omega t + \varphi)$$

Les expressions des énergies potentielles et cinétiques sont les suivantes :
$$E_p = \frac{1}{2} k x^2 = \frac{1}{2} k X_m^2 e^{-2\xi t} \cos^2(\Omega t + \varphi)$$
$$E_c = \frac{1}{2} m \dot{x}^2 =\frac12 m\omega_0^2X^2e^{-2\xi t}(\xi\cos(\Omega t + \varphi) + \Omega\sin(\Omega t + \varphi))^2$$
$$E_m = E_p + E_c$$

L'énergie mécanique totale diminue au cours du temps à cause de l'amortissement, l'énergie dissipée étant transformée en chaleur par effet Joule dans le cas d'un amortissement visqueux.

**Diapo 22 : Cas d'un amortissement très faible**

Lorsque l'amortissement est très faible ($\xi \ll \omega_0$), on peut faire les approximations suivantes :
* $\Omega \approx \omega_0$
* $E_p \approx \frac{1}{2} k X_m^2 e^{-2\xi t} \cos^2(\omega_0 t + \varphi)$
* $E_c \approx \frac{1}{2} m \omega_0^2 X_m^2 e^{-2\xi t} \sin^2(\omega_0 t + \varphi)$
* $E_m \approx \frac{1}{2} k X_m^2 e^{-2\xi t} = \frac12 m \omega_0^2 X_m^2 e^{\frac{-t}{\tau}}$ avec $\tau = \frac{1}{2\xi}$

On peut alors estimer la perte d'énergie mécanique sur une période $T_0$ :
$$\Delta E_m = E_m(t) - E_m(t + T_0) \approx \frac{1}{2} k X_m^2 e^{-2\xi t} (1 - e^{-2\xi T_0})$$
En réécrivant avec $\tau$ :
$$\Delta E_m \approx \frac{1}{2} k X_m^2 e^{\frac{-t}{\tau}} \left(1 - e^{-\frac{T_0}{\tau}}\right)$$
On a : $\frac{\Delta E_m}{E_m} \approx 1 - e^{-\frac{T_0}{\tau}}$.

Dans le cas où l'amortissement est très faible, on peut faire l'approximation $e^{-\frac{T_0}{\tau}} \approx 1 - \frac{T_0}{\tau}$. Justification : développement limité à l'ordre 1 de l'exponentielle.
On obtient alors :
$$\frac{\Delta E_m}{E_m} \approx \frac{T_0}{\tau}$$

On peut réécrire cette expression comme suit :
$$\frac{\Delta E_m}{E_m} \approx \frac{2\pi}{Q}$$
avec $Q = \omega_0 \tau = \frac{\sqrt{km}}{\lambda}$ le facteur de qualité de l'oscillateur amorti.

Plus le facteur de qualité est grand, plus l'amortissement est faible et plus l'oscillateur conserve son énergie mécanique sur une période. A ce moment là, on dit que l'oscillateur est *sous-amorti*. $\lambda$ est petit devant $\sqrt{km}$.

L'origine de cette variation de l'énergie mécanique provient aussi de son expression initiale en tant que $\Delta E_m = -\int \lambda \dot{x}^2 dt < 0$.

$$\frac{dE_m}{dt} = P(\vec{F}_{n.c.}) = \vec{F}_{n.c.} \cdot \vec{v} = -\lambda \dot{x}^2$$

**Diapo 27 : Portrait de phase de l'oscillateur amorti**

Le portrait de phase d'un oscillateur amorti dans le régime pseudo-périodique est une spirale centrée à l'origine du plan $(x, \dot{x})$. Chaque point de cette spirale représente un état possible du système à un instant donné, avec une position $x$ et une vitesse $\dot{x}$.

**Diapo 25 : Analogie mécanique - électronique**

||Mécanique|Électronique|
|---|---|---|
|Équation du mouvement|$m\ddot{x} + \lambda \dot{x} + kx = 0$|$L\ddot{q} + R\dot{q} + \frac{1}{C}q = 0$|
|Énergie mécanique|$E_m = \frac{1}{2} m \dot{x}^2 + \frac{1}{2} k x^2$|$E_m = \frac{1}{2} L \dot{q}^2 + \frac{1}{2} \frac{1}{C} q^2$|
|Amortissement|$\frac{dE_m}{dt} = -\lambda \dot{x}^2$|$\frac{dE_m}{dt} = -R \dot{q}^2$|
|Pulsation propre|$\omega_0 = \sqrt{\frac{k}{m}}$|$\omega_0 = \frac{1}{\sqrt{LC}}$|

| Variables (Mécanique) | Variables (Électronique) |
|---|---|
|Élongation $x$|Charge $q$|
|Vitesse $\dot{x}$|Courant $i = \dot{q}$|
|Masse $m$|Inductance $L$|
|Raideur $k$|Capacité $C$|
|Frottement visqueux $\lambda$|Résistance $R$|
|Energie cinétique $\frac{1}{2} m \dot{x}^2$|Énergie magnétique $\frac{1}{2} L i^2$|
|Energie potentielle $\frac{1}{2} k x^2$|Énergie électrique $\frac{1}{2} \frac{1}{C} q^2$|

**Diapo 30 : Oscillations forcées**

On considère un oscillateur harmonique soumis à une force extérieure périodique de la forme $F(t) = F_0 \cos(\omega t)$. On appelle $\omega$ la pulsation de la force extérieure, et cette force est souvent appelée *force excitatrice*.

L'équation différentielle régissant le mouvement de l'oscillateur forcé est alors :
$$m\ddot{x} = \underbrace{-\lambda \dot{x}}_{\text{amortissement}} - \underbrace{kx}_{\text{élongation}} + \underbrace{f(t)}_{\text{force excitatrice}}$$

On peut la réécrire sous la forme canonique suivante :
$$\ddot{x} + 2\xi \dot{x} + \omega_0^2 x = \frac{f(t)}{m}$$
où $\xi = \frac{\lambda}{2m}$ est le coefficient d'amortissement et $\omega_0 = \sqrt{\frac{k}{m}}$ est la pulsation propre de l'oscillateur.

On a : $f(t)=\begin{cases} \sum_n a_n \cos(n\omega t + \phi_n) & \text{(décomposition en série de Fourier)} \\ \int f(t)e^{i2\pi \frac{n}{T} t}dt\end{cases}$
<!-- $$\boxed{b\cos, B(r,e^{\alpha d})>ke^{\gamma}}$$ -->

La solution générale de cette équation différentielle est la somme de la solution générale de l'équation homogène associée (oscillateur amorti) et d'une solution particulière de l'équation complète (oscillateur forcé).
$$x(t) = x_h(t) + x_p(t)$$

La solution homogène $x_h(t)$ est donnée par les expressions déjà vues pour l'oscillateur amorti, tandis que la solution particulière $x_p(t)$ dépend de la forme de la force excitatrice $f(t)$.

Pour trouver la solution particulière telle que $x_p(t) = X \cos(\omega t + \varphi)$, on injecte cette forme dans l'équation différentielle complète et on résout pour $X$ et $\varphi$. La représentation complexe de $x_p(t)$ est souvent utilisée pour simplifier les calculs. On a : $x=Xe^{j(\omega t + \varphi)}=Xe^{j\varphi}e^{j\omega t}=X'e^{j\omega t}$ avec $X' = Xe^{j\varphi}$.

*Il est clair que $j=i$ (avec $i$ l'unité complexe) dans ce contexte (comme dans la programmation en Python, et d'autres domaines scientifiques).*

En injectant cette forme dans l'équation différentielle, on obtient :
$$(-\omega^2 + 2j\xi\omega + \omega_0^2)X'e^{j\omega t} = \frac{F_0}{m} e^{j\omega t}$$
En simplifiant par $e^{j\omega t}$, on trouve :
$$X' = \frac{F_0/m}{\omega_0^2 - \omega^2 + 2j\xi\omega}$$
On sait que $X' = Xe^{j\varphi}$, donc :
$$Xe^{j\varphi} = \frac{F_0/m}{\omega_0^2 - \omega^2 + 2j\xi\omega}$$
On peut alors déterminer l'amplitude $X$ et la phase $\varphi$ de la solution particulière :
$$X = \frac{F_0/m}{\sqrt{(\omega_0^2 - \omega^2)^2 + (2\xi\omega)^2}}$$
$$\varphi = \arctan\left(\frac{-2\xi}{\omega_0^2 - \omega^2}\right)$$