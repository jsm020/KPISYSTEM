from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render,redirect
from .models import *
from django.db.models import Sum
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.apps import apps
def calculate_progress(queryset, max_score):
    """
    Helper function to calculate total score and progress percentage.
    """
    total_score = queryset.aggregate(Sum('score'))['score__sum'] or 0
    progress_percent = (total_score / max_score) * 100 if max_score > 0 else 0
    return total_score, progress_percent


@login_required
def all_data_view(request):
    if request.method == 'POST' and 'fvk_form_submit' in request.POST:
        form_fvk = FanVideoKontentForm(request.POST, user=request.user)
        if form_fvk.is_valid():
            maqola_instance = form_fvk.save(commit=False)
            maqola_instance.user = request.user
            maqola_instance.save()
            return redirect('home')
    else:
        form_fvk = FanVideoKontentForm(user=request.user)

    if request.method == 'POST' and 'ned_form_submit' in request.POST:
        form_ned = NashrEtilganDarsliklarForm(request.POST, request.FILES, user=request.user)  # request.FILES qo'shildi
        if form_ned.is_valid():
            maqola_instance = form_ned.save(commit=False)
            maqola_instance.user = request.user  # Foydalanuvchini qo'shish
            maqola_instance.save()
            return redirect('home')
    else:
        form_ned = NashrEtilganDarsliklarForm(user=request.user)

        #############################################################################
        #ikkinchi bulim#

    if request.method == 'POST' and 'sws_form_submit' in request.POST:
        form_sws = ScopusWebOfScienceForm(request.POST, request.FILES, user=request.user)  # request.FILES qo'shildi
        if form_sws.is_valid():
            maqola_instance = form_sws.save(commit=False)
            maqola_instance.user = request.user  # Foydalanuvchini qo'shish
            maqola_instance.save()
            return redirect('home')
    else:
        form_sws = ScopusWebOfScienceForm(user=request.user)

    if request.method == 'POST' and 'oam_form_submit' in request.POST:
        form_oam = OAKJurnaliMaqolaForm(request.POST, request.FILES, user=request.user)  # request.FILES qo'shildi
        if form_oam.is_valid():
            maqola_instance = form_oam.save(commit=False)
            maqola_instance.user = request.user  # Foydalanuvchini qo'shish
            maqola_instance.save()
            return redirect('home')
    else:
        form_oam = OAKJurnaliMaqolaForm(user=request.user)

    if request.method == 'POST' and 'h_form_submit' in request.POST:
        form_h = HIndexForm(request.POST, request.FILES, user=request.user)  # request.FILES qo'shildi
        if form_h.is_valid():
            maqola_instance = form_h.save(commit=False)
            maqola_instance.user = request.user  # Foydalanuvchini qo'shish
            maqola_instance.save()
            return redirect('home')
    else:
        form_h = HIndexForm(user=request.user)

    if request.method == 'POST' and 'konf_form_submit' in request.POST:
        form_konf = KonferensiyaMaqolaForm(request.POST, request.FILES, user=request.user)  # request.FILES qo'shildi
        if form_loyiha.is_valid():
            maqola_instance = form_konf.save(commit=False)
            maqola_instance.user = request.user  # Foydalanuvchini qo'shish
            maqola_instance.save()
            return redirect('home')
    else:
        form_konf = KonferensiyaMaqolaForm(user=request.user)
        
    if request.method == 'POST' and 'loyiha_form_submit' in request.POST:
        form_loyiha = LoyihalarTayyorlashForm(request.POST, request.FILES, user=request.user)  # request.FILES qo'shildi
        if form_loyiha.is_valid():
            maqola_instance = form_loyiha.save(commit=False)
            maqola_instance.user = request.user  # Foydalanuvchini qo'shish
            maqola_instance.save()
            return redirect('home')
    else:
        form_loyiha = LoyihalarTayyorlashForm(user=request.user)

    if request.method == 'POST' and 'loyiha_moliya_form_submit' in request.POST:
        form_loyiha_moliya = LoyihaMoliyaForm(request.POST, request.FILES, user=request.user)  # request.FILES qo'shildi
        if form_loyiha_moliya.is_valid():
            maqola_instance = form_loyiha_moliya.save(commit=False)
            maqola_instance.user = request.user  # Foydalanuvchini qo'shish
            maqola_instance.save()
            return redirect('home')
    else:
        form_loyiha_moliya = LoyihaMoliyaForm(user=request.user)


    if request.method == 'POST' and 'akt_form_submit' in request.POST:
        form_akt = AKTDasturlarForm(request.POST, request.FILES, user=request.user)  # request.FILES qo'shildi
        if form_akt.is_valid():
            maqola_instance = form_akt.save(commit=False)
            maqola_instance.user = request.user  # Foydalanuvchini qo'shish
            maqola_instance.save()
            return redirect('home')
    else:
        form_akt = AKTDasturlarForm(user=request.user)

    if request.method == 'POST' and 'tif_form_submit' in request.POST:
        form_tif = TalabaIlmiyFaoliyatiForm(request.POST, request.FILES, user=request.user)  # request.FILES qo'shildi
        if form_tif.is_valid():
            maqola_instance = form_tif.save(commit=False)
            maqola_instance.user = request.user  # Foydalanuvchini qo'shish
            maqola_instance.save()
            return redirect('home')
    else:
        form_tif = TalabaIlmiyFaoliyatiForm(user=request.user)

    if request.method == 'POST' and 'ttf_form_submit' in request.POST:
        form_ttf = TarbiyaTadbirlarForm(request.POST, request.FILES, user=request.user)  # request.FILES qo'shildi
        if form_ttf.is_valid():
            maqola_instance = form_ttf.save(commit=False)
            maqola_instance.user = request.user  # Foydalanuvchini qo'shish
            maqola_instance.save()
            return redirect('home')
    else:
        form_ttf = TarbiyaTadbirlarForm(user=request.user)

    if request.method == 'POST' and 'dttf_form_submit' in request.POST:
        form_dttf = DarstanTashqariTadbirlarForm(request.POST, request.FILES, user=request.user)  # request.FILES qo'shildi
        if form_dttf.is_valid():
            maqola_instance = form_dttf.save(commit=False)
            maqola_instance.user = request.user  # Foydalanuvchini qo'shish
            maqola_instance.save()
            return redirect('home')
    else:
        form_dttf = DarstanTashqariTadbirlarForm(user=request.user)


    if request.method == 'POST' and 'ttjtf_form_submit' in request.POST:
        form_ttjtf = TalabalarTurarJoyTadbirlarForm(request.POST, request.FILES, user=request.user)  # request.FILES qo'shildi
        if form_ttjtf.is_valid():
            maqola_instance = form_ttjtf.save(commit=False)
            maqola_instance.user = request.user  # Foydalanuvchini qo'shish
            maqola_instance.save()
            return redirect('home')
    else:
        form_ttjtf = TalabalarTurarJoyTadbirlarForm(user=request.user)

    if request.method == 'POST' and 'oaif_form_submit' in request.POST:
        form_oaif = OtaOnalarIshlashForm(request.POST, request.FILES, user=request.user)  # request.FILES qo'shildi
        if form_oaif.is_valid():
            maqola_instance = form_oaif.save(commit=False)
            maqola_instance.user = request.user  # Foydalanuvchini qo'shish
            maqola_instance.save()
            return redirect('home')
    else:
        form_oaif = OtaOnalarIshlashForm(user=request.user)

    if request.method == 'POST' and 'amsf_form_submit' in request.POST:
        form_amsf = AxborotMurobbiylikSoatForm(request.POST,user=request.user)  # request.FILES qo'shildi
        if form_amsf.is_valid():
            maqola_instance = form_amsf.save(commit=False)
            maqola_instance.user = request.user  # Foydalanuvchini qo'shish
            maqola_instance.save()
            return redirect('home')
    else:
        form_amsf = AxborotMurobbiylikSoatForm(user=request.user)

    if request.method == 'POST' and 'mtif_form_submit' in request.POST:
        form_mtif = MuhimTashabbuslarIshlariForm(request.POST,request.FILES,user=request.user)  # request.FILES qo'shildi
        if form_mtif.is_valid():
            maqola_instance = form_mtif.save(commit=False)
            maqola_instance.user = request.user  # Foydalanuvchini qo'shish
            maqola_instance.save()
            return redirect('home')
    else:
        form_mtif = MuhimTashabbuslarIshlariForm(user=request.user)

    if request.method == 'POST' and 'bzbmf_form_submit' in request.POST:
        form_bzbmf = BirZiyoliBirMahallaForm(request.POST,request.FILES,user=request.user)  # request.FILES qo'shildi
        if form_bzbmf.is_valid():
            maqola_instance = form_bzbmf.save(commit=False)
            maqola_instance.user = request.user  # Foydalanuvchini qo'shish
            maqola_instance.save()
            return redirect('home')
    else:
        form_bzbmf = BirZiyoliBirMahallaForm(user=request.user)

