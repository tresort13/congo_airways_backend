
from email import message
from functools import partial
from ntpath import join
from urllib import response

from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from congoairwaysapi.models import Passager_informations_vol
from congoairwaysapi.models import Bagage_informations_vol
from congoairwaysapi.serializers import Passager_informationsSerializer
from congoairwaysapi.serializers import Vol_informationsSerializer
from rest_framework import generics, permissions
from knox.models import AuthToken
from .serializers import Bagage_informationsSerializer, UserSerializer, RegisterSerializer,ManifestSerializer
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from .models import  Manifest, Vol_information
import re
from rest_framework.views import APIView
from datetime import date
from rest_framework.permissions import IsAuthenticated



class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response({"username" : user.username})

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
        
def welcom(request):
    return HttpResponse('WELCOM TO CONGO AIRWAYS API RESOURCES')

class VolInformations(APIView):
      
    def post(self, request, *args, **kwargs):
        destination = request.data['volDestination']
        avion = request.data['volTypeAvion']
        temps = request.data['volTime']
        date_info = request.data['dateType']
        
        combinedData = ""+destination+" "+avion+" "+temps+" "+date_info+" "  
        serializer = Vol_informationsSerializer(data = {'flight_info':combinedData})
        if serializer.is_valid() :
           serializer.save()
           return Response("ok")
        return Response("saving failed")


class ManifestUpload(APIView): 
  
  def post(self,request,*args, **kwargs):
    fichier = request.data['manifest']
    serializer = ManifestSerializer(data = {'manifest':fichier})
    if serializer.is_valid() :
        serializer.save()
        return Response('ok')
    return Response('',status=status.HTTP_400_BAD_REQUEST)
               
             
        
    
class PassagerInformations(APIView):

    def post(self, request, *args, **kwargs):
        barcodePassager = request.data['barcodePassager']
        volInfo = request.data['volInfo']
    
        
        serializer = Passager_informationsSerializer(data = {'numero_barcode_passager':barcodePassager,'vol_information':volInfo,'count_numero_barcode_passager':1})
        if serializer.is_valid() :
           serializer.save()
           return Response("ok")
        return Response('enregistrement echoué (veuillez selectionner le vol ou peut etre le barcode est déjà enregistré!!)',status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, *args, **kwargs):
        barcodePassager =int(request.data['barcodePassager'])
        passager_informations_vol = Passager_informations_vol.objects.get(numero_barcode_passager = barcodePassager)
        manifests = Manifest.objects.filter(date_envoie = passager_informations_vol.date_operation)
        strutured_data = []
        digit = 1
        check_value = str(barcodePassager)
        for manifest in manifests:
            fichier = manifest.manifest
            lines = fichier.readlines()
            lines_conversion = ' '.join(map(str,lines))
            recherche_barcode_in_manifest = re.search(check_value,string=lines_conversion)
            if recherche_barcode_in_manifest:
              for line in lines:
                  convert_digit = str(digit)
                  count = convert_digit+" "
                  checking = re.search(count,string=str(line))
                  if checking:
                      i=int (lines.index(line))
                      passenger_info = lines[i:i+3]
                      flight_info = lines[:4]
                      #conversion = ' '.join(map(str, passenger_info))
                      #strutured_data.append(conversion.strip())
                      strutured_data.append(passenger_info)
                      digit = digit + 1
    
              for final_manifest in strutured_data:       
                  recherche = re.search(check_value,string=''.join(map(str,final_manifest)))
                  if recherche:
                      #final_manifest_list = final_manifest.split(" \n ")
                      serializer = Passager_informationsSerializer(passager_informations_vol,data = {'passenger_and_ticket_info':str(final_manifest[0]).strip(),'pnr_and_bagage_info':str(final_manifest[1]).strip(),'bagage_weight_info':str(final_manifest[2]).strip(),'flight_info':str(flight_info[0]),'avion_info':str(flight_info[2])},partial=True)
                      if serializer.is_valid() :
                          serializer.save()
                          return Response(serializer.data)
                      return Response('serializer is not valid',status=status.HTTP_400_BAD_REQUEST)
                        
        return Response(strutured_data)
    
class UpdatePoidsBagages(APIView):
    
    def put(self, request, *args, **kwargs):
        barcodeBagage = int(request.data['barcodeBagage'])
        poids_bagage =request.data['poids_bagage']
        
        bagage_informations_vol = Bagage_informations_vol.objects.get(numero_barcode_bagage = barcodeBagage)
        
        serializer = Bagage_informationsSerializer(bagage_informations_vol,data = {'kilos_bagage_tarmaque':poids_bagage},partial=True)
        if serializer.is_valid() :
            serializer.save()
            return Response("ok")
        return Response("no",status=status.HTTP_400_BAD_REQUEST)
       

