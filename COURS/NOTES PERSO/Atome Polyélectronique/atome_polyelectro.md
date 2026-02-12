# Atome polyélectronique

## Rappel sur les notions vues précédemment

La dernière fois, nous avons caractérisé l'état quantique d'un électron dans un atome par :

- le nombre quantique principal $n$ ;
  - qui correspond à l'énergie de l'électron dans l'atome, peut prendre des valeurs entières $n = 1, 2, 3, \ldots$ ;
- le nombre quantique azimutal $l$ ;
  - qui correspond à la forme de l'orbitale, peut prendre des valeurs entières $l = 0, 1, 2, \ldots, n-1$ ;
- le nombre quantique magnétique $m_l$ ;
  - qui correspond à l'orientation spatiale de l'orbitale, peut prendre des valeurs entières $m_l = -l, \ldots, 0, \ldots, +l$ ;
- le nombre quantique de spin $m_s$.
  - qui correspond à l'orientation du spin de l'électron, peut prendre les valeurs $m_s = -\frac{1}{2}, +\frac{1}{2}$.

Un niveau d'énergie dans un atome est donc caractérisé par la valeur de $n$. Chaque niveau d'énergie est divisé en sous-niveaux d'énergie caractérisés par la valeur de $l$. Chaque sous-niveau est lui-même divisé en orbitales caractérisées par la valeur de $m_l$. Enfin, chaque orbitale peut contenir deux électrons de spins opposés caractérisés par la valeur de $m_s$.

La case quantique est donc définie par l'ensemble des quatre nombres quantiques $(n, l, m_l)$, généralement représentée sous la forme d'un carré $\boxed{~\textcolor{white}{!}~}$.

Pour $n=1$, il y a un seul sous-niveau ($l=0$) et une seule orbitale ($m_l=0$) : la case quantique 1s. On dit que l'orbitale est de type s.

Pour $n=2$, il y a deux sous-niveaux ($l=0$ et $l=1$). Le sous-niveau $l=0$ correspond à l'orbitale 2s ($m_l=0$), de type s, et le sous-niveau $l=1$ correspond aux orbitales 2p ($m_l=-1, 0, +1$), de type p.

> Dans ce cours, nous allons considérer l'atome dans son état fondamental, c'est-à-dire lorsque les électrons occupent les niveaux d'énergie les plus bas possibles.

## Répartition des $Z~e^-$ électrons dans les orbitales de l'atome

Considérons un atome de numéro atomique $Z$, c'est-à-dire un atome possédant $Z$ électrons. La répartition des électrons dans les différentes orbitales de l'atome obéit à trois règles principales :

1. **Principe de Pauli** : Deux électrons dans un atome ne peuvent pas avoir les mêmes valeurs pour les quatre nombres quantiques $(n, l, m_l, m_s)$. En d'autres termes, une case quantique peut contenir au maximum deux électrons de spins opposés.
   
   Si une case quantique ne contient qu'un seul électron, on dit qu'elle est "demi-pleine" et que cet électron est "non apparié" ou "célibataire". $\boxed{~\uparrow~}$

   Si elle contient deux électrons, on dit qu'elle est "pleine" et que les électrons sont "appariés" et forment un "doublet" ou une "paire". Leurs spins sont antiparallèles. $\boxed{\uparrow\downarrow}$

   Cela signifie que, pour l'orbitale correspondant à $n=1$ (1s), on peut avoir au maximum deux électrons. Leur configuration sera donc $\boxed{\uparrow\downarrow}$, et $(1,0,0,+\frac{1}{2})$ et $(1,0,0,-\frac{1}{2})$ sont les deux seuls états quantiques possibles pour ces deux électrons.
   
   Pour l'orbitale 2s, on peut également avoir au maximum deux électrons. Pour les trois orbitales 2p ($m_l=-1, 0, +1$), on peut avoir au maximum six électrons (deux par orbitale). Leurs états quantiques possibles sont donc :
   - $\boxed{\uparrow\downarrow}$ pour l'orbitale 2p avec $m_l=-1$ ; on notera $(2,1,-1,+\frac{1}{2})$ et $(2,1,-1,-\frac{1}{2})$ les états quantiques des deux électrons.
   - $\boxed{\uparrow\downarrow}$ pour l'orbitale 2p avec $m_l=0$ ; on notera $(2,1,0,+\frac{1}{2})$ et $(2,1,0,-\frac{1}{2})$ les états quantiques des deux électrons.
   - $\boxed{\uparrow\downarrow}$ pour l'orbitale 2p avec $m_l=+1$ ; on notera $(2,1,+1,+\frac{1}{2})$ et $(2,1,+1,-\frac{1}{2})$ les états quantiques des deux électrons.
   
   On peut aussi représenter la configuration électronique de l'atome en utilisant des diagrammes de cases quantiques, où chaque case représente une orbitale et les flèches représentent les électrons avec leur spin, de la manière suivante :

   $$\begin{array}{|c|c|c|c|c|c|}
   \hline
    \text{1s} & \text{2s} & \text{2p}_{-1} & \text{2p}_0 & \text{2p}_{+1} \\
    \hline
    \uparrow\downarrow & \uparrow\downarrow & \uparrow\downarrow & \uparrow\downarrow & \uparrow\downarrow \\
    \hline
    \end{array}$$

