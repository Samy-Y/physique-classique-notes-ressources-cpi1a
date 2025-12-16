Parfait ! Passons à la formalisation mathématique. On va garder l'analogie de la voiture mais avec un cas concret et calculable.

## Contexte et Notation

Soit :
- $\mathcal{R}(O, \vec{i}, \vec{j}, \vec{k})$ : Référentiel fixe (le bord de la route)
- $\mathcal{R}'(O', \vec{i}', \vec{j}', \vec{k}')$ : Référentiel mobile (la voiture)
- $M$ : Le point matériel (notre mouche)

### 1. Position et Mouvement d'Entraînement

Définissons d'abord le mouvement de la voiture ($\mathcal{R}'$) par rapport à la route ($\mathcal{R}$) :

**Position de $O'$ dans $\mathcal{R}$** : $\vec{OO'} = x_{O'}(t)\vec{i} + y_{O'}(t)\vec{j}$

**Rotation de $\mathcal{R}'$ par rapport à $\mathcal{R}$** : Soit $\theta(t)$ l'angle entre les axes $\vec{i}$ et $\vec{i}'$. La vitesse angulaire est $\vec{\omega} = \dot{\theta} \vec{k}$

**Vecteurs de base** : La relation entre les bases est :
$\vec{i}' = \cos\theta\vec{i} + \sin\theta\vec{j}$
$\vec{j}' = -\sin\theta\vec{i} + \cos\theta\vec{j}$

### 2. Composition des Vitesses (Démonstration)

La position absolue de $M$ s'écrit de deux façons :
$\vec{OM} = \vec{OO'} + \vec{O'M}$

Dérivons par rapport au temps **dans le référentiel fixe $\mathcal{R}$** :

$\left(\frac{d\vec{OM}}{dt}\right)_{\mathcal{R}} = \left(\frac{d\vec{OO'}}{dt}\right)_{\mathcal{R}} + \left(\frac{d\vec{O'M}}{dt}\right)_{\mathcal{R}}$

Le premier terme est simplement la vitesse de $O'$ dans $\mathcal{R}$ : $\vec{v}_{O'/\mathcal{R}}$

Pour le second terme, utilisons la **formule de dérivation vectorielle dans un référentiel tournant** :

$\left(\frac{d\vec{O'M}}{dt}\right)_{\mathcal{R}} = \left(\frac{d\vec{O'M}}{dt}\right)_{\mathcal{R}'} + \vec{\omega} \wedge \vec{O'M}$

Reconnaissons :
- $\left(\frac{d\vec{O'M}}{dt}\right)_{\mathcal{R}'} = \vec{v}_{M/\mathcal{R}'}$ : vitesse relative
- $\vec{\omega} \wedge \vec{O'M}$ : contribution de la rotation

Ainsi : $\vec{v}_{M/\mathcal{R}} = \vec{v}_{O'/\mathcal{R}} + \vec{\omega} \wedge \vec{O'M} + \vec{v}_{M/\mathcal{R}'}$

On identifie :
- **Vitesse d'entraînement** : $\vec{v}_e = \vec{v}_{O'/\mathcal{R}} + \vec{\omega} \wedge \vec{O'M}$
- **Vitesse relative** : $\vec{v}_r = \vec{v}_{M/\mathcal{R}'}$

**Formule finale** : $\boxed{\vec{v}_{a} = \vec{v}_{e} + \vec{v}_{r}}$

### 3. Composition des Accélérations (Démonstration)

Partons de la composition des vitesses et dérivons à nouveau dans $\mathcal{R}$ :

$\left(\frac{d\vec{v}_{a}}{dt}\right)_{\mathcal{R}} = \left(\frac{d\vec{v}_{e}}{dt}\right)_{\mathcal{R}} + \left(\frac{d\vec{v}_{r}}{dt}\right)_{\mathcal{R}}$

**Premier terme** : Accélération d'entraînement
$\vec{a}_e = \left(\frac{d\vec{v}_{e}}{dt}\right)_{\mathcal{R}} = \left(\frac{d}{dt}[\vec{v}_{O'/\mathcal{R}} + \vec{\omega} \wedge \vec{O'M}]\right)_{\mathcal{R}}$

**Second terme** : Dérivée de la vitesse relative
$\left(\frac{d\vec{v}_{r}}{dt}\right)_{\mathcal{R}} = \left(\frac{d\vec{v}_{r}}{dt}\right)_{\mathcal{R}'} + \vec{\omega} \wedge \vec{v}_{r} = \vec{a}_{r} + \vec{\omega} \wedge \vec{v}_{r}$

En développant complètement le calcul (qui nécessite plusieurs applications de la formule de dérivation vectorielle), on obtient :

**Formule finale** : $\boxed{\vec{a}_{a} = \vec{a}_{e} + \vec{a}_{r} + 2\vec{\omega} \wedge \vec{v}_{r}}$

Avec :
- $\vec{a}_{e} = \vec{a}_{O'/\mathcal{R}} + \frac{d\vec{\omega}}{dt} \wedge \vec{O'M} + \vec{\omega} \wedge (\vec{\omega} \wedge \vec{O'M})$ : accélération d'entraînement
- $2\vec{\omega} \wedge \vec{v}_{r}$ : accélération de Coriolis

### 4. Application Numérique Simple

**Situation** : Une voiture ($\mathcal{R}'$) prend un virage circulaire de rayon $R = 100$ m à la vitesse constante $V = 90$ km/h ($25$ m/s). Une mouche ($M$) se déplace vers l'avant dans la voiture à $2$ m/s.

**Données** :
- Vitesse angulaire de la voiture : $\omega = V/R = 0,25$ rad/s
- $\vec{v}_r = 2\vec{i}'$ (m/s)
- $\vec{O'M} = 0$ (la mouche est sur le volant)

**Calculs** :
- **Vitesse d'entraînement** : $\vec{v}_e = \vec{\omega} \wedge \vec{O'M} = \vec{0}$
- **Vitesse absolue** : $\vec{v}_a = \vec{v}_e + \vec{v}_r = 2\vec{i}'$ m/s

- **Accélération d'entraînement** : $\vec{a}_e = \vec{\omega} \wedge (\vec{\omega} \wedge \vec{O'O}) = -\omega^2 R \vec{n} = -6,25$ m/s²
- **Accélération de Coriolis** : $\vec{a}_c = 2\vec{\omega} \wedge \vec{v}_r = 2 \times 0,25 \times 2 = 1$ m/s² dirigée vers l'extérieur du virage
- **Accélération absolue** : $\vec{a}_a = \vec{a}_e + \vec{a}_c = -6,25 + 1 = -5,25$ m/s²

Cette application montre comment la mouche subit une accélération légèrement différente de celle de la voiture à cause de son mouvement relatif !