class UpdateBagages(APIView):

    def put(self, request, *args, **kwargs):
        barcodeBagage = int(request.data['barcodeBagage'])
        operation =request.data['operation']
        position =request.data['position']
        vol_info =request.data['volInfo']
        
        
        bagage_informations_vol = Bagage_informations_vol.objects.get(numero_barcode_bagage = barcodeBagage)
        
        serializer = Bagage_informationsSerializer(bagage_informations_vol,data = {operation:operation,position:position,'vol_information':vol_info,'count_'+operation:1,'count_'+position:1},partial=True)
        if serializer.is_valid() :
            serializer.save()
            return Response("ok")
        return Response("no",status=status.HTTP_400_BAD_REQUEST)
       
    
class UpdatePassagers(APIView):
    
    def put(self, request, *args, **kwargs):
        barcodePassager = int(request.data['barcodePassager'])
        operation =request.data['operation']
        position =request.data['position']
        vol_info =request.data['volInfo']
        passager_informations_vol = Passager_informations_vol.objects.get(numero_barcode_passager = barcodePassager)
        serializer = Passager_informationsSerializer(passager_informations_vol,data = {operation:operation,position:position,'vol_information':vol_info,'count_'+operation:1,'count_'+position:1},partial=True)
        if serializer.is_valid() :
            serializer.save()
            return Response("ok")
        return Response('veuillez selectionner votre position , vol ,type operation avant de scanner!! (au cas contraire veuillez enregistrer le barcode)')
    
    
