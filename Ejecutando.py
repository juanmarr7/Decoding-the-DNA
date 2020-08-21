# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 10:36:57 2020

@author: Juanma
"""

from DNA_funciones import *
from utilidades import colored
cadena="acgta"

# Creando cadenas random. Ya en mayúsculas gracias a base_nuc
import random
cadena_random=''.join([random.choice(base_nuc) for nuc in range (75)])
print(validar(cadena_random))
print(contar(cadena_random))
print("Cadena transcrita: " + transcribir(cadena_random))
print( "Cadena reversa: " + reversa(cadena_random))
patron_dna(cadena_random)
print("GC Content: " + str(gc_content(cadena_random)) +" %")
print("GC Content por intevalos: "+ str(gc_content_intervalos(cadena_random,10)) + " en %")
print("Cadena de aa: "+ str(traducir_dna(cadena_random)))
print("Aa responsables: " + str(codon_use(cadena_random, "L")))
print("Los 6 marcos de lectura posibles son: " + str(marcos_de_lectura(cadena_random)))

cadena=['_', 'R', 'M', 'P', 'V', 'V', 'P', 'S', 'K', 'R', 'R', 'D', 'V', 'S', 'G', 'I', 'D', 'R', 'G', 'T', 'G', 'W', 'H', 'L', '_']
print(proteinas_en_marco(cadena))



NM_000207="AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGATCACTGTCCTTCTGCCATGGCCCTGTGGATGCGCCTCCTGCCCCTGCTGGCGCTGCTGGCCCTCTGGGGACCTGACCCAGCCGCAGCCTTTGTGAACCAACACCTGTGCGGCTCACACCTGGTGGAAGCTCTCTACCTAGTGTGCGGGGAACGAGGCTTCTTCTACACACCCAAGACCCGCCGGGAGGCAGAGGACCTGCAGGTGGGGCAGGTGGAGCTGGGCGGGGGCCCTGGTGCAGGCAGCCTGCAGCCCTTGGCCCTGGAGGGGTCCCTGCAGAAGCGTGGCATTGTGGAACAATGCTGTACCAGCATCTGCTCCCTCTACCAGCTGGAGAACTACTGCAACTAGACGCAGCCCGCAGGCAGCCCCACACCCGCCGCCTCCTGCACCGAGAGAGATGGAATAAAGCCCTTGAACCAGC"

print("Aqui empezamos:")
print(marcos_de_lectura(NM_000207))
for prot in todas_las_proteinas(NM_000207,0,0,True):
    print(prot)
    
    