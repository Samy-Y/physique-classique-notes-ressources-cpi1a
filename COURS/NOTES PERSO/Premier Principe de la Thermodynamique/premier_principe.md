# Premier principe de la thermodynamique
*Notes personelles - SY0226*

Le principe de la thermodynamique, qu'on appelle aussi le principe des bilans énergétiques ou encore le principe de conservation de l'énergie, nous permet de **faire le lien entre les différentes formes d'énergie**, et de comprendre comment elles se transforment les unes en les autres.

Nous n'allons pas nous intéresser au sens de l'évolution d'un système et à sa réversibilité, mais plutôt aux échanges d'énergie qui ont lieu au sein de ce dernier, et entre le système et son environnement.

En mécanique, le bilan énergétique est donné grâce au théorème de l'énergie mécanique, qui nous permet de lier le travail des forces non-conservatives à la variation de l'énergie mécanique d'un système.

$$\Delta E_m = W_{nc}$$

$$\frac{dE_m}{dt} = P(\vec f_{nc})$$

L'énergie mécanique n'est donc pas conservée en présence de forces non-conservatives. Ce travail, toujours négatif et qui dépend du travail suivi (force non-conservative), correspond à une dissipation d'énergie mécanique. Nous allons maintenant étudier un bilan énergétique plus complet, qui prend en compte d'autres formes d'énergie.

## Étude de l'énergie interne via un exemple

Prenons comme exemple simple un ressort situé dans une enceinte calorifugée, c'est-à-dire sans échange de chaleur avec l'extérieur, et soumis à une force de frottement. Lorsqu'on déplace le ressort est déplacé de sa position d'équilibre, il effectuera des oscillations avant de s'arrêter. L'énergie mécanique du ressort est alors dissipée par les forces de frottement (on considérera uniquement les frottements fluides), et transformée en énergie thermique. L'énergie mécanique de départ est donc **entièrement transférée/restituée** vers l'air.

Il est donc nécessaire de faire un suivi thermodynamique de l'air, et il faut mesurer l'évolution de la température de l'air pour déterminer ce transfert. **L'énergie interne** de l'air va donc évoluer.

On l'appelle **énergie interne** parce qu'elle ne peut pas être observée de manière macroscopique, contrairement à l'énergie mécanique qui peut être observée à travers les mouvements d'un système. L'énergie interne est une énergie microscopique.

En utilisant le modèle des gaz parfaits, on peut exprimer l'évolution de cette énergie interne en fonction de la température de l'air, et ainsi faire le lien entre les différentes formes d'énergie, de la manière suivante :

$$dU = C_v dT$$

avec $C_v$ la capacité thermique à volume constant de l'air, qui est par exemple égale à $C_v = \frac f2 nR$ pour un gaz parfait, avec $f$ le nombre de degrés de liberté du gaz *(voir le chapitre sur la cinétique des gaz parfaits)*.

$$\Delta U = U_2 - U_1 = C_v (T_2 - T_1)$$

Après mesures de température, on trouve que $T_2 > T_1$, ce qui fait que $\Delta U > 0$, et correspond donc à une augmentation de l'énergie interne de l'air. Cette perte d'énergie mécanique se traduit alors par un gain d'énergie interne de l'air, ce qui correspond à une évolution thermodynamique du système, et à une transformation de l'énergie mécanique en énergie thermique.

Et sachant que le système est isolé (aucune énergie additionnelle ne peut entrer ou sortir), l'énergie mécanique du pendule est entièrement transférée vers l'énergie interne de l'air, ce qui correspond à une conservation de l'énergie totale du système. On peut écrire :

$$\underbrace{E_m}_{pendule} + \underbrace{U}_{air} = \text{constante}$$

On va donc définir une nouvelle grandeur énergétique pour un **système fermé et isolé**, donc sans échange de matière et d'énergie avec l'extérieur, qui correspond à la somme de l'énergie mécanique et de l'énergie interne :

$$E_{total} = E_m + U$$

>[!NOTE]Système isolé
> Un système est isolé s'il n'échange ni matière ni énergie avec son environnement. Une surface de contrôle entoure le système, et aucune interaction ne peut la traverser. Elle agit comme une frontière *imperméable*.
>
> Notre système-exemple est donc constitué de deux parties : le pendule et l'air, qui sont tous les deux isolés de l'extérieur, mais qui peuvent échanger de l'énergie entre eux. Le pendule perd de l'énergie mécanique, tandis que l'air gagne de l'énergie interne, mais la somme des deux énergies reste constante.

>[!TIP]Travail des forces non-conservatives
> Le travail des forces non-conservatives $W_{nc}$ comme celui des frottements fluides dans notre exemple, permet de transformer l'énergie mécanique en énergie thermique. C'est pour ça qu'il y a une évolution *thermodynamique*.

### Définition de l'énergie interne d'un système

L'énergie interne du système est définie comme étant la somme de l'énergie cinétique microscopique et de l'énergie potentielle microscopique des particules qui composent le système. Il s'agit aussi d'une **fonction d'état**, ce qui signifie que sa valeur ne dépend que de l'état du système, et pas du chemin suivi pour atteindre cet état.

$$U = E_{cin.\ micro.} + E_{potent.\ micro.}$$

L'énergie potentielle microscopique peut, elle aussi, être décomposée en plusieurs sous énergies potentielles microscopiques, liées par exemple à :

- des interactions entre les molécules, atomes et particules du système
- des termes constants dans le cadre de l'évolution thermodynamique, liés à :
  - des interactions entre les électrons et les noyaux des atomes
  - des interactions entre les électrons eux-mêmes
  - des interactions entre les noyaux eux-mêmes

