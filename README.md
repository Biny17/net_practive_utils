# Guide d'utilisation des outils

## Utilisation de l'exécutable `ip_range`

L'exécutable `ip_range` permet de calculer la plage d'adresses IP à partir d'une adresse IP et d'un masque de sous-réseau. Pour l'utiliser :

Exécutez la commande suivante en fournissant une adresse IP et un masque :
   ```bash
   ./ip_range 192.168.1.1 /24
   ```
   ou
   ```bash
   ./ip_range 192.168.1.1 255.255.255.0
   ```

Cela affichera la plage d'adresses IP correspondante.

## Utilisation des fonctions Python

Le fichier `net_utils.py` contient plusieurs fonctions utiles que vous pouvez utiliser directement dans un terminal Python.

### Étapes pour accéder aux fonctions :

1. Ouvrez un terminal dans le dossier contenant le fichier `net_utils.py`.

1. Lancez l'interpréteur Python :
   ```bash
   python
   ```

3. Importez les fonctions du fichier :
   ```python
   from net_utils import *
   ```

### Liste des fonctions disponibles et leur utilisation :

- **`ip_to_i(mask: str) -> int`** : Convertit un masque de sous-réseau en entier.
  ```python
  ip_to_i("255.255.255.0")
  ```

- **`slash_mask(mask: str) -> int`** : Convertit un masque en notation slash (ex: `/24`) en entier.
  ```python
  slash_mask("/24")
  ```

- **`mask_to_str(mask: int) -> str`** : Convertit un masque entier en notation décimale.
  ```python
  mask_to_str(4294967040)
  ```

- **`mask_to_slash(mask: int) -> str`** : Convertit un masque entier en notation slash.
  ```python
  mask_to_slash(4294967040)
  ```

- **`pr(ip: str, mask: str)`** : Affiche la plage d'adresses IP pour une adresse et un masque donnés.
  ```python
  pr("192.168.1.0", "/24")
  ```

- **`ip4()`** : Affiche les plages d'adresses IP des réseaux privés.
  ```python
  ip4()
  ```

- **`mask_eq(mask: str)`** : Convertit un masque entre les notations slash et décimale.
  ```python
  mask_eq("255.255.255.0")
  mask_eq("/24")
  ```