2. **Règle de Hund** : Lors du remplissage des orbitales d'un même sous-niveau (même valeur de $n$ et $l$), les électrons occupent d'abord les orbitales vides avant de se coupler par paires. De plus, les électrons dans des orbitales différentes d'un même sous-niveau ont des spins parallèles (même valeur de $m_s$) autant que possible.

   Par exemple, pour le sous-niveau 2p, si nous avons trois électrons à placer, ils occuperont d'abord les trois orbitales 2p séparément avec des spins parallèles :

   $$\begin{array}{|c|c|c|c|}
   \hline
    \text{2p}_{-1} & \text{2p}_0 & \text{2p}_{+1} \\
    \hline
    \uparrow & \uparrow & \uparrow \\
    \hline
    \end{array}$$

   Ce n'est qu'après que chaque orbitale contient un électron que les électrons commenceront à se coupler par paires. On aura alors :

    $$\begin{array}{|c|c|c|c|}
    \hline
     \text{2p}_{-1} & \text{2p}_0 & \text{2p}_{+1} \\
     \hline
     \uparrow\downarrow & \uparrow\downarrow & \uparrow \\
     \hline
     \end{array}$$
    
   L'exemple ici illustre la configuration électronique de l'atome de Bore (B), qui possède 5 électrons.

   **En résumé :** Il faut "remplir" chaque orbitale d'un sous-niveau avant de commencer à les "doubler"/"apparier".

3. **Ordre de remplissage des orbitales** : Les électrons remplissent les orbitales dans l'ordre croissant de leur énergie. L'ordre de remplissage des orbitales est donné par la règle de Klechkowski (ou règle $n+l$) :

<img src="https://www.terres-du-passe.com/upload/image/Theme/ScienceTetU/Chimie/Partie6/Chimie3-klechkowski.png" >

   Selon cette règle, les orbitales sont remplies dans l'ordre suivant :

   1s → 2s → 2p → 3s → 3p → 4s → 3d → 4p → 5s → 4d → 5p → 6s → 4f → 5d → 6p → 7s → 5f → 6d

   Par exemple, pour un atome avec $Z=10$ (néon, Ne), les électrons seront répartis comme suit :

   - 1s : 2 électrons
   - 2s : 2 électrons
   - 2p : 6 électrons

   La configuration électronique du néon dans son état fondamental est donc : $1s^2\,2s^2\,2p^6$. Les puissances indiquent le nombre d'électrons dans chaque type d'orbitale.

