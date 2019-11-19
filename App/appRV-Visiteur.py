#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import *
import json

from modeles import modeleGSBRV
from datetime import datetime
app = Flask( __name__ )


@app.route( '/visiteurs/<matricule>/<mdp>' , methods = [ 'GET' ] )
def seConnecter( matricule , mdp ) :
	visiteur = modeleGSBRV.seConnecter( matricule , mdp )
	
	if visiteur != None and len( visiteur ) != 0 :
		reponse = make_response( json.dumps( visiteur ) )
		reponse.mimetype = 'application/json'
		reponse.status_code = 200
	else :
		reponse = make_response( 'Veuillez recommencer Si le probleme persiste, contacter le développeur' )
		reponse.mimetype = 'application/json'
		reponse.status_code = 404
	return reponse
		
	
@app.route( '/rapports/<matricule>/<mois>/<annee>' , methods = [ 'GET' ] )
def getRapportsVisite( matricule , mois , annee ) :
	rapports = modeleGSBRV.getRapportsVisite( matricule , mois , annee )
	
	if rapports != None :
		reponse = make_response( json.dumps( rapports ) )
		reponse.mimetype = 'application/json'
		reponse.status_code = 200
	else :
		reponse = make_response( '' )
		reponse.mimetype = 'application/json'
		reponse.status_code = 404
	return reponse
	

@app.route( '/rapports/echantillons/<matricule>/<numRapport>' , methods = [ 'GET' ] )
def getEchantillonsOfferts( matricule , numRapport ) :
	offres = modeleGSBRV.getEchantillonsOfferts( matricule , numRapport )
	print offres
	
	if offres != None :
		reponse = make_response( json.dumps( offres ) )
		reponse.mimetype = 'application/json'
		reponse.status_code = 200
	else :
		reponse = make_response( '' )
		reponse.mimetype = 'application/json'
		reponse.status_code = 404
	return reponse

	
@app.route( '/praticiens' , methods = [ 'GET' ] )
def getPraticiens() :
	praticiens = modeleGSBRV.getPraticiens()
	
	if praticiens != None :
		reponse = make_response( json.dumps( praticiens ) )
		reponse.mimetype = 'application/json'
		reponse.status_code = 200
	else :
		reponse = make_response( '' )
		reponse.mimetype = 'application/json'
		reponse.status_code = 404
	return reponse
	
@app.route( '/medicaments' , methods = [ 'GET' ] )
def getMedicaments() :
	medicaments = modeleGSBRV.getMedicaments()
	
	if medicaments != None :
		reponse = make_response( json.dumps( medicaments ) )
		reponse.mimetype = 'application/json'
		reponse.status_code = 200
	else :
		reponse = make_response( '' )
		reponse.mimetype = 'application/json'
		reponse.status_code = 404
	return reponse
	
@app.route('/motifs' , methods = ['GET'])
def getMotifs() :
	motifs = modeleGSBRV.getMotifs()
	
	if motifs != None :
		reponse = make_response( json.dumps( motifs ) )
		reponse.mimetype = 'application/json'
		reponse.status_code = 200
	else :
		reponse = make_response( '' )
		reponse.mimetype = 'application/json'
		reponse.status_code = 404
	return reponse
	
@app.route( '/rapports' , methods = [ 'POST' ] )
def addRapportVisite() :
	date = datetime.now().date()
	
	unRapport = json.loads( request.data )
	numRapport = modeleGSBRV.enregistrerRapportVisite( 	unRapport[ 'matricule' ], unRapport[ 'praticien' ], unRapport[ 'visite' ], unRapport[ 'bilan' ], unRapport['confiance'], unRapport['motif'],date )
	
	reponse = make_response( '' )												
	if numRapport != None :
		reponse.headers[ 'Location' ] = '/rapports/%s/%d' % ( unRapport[ 'matricule' ] , numRapport )
		reponse.status_code = 201
	else :
		reponse.status_code = 409
	return reponse
	

@app.route( '/rapports/echantillons/<matricule>/<numRapport>' , methods = [ 'POST' ] )
def addEchantillonsOfferts( matricule , numRapport ) :
	echantillons = json.loads( request.data )
	nbEchantillons = modeleGSBRV.enregistrerEchantillonsOfferts( matricule , numRapport , echantillons )
	
	
	reponse = make_response( '' )												
	if numRapport != None :
		reponse.headers[ 'Location' ] = '/rapports/echantillons/%s/%s' % ( matricule , numRapport )
		reponse.status_code = 201
	else :
		reponse.status_code = 409
	return reponse






if __name__ == '__main__' :
	app.run( debug = True , host = '0.0.0.0' , port = 5000 )