L'énergie mécanique du système est définie comme étant la somme de l'énergie cinétique macroscopique et de l'énergie potentielle macroscopique (associée à une ou *plusieurs* forces externes) du système.

$$E_m = E_{c,macro} + E_{p,macro}$$

## Énoncé du premier principe

**Le premier principe de la thermodynamique énonce que l'énergie interne d'un système fermé et isolé est conservée et constante.**

Considérons par exemple *l'univers*, défini comme étant un système fermé et isolé, qui contient tous les systèmes physiques. L'énergie totale de l'univers est donc constante, et il n'y a pas d'échange d'énergie avec l'extérieur (parce qu'il n'y a pas d'extérieur).

Une conséquence directe de cette notion d'univers isolé et que l'évolution de l'énergie interne d'un système fermé, situé à l'intérieur de cet univers, peut être étudiée de la manière suivante :

$$\Delta E_{univers} = \Delta \underbrace{E_{système}}_{E_\Sigma} + \Delta E_{environnement} = 0$$

(L'environnement correspond à tout ce qui n'est pas le système étudié, c'est-à-dire à l'univers privé du système $[\mathrm{Univers} - \Sigma]$)

On a donc $\Delta E_\Sigma = - \Delta E_{environnement}$, ce qui signifie que l'évolution de l'énergie interne d'un système est égale à l'opposé de l'évolution de l'énergie de son environnement.

- Si $\Delta E_{\Sigma} > 0$, alors le système gagne de l'énergie interne, et il y a un transfert d'énergie vers le système. **Le système gagne de l'énergie depuis le milieu extérieur.**
- Si $\Delta E_{\Sigma} < 0$, alors le système perd de l'énergie interne, et il y a un transfert d'énergie depuis le système. **Le système cède de l'énergie au milieu extérieur.**

>[!NOTE]Production interne
> Une hypothèse que nous avons réalisé implicitement est que le système ne peut pas produire d'énergie. Mais le système peut être le siège de réactions chimiques et d'autres transformations physiques.
>
> L'influence de cette production interne est détaillée ci-dessous.

Considérons un système $\Sigma$ en évolution. Nous allons étudier sa transformation élémentaire pour une grandeur $X$.

$$X \xrightarrow{\text{transformation élémentaire}} X + \mathrm dX$$

Et on peut définir cette variation élémentaire de la manière suivante :

$$\mathrm d X = \delta X_{éch ~ \leftrightarrow ~ext.} + \delta X_{prod\ int}$$

> Dans le cas, par exemple, de l'eau chauffée grâce à un thermoplongeur (résistance chauffante) dans un système isolé, la variation de l'énergie interne peut déterminée à partir de la puissance électrique fournie $P = R\cdot I^2$.

On peut ensuite étudier la variation de l'énergie du système de la manière suivante :

$$\Delta E_\Sigma = W+Q$$

$W$ et $Q$ sont des **grandeurs algébriques**. Elles sont comptées positivement uniquement si elles sont reçues par le système.

Cela nous permet de conclure sur le premier principe de la thermodynamique, qui énonce que l'énergie interne d'un système fermé et isolé est conservée et constante, et que les variations d'énergie interne d'un système sont dues à des échanges d'énergie avec l'extérieur, sous forme de travail ou de chaleur.

## Transferts d'énergie

### Transfert mécanique

Un transfert mécanique est défini comme étant un transfert d'énergie qui se produit lorsque des forces mécaniques non conservatives agissent sur le système, ce qui peut entraîner une variation de l'énergie mécanique du système. Il résulte donc d'un déplacement macroscopique mesurable (d'un travail de forces extérieures).

### Transfert thermique

Un transfert thermique apparaît lorsque la paroi délimitant le système n'est pas calorifugée et qu'elle est perméable à la chaleur. Il y a alors un échange de chaleur entre le système et son environnement, ce qui peut entraîner une variation de l'énergie interne du système.

Ces échanges de chaleur peuvent être causés par des différences de température entre le système et son environnement, ou par des processus de conduction, de convection ou de rayonnement thermique.

- **La conduction thermique** se produit lorsque la chaleur est transférée à travers un matériau solide, sans mouvement de matière. Par exemple, lorsqu'on touche une surface chaude, la chaleur est transférée de la surface à notre main par conduction.
  - Lorsque la paroi du système est *diathermane*, perméable à la chaleur, il y a contact thermique avec l'extérieur.
  - Lorsque la paroi du système est *athermane*, imperméable à la chaleur, il n'y a pas de contact thermique avec l'extérieur. Dans le cas idéal, on considère que la paroi est calorifugée, c'est-à-dire qu'elle est parfaitement isolante, et qu'il n'y a pas d'échange de chaleur avec l'extérieur. Le système est aussi dit **adiabatique**.

- **La convection thermique** est un transport d'énergie dû à un déplacement de matière. On peut distinguer deux types de convections : une convection *naturelle*, qui est causée par des différences de densité dans un fluide, et une convection *forcée*, qui est causée par une action mécanique externe, comme un ventilateur ou une pompe.

<img src="./convection_naturelle.jpg" alt="Convection naturelle" width="400">

*Un exemple de convection naturelle via système de chauffage*

<img src="./convection_forcee.jpg" alt="Convection forcée" width="400">

*Un exemple de convection forcée via ventilateur*

- **Le rayonnement thermique** est un transfert d'énergie qui se produit par l'émission de rayonnements électromagnétiques, comme la lumière ou les ondes radio. **Tous les corps émettent du rayonnement thermique en fonction de leur température**, et ce rayonnement peut être absorbé par d'autres corps, ce qui entraîne un transfert d'énergie.

