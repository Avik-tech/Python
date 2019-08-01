#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Crypto.Util.number import inverse

# Le couple (n, e) correspond à la clé publique de chiffrement
# n = pq, appelé module de chiffrement
n = 165481207658568424313022356820498512502867488746572300093793
# Exposant de chiffrement
e = 65537

# c correspond au message chiffré
c = 150635433712900935381157860417761227624682377134647578768653

# p et q sont les facteurs premiers de n
p = 404796306518120759733507156677
q = 408801179738927870766525808109

# phi correspond à la valeur de l'indicatrice d'Euler en n
phi = (p - 1) * (q - 1)

# d correspond à la clé privée
d = inverse(e, phi)

# Pour déchiffrer le message, on utilise d (l'inverse de e modulo phi)
# et l'on retrouve le message en clair par :
m = pow(c, d, n)

# Puis on decode la valeur hexadécimal m en ascii
print hex(m)[2:-1].decode('hex')