>[!TIP]Configuration électronique d'un ion
> Lorsqu'un atome perd ou gagne des électrons pour former un ion, la configuration électronique de l'ion est obtenue en ajoutant ou en retirant des électrons de la configuration électronique de l'atome neutre. Par exemple, pour l'ion $Na^+$ (sodium), qui a perdu un électron, la configuration électronique est $1s^2\,2s^2\,2p^6$, car le sodium neutre a une configuration électronique de $1s^2\,2s^2\,2p^6\,3s^1$.

>[!NOTE]Configurations électroniques et état excité
> Il faut noter que les configurations électroniques que nous venons de voir ne sont valables que pour les atomes dans leur état fondamental. Pour les atomes excités, les électrons peuvent occuper des orbitales de plus haute énergie, ce qui peut conduire à des configurations électroniques différentes.

## Exceptions à la règle de Klechkowski

Il existe quelques exceptions à la règle de Klechkowski, qui sont principalement dues à des effets de stabilisation liés à la configuration électronique. Ces exceptions concernent principalement les éléments de transition...

Par exemple, pour le chrome (Cr, $Z=24$), la configuration électronique attendue selon la règle de Klechkowski serait $[Ar]\,3d^4\,4s^2$. Cependant, la configuration réelle du chrome est $[Ar]\,3d^5\,4s^1$.

Pour le Palladium (Pd, $Z=46$), la configuration électronique attendue serait $[Kr]\,4d^8\,5s^2$, mais la configuration réelle est $[Kr]\,4d^{10}\,5s^0$.

Enfin, pour le Cuivre (Cu, $Z=29$), la configuration électronique attendue serait $[Ar]\,3d^9\,4s^2$, mais la configuration réelle est $[Ar]\,3d^{10}\,4s^1$.

>[!NOTE]
> $[Ar]$ et $[Kr]$ sont des notations de configuration électronique abrégée, où $[Ar]$ représente la configuration électronique du gaz noble argon ($1s^2\,2s^2\,2p^6$) et $[Kr]$ représente la configuration électronique du gaz noble krypton ($1s^2\,2s^2\,2p^6\,3s^2\,3p^6$).

## Représentation énergétique des orbitales

La représentation énergétique des orbitales d'un atome polyélectronique peut être illustrée à l'aide d'un diagramme où les orbitales sont disposées en fonction de leur énergie croissante. Chaque orbitale est représentée par une ligne horizontale, et les électrons sont indiqués par des flèches (↑ pour un électron de spin +1/2 et ↓ pour un électron de spin -1/2).

Par exemple, pour l'atome d'oxygène (O, $Z=8$), la configuration électronique dans son état fondamental est $1s^2\,2s^2\,2p^4$. Le diagramme énergétique correspondant serait :

<!-- ─ -->

```
      Energie
        ↑
        |                ╖ 	
   2p   |   ↑ ↓   ↑   ↑  ║
        |_________       ║ 6 électrons de valence
   2s   |   ↑ ↓          ║
        |_________       ╜
   1s   |   ↑ ↓
        |_________
        |
```

Pour le Manganèse (Mn, $Z=25$), la configuration électronique dans son état fondamental est $[Ar]\,3d^5\,4s^2$. Le diagramme énergétique correspondant serait :

```
      Energie
        ↑
        |
   4s   |   ↑ ↓
        |_________
   3d   |   ↑   ↑   ↑   ↑   ↑
        |_________
  [Ar]  |   ...
        |
```

## Représentation de Lewis

La représentation de Lewis est une manière simplifiée de représenter la configuration électronique des atomes, en mettant l'accent sur les électrons de valence, c'est-à-dire les électrons situés dans la couche externe de l'atome. Ces électrons sont responsables des liaisons chimiques entre les atomes.

Dans la représentation de Lewis, les électrons de valence sont représentés par des points autour du symbole chimique de l'élément. Chaque point représente un électron de valence, et les paires d'électrons (électrons appariés) sont souvent représentées par des paires de points.

<img src="">

