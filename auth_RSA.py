#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Le couple (n, e) correspond à la clé publique de chiffrement
n = 59883006898206291499785811163190956754007806709157091648869
e = 65537

# c correspond au message chiffré
c = 23731413167627600089782741107678182917228038671345300608183

# Formule pour déchiffrer le message
m = pow(c, e, n)

# On affiche la valeur hexadécimal m en ascii
print hex(m)[2:-1].decode('hex')