>[!NOTE]Analogie thermo-électrique de la conduction
> On peut faire une analogie entre les transferts thermiques et les transferts électriques. Par exemple, considérons une résistance traversée par un courant $i$. Quand $R \to 0$, le courant $i$ devient très grand, ce qui correspond à une situation de court-circuit. $i \nearrow$.
> 
> De la même manière, lorsqu'une paroi est très conductrice, elle permet un transfert de chaleur important, ce qui correspond à une situation de contact thermique parfait $Q \nearrow$.
>
> Inversement, lorsqu'une paroi est très isolante, elle empêche le transfert de chaleur, ce qui correspond à une situation d'adiabatisme parfait $Q \searrow$. Elle correspond électriquement à un circuit où $R \to \infty$, ce qui empêche le passage du courant. $i \searrow$.

<img src="./analogie_thermo_elec.svg" alt="Analogie thermo-électrique" width="400">

*Schéma récapitulatif de l'analogie thermo-électrique*

## Transformation adiabatique

Une transformation adiabatique est une transformation dans laquelle il n'y a pas d'échange de chaleur entre le système et son environnement. Cela signifie que la paroi du système est parfaitement isolante, et qu'il n'y a pas de contact thermique avec l'extérieur.

- **Pour des transformations rapides**, il n'y a pas le temps pour que la chaleur soit transférée, ce qui correspond à une situation d'adiabatisme quasi-parfait. On admettra très souvent que les transformations rapides sont adiabatiques.

>[!TIP]Temps caractéristique
> Pour une transformation rapide, le système n'a pas "le temps" de transférer de la chaleur, ce qui correspond à une situation d'adiabatisme quasi-parfait. Cela signifie qu'il y a un temps caractéristique de transfert de chaleur, qui est lié à la nature du système et à sa configuration. Si la transformation se déroule sur une durée beaucoup plus courte que ce temps caractéristique, alors on peut considérer que la transformation est adiabatique.

>[!IMPORTANT]Confusion transformation adiabatique/isotherme 
> Une transformation isotherme est une transformation dans laquelle la température du système reste constante. Le système peut échanger de l'énergie avec l'extérieur, mais il doit compenser cette énergie par un transfert de chaleur pour maintenir sa température constante.
> 
> Si $Q=0$, alors le système est isolé thermiquement. En revanche, si $Q \ne 0$, alors le système échange de la chaleur avec l'extérieur pour maintenir sa température constante. Le milieu extérieur agit comme un thermostat ou un réservoir thermique/de chaleur, et on peut le considérer comme un système à capacité thermique infinie.
> 
> En revanche, une transformation adiabatique peut entraîner une variation de la température du système, et donc de son énergie interne, même s'il n'y a pas d'échange de chaleur avec l'extérieur ($Q=0$).

## Travail des forces de pression

Prenons l'exemple du travail d'une force exercée par un piston. Nous allons négliger la masse du piston.

L'expression de la force exercée par le piston est donnée par :

$$\vec F_p = -P_{ext} S \vec u_z$$

Si le déplacement élémentaire du piston est :

$$d\vec l = dz \vec u_z$$

Alors le travail élémentaire de cette force est donné par : 
$$\delta W_p = \vec F_p \cdot d\vec l = -P_{ext} S dz$$

$$\delta W_p = -P_{ext} dV$$

### Dans le cas d'une transformation monobare

Et le travail total de cette force est donné par :

$$W_p = - \int_{V_1}^{V_2} P_{ext} dV = -P_{ext} \int_{V_1}^{V_2} dV$$

$$W_p = -P_{ext} \Delta V$$

On a donc déduit l'expression non-élémentaire du travail d'une force de pression dans le cas d'une transformation monobare, c'est-à-dire lorsque la pression extérieure $P_{ext}$ est constante.

### Dans le cas d'une transformation quasi-statique

