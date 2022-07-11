from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Passager_informations_vol(models.Model):
    numero_barcode_passager = models.CharField(max_length=13,unique=True)
    passenger_and_ticket_info = models.TextField(default="")
    pnr_and_bagage_info = models.TextField(default="")
    bagage_weight_info = models.TextField(default="")
    flight_info = models.TextField(default="")
    avion_info = models.TextField(default="")
    ok_passager_checker_depart = models.CharField(max_length=100,default="")
    ok_passager_checker_arriver = models.CharField(max_length=100,default="")
    ok_passager_localisation_dgm = models.CharField(max_length=100,default="")
    ok_passager_localisation_salle_attente = models.CharField(max_length=100,default="")
    ok_passager_embarquement_avion = models.CharField(max_length=100,default="")
    ok_passager_debarquement_avion = models.CharField(max_length=100,default="")
    ok_passager_arriver_et_recuperer_baggage = models.CharField(max_length=100,default="")
    ok_passager_arriver_et_recuperer_baggage = models.CharField(max_length=100,default="")
    date_heure_operation =models.DateTimeField(auto_now_add=True)
    date_operation = models.DateField(auto_now_add=True)
    agent_id_save = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    vol_information = models.CharField(max_length=200,default="")
    count_numero_barcode_passager = models.CharField(max_length=100,default=0)
    count_ok_passager_checker_depart = models.CharField(max_length=100,default=0)
    count_ok_passager_checker_arriver = models.CharField(max_length=100,default=0)
    count_ok_passager_localisation_dgm = models.CharField(max_length=100,default=0)
    count_ok_passager_localisation_salle_attente = models.CharField(max_length=100,default=0)
    count_ok_passager_embarquement_avion = models.CharField(max_length=100,default=0)
    count_ok_passager_debarquement_avion = models.CharField(max_length=100,default=0)
    count_ok_passager_arriver_et_recuperer_baggage = models.CharField(max_length=100,default=0  )
    
    
    
class Bagage_informations_vol(models.Model):
    numero_barcode_bagage = models.CharField(max_length=10,unique=True)
    passenger_and_ticket_info = models.TextField(default="")
    pnr_and_bagage_info = models.TextField(default="")
    bagage_weight_info = models.TextField(default="")
    flight_info = models.TextField(default="")
    avion_info = models.TextField(default="")
    ok_bagage_fin_tapis = models.CharField(max_length=100,default="")
    ok_pied_avion = models.CharField(max_length=100,default="")
    ok_bagage_embarquement_depart =models.CharField(max_length=100,default="")
    ok_bagage_emplacement_south_A =models.CharField(max_length=100,default="")
    ok_bagage_emplacement_south_B =models.CharField(max_length=100,default="")
    ok_bagage_emplacement_south_C =models.CharField(max_length=100,default="")
    ok_bagage_debarquement_depart =models.CharField(max_length=100,default="")
    ok_bagage_debarquement_arrivee =models.CharField(max_length=100,default="")
    ok_bagage_checker_depart = models.CharField(max_length=100,default="")
    ok_bagage_checker_arriver = models.CharField(max_length=100,default="")
    ok_bagage_en_tapis_livraison = models.CharField(max_length=100,default="")
    ok_bagage_livrer = models.CharField(max_length=100,default="")
    ok_bagage_stocke_depart = models.CharField(max_length=100,default="")
    ok_bagage_stocke_arrivee = models.CharField(max_length=100,default="")
    kilos_bagage_tarmaque = models.CharField(max_length=100,default="")
    date_heure_operation =models.DateTimeField(auto_now_add=True)
    date_operation = models.DateField(auto_now_add=True)
    agent_id_save = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    vol_information = models.CharField(max_length=200,default="")
    count_numero_barcode_bagage = models.CharField(max_length=100,default=0) 
    count_ok_bagage_fin_tapis = models.CharField(max_length=100,default=0)
    count_ok_pied_avion = models.CharField(max_length=100,default=0)
    count_ok_bagage_embarquement_depart =models.CharField(max_length=100,default=0)
    count_ok_bagage_emplacement_south_A =models.CharField(max_length=100,default=0)
    count_ok_bagage_emplacement_south_B =models.CharField(max_length=100,default=0)
    count_ok_bagage_emplacement_south_C =models.CharField(max_length=100,default=0)
    count_ok_bagage_debarquement_depart =models.CharField(max_length=100,default=0)
    count_ok_bagage_debarquement_arrivee =models.CharField(max_length=100,default=0)
    count_ok_bagage_checker_depart = models.CharField(max_length=100,default=0)
    count_ok_bagage_checker_arriver = models.CharField(max_length=100,default=0)
    count_ok_bagage_en_tapis_livraison = models.CharField(max_length=100,default=0)
    count_ok_bagage_livrer = models.CharField(max_length=100,default=0)
    count_ok_bagage_stocke_depart = models.CharField(max_length=100,default=0)
    count_ok_bagage_stocke_arrivee = models.CharField(max_length=100,default=0)
         
   
    
    
    
class Manifest(models.Model):
    manifest = models.FileField(upload_to='files')
    date_heure_envoie =models.DateTimeField(auto_now_add=True)
    date_envoie = models.DateField(auto_now_add=True)
    agent_id = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    
class Vol_information(models.Model):
    flight_info = models.CharField(max_length=200,unique=True,default="")
    date_heure_operation =models.DateTimeField(auto_now_add=True)
    date_envoie = models.DateField(auto_now_add=True)
    agent_id = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    
    
    
    
    
    
    
    