#############
    if request.method == 'POST' and 'dyqf_form_submit' in request.POST:
        form_dyqf = DarslikYokiQollanmaForm(request.POST,request.FILES,user=request.user)  # request.FILES qo'shildi
        if form_dyqf.is_valid():
            maqola_instance = form_dyqf.save(commit=False)
            maqola_instance.user = request.user  # Foydalanuvchini qo'shish
            maqola_instance.save()
            return redirect('home')
    else:
        form_dyqf = DarslikYokiQollanmaForm(user=request.user)

    if request.method == 'POST' and 'dhf_form_submit' in request.POST:
        form_dhf = DissertationHimoyaForm(request.POST,request.FILES,user=request.user)  # request.FILES qo'shildi
        if form_dhf.is_valid():
            maqola_instance = form_dhf.save(commit=False)
            maqola_instance.user = request.user  # Foydalanuvchini qo'shish
            maqola_instance.save()
            return redirect('home')
    else:
        form_dhf = DissertationHimoyaForm(user=request.user)

    if request.method == 'POST' and 'irf_form_submit' in request.POST:
        form_irf = IlmiyRahbarlikForm(request.POST,request.FILES,user=request.user)  # request.FILES qo'shildi
        if form_irf.is_valid():
            maqola_instance = form_irf.save(commit=False)
            maqola_instance.user = request.user  # Foydalanuvchini qo'shish
            maqola_instance.save()
            return redirect('home')
    else:
        form_irf = IlmiyRahbarlikForm(user=request.user)

    if request.method == 'POST' and 'hmof_form_submit' in request.POST:
        form_hmof = HorijdaMalakaOshirishForm(request.POST,request.FILES,user=request.user)  # request.FILES qo'shildi
        if form_hmof.is_valid():
            maqola_instance = form_hmof.save(commit=False)
            maqola_instance.user = request.user  # Foydalanuvchini qo'shish
            maqola_instance.save()
            return redirect('home')
    else:
        form_hmof = HorijdaMalakaOshirishForm(user=request.user)

    # Filtering objects based on the logged-in user
    scopus_maqolalar = ScopusWebOfScience.objects.filter(user=request.user)
    oak_maqolalar = OAKJurnaliMaqola.objects.filter(user=request.user)
    h_index = HIndex.objects.filter(user=request.user)
    konferensiya_maqolalar = KonferensiyaMaqola.objects.filter(user=request.user)
    loyihalar = LoyihalarTayyorlash.objects.filter(user=request.user)
    loyiha_moliya = LoyihaMoliya.objects.filter(user=request.user)
    AKT_dasturlar = AKTDasturlar.objects.filter(user=request.user)
    talaba_ilmiy = TalabaIlmiyFaoliyati.objects.filter(user=request.user)
    tarbiya_tadbirlar = TarbiyaTadbirlar.objects.filter(user=request.user)
    darstan_tashqari_tadbirlar = DarstanTashqariTadbirlar.objects.filter(user=request.user)
    talabalar_turar_joy = TalabalarTurarJoyTadbirlar.objects.filter(user=request.user)
    ota_onalar_ishlash = OtaOnalarIshlash.objects.filter(user=request.user)
    axborot_murobbiylik = AxborotMurobbiylikSoat.objects.filter(user=request.user)
    muhim_tashabbuslar = MuhimTashabbuslarIshlari.objects.filter(user=request.user)
    bir_ziyoli_bir_mahalla = BirZiyoliBirMahalla.objects.filter(user=request.user)
    oquv_yili_fanlar = OquvYiliFanlar.objects.filter(user=request.user)
    mustaqil_talim_topshiriqlari = MustaqilTalimTopshiriqlari.objects.filter(user=request.user)
    fan_video_kontent = FanVideoKontent.objects.filter(user=request.user)
    oqitish_sifati = OqitishSifati.objects.filter(user=request.user)
    nashr_etilgan_darsliklar = NashrEtilganDarsliklar.objects.filter(user=request.user)
    faol_interfaol_metodlar = FaolInterfaolMetodlar.objects.filter(user=request.user)
    darslik_yoki_qollanma = DarslikYokiQollanma.objects.filter(user=request.user)   
    dissertation_himoya = DissertationHimoya.objects.filter(user=request.user)
    ilmiy_rahbarlik = IlmiyRahbarlik.objects.filter(user=request.user)
    horijda_malaka_oshirish = HorijdaMalakaOshirish.objects.filter(user=request.user)
    #########3#################################3
    #Ўқув-методик фаолияти (максимал 30 балл)
    max_score = 2  
    total_score_oyf = oquv_yili_fanlar.aggregate(Sum('score'))['score__sum'] or 0  # Agar ballar bo'lmasa, 0
    progress_percent_oyf = (total_score_oyf / max_score) * 100 if max_score > 0 else 0
    #
    max_score = 4  
    total_score_fim = faol_interfaol_metodlar.aggregate(Sum('score'))['score__sum'] or 0  # Agar ballar bo'lmasa, 0
    progress_percent_fim = (total_score_fim / max_score) * 100 if max_score > 0 else 0
    # Maksimal ball
    max_score = 4  
    total_score_mtt = mustaqil_talim_topshiriqlari.aggregate(Sum('score'))['score__sum'] or 0  # Agar ballar bo'lmasa, 0
    progress_percent_mtt = (total_score_mtt / max_score) * 100 if max_score > 0 else 0
    #Maksimal ball
    max_score = 8  
    total_score_fvk = fan_video_kontent.aggregate(Sum('score'))['score__sum'] or 0  # Agar ballar bo'lmasa, 0
    progress_percent_fvk = (total_score_fvk / max_score) * 100 if max_score > 0 else 0
    #Maksimal ball
    max_score = 6  
    total_score_os = oqitish_sifati.aggregate(Sum('score'))['score__sum'] or 0  # Agar ballar bo'lmasa, 0
    progress_percent_os = (total_score_os / max_score) * 100 if max_score > 0 else 0
    #Maksimal ball
    max_score = 6  
    total_score_ned = nashr_etilgan_darsliklar.aggregate(Sum('score'))['score__sum'] or 0  # Agar ballar bo'lmasa, 0
    progress_percent_ned = (total_score_ned / max_score) * 100 if max_score > 0 else 0
    #ikinchi bulim
    max_score = 15  
    total_score_sws = scopus_maqolalar.aggregate(Sum('score'))['score__sum'] or 0  # Agar ballar bo'lmasa, 0
    progress_percent_sws = (total_score_sws / max_score) * 100 if max_score > 0 else 0
    #Maxsimal ball
    max_score = 5  
    total_score_h = h_index.aggregate(Sum('score'))['score__sum'] or 0  # Agar ballar bo'lmasa, 0
    progress_percent_h = (total_score_h / max_score) * 100 if max_score > 0 else 0
    #Maxsimal ball
    max_score = 5  
    total_score_oam = oak_maqolalar.aggregate(Sum('score'))['score__sum'] or 0  # Agar ballar bo'lmasa, 0
    progress_percent_oam = (total_score_oam / max_score) * 100 if max_score > 0 else 0
    #Maxsimal ball
    max_score = 2  
    total_score_konf = konferensiya_maqolalar.aggregate(Sum('score'))['score__sum'] or 0  # Agar ballar bo'lmasa, 0
    progress_percent_konf = (total_score_konf / max_score) * 100 if max_score > 0 else 0
    #Maxsimal ball
    max_score = 5  
    total_score_loyiha = loyihalar.aggregate(Sum('score'))['score__sum'] or 0  # Agar ballar bo'lmasa, 0
    progress_percent_loyiha = (total_score_loyiha / max_score) * 100 if max_score > 0 else 0
    #Maxsimal ball
    max_score = 6  
    total_score_loyiha_moliya = loyiha_moliya.aggregate(Sum('score'))['score__sum'] or 0  # Agar ballar bo'lmasa, 0
    progress_percent_loyiha_moliya = (total_score_loyiha_moliya / max_score) * 100 if max_score > 0 else 0
    #Maxsimal ball
    max_score = 3  
    total_score_akt = AKT_dasturlar.aggregate(Sum('score'))['score__sum'] or 0  # Agar ballar bo'lmasa, 0
    progress_percent_akt = (total_score_akt / max_score) * 100 if max_score > 0 else 0  
    #Maxsimal ball
    max_score = 5  
    total_score_ilmiy = talaba_ilmiy.aggregate(Sum('score'))['score__sum'] or 0  # Agar ballar bo'lmasa, 0
    progress_percent_ilmiy = (total_score_ilmiy / max_score) * 100 if max_score > 0 else 0  
    #Maxsimal ball
    max_score = 3  
    total_score_tartad = tarbiya_tadbirlar.aggregate(Sum('score'))['score__sum'] or 0  # Agar ballar bo'lmasa, 0
    progress_percent_tartad = (total_score_tartad / max_score) * 100 if max_score > 0 else 0
    
    #Maxsimal ball
    max_score = 4  
    total_score_dtt = darstan_tashqari_tadbirlar.aggregate(Sum('score'))['score__sum'] or 0  # Agar ballar bo'lmasa, 0
    progress_percent_dtt = (total_score_dtt / max_score) * 100 if max_score > 0 else 0
    
    #Maxsimal ball
    max_score = 3  
    total_score_ttj = talabalar_turar_joy.aggregate(Sum('score'))['score__sum'] or 0  # Agar ballar bo'lmasa, 0
    progress_percent_ttj = (total_score_ttj / max_score) * 100 if max_score > 0 else 0
  
    #Maxsimal ball
    max_score = 3  
    total_score_oai = ota_onalar_ishlash.aggregate(Sum('score'))['score__sum'] or 0  # Agar ballar bo'lmasa, 0
    progress_percent_oai = (total_score_oai / max_score) * 100 if max_score > 0 else 0
    #Maxsimal ball
    max_score = 3  
    total_score_axborot = axborot_murobbiylik.aggregate(Sum('score'))['score__sum'] or 0  # Agar ballar bo'lmasa, 0
    progress_percent_axborot = (total_score_axborot / max_score) * 100 if max_score > 0 else 0
    #Maxsimal ball
    max_score = 3  
    total_score_tashabbus = muhim_tashabbuslar.aggregate(Sum('score'))['score__sum'] or 0  # Agar ballar bo'lmasa, 0
    progress_percent_tashabbus = (total_score_tashabbus / max_score) * 100 if max_score > 0 else 0
    #Maxsimal ball
    max_score = 5  
    total_score_bzbm = bir_ziyoli_bir_mahalla.aggregate(Sum('score'))['score__sum'] or 0  # Agar ballar bo'lmasa, 0
    progress_percent_bzbm = (total_score_bzbm / max_score) * 100 if max_score > 0 else 0
    #Maxsimal ball
    max_score = 50 
    total_score_dyq = darslik_yoki_qollanma.aggregate(Sum('score'))['score__sum'] or 0  # Agar ballar bo'lmasa, 0
    progress_percent_dyq = (total_score_dyq / max_score) * 100 if max_score > 0 else 0
    #Maxsimal ball
    max_score = 100  
    total_score_dhimoya = dissertation_himoya.aggregate(Sum('score'))['score__sum'] or 0  # Agar ballar bo'lmasa, 0
    progress_percent_dhimoya = (total_score_dhimoya / max_score) * 100 if max_score > 0 else 0
    #Maxsimal ball
    max_score = 100  
    total_score_ilmiyrahbarlik = ilmiy_rahbarlik.aggregate(Sum('score'))['score__sum'] or 0  # Agar ballar bo'lmasa, 0
    progress_percent_ilmiyrahbarlik = (total_score_ilmiyrahbarlik / max_score) * 100 if max_score > 0 else 0
    #Maxsimal ball
    max_score = 100  
    total_score_hmo = horijda_malaka_oshirish.aggregate(Sum('score'))['score__sum'] or 0  # Agar ballar bo'lmasa, 0
    progress_percent_hmo = (total_score_hmo / max_score) * 100 if max_score > 0 else 0


    # Extracting model names using verbose_name
    scopus_model_name = ScopusWebOfScience._meta.verbose_name
    oak_model_name = OAKJurnaliMaqola._meta.verbose_name
    h_index_model_name = HIndex._meta.verbose_name
    konferensiya_model_name = KonferensiyaMaqola._meta.verbose_name
    loyihalar_model_name = LoyihalarTayyorlash._meta.verbose_name
    loyiha_moliya_model_name = LoyihaMoliya._meta.verbose_name
    AKT_dasturlar_model_name = AKTDasturlar._meta.verbose_name
    talaba_ilmiy_model_name = TalabaIlmiyFaoliyati._meta.verbose_name
    tarbiya_tadbirlar_model_name = TarbiyaTadbirlar._meta.verbose_name
    darstan_tashqari_tadbirlar_model_name = DarstanTashqariTadbirlar._meta.verbose_name
    talabalar_turar_joy_model_name = TalabalarTurarJoyTadbirlar._meta.verbose_name
    ota_onalar_model_name = OtaOnalarIshlash._meta.verbose_name
    axborot_murobbiylik_model_name = AxborotMurobbiylikSoat._meta.verbose_name
    muhim_tashabbuslar_model_name = MuhimTashabbuslarIshlari._meta.verbose_name
    bir_ziyoli_bir_mahalla_model_name = BirZiyoliBirMahalla._meta.verbose_name
    oquv_yili_fanlar_model_name = OquvYiliFanlar._meta.verbose_name
    mustaqil_talim_model_name = MustaqilTalimTopshiriqlari._meta.verbose_name
    fan_video_kontent_model_name = FanVideoKontent._meta.verbose_name
    oqitish_sifati_model_name = OqitishSifati._meta.verbose_name
    nashr_etilgan_darsliklar_model_name = NashrEtilganDarsliklar._meta.verbose_name
    faol_interfaol_metodlar_model_name = FaolInterfaolMetodlar._meta.verbose_name
    darslik_yoki_qollanma_name = DarslikYokiQollanma._meta.verbose_name
    dissertation_himoya_name = DissertationHimoya._meta.verbose_name
    ilmiy_rahbarlik_name = IlmiyRahbarlik._meta.verbose_name
    horijda_malaka_oshirish_name = HorijdaMalakaOshirish._meta.verbose_name
    

    context = {
        'form_sws':form_sws,
        'form_fvk':form_fvk,
        'form_ned':form_ned,
        'form_oam':form_oam,
        'form_h':form_h,
        'form_konf':form_konf,
        'form_loyiha':form_loyiha,
        'form_loyiha_moliya':form_loyiha_moliya,
        'form_akt':form_akt,
        'form_tif':form_tif,
        'form_ttf':form_ttf,
        'form_dttf':form_dttf,
        'form_ttjtf':form_ttjtf,
        'form_oaif':form_oaif,
        'form_amsf':form_amsf,
        'form_mtif':form_mtif,
        'form_bzbmf':form_bzbmf,
        'form_dyqf':form_dyqf,
        'form_dhf':form_dhf,
        'form_irf':form_irf,
        'form_hmof':form_hmof,
        # 'oquvyili_form':oquvyili_form,
        'total_score_oyf':total_score_oyf,
        'progress_percent_oyf':progress_percent_oyf,
        'total_score_fim':total_score_fim,
        'progress_percent_fim':progress_percent_fim, 
        'total_score_mtt':total_score_mtt,
        'progress_percent_mtt':progress_percent_mtt,
        'total_score_fvk':total_score_fvk,
        'progress_percent_fvk':progress_percent_fvk,
        'total_score_os':total_score_os,
        'progress_percent_os':progress_percent_os,
        'total_score_ned':total_score_ned,
        'progress_percent_ned':progress_percent_ned,
        'total_score_sws':total_score_sws,
        'progress_percent_sws':progress_percent_sws,
        'total_score_oam':total_score_oam,  
        'progress_percent_oam':progress_percent_oam,
        'total_score_h':total_score_h,  
        "progress_percent_h":progress_percent_h,
        'total_score_konf':total_score_konf,  
        'progress_percent_konf':progress_percent_konf,
        'total_score_loyiha':total_score_loyiha,
        'progress_percent_loyiha':progress_percent_loyiha,
        'total_score_loyiha_moliya':total_score_loyiha_moliya,
        'progress_percent_loyiha_moliya':progress_percent_loyiha_moliya,
        'total_score_akt':total_score_akt,
        'progress_percent_akt':progress_percent_akt,
        'total_score_ilmiy':total_score_ilmiy,
        'progress_percent_ilmiy':progress_percent_ilmiy,
        'total_score_tartad':total_score_tartad,
        'progress_percent_tartad':progress_percent_tartad,
        'total_score_dtt':total_score_dtt,
        'progress_percent_dtt':progress_percent_dtt, 
        'total_score_ttj':total_score_ttj,
        'progress_percent_ttj':progress_percent_ttj,
        'total_score_oai':total_score_oai,
        'progress_percent_oai':progress_percent_oai,
        'total_score_axborot':total_score_axborot,
        'progress_percent_axborot':progress_percent_axborot,
        'total_score_tashabbus':total_score_tashabbus,
        'progress_percent_tashabbus':progress_percent_tashabbus,
        'total_score_bzbm':total_score_bzbm,
        'progress_percent_bzbm':progress_percent_bzbm,
        'total_score_dyq':total_score_dyq,
        'progress_percent_dyq':progress_percent_dyq,
        'total_score_dhimoya':total_score_dhimoya,
        'progress_percent_dhimoya':progress_percent_dhimoya,
        'total_score_ilmiyrahbarlik':total_score_ilmiyrahbarlik,
        'progress_percent_ilmiyrahbarlik':progress_percent_ilmiyrahbarlik,
        'total_score_hmo':total_score_hmo,
        'progress_percent_hmo':progress_percent_hmo,
        #########################################################################
        'scopus_maqolalar': scopus_maqolalar,
        'oak_maqolalar': oak_maqolalar,
        'h_index': h_index,
        'konferensiya_maqolalar': konferensiya_maqolalar,
        'loyihalar': loyihalar,
        'loyiha_moliya': loyiha_moliya,
        'AKT_dasturlar': AKT_dasturlar,
        'talaba_ilmiy': talaba_ilmiy,
        'tarbiya_tadbirlar': tarbiya_tadbirlar,
        'darstan_tashqari_tadbirlar': darstan_tashqari_tadbirlar,
        'talabalar_turar_joy': talabalar_turar_joy,
        'ota_onalar': ota_onalar_ishlash,
        'axborot_murobbiylik': axborot_murobbiylik,
        'muhim_tashabbuslar': muhim_tashabbuslar,
        'bir_ziyoli_bir_mahalla': bir_ziyoli_bir_mahalla,
        'oquv_yili_fanlar': oquv_yili_fanlar,
        'mustaqil_talim': mustaqil_talim_topshiriqlari,
        'fan_video_kontent': fan_video_kontent,
        'oqitish_sifati': oqitish_sifati,
        'nashr_etilgan_darsliklar': nashr_etilgan_darsliklar,
        'faol_interfaol_metodlar': faol_interfaol_metodlar,
        "darslik_yoki_qollanma":darslik_yoki_qollanma,
        "dissertation_himoya":dissertation_himoya,
        "ilmiy_rahbarlik":ilmiy_rahbarlik,
        "horijda_malaka_oshirish":horijda_malaka_oshirish,
        # Add model names to the context
        'scopus_model_name': scopus_model_name,
        'oak_model_name': oak_model_name,
        'h_index_model_name': h_index_model_name,
        'konferensiya_model_name': konferensiya_model_name,
        'loyihalar_model_name': loyihalar_model_name,
        'loyiha_moliya_model_name': loyiha_moliya_model_name,
        'AKT_dasturlar_model_name': AKT_dasturlar_model_name,
        'talaba_ilmiy_model_name': talaba_ilmiy_model_name,
        'tarbiya_tadbirlar_model_name': tarbiya_tadbirlar_model_name,
        'darstan_tashqari_tadbirlar_model_name': darstan_tashqari_tadbirlar_model_name,
        'talabalar_turar_joy_model_name': talabalar_turar_joy_model_name,
        'ota_onalar_model_name': ota_onalar_model_name,
        'axborot_murobbiylik_model_name': axborot_murobbiylik_model_name,
        'muhim_tashabbuslar_model_name': muhim_tashabbuslar_model_name,
        'bir_ziyoli_bir_mahalla_model_name': bir_ziyoli_bir_mahalla_model_name,
        'oquv_yili_fanlar_model_name': oquv_yili_fanlar_model_name,
        'mustaqil_talim_model_name': mustaqil_talim_model_name,
        'fan_video_kontent_model_name': fan_video_kontent_model_name,
        'oqitish_sifati_model_name': oqitish_sifati_model_name,
        'nashr_etilgan_darsliklar_model_name': nashr_etilgan_darsliklar_model_name,
        'faol_interfaol_metodlar_model_name': faol_interfaol_metodlar_model_name,
        'darslik_yoki_qollanma_name':darslik_yoki_qollanma_name,
        'dissertation_himoya_name':dissertation_himoya_name,
        'ilmiy_rahbarlik_name':ilmiy_rahbarlik_name,
        'horijda_malaka_oshirish_name':horijda_malaka_oshirish_name,
    }

    return render(request, 'custom_page.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Foydalanuvchini autentifikatsiya qilish
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Foydalanuvchini tizimga kirgizish
            login(request, user)
            
            # Agar foydalanuvchi superuser bo'lsa, admin sahifasiga yo'naltirish
            if user.is_superuser:
                return redirect('admin')  # Admin sahifasiga yo'naltirish
            else:
                return redirect('home')  # Oddiy foydalanuvchini asosiy sahifaga yo'naltirish
        else:
            # Login yoki parol xato bo'lsa xabar chiqarish
            messages.error(request, 'Login yoki parol noto‘g‘ri.')
    return render(request, 'login.html')  # Login sahifasini qayta ko'rsatish


def logout_view(request):
    logout(request)
    return redirect('login')  # Logoutdan keyin login sahifasiga yo'naltirish

def custom_error_view(request, exception=None):
    return render(request, 'error.html')





def is_admin(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_superuser:  # Foydalanuvchi superuser ekanligini tekshirish
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Sizda ushbu sahifaga kirish uchun huquq yo'q.")  # Kirish taqiqlangan
    return wrapper

@is_admin
def kafedralar_jadvali(request):
    users = User.objects.all()  # Fetch all users
    context = {
        'users': users
    }
    return render(request, 'main.html', context)
def view_name(request, username):
    selected_user = get_object_or_404(User, username=username)
    scopus_maqolalar = ScopusWebOfScience.objects.filter(user=selected_user)
    oak_maqolalar = OAKJurnaliMaqola.objects.filter(user=selected_user)
    h_index = HIndex.objects.filter(user=selected_user)
    konferensiya_maqolalar = KonferensiyaMaqola.objects.filter(user=selected_user)
    loyihalar = LoyihalarTayyorlash.objects.filter(user=selected_user)
    loyiha_moliya = LoyihaMoliya.objects.filter(user=selected_user)
    AKT_dasturlar = AKTDasturlar.objects.filter(user=selected_user)
    talaba_ilmiy = TalabaIlmiyFaoliyati.objects.filter(user=selected_user)
    tarbiya_tadbirlar = TarbiyaTadbirlar.objects.filter(user=selected_user)
    darstan_tashqari_tadbirlar = DarstanTashqariTadbirlar.objects.filter(user=selected_user)
    talabalar_turar_joy = TalabalarTurarJoyTadbirlar.objects.filter(user=selected_user)
    ota_onalar_ishlash = OtaOnalarIshlash.objects.filter(user=selected_user)
    axborot_murobbiylik = AxborotMurobbiylikSoat.objects.filter(user=selected_user)
    muhim_tashabbuslar = MuhimTashabbuslarIshlari.objects.filter(user=selected_user)
    bir_ziyoli_bir_mahalla = BirZiyoliBirMahalla.objects.filter(user=selected_user)
    oquv_yili_fanlar = OquvYiliFanlar.objects.filter(user=selected_user)
    mustaqil_talim_topshiriqlari = MustaqilTalimTopshiriqlari.objects.filter(user=selected_user)
    fan_video_kontent = FanVideoKontent.objects.filter(user=selected_user)
    oqitish_sifati = OqitishSifati.objects.filter(user=selected_user)
    nashr_etilgan_darsliklar = NashrEtilganDarsliklar.objects.filter(user=selected_user)
    faol_interfaol_metodlar = FaolInterfaolMetodlar.objects.filter(user=selected_user)
    darslik_yoki_qollanma = DarslikYokiQollanma.objects.filter(user=selected_user)   
    dissertation_himoya = DissertationHimoya.objects.filter(user=selected_user)
    ilmiy_rahbarlik = IlmiyRahbarlik.objects.filter(user=selected_user)
    horijda_malaka_oshirish = HorijdaMalakaOshirish.objects.filter(user=selected_user)
    scores = {
            'oyf': calculate_progress(oquv_yili_fanlar, 2),
            'fim': calculate_progress(faol_interfaol_metodlar, 4),
            'mtt': calculate_progress(mustaqil_talim_topshiriqlari, 4),
            'fvk': calculate_progress(fan_video_kontent, 8),
            'os': calculate_progress(oqitish_sifati, 6),
            'ned': calculate_progress(nashr_etilgan_darsliklar, 6),
            'sws': calculate_progress(scopus_maqolalar, 15),
            'h': calculate_progress(h_index, 5),
            'oam': calculate_progress(oak_maqolalar, 5),
            'konf': calculate_progress(konferensiya_maqolalar, 2),
            'loyiha': calculate_progress(loyihalar, 5),
            'loyiha_moliya': calculate_progress(loyiha_moliya, 6),
            'akt': calculate_progress(AKT_dasturlar, 3),
            'ilmiy': calculate_progress(talaba_ilmiy, 5),
            'tartad': calculate_progress(tarbiya_tadbirlar, 3),
            'dtt': calculate_progress(darstan_tashqari_tadbirlar, 4),
            'ttj': calculate_progress(talabalar_turar_joy, 3),
            'oai': calculate_progress(ota_onalar_ishlash, 3),
            'axborot': calculate_progress(axborot_murobbiylik, 3),
            'tashabbus': calculate_progress(muhim_tashabbuslar, 3),
            'bzbm': calculate_progress(bir_ziyoli_bir_mahalla, 5),
            'dyq': calculate_progress(darslik_yoki_qollanma, 50),
            'dhimoya': calculate_progress(dissertation_himoya, 100),
            'ilmiyrahbarlik': calculate_progress(ilmiy_rahbarlik, 100),
            'hmo':calculate_progress(horijda_malaka_oshirish,100),
        }


    # Extracting model names using verbose_name
    scopus_model_name = ScopusWebOfScience._meta.verbose_name
    oak_model_name = OAKJurnaliMaqola._meta.verbose_name
    h_index_model_name = HIndex._meta.verbose_name
    konferensiya_model_name = KonferensiyaMaqola._meta.verbose_name
    loyihalar_model_name = LoyihalarTayyorlash._meta.verbose_name
    loyiha_moliya_model_name = LoyihaMoliya._meta.verbose_name
    AKT_dasturlar_model_name = AKTDasturlar._meta.verbose_name
    talaba_ilmiy_model_name = TalabaIlmiyFaoliyati._meta.verbose_name
    tarbiya_tadbirlar_model_name = TarbiyaTadbirlar._meta.verbose_name
    darstan_tashqari_tadbirlar_model_name = DarstanTashqariTadbirlar._meta.verbose_name
    talabalar_turar_joy_model_name = TalabalarTurarJoyTadbirlar._meta.verbose_name
    ota_onalar_model_name = OtaOnalarIshlash._meta.verbose_name
    axborot_murobbiylik_model_name = AxborotMurobbiylikSoat._meta.verbose_name
    muhim_tashabbuslar_model_name = MuhimTashabbuslarIshlari._meta.verbose_name
    bir_ziyoli_bir_mahalla_model_name = BirZiyoliBirMahalla._meta.verbose_name
    oquv_yili_fanlar_model_name = OquvYiliFanlar._meta.verbose_name
    mustaqil_talim_model_name = MustaqilTalimTopshiriqlari._meta.verbose_name
    fan_video_kontent_model_name = FanVideoKontent._meta.verbose_name
    oqitish_sifati_model_name = OqitishSifati._meta.verbose_name
    nashr_etilgan_darsliklar_model_name = NashrEtilganDarsliklar._meta.verbose_name
    faol_interfaol_metodlar_model_name = FaolInterfaolMetodlar._meta.verbose_name
    darslik_yoki_qollanma_name = DarslikYokiQollanma._meta.verbose_name
    dissertation_himoya_name = DissertationHimoya._meta.verbose_name
    ilmiy_rahbarlik_name = IlmiyRahbarlik._meta.verbose_name
    horijda_malaka_oshirish_name = HorijdaMalakaOshirish._meta.verbose_name
    name = selected_user.first_name
    last_name = selected_user.last_name
    context = {
        'scores':scores,
        'name':name,
        "last_name":last_name,
        # 'oquvyili_form':oquvyili_form,
        #########################################################################
        'scopus_maqolalar': scopus_maqolalar,
        'oak_maqolalar': oak_maqolalar,
        'h_index': h_index,
        'konferensiya_maqolalar': konferensiya_maqolalar,
        'loyihalar': loyihalar,
        'loyiha_moliya': loyiha_moliya,
        'AKT_dasturlar': AKT_dasturlar,
        'talaba_ilmiy': talaba_ilmiy,
        'tarbiya_tadbirlar': tarbiya_tadbirlar,
        'darstan_tashqari_tadbirlar': darstan_tashqari_tadbirlar,
        'talabalar_turar_joy': talabalar_turar_joy,
        'ota_onalar': ota_onalar_ishlash,
        'axborot_murobbiylik': axborot_murobbiylik,
        'muhim_tashabbuslar': muhim_tashabbuslar,
        'bir_ziyoli_bir_mahalla': bir_ziyoli_bir_mahalla,
        'oquv_yili_fanlar': oquv_yili_fanlar,
        'mustaqil_talim': mustaqil_talim_topshiriqlari,
        'fan_video_kontent': fan_video_kontent,
        'oqitish_sifati': oqitish_sifati,
        'nashr_etilgan_darsliklar': nashr_etilgan_darsliklar,
        'faol_interfaol_metodlar': faol_interfaol_metodlar,
        "darslik_yoki_qollanma":darslik_yoki_qollanma,
        "dissertation_himoya":dissertation_himoya,
        "ilmiy_rahbarlik":ilmiy_rahbarlik,
        "horijda_malaka_oshirish":horijda_malaka_oshirish,
        # Add model names to the context
        'scopus_model_name': scopus_model_name,
        'oak_model_name': oak_model_name,
        'h_index_model_name': h_index_model_name,
        'konferensiya_model_name': konferensiya_model_name,
        'loyihalar_model_name': loyihalar_model_name,
        'loyiha_moliya_model_name': loyiha_moliya_model_name,
        'AKT_dasturlar_model_name': AKT_dasturlar_model_name,
        'talaba_ilmiy_model_name': talaba_ilmiy_model_name,
        'tarbiya_tadbirlar_model_name': tarbiya_tadbirlar_model_name,
        'darstan_tashqari_tadbirlar_model_name': darstan_tashqari_tadbirlar_model_name,
        'talabalar_turar_joy_model_name': talabalar_turar_joy_model_name,
        'ota_onalar_model_name': ota_onalar_model_name,
        'axborot_murobbiylik_model_name': axborot_murobbiylik_model_name,
        'muhim_tashabbuslar_model_name': muhim_tashabbuslar_model_name,
        'bir_ziyoli_bir_mahalla_model_name': bir_ziyoli_bir_mahalla_model_name,
        'oquv_yili_fanlar_model_name': oquv_yili_fanlar_model_name,
        'mustaqil_talim_model_name': mustaqil_talim_model_name,
        'fan_video_kontent_model_name': fan_video_kontent_model_name,
        'oqitish_sifati_model_name': oqitish_sifati_model_name,
        'nashr_etilgan_darsliklar_model_name': nashr_etilgan_darsliklar_model_name,
        'faol_interfaol_metodlar_model_name': faol_interfaol_metodlar_model_name,
        'darslik_yoki_qollanma_name':darslik_yoki_qollanma_name,
        'dissertation_himoya_name':dissertation_himoya_name,
        'ilmiy_rahbarlik_name':ilmiy_rahbarlik_name,
        'horijda_malaka_oshirish_name':horijda_malaka_oshirish_name,
    }

    return render(request, 'submit_page.html', context)


def update_score_generic(request, submit_button_name, model_name, redirect_view_name):
    if request.method == 'POST' and submit_button_name in request.POST:
        item_id = request.POST.get('item_id')
        score = request.POST.get('score')
        izoh = request.POST.get('izoh')  # Izoh maydonini olish
        
        # Dinamik tarzda model klassini olish
        try:
            model_class = apps.get_model('mainSystem', model_name)  # 'your_app_name' ni to'g'ri dastur nomi bilan almashtiring
            item = model_class.objects.get(id=item_id)
            print(item.score)
            
            # Agar foydalanuvchi allaqachon bir marta yangilagan bo'lsa, qaytish
            if item.score is not None:  
                return HttpResponse(f"Siz bu ob'ekt uchun allaqachon score yoki izohni o'zgartirgansiz.", status=403)

            # Agar yangilanish kerak bo'lsa
            if score:
                item.score = score
            if izoh:
                item.izoh = izoh
            
            item.save()
                
            return redirect(redirect_view_name)
        
        except model_class.DoesNotExist:
            return HttpResponse(f"{model_name} ID {item_id} bilan topilmadi", status=404)
        
        except LookupError:
            return HttpResponse(f"Model {model_name} mavjud emas.", status=500)
        
    return redirect(redirect_view_name)

def update_OquvYiliFanlar_score(request):
    return update_score_generic(request, 'update_score_submit_oquv_yili_fanlar', 'OquvYiliFanlar', 'admin')
def update_FaolInterfaolMetodlar_score(request):
    return update_score_generic(request, 'update_score_submit_FaolInterfaolMetodlar', 'FaolInterfaolMetodlar', 'admin')
def update_MustaqilTalimTopshiriqlari_score(request):
    return update_score_generic(request, 'update_score_submit_MustaqilTalimTopshiriqlari', 'MustaqilTalimTopshiriqlari', 'admin')
def update_FanVideoKontent_score(request):
    return update_score_generic(request, 'update_score_submit_FanVideoKontent', 'FanVideoKontent', 'admin')
def update_OqitishSifati_score(request):
    return update_score_generic(request, 'update_score_submit_OqitishSifati', 'OqitishSifati', 'admin')
def update_NashrEtilganDarsliklar(request):
    return update_score_generic(request, 'update_score_submit_NashrEtilganDarsliklar', 'NashrEtilganDarsliklar', 'admin')
def update_ScopusWebOfScience(request):
    return update_score_generic(request, 'update_score_submit_ScopusWebOfScience', 'ScopusWebOfScience', 'admin')
def update_OAKJurnaliMaqola(request):
    return update_score_generic(request, 'update_score_submit_OAKJurnaliMaqola', 'OAKJurnaliMaqola', 'admin')
def update_HIndex(request):
    return update_score_generic(request, 'update_score_submit_HIndex', 'HIndex', 'admin')
def update_KonferensiyaMaqola(request):
    return update_score_generic(request, 'update_score_submit_KonferensiyaMaqola', 'KonferensiyaMaqola', 'admin')
def update_LoyihalarTayyorlash(request):
    return update_score_generic(request, 'update_score_submit_LoyihalarTayyorlash', 'LoyihalarTayyorlash', 'admin')
def update_LoyihaMoliya(request):
    return update_score_generic(request, 'update_score_submit_LoyihaMoliya', 'LoyihaMoliya', 'admin')
def update_AKTDasturlar(request):
    return update_score_generic(request, 'update_score_submit_AKTDasturlar', 'AKTDasturlar', 'admin')
def update_TalabaIlmiyFaoliyati(request):
    return update_score_generic(request, 'update_score_submit_TalabaIlmiyFaoliyati', 'TalabaIlmiyFaoliyati', 'admin')
def update_TarbiyaTadbirlar(request):
    return update_score_generic(request, 'update_score_submit_TarbiyaTadbirlar', 'TarbiyaTadbirlar', 'admin')
def update_DarstanTashqariTadbirlar(request):
    return update_score_generic(request, 'update_score_submit_DarstanTashqariTadbirlar', 'DarstanTashqariTadbirlar', 'admin')
def update_TalabalarTurarJoyTadbirlar(request):
    return update_score_generic(request, 'update_score_submit_TalabalarTurarJoyTadbirlar', 'TalabalarTurarJoyTadbirlar', 'admin')
def update_OtaOnalarIshlash(request):
    return update_score_generic(request, 'update_score_submit_OtaOnalarIshlash', 'OtaOnalarIshlash', 'admin')
def update_AxborotMurobbiylikSoat(request):
    return update_score_generic(request, 'update_score_submit_AxborotMurobbiylikSoat', 'AxborotMurobbiylikSoat', 'admin')
def update_MuhimTashabbuslarIshlari(request):
    return update_score_generic(request, 'update_score_submit_MuhimTashabbuslarIshlari', 'MuhimTashabbuslarIshlari', 'admin')
def update_BirZiyoliBirMahalla(request):
    return update_score_generic(request, 'update_score_submit_BirZiyoliBirMahalla', 'BirZiyoliBirMahalla', 'admin')
def update_DarslikYokiQollanma(request):
    return update_score_generic(request, 'update_score_submit_DarslikYokiQollanma', 'DarslikYokiQollanma', 'admin')
def update_DissertationHimoya(request):
    return update_score_generic(request, 'update_score_submit_DissertationHimoya', 'DissertationHimoya', 'admin')
def update_IlmiyRahbarlik(request):
    return update_score_generic(request, 'update_score_submit_IlmiyRahbarlik', 'IlmiyRahbarlik', 'admin')
def update_HorijdaMalakaOshirish(request):
    return update_score_generic(request, 'update_score_submit_HorijdaMalakaOshirish', 'HorijdaMalakaOshirish', 'admin')
