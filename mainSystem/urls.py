from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('admin/',kafedralar_jadvali, name='admin'),
    path('user/<str:username>/',view_name, name='view_name'),
    path('update-OquvYiliFanlar-score/', update_OquvYiliFanlar_score, name='update_OquvYiliFanlar_score'),
    path('update-FaolInterfaolMetodlar-score/', update_FaolInterfaolMetodlar_score, name='update_FaolInterfaolMetodlar_score'),
    path('update-MustaqilTalimTopshiriqlari-score/', update_MustaqilTalimTopshiriqlari_score, name='update_MustaqilTalimTopshiriqlari_score'),
    path('update-FanVideoKontent-score/', update_FanVideoKontent_score, name='update_FanVideoKontent_score'),
    path('update-OqitishSifati-score/', update_OqitishSifati_score, name='update_OqitishSifati_score'),
    path('update-NashrEtilganDarsliklar/', update_NashrEtilganDarsliklar, name='update_NashrEtilganDarsliklar'),
    path('update-ScopusWebOfScience/', update_ScopusWebOfScience, name='update_ScopusWebOfScience'),
    path('update-OAKJurnaliMaqola/', update_OAKJurnaliMaqola, name='update_OAKJurnaliMaqola'),
    path('update-HIndex/', update_HIndex, name='update_HIndex'),
    path('update-KonferensiyaMaqola/', update_KonferensiyaMaqola, name='update_KonferensiyaMaqola'),
    path('update-LoyihalarTayyorlash/', update_LoyihalarTayyorlash, name='update_LoyihalarTayyorlash'),
    path('update-LoyihaMoliya/', update_LoyihaMoliya, name='update_LoyihaMoliya'),
    path('update-AKTDasturlar/', update_AKTDasturlar, name='update_AKTDasturlar'),
    path('update-TalabaIlmiyFaoliyati/', update_TalabaIlmiyFaoliyati, name='update_TalabaIlmiyFaoliyati'),
    path('update-TarbiyaTadbirlar/', update_TarbiyaTadbirlar, name='update_TarbiyaTadbirlar'),
    path('update-DarstanTashqariTadbirlar/', update_DarstanTashqariTadbirlar, name='update_DarstanTashqariTadbirlar'),
    path('update-TalabalarTurarJoyTadbirlar/', update_TalabalarTurarJoyTadbirlar, name='update_TalabalarTurarJoyTadbirlar'),
    path('update-OtaOnalarIshlash/', update_OtaOnalarIshlash, name='update_OtaOnalarIshlash'),
    path('update-AxborotMurobbiylikSoat/', update_AxborotMurobbiylikSoat, name='update_AxborotMurobbiylikSoat'),
    path('update-MuhimTashabbuslarIshlari/', update_MuhimTashabbuslarIshlari, name='update_MuhimTashabbuslarIshlari'),
    path('update-BirZiyoliBirMahalla/', update_BirZiyoliBirMahalla, name='update_BirZiyoliBirMahalla'),
    path('update-DarslikYokiQollanma/', update_DarslikYokiQollanma, name='update_DarslikYokiQollanma'),
    path('update-DissertationHimoya/', update_DissertationHimoya, name='update_DissertationHimoya'),
    path('update-IlmiyRahbarlik/', update_IlmiyRahbarlik, name='update_IlmiyRahbarlik'),
    path('update-HorijdaMalakaOshirish/', update_HorijdaMalakaOshirish, name='update_HorijdaMalakaOshirish'),
    path('', all_data_view, name='home'),
]