>[!IMPORTANT]Hypervalence
> Certains éléments peuvent avoir plus de huit électrons de valence, ce qui est appelé hypervalence, et ne respecte pas la règle de l'octet. Par exemple, le soufre (S) peut avoir une configuration électronique de valence de $3s^2\,3p^4$, ce qui lui permet d'avoir jusqu'à 12 électrons de valence dans certaines molécules, comme le sulfate ($SO_4^{2-}$).

## Configurations électroniques selon les familles d'éléments

- **Groupe 1 (Alcalins)** : Les éléments du groupe 1 ont une configuration électronique de valence de $ns^1$. Par exemple, le lithium (Li) a une configuration électronique de $1s^2\,2s^1$.
- **Groupe 2 (Alcalino-terreux)** : Les éléments du groupe 2 ont une configuration électronique de valence de $ns^2$. Par exemple, le béryllium (Be) a une configuration électronique de $1s^2\,2s^2$.
- **Groupes 3 à 12 (Métaux de transition)** : Les éléments de ces groupes ont des configurations électroniques de valence qui impliquent les orbitales d. Par exemple, le fer (Fe) a une configuration électronique de $[Ar]\,3d^6\,4s^2$.
- **Groupe 13 (Boreux)** : Les éléments du groupe 13 ont une configuration électronique de valence de $ns^2\,np^1$. Par exemple, le bore (B) a une configuration électronique de $1s^2\,2s^2\,2p^1$.
- **Groupe 14 (Carboneux)** : Les éléments du groupe 14 ont une configuration électronique de valence de $ns^2\,np^2$. Par exemple, le carbone (C) a une configuration électronique de $1s^2\,2s^2\,2p^2$.
- **Groupe 15 (Azotés)** : Les éléments du groupe 15 ont une configuration électronique de valence de $ns^2\,np^3$. Par exemple, l'azote (N) a une configuration électronique de $1s^2\,2s^2\,2p^3$.
- **Groupe 16 (Chalcogènes)** : Les éléments du groupe 16 ont une configuration électronique de valence de $ns^2\,np^4$. Par exemple, l'oxygène (O) a une configuration électronique de $1s^2\,2s^2\,2p^4$.
- **Groupe 17 (Halogènes)** : Les éléments du groupe 17 ont une configuration électronique de valence de $ns^2\,np^5$. Par exemple, le fluor (F) a une configuration électronique de $1s^2\,2s^2\,2p^5$.
- **Groupe 18 (Gaz nobles)** : Les éléments du groupe 18 ont une configuration électronique de valence de $ns^2\,np^6$, ce qui correspond à une configuration électronique complète et très stable. Par exemple, le néon (Ne) a une configuration électronique de $1s^2\,2s^2\,2p^6$.

Sous forme de tableau, cela peut être résumé comme suit :

| Groupe | Configuration électronique de valence | Exemple |
|-------|--------------------------------------|---------|
| 1 (Alcalins) | $ns^1$ | Lithium (Li) : $1s^2\,2s^1$ |
| 2 (Alcalino-terreux) | $ns^2$ | Béryllium (Be) : $1s^2\,2s^2$ |
| 3 à 12 (Métaux de transition) | $[n-1]d^{1-10}\,ns^{0-2}$ | Fer (Fe) : $[Ar]\,3d^6\,4s^2$ |
| 13 (Boreux) | $ns^2\,np^1$ | Bore (B) : $1s^2\,2s^2\,2p^1$ |
| 14 (Carboneux) | $ns^2\,np^2$ |   Carbone (C) : $1s^2\,2s^2\,2p^2$ |
| 15 (Azotés) | $ns^2\,np^3$ |  Azote (N) : $1s^2\,2s^2\,2p^3$ |
| 16 (Chalcogènes) | $ns^2\,np^4$ | Oxygène (O) : $1s^2\,2s^2\,2p^4$ |
| 17 (Halogènes) | $ns^2\,np^5$ | Fluor (F) : $1s^2\,2s^2\,2p^5$ |
| 18 (Gaz nobles) | $ns^2\,np^6$ | Néon (Ne) : $1s^2\,2s^2\,2p^6$ |