La pression extérieure $P_{ext}$ est alors égale à la pression intérieure $P_{int}=P$ (en constant équilibre avec l'extérieur). L'expression du travail de la force de pression devient alors :

$$W_p = - \int_{V_1}^{V_2} P dV$$

Évidemment, les transformations réelles ne sont pas quasi-statiques, mais comme on effectue le bilan d'énergie entre les états initial et final, on peut faire l'hypothèse que le travail de la force de pression est égal à celui d'une transformation quasi-statique, ce qui nous permet d'utiliser l'expression ci-dessus pour calculer le travail de la force de pression dans une transformation réelle.

L'état du système lors de la transformation réelle à un instant $t$ peut être différent de l'état hypothétique que nous utilisons pour déterminer le bilan énergétique, mais cela n'affecte pas le résultat final du bilan énergétique, qui est basé sur les états initial et final du système. **On peut faire l'hypothèse que le système évolue sur un trajet idéal**

### Diagramme de Clapeyron (P-V)

On peut représenter graphiquement le travail de la force de pression dans un diagramme de Clapeyron, qui est un diagramme représentant la pression $P$ en fonction du volume $V$ du système.

<img src="./diagramme_claperyron.svg" alt="Diagramme de Clapeyron" width="400">

Certains systèmes peuvent décrire des cycles, c'est-à-dire que le système revient à son état initial après une série de transformations.

Dans ce cas, le travail total de la force de pression sur un cycle est donné par l'aire entourée par la courbe dans le diagramme de Clapeyron.

Si le cycle est parcouru dans le sens anti-horaire, alors le travail est positif, ce qui correspond à un gain d'énergie pour le système. On dit que c'est un **cycle récepteur**.

Si le cycle est parcouru dans le sens horaire, alors le travail est négatif, ce qui correspond à une perte d'énergie pour le système. Par exemple, dans un moteur thermique, le cycle est parcouru dans le sens horaire, ce qui correspond à une perte d'énergie pour le système, qui est convertie en travail mécanique (**cycle moteur**).

<img src="./cycles_moteurs_recepteurs.jpg" alt="Cycles moteurs et récepteurs">


$$W = \oint P dV$$

- Lors d'une transformation isochore, le volume du système reste constant ($V_1 = V_2$), ce qui correspond à une situation où il n'y a pas de travail de la force de pression, puisque $dV=0$. On a donc $W=0$.
- Lors d'une transformation monobare, la pression extérieure est constante, ce qui correspond à une situation où le travail de la force de pression est donné par $W = -P_{ext} \Delta V$.
- Lors d'une transformation isobare, la pression intérieure est constante, ce qui correspond à une situation où le travail de la force de pression est donné par $W = -P \Delta V$.
- Lors d'une transformation polytropique ($PV^k = \text{constante}$)...
  - Pour une transformation isobare, on prend $k=0$, ce qui correspond à une situation où le travail de la force de pression est donné par $W = -P \Delta V$.
  - Pour une transformation isotherme, on prend $k=1$, ce qui correspond à une situation où le travail de la force de pression est donné par $W = -nRT \ln\left(\frac{V_2}{V_1}\right)$.
    - Si $V_2 > V_1$, alors $W < 0$, ce qui correspond à une situation où le système perd de l'énergie, et où il y a un transfert d'énergie depuis le système vers l'extérieur.
    - Si $V_2 < V_1$, alors $W > 0$, ce qui correspond à une situation où le système gagne de l'énergie, et où il y a un transfert d'énergie depuis l'extérieur vers le système.
  - Si on prend $k\ne1$, on trouve $W = \frac{P_2 V_2 - P_1 V_1}{k-1}$. **La température peut varier**, mais on peut l'inclure dans cette expression à partir de l'équation d'état des gaz parfaits $PV^k=\text{constante}$.
    - Lors d'une compression polytropique, le travail de la force de pression est positif, et la température du système augmente. Lors d'une détente polytropique, le travail de la force de pression est négatif, et la température du système diminue. Ceci n'est valable que si un thermostat n'est pas présent pour maintenir la température constante.
    - L'expression du travail en fonction de la température est donnée par $W = \frac{nR(T_2 - T_1)}{k-1}$.
  - Pour une transformation isochore, on prend $k \to \infty$, ce qui correspond à une situation où le travail de la force de pression est donné par $W = 0$.

>[!NOTE]Démonstration rapide de l'expression de l'expression du travail pour une transformation polytropique
> Pour $k \ne 1$, on a $W = -\alpha \int_{V_1}^{V_2} V^{-k} dV$, ce qui correspond à $W = -\alpha\left[\frac{V^{1-k}}{1-k}\right]_{V_1}^{V_2} = \frac{P_2 V_2 - P_1 V_1}{k-1}$.

>[!IMPORTANT]Nature de k
> $k$ n'est pas forcément un entier. C'est un réel positif quelconque. Il est aussi appelé **coefficient de Laplace**. Il s'agit d'une caractéristique du gaz étudié.

<img src="trans_isobare_diag.svg" alt="Transformation isobare dans un diagramme de Clapeyron" width="400">

*Schéma d'une transformation isobare dans un diagramme de Clapeyron*

<img src="./trans_isochore_diag.svg" alt="Transformation isochore dans un diagramme de Clapeyron" width="400">

*Schéma d'une transformation isochore dans un diagramme de Clapeyron*

On peut ensuite réutiliser l'expression donnée de l'évolution de l'énergie interne du système pour faire le lien entre les différentes formes d'énergie, de la manière suivante :

$$\underbrace{\mathrm dU}_{\text{différentielle exacte}} = \underbrace{\delta W + \delta Q}_{\text{différentielles inexactes}}$$

> On peut utiliser la différentielle exacte de l'énergie interne pour faire le lien entre les différentes formes d'énergie à partir de leurs différentielles inexactes **parce que celle-ci ne dépend pas de la nature du processus de transformation**.

**Nous allons maintenant exprimer $Q$, la quantité de chaleur transférée, à partir de $\Delta U$ et $W$, lors d'une transformation <u>polytropique</u>** (nous allons nous contenter de différences $\Delta$ et non pas de différentielles $\rm d$)

**Dans le cas d'un gaz parfait <u>monoatomique</u>**

D'après l'expression de l'énergie interne d'un gaz parfait vue dans le chapitre de la cinétique des gaz parfaits, on a $U = \frac{3}{2} nRT$. On trouve donc $\Delta U = \frac{3}{2} nR \Delta T = \frac32 nR \left[T_2 - T_1\right]$.

Et comme l'expression du travail de la force de pression pour une transformation polytropique est donnée par $W = \frac{nR(T_2 - T_1)}{k-1}$, on trouve que la quantité de chaleur transférée est donnée par :

$$Q = \Delta U - W = \frac{3}{2} nR (T_2 - T_1) - \frac{nR(T_2 - T_1)}{k-1}$$

$$\boxed{Q = nR \left[\frac32 - \frac{1}{k-1}\right] (T_2 - T_1)}$$

**Dans le cas d'un gaz parfait général**

L'énergie interne d'un gaz parfait général est donnée par $U = C_{v,m} nRT$, ce qui correspond à $\Delta U = C_{v,m} nR \Delta T = C_{v,m} nR (T_2 - T_1)$.

On trouve l'expression de $Q$ suivante :

$$\boxed{Q = n(C_{v,m} - \frac{R}{k-1}) (T_2 - T_1)}$$

**Dans le cas d'une transformation adiabatique, on trouve que :**

$$Q = 0 \iff C_{v,m} = \frac{R}{k-1} \iff k = \frac{C_{v,m}}{C_{v,m} - R}$$

## Enthalpie d'un système

L'enthalpie d'un système est une grandeur énergétique qui correspond à la somme de l'énergie interne du système et du produit de sa pression par son volume :

$$H = U + PV$$

L'enthalpie est une fonction d'état, ce qui signifie que sa valeur ne dépend que de l'état du système, et pas du chemin suivi pour atteindre cet état. Sa différentielle $dH$ est totale exacte, donc sur un cycle, on trouve que $\oint dH = 0$ ou $\Delta H = 0$.

On peut aussi définir l'enthalpie molaire $H_m$ d'un système, qui correspond à l'enthalpie par mole de substance, ainsi que l'enthalpie massique $H_s$ d'un système, qui correspond à l'enthalpie par unité de masse de substance :

$$H_m = \frac{H}{n}$$

$$H_s = \frac{H}{m}$$

> On peut effectuer une [transformation de Legendre](https://fr.wikipedia.org/wiki/Transformation_de_Legendre#Thermodynamique) pour faire le lien entre l'enthalpie et l'énergie interne, mais c'est hors de portée du cours.

$$U(T,V) \xrightarrow{\text{transfo. de Legendre}} H(T,P)$$

L'enthalpie représente un [potentiel thermodynamique](https://fr.wikipedia.org/wiki/Potentiel_thermodynamique), c'est-à-dire qu'elle permet de prédire l'évolution et l'équilibre d'un système thermodynamique, en fonction de ses variables d'état. Elle synthétise en une seule fonction l'énergie interne $U$ du système et le travail de frontière (lié à sa pression) $PV$, qui est l'énergie mécanique "de surface" échangée à la limite d'un système fermé lors d'une déformation (comme dans un piston).

On peut définir la **capacité thermique à pression constante** $C_p$ et la **capacité thermique à volume constant** $C_v$ de la manière suivante (en nous limitant à la variable d'état $T$) :

$$C_p = \left(\frac{\partial H}{\partial T}\right)_P$$

$$C_v = \left(\frac{\partial U}{\partial T}\right)_V$$

> La capacité thermique à volume constant a déjà été abordée dans le chapitre de la cinétique des gaz parfaits, et elle est donnée par $C_v = \left(\frac{\partial U}{\partial T}\right)_V$ pour un gaz parfait.

On peut aussi définir les capacités thermiques molaires à pression constante $C_{p,m}$ et à volume constant $C_{v,m}$ de la manière suivante :

$$C_p = \left(\frac{\partial H}{\partial T}\right)_P = C_{p,m} n$$

$$C_v = \left(\frac{\partial U}{\partial T}\right)_V = C_{v,m} n$$

On peut écrire la variation de l'énergie interne $U$ en fonction de la température $T$ de la manière suivante :

$$\Delta U = n C_{v,m} \Delta T$$

Le travail effectué par les forces de pression lors d'une quasi-statique quelconque est donné par $W = -\int P dV$.

Comme $\Delta U = Q + W$, on trouve que la quantité de chaleur transférée est donnée par :

$$Q = \Delta U - W = n C_{v,m} \Delta T + \int P dV$$

> Techniquement, la formule ci-dessus n'a pas été explicitée en cours... Mais l'auteur (moi) préfère l'utiliser parce qu'elle est plus générale. On peut ensuite dériver plusieurs formules à partir de celle-ci, en fonction du type de la transformation étudiée. **C'est beaucoup plus naturel :)**

On rappelle que l'expression de l'enthalpie est donnée par $H = U + PV$. On peut donc en déduire l'expression de la variation de l'enthalpie, qui est :

$$\begin{align*}
\Delta H &= \Delta U + P\Delta V + V\Delta P \\
&= n C_{v,m} \Delta T + P\Delta V + V\Delta P
\end{align*}$$

- Dans le cas d'une transformation isobare, on a $\Delta P = 0$, et donc $\Delta H = n C_{v,m} \Delta T + P\Delta V$.
  - On peut aussi en déduire que $\Delta H = Q_p$, ce qui correspond à une situation où l'énergie apportée sous forme de chaleur est utilisée à la fois pour faire du travail de frontière (lié à la pression) $P\Delta V$, et pour augmenter l'agitation des molécules.
- Dans le cas d'une transformation isochore, on a $\Delta V = 0$, et donc $\Delta H = n C_{v,m} \Delta T + V\Delta P$.
  - On peut aussi en déduire que $\Delta H = Q_v + V\Delta P$, ce qui correspond à une situation où l'énergie apportée sous forme de chaleur est utilisée uniquement pour augmenter l'agitation des molécules, et pour faire du travail de frontière (lié à la pression) $V\Delta P$. **À quantité de chaleur $Q$ égale, l'énergie interne augmente plus en isochore car aucune énergie n'est perdue sous forme de travail.**

>[!NOTE]Plus concrètement...
> À volume constant, toute l'énergie apportée sous forme de chaleur reste dans le système pour augmenter l'agitation des molécules, et donc pour augmenter son énergie interne (uniquement).
> 
> À pression constante, une partie de l'énergie apportée sous forme de chaleur est utilisée pour faire du travail de frontière (lié à la pression) $PV$, et l'autre partie est utilisée pour augmenter l'agitation des molécules, et donc pour augmenter son énergie interne. 
>
> On comprend naturellement que la capacité thermique à pression constante $C_p$ est plus grande que la capacité thermique à volume constant $C_v$, puisque dans le cas d'une transformation isobare, il faut fournir plus d'énergie pour faire à la fois du travail de frontière et pour augmenter l'énergie interne du système, alors que dans le cas d'une transformation isochore, il faut fournir moins d'énergie pour faire uniquement augmenter l'énergie interne du système.

En limitant notre étude thermodynamique au gaz parfaits, on peut lier $H(T)$ et $U(T)$ de la manière suivante :

$$H(T) = U(T) + PV = U(T) + nRT$$

$$\implies \frac{\mathrm dH}{\mathrm dT} = \frac{\mathrm dU}{\mathrm dT} + nR$$

Et, d'après les définitions de $C_p$ et $C_v$, on trouve que :

$$\begin{align*}
C_p &= \left(\frac{\partial H}{\partial T}\right)_P \\
&= \frac{\mathrm dH}{\mathrm dT} \\
&= \frac{\mathrm dU}{\mathrm dT} + nR \\
&= C_v + nR
\end{align*}$$

On en déduit donc que :

$$\underset{\text{Relation de Mayer}}{\boxed{C_p - C_v = nR}}$$

Et en utilisant les définitions des capacités thermiques molaires, on trouve que :

$$\boxed{C_{p,m} - C_{v,m} = R}$$

### Détermination de $C_p$ et $C_v$ pour un gaz parfait monoatomique

On sait que, lors d'une transformation quasi statique, la variation de l'enthalpie est donnée par :

$$\Delta H = \Delta U + P\Delta V + V\Delta P$$

On sait que $\frac{\Delta H}{\Delta T} = C_p$, donc $\Delta H = C_p \Delta T$.

En la réintégrant dans l'expression de $\Delta H$, on trouve que :

$$C_p \Delta T = \Delta U + P\Delta V + V\Delta P$$

On sait que l'énergie interne d'un gaz parfait à $f$ degrés de liberté est donnée par $U = \frac{f}{2} nRT$, ce qui correspond à $\Delta U = \frac{f}{2} nR \Delta T$.

En la réintégrant dans l'expression de $C_p \Delta T$, on trouve que :

$$C_p \Delta T = \frac{f}{2} nR \Delta T + P\Delta V + V\Delta P$$

On factorise par $\Delta T$ pour trouver :

$$\Delta T\left(C_p - \frac{f}{2} nR\right) = P\Delta V + V\Delta P$$

- **Dans le cas d'une transformation isobare,**
  - On a $\Delta P = 0$, et donc $\Delta T\left(C_p - \frac{f}{2} nR\right) = P\Delta V$.
  - En utilisant l'équation d'état des gaz parfaits $PV = nRT$, on trouve que $P\Delta V = nR \Delta T$, ce qui correspond à $\Delta T\left(C_p - \frac{f}{2} nR\right) = nR \Delta T$.
  - En simplifiant par $\Delta T$ (si on le considère non-nul, évidemment...), on trouve que $C_p = \frac{f}{2} nR + nR = (\frac{f}{2}+1) nR$.
  - Et comme $C_v = C_p - nR$, on trouve que $C_v = \frac{f}{2} nR$, on a retrouvé l'expression de $C_v$ pour un gaz parfait à $f$ degrés de liberté, ce qui correspond à **une validation de notre démarche.**
- **Dans le cas d'une transformation isochore,**
  - La démarche suivie est la même et on aboutit aux mêmes résultats.

> Techniquement, on peut même *ne pas distinguer les cas isobares et isochores*. On sait que pour un gaz parfait, $PV = nRT$. Donc $\Delta PV = nR \Delta T$. En réintégrant dans l'expression de $C_p \Delta T$, on retrouve exactement les mêmes résultats.

On en déduit donc les expressions des capacités thermiques molaires à pression constante et à volume constant pour un gaz parfait à $f$ degrés de liberté, qui sont données par :

$$\begin{cases}
C_{p,m} = \left(\frac{f}{2}+1\right) R = \dfrac{C_p}n\\
C_{v,m} = \frac{f}{2} R = \dfrac{C_v}n
\end{cases}$$

Ensuite, on peut en déduire l'expression du coefficient de Laplace $k$, qu'on notera par la suite $\gamma$, qui est donnée par :

$$\begin{align*}
\gamma = k &= \frac{C_{p,m}}{C_{v,m}} \\
&= \frac{\frac52 R}{\frac32 R} \\
&= \frac52 \cdot \frac23 \\
&= \frac53\\
\implies \gamma &\approx 1.67
\end{align*}$$

Lors d'une **transformation isochore**, le volume est constant ($\mathrm dV = 0$), donc le travail des forces de pression est nul ($\delta W = 0$).
* La chaleur échangée est égale à la variation d'énergie interne : $Q_v = \Delta U = n C_{v,m} \Delta T$ (sachant que $C_{v,m} = \frac1n \left(\frac{\partial U}{\partial T}\right)_V$).
* La variation d'enthalpie reste calculable par $\Delta H = n C_{p,m} \Delta T$ (car pour un GP, $H$ ne dépend que de $T$).

Le tableau ci-dessous résume les valeurs des capacités thermiques et du coefficient de Laplace $\gamma$ :

| Type de Gaz | $C_{v,m}$ | $C_{p,m} = C_{v,m} + R$ | $\gamma = \frac{C_p}{C_v}$ |
| :--- | :--- | :--- | :--- |
| **Monoatomique** (He, Ar...) | $\frac{3}{2}R$ | $\frac{5}{2}R$ | $5/3 \approx 1,67$ |
| **Diatomique** ($O_2, N_2, \text{Air}$...) | $\frac{5}{2}R$ | $\frac{7}{2}R$ | $7/5 = 1,4$ |



## Pour résumer...

- **Premier principe de la thermodynamique :** l'énergie interne d'un système fermé et isolé est conservée et constante, et les variations d'énergie interne d'un système sont dues à des échanges d'énergie avec l'extérieur, sous forme de travail ou de chaleur.
  - On a défini un système fermé et isolé, qui correspond à un système qui n'échange ni matière ni énergie avec son environnement. L'énergie totale d'un tel système est donc constante.
  - Cette énergie totale peut être exprimée à partir de l'énergie mécanique du système $E_m$ et de son énergie interne $U$, de la manière suivante : $E_{total} = E_m + U$.
  - Le premier principe de la thermodynamique énonce que l'énergie interne d'un système fermé et isolé est conservée et constante, et que les variations d'énergie interne d'un système sont dues à des échanges d'énergie avec l'extérieur, sous forme de travail ou de chaleur. On écrit donc $\Delta U = W + Q$, où $W$ et $Q$ sont des grandeurs algébriques, comptées positivement uniquement si elles sont reçues par le système.
  - On a défini les transferts d'énergie mécanique et thermique, qui correspondent respectivement à des forces mécaniques non conservatives agissant sur le système, et à des échanges de chaleur entre le système et son environnement.
    - Un transfert thermique peut se produire par conduction, convection ou rayonnement thermique.
  - On a défini une transformation adiabatique comme étant une transformation dans laquelle il n'y a pas d'échange de chaleur entre le système et son environnement, ce qui correspond à une situation où la paroi du système est parfaitement isolante, et où il n'y a pas de contact thermique avec l'extérieur.
  - On a rappelé la transformation quasi-statique, qui correspond à une transformation dans laquelle le système évolue de manière suffisamment lente pour que les variables d'état du système soient définies à tout instant, et pour que le système soit en équilibre avec son environnement à tout instant.
  - On a défini le travail des forces de pression, qui correspond à l'énergie mécanique échangée à la limite d'un système fermé lors d'une déformation, comme dans un piston. Son expression est donnée par $W = -\int P dV$ pour une transformation quasi-statique.
    - On a aussi défini le diagramme de Clapeyron, qui est un diagramme représentant la pression $P$ en fonction du volume $V$ du système, et qui permet de représenter graphiquement les transformations d'un système, ainsi que les cycles qu'il peut décrire.
    - On a retrouvé les expressions du travail de la force de pression pour les différentes transformations étudiées, comme les transformations isobares, isochores, polytropiques, etc.
    - On a trouvé que :
      - Lors d'une transformation isochore, le travail de la force de pression est nul, puisque $dV=0$.
      - Lors d'une transformation monobare, le travail de la force de pression est donné par $W = -P_{ext} \Delta V$.
      - Lors d'une transformation isobare, le travail de la force de pression est donné par $W = -P \Delta V$.
      - Lors d'une transformation polytropique ($PV^k = \text{constante}$), le travail de la force de pression est donné par $W = \frac{P_2 V_2 - P_1 V_1}{k-1}$, ou $W = \frac{nR(T_2 - T_1)}{k-1}$.
- On a défini **l'enthalpie d'un système**, qui correspond à la somme de l'énergie interne du système et du produit de sa pression par son volume : $H = U + PV$. L'enthalpie est une fonction d'état, ce qui signifie que sa valeur ne dépend que de l'état du système, et pas du chemin suivi pour atteindre cet état. Sa différentielle $dH$ est totale exacte, donc sur un cycle, on trouve que $\oint dH = 0$ ou $\Delta H = 0$.
- On a aussi défini les capacités thermiques à volume constant $C_v$ et à pression constante $C_p$, qui correspondent respectivement à la variation de l'énergie interne et de l'enthalpie du système en fonction de la température : $C_v = \left(\frac{\partial U}{\partial T}\right)_V$ et $C_p = \left(\frac{\partial H}{\partial T}\right)_P$.
  - On a aussi défini les capacités thermiques molaires à volume constant $C_{v,m}$ et à pression constante $C_{p,m}$, qui correspondent respectivement à la variation de l'énergie interne et de l'enthalpie du système en fonction de la température, par mole : $C_{v,m} = \frac{C_v}{n}$ et $C_{p,m} = \frac{C_p}{n}$.
  - On a trouvé que $C_p - C_v = nR$, ce qui correspond à la relation de Mayer, et que $C_{p,m} - C_{v,m} = R$.
  - On a aussi retrouvé les expressions de $C_p$ et $C_v$ pour un gaz parfait à $f$ degrés de liberté, qui sont données par $C_p = (\frac{f}{2}+1) nR$ et $C_v = \frac{f}{2} nR$, ce qui correspond à des capacités thermiques molaires à pression constante et à volume constant de $C_{p,m} = (\frac{f}{2}+1) R$ et $C_{v,m} = \frac{f}{2} R$. On a aussi trouvé que le coefficient de Laplace $\gamma$ est donné par $\gamma = \frac{C_{p,m}}{C_{v,m}}$.

## Récapitulatif (cours)

**Enthalpie :** $H = U + PV$

**Capacité thermique à pression constante :** $C_p = \left(\frac{\partial H}{\partial T}\right)_P$

**Capacité thermique à volume constant :** $C_v = \left(\frac{\partial U}{\partial T}\right)_V$

Dans le cas d'un gaz parfait : $C_p - C_v = nR$ (relation de Mayer)

**Identités de Joule :** $\mathrm d U = C_v \mathrm dT$ et $\mathrm dH = C_p \mathrm dT$ pour un gaz parfait

**Dans le cas d'une transformation isotherme :** $\Delta U = 0$ et $\Delta H = 0$ pour un gaz parfait.

**Dans le cas d'une transformation quelconque :** $\Delta U = C_v(T_2 - T_1)$ et $\Delta H = C_p (T_2 - T_1)$ pour un gaz parfait.

**Premier principe de la thermodynamique :** $\mathrm dU = \delta W + \delta Q$ (différentielle exacte pour $U$, différentielle inexacte pour $W$ et $Q$)

$U$ est une fonction d'état, donc :

$$\mathrm dU = \delta W + \delta Q = \delta Q_{réelle} + \delta W_{réelle} = \delta Q_{réversible} + \delta W_{réversible}$$

Dans le cas où seule la pression intervient dans le travail de frontière, on trouve que :

$$\delta W_{réversible} = -P dV$$

$$\delta W = -P_{ext} dV$$

$$\implies \underset{\text{Identité importante}}{\boxed{\mathrm dU = -P\mathrm dV + \delta Q_{réversible}}}\\=-P_{ext} \mathrm dV + \delta Q_{réelle}$$

$$\implies dH = dU +P dV = -P dV + \delta Q_{réversible} + P dV = \delta Q_{réversible}$$

## Calorimétrie

La calorimétrie est l'ensemble des techniquement permettant de mesurer les transferts thermiques, c'est-à-dire les échanges de chaleur entre un système et son environnement.

On utilise généralement un calorimètre, qui est un dispositif permettant de mesurer les transferts thermiques. Il est composé d'une **paroi imperméable** à la chaleur, d'un **agitateur**, d'un **thermomètre** et d'un **vase/récipient**, ainsi que tout autre dispositif nécessaire pour réaliser l'expérience.

On doit tenir compte de la capacité calorifique $\Gamma$ du calorimètre (tous composants inclus). Il diffère évidemment d'un calorimètre à l'autre. Pour le mesurer, on étudie généralement son "équivalence" par rapport à une masse d'eau, qui a une capacité calorifique massique de $c_e = 4,18 \text{ kJ/(kg}\cdot\text{K)}$.

$$\underbrace{\mu = \frac{\Gamma}{c_e}}_{\text{équivalence du calorimètre }\mu}$$

$\mu$ est aussi appelée la "masse d'eau équivalente" du calorimètre, et elle correspond à la masse d'eau qui aurait la même capacité calorifique que le calorimètre.

**La mesure de $\mu$ :** Pour déterminer $\mu$ expérimentalement, on réalisé l'expérience suivante :

- On prépare une masse d'eau $m$ à une température $T_2$.
- Le calorimètre est initialement à une température $T_1 < T_2$.

Le système $\Sigma = \{m+\mu\}$ est isolé thermiquement, et on mesure la température d'équilibre $T_f$ du système.

Comme le système $\Sigma$ est isolé, alors sa variation d'enthalpie $\Delta H_\Sigma$ est nulle, ce qui correspond à une situation où la chaleur perdue par l'eau est égale à la chaleur gagnée par le calorimètre :

$$\Delta H_\Sigma = \Delta H_m + \Delta H_\mu = 0$$

$$\begin{cases}
\Delta H_m = \Gamma(T_f-T_1) = \mu c_e (T_f - T_1)\\
\Delta H_\mu = m c_e (T_f - T_2)
\end{cases}$$

En réintégrant dans l'expression de $\Delta H_\Sigma$, on trouve que :

$$\mu = m \frac{T_2 - T_f}{T_f - T_1}$$

<img src="./graph_evol_temp.svg" alt="Graphique de l'évolution de la température du système lors de l'expérience de calorimétrie" width="400">

On peut par exemple chauffer une masse d'eau dans un calorimètre grâce à un thermoplongeur.

La variation d'enthalpie est alors :
$$\Delta H = Q_p = Ri^2\Delta t$$

Et on sait déjà que :
$$\Delta H = (m+\mu)c_e \Delta T$$

On peut donc en déduire une expression de la variation de température :

$$\Delta T = \frac{Ri^2\Delta t}{(m+\mu)c_e}$$

L'évolution de la température $T(t)$ sera donc linéaire (le coefficient $\frac{Ri^2}{(m+\mu)c_e}$ est constant).

À partir de la pente obtenue expérimentalement, et sachant que $m$, $R$ et $i$ sont connus, on peut en déduire la valeur de $\mu$.

<img src="./graph_evol_temp_calorim_mu.svg" alt="Graphique de l'évolution de la température du système lors de l'expérience de calorimétrie pour différentes valeurs de $\mu$" width="400">

Pour une expérience plus rigoureuse, il faut faire varier la résistance utilisée (qui varie avec la chaleur) etc. etc. (hors de portée du cours, physique expérimentale...)

**Application : détermination de la capacité thermique d'un métal.**

> Trivial.

>[!IMPORTANT] Corps à l'état condensé (liquides et solides)
>Ces états-là sont caractérisés par une compressibilité très faible.
>
>Leurs transformations sont donc isobares (et aussi isochores).
>$$\Delta H = \Delta U$$
>$$dH = c\cdot dT = dU$$