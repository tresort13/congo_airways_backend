from rest_framework import serializers

from .models import Passager_informations_vol
from .models import Bagage_informations_vol
from .models import Vol_information,Manifest
from django.contrib.auth.models import User


#passager information serializer
class Passager_informationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passager_informations_vol
        fields = ['id', 'numero_barcode_passager', 'passenger_and_ticket_info', 'pnr_and_bagage_info', 
                  'bagage_weight_info','flight_info','avion_info','ok_passager_checker_depart','ok_passager_checker_arriver',
                  'ok_passager_localisation_dgm',
                  'ok_passager_localisation_salle_attente','ok_passager_embarquement_avion',
                  'ok_passager_debarquement_avion','ok_passager_arriver_et_recuperer_baggage',
                  'date_heure_operation','date_operation','agent_id_save','vol_information','count_numero_barcode_passager',
                  'count_ok_passager_checker_depart','count_ok_passager_checker_arriver','count_ok_passager_localisation_dgm',
                  'count_ok_passager_localisation_salle_attente','count_ok_passager_embarquement_avion',
                  'count_ok_passager_debarquement_avion','count_ok_passager_arriver_et_recuperer_baggage']
        
        
#bagage information serializer
class Bagage_informationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bagage_informations_vol
        fields = ['id', 'numero_barcode_bagage', 'passenger_and_ticket_info', 'pnr_and_bagage_info',
                  'bagage_weight_info','flight_info','avion_info',
                  'ok_bagage_fin_tapis','ok_pied_avion','ok_bagage_embarquement_depart','ok_bagage_emplacement_south_A',
                  'ok_bagage_emplacement_south_B','ok_bagage_emplacement_south_C','ok_bagage_debarquement_depart','ok_bagage_debarquement_arrivee','ok_bagage_checker_depart','ok_bagage_checker_arriver',
                  'ok_bagage_en_tapis_livraison',
                  'ok_bagage_livrer','ok_bagage_stocke_depart','ok_bagage_stocke_arrivee','kilos_bagage_tarmaque',
                  'date_heure_operation','date_operation','agent_id_save','vol_information','count_numero_barcode_bagage','count_ok_bagage_fin_tapis',
                  'count_ok_pied_avion','count_ok_bagage_embarquement_depart','count_ok_bagage_emplacement_south_A',
                  'count_ok_bagage_emplacement_south_B','count_ok_bagage_emplacement_south_C','count_ok_bagage_debarquement_depart',
                  'count_ok_bagage_debarquement_arrivee','count_ok_bagage_checker_depart','count_ok_bagage_checker_arriver',
                  'count_ok_bagage_en_tapis_livraison','count_ok_bagage_livrer','count_ok_bagage_stocke_depart',
                  'count_ok_bagage_stocke_arrivee']

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
    
class ManifestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manifest
        fields = ('id', 'manifest')
        
class Vol_informationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vol_information
        fields = ('id', 'flight_info')




        