@api_view(['GET'])   
def bagageAutoQuery(request,pk): 
       
        barcodeBagage = pk
        bagage_informations_vol = Bagage_informations_vol.objects.get(numero_barcode_bagage = barcodeBagage)
        manifests = Manifest.objects.filter(date_envoie = bagage_informations_vol.date_operation)
        strutured_data = []
        digit = 0
        check_value = barcodeBagage
        for manifest in manifests:
            fichier = manifest.manifest
            lines = fichier.readlines()
            lines_conversion = ' '.join(map(str,lines))
            recherche_barcode_in_manifest = re.search(str(check_value),string=lines_conversion)
            if recherche_barcode_in_manifest:
              for line in lines:
                  convert_digit = str(digit)
                  count = convert_digit+" "
                  checking = re.search(count,string=str(line))
                  if checking:
                      i=int (lines.index(line))
                      passenger_info = lines[i:i+3]
                      flight_info = lines[:4]
                      #conversion = ' '.join(map(str, passenger_info))
                      #strutured_data.append(conversion.strip())
                      strutured_data.append(passenger_info)
                      digit = digit + 1
    
              for final_manifest in strutured_data:       
                  recherche = re.search(str(check_value),string=''.join(map(str,final_manifest)))
                  if recherche:
                      #final_manifest_list = final_manifest.split(" \n ")
                      noms_passager=str(final_manifest[0])
                      pnr_passager=str(final_manifest[1])
                      bagage_passager=str(final_manifest[2])
                      bagage_informations_vol.passenger_and_ticket_info = noms_passager
                      bagage_informations_vol.pnr_and_bagage_info=pnr_passager
                      bagage_informations_vol.bagage_weight_info = bagage_passager
                      bagage_informations_vol.flight_info = str(flight_info[0])
                      bagage_informations_vol.avion_info = str(flight_info[2])
                      
                      bagage_informations_vol.save()
                      
                        
        
        try:
          bagage_informations_vol = Bagage_informations_vol.objects.get(numero_barcode_bagage = pk)
        except bagage_informations_vol.DoesNotExist:
          return Response(status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'GET':
            serializer = Bagage_informationsSerializer(bagage_informations_vol)
            return Response(serializer.data)
        
        
@api_view(['GET'])   
def passagerAutoQuery(request,pk): 
    
        barcodePassager = pk
        passager_informations_vol = Passager_informations_vol.objects.get(numero_barcode_passager = barcodePassager)
        manifests = Manifest.objects.filter(date_envoie = passager_informations_vol.date_operation)
        strutured_data = []
        digit = 0
        check_value = barcodePassager
        for manifest in manifests:
            fichier = manifest.manifest
            lines = fichier.readlines()
            lines_conversion = ' '.join(map(str,lines))
            recherche_barcode_in_manifest = re.search(str(check_value),string=lines_conversion)
            if recherche_barcode_in_manifest:
              for line in lines:
                  convert_digit = str(digit)
                  count = convert_digit+" "
                  checking = re.search(count,string=str(line))
                  if checking:
                      i=int (lines.index(line))
                      passenger_info = lines[i:i+3]
                      flight_info = lines[:4]
                      #conversion = ' '.join(map(str, passenger_info))
                      #strutured_data.append(conversion.strip())
                      strutured_data.append(passenger_info)
                      digit = digit + 1
    
              for final_manifest in strutured_data:       
                  recherche = re.search(str(check_value),string=''.join(map(str,final_manifest)))
                  if recherche:
                      #final_manifest_list = final_manifest.split(" \n ")
                      noms_passager=str(final_manifest[0])
                      pnr_passager=str(final_manifest[1])
                      bagage_passager=str(final_manifest[2])
                      passager_informations_vol.passenger_and_ticket_info = noms_passager
                      passager_informations_vol.pnr_and_bagage_info=pnr_passager
                      passager_informations_vol.bagage_weight_info = bagage_passager
                      passager_informations_vol.flight_info = str(flight_info[0])
                      passager_informations_vol.avion_info = str(flight_info[2])
                      
                      passager_informations_vol.save()
                      
                        
              try:
                passager_informations_vol = Passager_informations_vol.objects.get(numero_barcode_passager = pk)
              except passager_informations_vol.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        
              if request.method == 'GET':
                 serializer = Passager_informationsSerializer(passager_informations_vol)
                 return Response(serializer.data)


@api_view(['GET'])   
def volAutoQuery(request): 
    try:
        vol_information = Vol_information.objects.filter(date_envoie = date.today())
    except vol_information.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method =='GET':
            serializer = Vol_informationsSerializer(vol_information,many=True)
            return Response(serializer.data)
        
@api_view(['GET'])   
def volAutoQuery2(request,pk): 
    temps = pk
    try:
        vol_information = Vol_information.objects.filter(date_envoie =temps)
    except vol_information.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method =='GET':
            serializer = Vol_informationsSerializer(vol_information,many=True)
            return Response(serializer.data)
        
        
@api_view(['GET'])   
def volBagagesAutoQuery(request,pk): 
    
    try:
        bagage_informations_vol = Bagage_informations_vol.objects.filter(vol_information= pk)
    except bagage_informations_vol.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method =='GET':
            serializer = Bagage_informationsSerializer(bagage_informations_vol,many=True)
            return Response(serializer.data)





@api_view(['GET'])   
def volPassagerAutoQuery(request,pk): 
    
    try:
        passager_informations_vol = Passager_informations_vol.objects.filter(vol_information= pk)
    except passager_informations_vol.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method =='GET':
            serializer = Passager_informationsSerializer(passager_informations_vol,many=True)
            return Response(serializer.data)




class BagageInformations(APIView):
     
    def post(self, request, *args, **kwargs):
        barcodeBagage = request.data['barcodeBagage']
        volInfo = request.data['volInfo']
        serializer = Bagage_informationsSerializer(data = {'numero_barcode_bagage':barcodeBagage,'vol_information':volInfo,'count_numero_barcode_bagage':1})
        if serializer.is_valid() :
           serializer.save()
           return Response("ok")
        return Response("no",status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, *args, **kwargs):
        barcodeBagage =request.data['barcodeBagage']
        bagage_informations_vol = Bagage_informations_vol.objects.get(numero_barcode_bagage = barcodeBagage)
        manifests = Manifest.objects.filter(date_envoie = bagage_informations_vol.date_operation)
        strutured_data = []
        digit = 0
        check_value = barcodeBagage
        for manifest in manifests:
            fichier = manifest.manifest
            lines = fichier.readlines()
            lines_conversion = ' '.join(map(str,lines))
            recherche_barcode_in_manifest = re.search(check_value,string=lines_conversion)
            if recherche_barcode_in_manifest:
              for line in lines:
                  convert_digit = str(digit)
                  count = convert_digit+" "
                  checking = re.search(count,string=str(line))
                  if checking:
                      i=int (lines.index(line))
                      passenger_info = lines[i:i+3]
                      flight_info = lines[:4]
                      #conversion = ' '.join(map(str, passenger_info))
                      #strutured_data.append(conversion.strip())
                      strutured_data.append(passenger_info)
                      digit = digit + 1
    
              for final_manifest in strutured_data:       
                  recherche = re.search(check_value,string=''.join(map(str,final_manifest)))
                  if recherche:
                      #final_manifest_list = final_manifest.split(" \n ")
                      noms_passager=str(final_manifest[0])
                      pnr_passager=str(final_manifest[1])
                      bagage_passager=str(final_manifest[2])
                      serializer = Bagage_informationsSerializer(bagage_informations_vol,data = {'passenger_and_ticket_info':noms_passager,'pnr_and_bagage_info':pnr_passager,'bagage_weight_info':bagage_passager,'flight_info':str(flight_info[0]),'avion_info':str(flight_info[2])},partial=True)
                      if serializer.is_valid() :
                          serializer.save()
                          return Response("ok")
                      return Response("no")
                        
        return Response("echec")











@api_view(['GET', 'PUT', 'DELETE'])
def passager_informations_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        passager_informations_vol = Passager_informations_vol.objects.get(pk=pk)
    except passager_informations_vol.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Passager_informationsSerializer(passager_informations_vol)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Passager_informationsSerializer(Passager_informations_vol, data={'passenger_and_ticket_info':'you are good one'})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        passager_informations_vol.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)