from ..system_models.ExtendedUser import ExtendedUser
from ..system_models.Geography import *
from ..system_models.Payment import * 
from ..system_models.Medical import * 
from ..system_models.TreatmentRequest import * 
from ..system_models.Viza import * 

class QueryBuilder():
    @staticmethod
    def get_treatment_request(tr_id,user_id=None):
        if (user_id == None):
            return TreatmentRequest.objects.filter(id=tr_id).first()
        else:
            return TreatmentRequest.objects.filter(id=tr_id,related_patient__id=user_id).first()
            
    def insert_treatment_request(pid,uid,td_ids):
        last_updated = datetime.now()
        ntr = TreatmentRequest(related_package_id =pid,related_patient_id= uid,last_updated=last_updated)
        ntr.save()
        for td_id in td_ids:
            ntr.related_documents.add(td_id)
        ntr.save()
        return ntr.id
    #-----------------------------------------------------------#
    def insert_docs(document_title,document_content,related_requirement_id):
        nd = Document(document_title=document_title,content=document_content,related_requirement_id=related_requirement_id)
        nd.save()
        return nd.id
    #-----------------------------------------------------------#
    def get_hotels(city_id):
        return Hotel.objects.filter(city__id=city_id)
    def get_hotel(hotel_id):
        return Hotel.objects.filter(id=hotel_id).first()
    #-----------------------------------------------------------#
    def get_all_packages():
        return Package.objects.select_related('related_doctor', 'related_hospital', 'disease').all()
    def get_package(id):
        return  Package.objects.filter(pk=id).first()
    
    #-----------------------------------------------------------#
    def get_user_by_token(token):
        return ExtendedUser.objects.filter(token = token).first()
