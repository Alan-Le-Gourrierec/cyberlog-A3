"""Calcul de la viscosité de l'anneau en fonction de la distance à l'astre
   cas de l'anneau A de saturne, densité de surface constante
"""

import numpy as np
import matplotlib.pyplot as plt

#variables globales
sigma = 400.0            #densité de surface de l'anneau en kg.m-2
G = 6.67430e-11          #constante de gravitation
M = 5.6834e26            #masse de l'astre en kg
sigma = 400.0            #densité de surface du disque

rp =  [10.0, 1.0, 0.1]   #rayons particules
rhoP = 900.0             #densité particules

Rmin, Rmax = 60e6, 140e6 #bornes de l'intervalle de distance
dr = 10000               #pas entre les différents disctances pour les calculs

R = np.arange(Rmin, Rmax, dr)

def variables(rp) :
	mp = rhoP*4/3*np.pi*rp**3          #masse particule en kg
	omega = np.sqrt(G*M/(R**3))        #fréquence orbitale en Hz
	dispR = np.sqrt(G*mp/rp)           #dispertion radiale en m.s-1
	
	Q = omega*dispR/(3.36*G*sigma)     #paramètre de Toomre
	
	tau = 3*sigma/(4*rp*rhoP)
	
	rHill = R*(2*mp/(3*M))**(1/3)
	HillEtoile = rHill/(2*rp)
	return mp, omega, dispR, Q, tau, HillEtoile

def CalcNuSG(rp, R, sigma):     #calcul des composantes de nu dans le régime SG
	nuTrans = np.zeros_like(R)
	nuGrav = np.zeros_like(R)
	
	mp, omega, dispR, Q, tau, HillEtoile = variables(rp)
	
	nuTrans = ((dispR**2)/(2*omega))*((0.46*tau)/(1+tau**2))
	nuColl = rp**2 * omega * tau
	plt.plot(R, nuTrans, label=f'trans rp = {rp}')
	plt.plot(R, nuColl, label=f'Coll rp = {rp}')
	return []


def CalcNuNSG(rp, R, Sigma):    #calcul des composantes de nu dans le régime NSG
	nuTrans = np.zeros_like(R)
	nuGrav = np.zeros_like(R)
	
	mp, omega, dispR, Q, tau, HillEtoile = variables(rp)
	
	nuTrans =  13 * HillEtoile**5 * G**2 * sigma**2/(omega**3)
	nuGrav = nuTrans
	nuColl = rp**2 * omega * tau
	plt.plot(R, nuTrans, label=f'trans rp = {rp}')
	return []


def graphique(rp):
	plt.figure()
	for i in range (3) :
		CalcNuSG(rp[i], R, sigma)
	CalcNuNSG(0.1, R, sigma)
	plt.xlabel("Distance à Saturne (100000 km)")
	plt.ylabel(r'Viscosité $(m².s^{-1})$')
	plt.yscale('log')
	plt.ylim(1e-8, 1)
	plt.legend()
	plt.show()
	return []

graphique(rp)