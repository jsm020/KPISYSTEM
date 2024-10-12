from django.contrib.admin import AdminSite
from django.contrib.auth.views import redirect_to_login
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import admin
from .models import *

admin.site.register([OquvYiliFanlar,FaolInterfaolMetodlar,MustaqilTalimTopshiriqlari,FanVideoKontent,OqitishSifati,NashrEtilganDarsliklar])
admin.site.register([ScopusWebOfScience,OAKJurnaliMaqola,HIndex,KonferensiyaMaqola,LoyihalarTayyorlash,LoyihaMoliya,AKTDasturlar,TalabaIlmiyFaoliyati])
admin.site.register([TarbiyaTadbirlar,DarstanTashqariTadbirlar,TalabalarTurarJoyTadbirlar,OtaOnalarIshlash,AxborotMurobbiylikSoat,MuhimTashabbuslarIshlari,BirZiyoliBirMahalla])
admin.site.register([DarslikYokiQollanma,DissertationHimoya,IlmiyRahbarlik,HorijdaMalakaOshirish])