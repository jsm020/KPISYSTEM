from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator

# 1. O'quv yili fanlar bo'yicha resurslar
class OquvYiliFanlar(models.Model):
    score = models.DecimalField(null=True, blank=True, verbose_name="Baholash",max_digits=2,decimal_places=1,validators=[MaxValueValidator(2.00)])
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    izoh = models.TextField()

    class Meta:
        verbose_name = "O'quv yili davomida fanlar bo'yicha resurslarni HEMIS tizimiga joylashtirish"
        verbose_name_plural = "O'quv yili davomida fanlar bo'yicha resurslarni HEMIS tizimiga joylashtirish"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - O'quv yili fanlar bo'yicha resurslar"

# 2. Faol va interfaol metodlar
class FaolInterfaolMetodlar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.DecimalField(null=True, blank=True, verbose_name="Baholash",max_digits=2,decimal_places=1,validators=[MaxValueValidator(4.00)])
    izoh = models.TextField()

    class Meta:
        verbose_name = "Faol va interfaol metod"
        verbose_name_plural = "Faol va interfaol metodlar"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - Faol va interfaol metodlar"
    


# 3. Mustaqil ta'lim topshiriqlari
class MustaqilTalimTopshiriqlari(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.DecimalField(null=True, blank=True, verbose_name="Baholash",max_digits=2,decimal_places=1,validators=[MaxValueValidator(4.00)])
    izoh = models.TextField()

    class Meta:
        verbose_name = "Mustaqil ta'lim topshiriqlari"
        verbose_name_plural = "Mustaqil ta'lim topshiriqlari"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - Mustaqil ta'lim topshiriqlari"

# 4. Fan video kontent
class FanVideoKontent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.DecimalField(null=True, blank=True, verbose_name="Baholash",max_digits=2,decimal_places=1,validators=[MaxValueValidator(8.00)])
    link = models.URLField(verbose_name="Maqolaga havola")
    izoh = models.TextField()

    class Meta:
        verbose_name = "Fan video kontenti"
        verbose_name_plural = "Fan video kontentlari"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - Fan video kontenti"
class OqitishSifati(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    talim_sifat_xulosasi = models.DecimalField(null=True, blank=True, verbose_name="ta'lim sifatini nazorat qilish bo‘limi xulosasi bo‘yicha",max_digits=2,decimal_places=1,validators=[MaxValueValidator(3.00)])
    talim_sifat = models.DecimalField(null=True, blank=True, verbose_name="talabalardan o‘tkazilgan so‘rovnomalar natijalari bo‘icha",max_digits=2,decimal_places=1,validators=[MaxValueValidator(3.00)])
    score = models.DecimalField(null=True, blank=True, verbose_name="Umumiy ball", editable=False,max_digits=2,decimal_places=1,validators=[MaxValueValidator(6.00)])

    izoh = models.TextField()

    class Meta:
        verbose_name = "O'qitish sifati baholanishi"
        verbose_name_plural = "O'qitish sifati baholanishi"

    def save(self, *args, **kwargs):
        # Automatically calculate score as the sum of talim_sifat and talim_sifat_xulosasi
        if self.talim_sifat is not None and self.talim_sifat_xulosasi is not None:
            self.score = self.talim_sifat + self.talim_sifat_xulosasi
        else:
            self.score = 0  # Handle case where either value is None
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - O'qitish sifati baholanishi"

# 6. Nashr etilgan darsliklar va uslubiy ko'rsatmalar
class NashrEtilganDarsliklar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    maqola = models.FileField(
        upload_to='nashr_etilgan_darsliklar_files/',
        verbose_name="Nashr etilgan darsliklar, qo'llanmalar va uslubiy ko'rsatmalar"
    )
    score = models.DecimalField(null=True, blank=True, verbose_name="Baholash",max_digits=2,decimal_places=1,validators=[MaxValueValidator(6.00)])
    izoh = models.TextField()

    class Meta:
        verbose_name = "Nashr etilgan darslik"
        verbose_name_plural = "Nashr etilgan darsliklar"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - Nashr etilgan darsliklar"

    #############################################################################3
# 1. Scopus va Web of Science xalqaro jurnallarida maqola chop etganligi
class ScopusWebOfScience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Foydalanuvchiga bog'langan
    maqola = models.FileField(
        upload_to='scopus_web_of_science_files/',
        verbose_name="Scopus va Web of Science xalqaro jurnallarida maqola chop etganligi"
    )
    link = models.URLField(verbose_name="Maqolaga havola")
    score = models.DecimalField(null=True, blank=True, verbose_name="Baholash",max_digits=2,decimal_places=1,validators=[MaxValueValidator(15.00)])
    izoh = models.TextField() 

    class Meta:
        verbose_name = "Scopus va Web of Science xalqaro ilmiy-texnik bazasiga kiruvchi jurnalda maqola chop etganligi"
        verbose_name_plural = "Scopus va Web of Science xalqaro ilmiy-texnik bazasiga kiruvchi jurnalda maqola chop etganligi"

    def __str__(self):
        return f"{self.user.username} - Scopus/Web of Science maqola"


# 2. OAK tasarrufidagi jurnalda maqola chop etganligi
class OAKJurnaliMaqola(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    maqola = models.FileField(
        upload_to='oak_jurnal_maqolalar_files/',
        verbose_name="OAK tasarrufidagi jurnalda maqola chop etganligi"
    )
    link = models.URLField(verbose_name="Maqolaga havola")
    score = models.DecimalField(null=True, blank=True, verbose_name="Baholash",max_digits=2,decimal_places=1,validators=[MaxValueValidator(5.00)])
    izoh = models.TextField()

    class Meta:
        verbose_name = "OAK tasarrufidagi jurnalda maqola chop etganligi"
        verbose_name_plural = "OAK tasarrufidagi jurnalda maqola chop etganligi"

    def __str__(self):
        return f"{self.user.username} - OAK maqola"


# 3. Scopus, Web of Science va Google Scholar h-indeksiga egaligi
class HIndex(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    maqola = models.FileField(
        upload_to='h_indeks_files/',
        verbose_name="Scopus, Web of Science va Google Scholar h-indeksiga egaligi"
    )
    link = models.URLField(verbose_name="H-indeks hujjatiga havola")
    score = models.DecimalField(null=True, blank=True, verbose_name="Baholash",max_digits=2,decimal_places=1,validators=[MaxValueValidator(5.00)])
    izoh = models.TextField()

    class Meta:
        verbose_name = "Scopus, Web of Science va Google Scholar h-indeksiga egaligi"
        verbose_name_plural = "Scopus, Web of Science va Google Scholar h-indeksiga egaligi"

    def __str__(self):
        return f"{self.user.username} - H-indeks hujjat"


# 4. Xalqaro va Respublika konferensiyalarida ma'ruza
class KonferensiyaMaqola(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    maqola = models.FileField(
        upload_to='konferensiya_maqolalari_files/',
        verbose_name="Xalqaro va Respublika konferensiyalaridagi ma'ruza"
    )
    link = models.URLField(verbose_name="Ma'ruzaga havola")
    score = models.DecimalField(null=True, blank=True, verbose_name="Baholash",max_digits=2,decimal_places=1,validators=[MaxValueValidator(2.00)])
    izoh = models.TextField()

    class Meta:
        verbose_name = "Xalqaro va Respublika konferensiyalarida ma'ruza"
        verbose_name_plural = "Xalqaro va Respublika konferensiyalarida ma'ruza"

    def __str__(self):
        return f"{self.user.username} - Konferensiya ma'ruza"


# 5. Loyiha tayyorlash
class LoyihalarTayyorlash(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    maqola = models.FileField(
        upload_to='loyihalar_tayyorlash_files/',
        verbose_name="Loyiha tayyorlash"
    )
    score = models.DecimalField(null=True, blank=True, verbose_name="Baholash",max_digits=2,decimal_places=1,validators=[MaxValueValidator(5.00)])
    izoh = models.TextField()

    class Meta:
        verbose_name = "Loyiha tayyorlash"
        verbose_name_plural = "Loyiha tayyorlash"

    def __str__(self):
        return f"{self.user.username} - Loyiha"


# 6. Ilmiy loyihalarni moliyalashtirish
class LoyihaMoliya(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    maqola = models.FileField(
        upload_to='loyiha_moliya_files/',
        verbose_name="Ilmiy loyihalarni moliyalashtirish"
    )
    score = models.DecimalField(null=True, blank=True, verbose_name="Baholash",max_digits=2,decimal_places=1,validators=[MaxValueValidator(6.00)])
    izoh = models.TextField()

    class Meta:
        verbose_name = "Ilmiy loyihalarni moliyalashtirish"
        verbose_name_plural = "Ilmiy loyihalarni moliyalashtirish"

    def __str__(self):
        return f"{self.user.username} - Loyiha moliyalashtirish"


# 7. AKT dasturlari va elektron ma'lumotlar bazalari guvohnomalari
class AKTDasturlar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    maqola = models.FileField(
        upload_to='akt_dasturlar_guvohnoma_files/',
        verbose_name="AKT dasturlari va elektron ma'lumotlar bazalari guvohnomalari"
    )
    score = models.DecimalField(null=True, blank=True, verbose_name="Baholash",max_digits=2,decimal_places=1,validators=[MaxValueValidator(3.00)])
    izoh = models.TextField()

    class Meta:
        verbose_name = "AKT dasturlari va elektron ma'lumotlar bazalari uchun guvohnoma"
        verbose_name_plural = "AKT dasturlari va elektron ma'lumotlar bazalari uchun guvohnomalar"

    def __str__(self):
        return f"{self.user.username} - AKT guvohnoma"


# 8. Talaba ilmiy faoliyati
class TalabaIlmiyFaoliyati(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    maqola = models.FileField(
        upload_to='talaba_ilmiy_faoliyati_files/',
        verbose_name="Talabaning ilmiy faoliyati"
    )
    score = models.DecimalField(null=True, blank=True, verbose_name="Baholash",max_digits=2,decimal_places=1,validators=[MaxValueValidator(5.00)])
    izoh = models.TextField()

    class Meta:
        verbose_name = "Talaba ilmiy faoliyati"
        verbose_name_plural = "Talaba ilmiy faoliyati"

    def __str__(self):
        return f"{self.user.username} - Talaba ilmiy faoliyati"



#######################################################################
# 9. Tarbiyaviy tadbirlar
class TarbiyaTadbirlar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    maqola = models.FileField(
        upload_to='tarbiya_tadbirlar_files/',
        verbose_name="Talabalar bilan tarbiyaviy ish bo'yicha tadbir"
        )
    score = models.DecimalField(null=True, blank=True, verbose_name="Baholash",max_digits=2,decimal_places=1,validators=[MaxValueValidator(3.00)])
    izoh = models.TextField()

    class Meta:
        verbose_name = "Tarbiya tadbiri"
        verbose_name_plural = "Tarbiya tadbirlari"

    def __str__(self):
        return f"{self.user.username} - Tarbiyaviy ish tadbiri"


# 10. Darstdan tashqari tadbirlar
class DarstanTashqariTadbirlar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    maqola = models.FileField(upload_to='darsdan_tashqari_files/',verbose_name="Darsdan tashqari madaniy va ma'rifiy tadbir")
    score = models.DecimalField(null=True, blank=True, verbose_name="Baholash",max_digits=2,decimal_places=1,validators=[MaxValueValidator(4.00)])
    izoh = models.TextField()

    class Meta:
        verbose_name = "Darsdan tashqari tadbir"
        verbose_name_plural = "Darsdan tashqari tadbirlar"

    def __str__(self):
        return f"{self.user.username} - Darstdan tashqari tadbir"


# 11. Talabalar turar joyidagi tadbirlar
class TalabalarTurarJoyTadbirlar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    maqola = models.FileField(
        upload_to='talabalar_ttj_tadbirlar_files/',
        verbose_name="Talabalar turar joyidagi madaniy va ma'rifiy tadbir")
    score = models.DecimalField(null=True, blank=True, verbose_name="Baholash",max_digits=2,decimal_places=1,validators=[MaxValueValidator(3.00)])
    izoh = models.TextField()

    class Meta:
        verbose_name = "Talabalar turar joyi tadbiri"
        verbose_name_plural = "Talabalar turar joyi tadbirlari"

    def __str__(self):
        return f"{self.user.username} - Talabalar turar joyi tadbiri"


# 12. Talabalar ota-onalari bilan ishlash
class OtaOnalarIshlash(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    maqola = models.FileField(upload_to='ota_onalar_bilan_ishlash_field/',verbose_name="Talabalar ota-onalari bilan ishlash")
    score = models.DecimalField(null=True, blank=True, verbose_name="Baholash",max_digits=2,decimal_places=1,validators=[MaxValueValidator(3.00)])
    izoh = models.TextField()

    class Meta:
        verbose_name = "Ota-onalar bilan ishlash"
        verbose_name_plural = "Ota-onalar bilan ishlash"

    def __str__(self):
        return f"{self.user.username} - Ota-onalar bilan ish"


# 13. Axborot va murobbiyslik soati
class AxborotMurobbiylikSoat(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.DecimalField(null=True, blank=True, verbose_name="Baholash",max_digits=2,decimal_places=1,validators=[MaxValueValidator(3.00)])
    izoh = models.TextField()

    class Meta:
        verbose_name = "Axborot va murobbiyslik soati"
        verbose_name_plural = "Axborot va murobbiyslik soatlari"

    def __str__(self):
        return f"{self.user.username} - Axborot va murobbiyslik soati"


# 14. 5 muhim tashabbus doirasida ishlari
class MuhimTashabbuslarIshlari(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    maqola = models.FileField(upload_to='muhim_tashabbus_field/',
                              verbose_name="5 muhim tashabbus doirasidagi ishlari")
    score = models.DecimalField(null=True, blank=True, verbose_name="Baholash",max_digits=2,decimal_places=1,validators=[MaxValueValidator(3.00)])
    izoh = models.TextField()

    class Meta:
        verbose_name = "5 muhim tashabbus ishi"
        verbose_name_plural = "5 muhim tashabbus ishlari"

    def __str__(self):
        return f"{self.user.username} - 5 muhim tashabbus ishi"


# 15. Bir ziyoli - bir mahallaga ma'naviy homiy
class BirZiyoliBirMahalla(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    maqola = models.FileField(upload_to='birziyoli_birmahalla_field/',verbose_name="Bir ziyoli – bir mahallaga ma'naviy homiy ishi")
    score = models.DecimalField(null=True, blank=True, verbose_name="Baholash",max_digits=2,decimal_places=1,validators=[MaxValueValidator(5.00)])
    izoh = models.TextField()

    class Meta:
        verbose_name = "Bir ziyoli – bir mahallaga ma'naviy homiy"
        verbose_name_plural = "Bir ziyoli – bir mahallaga ma'naviy homiy ishlari"

    def __str__(self):
        return f"{self.user.username} - Bir ziyoli – bir mahallaga ma'naviy homiy ishi"


# 1. Darslik yoki o‘quv qo‘llanma tayyorlash va nashr qilish
class DarslikYokiQollanma(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Foydalanuvchiga bog'langan
    maqola = models.FileField(
        upload_to='darslik_yoki_qollanma_files/',
        verbose_name="Darslik yoki o‘quv qo‘llanma tayyorlash va nashr qilish"
    )
    link = models.URLField(verbose_name="Maqolaga havola")
    score = models.DecimalField(null=True, blank=True, verbose_name="Baholash",max_digits=3,decimal_places=1,validators=[MaxValueValidator(50.00)])  # Superuser reytingi
    izoh = models.TextField()

    class Meta:
        verbose_name = "Darslik yoki o‘quv qo‘llanma"
        verbose_name_plural = "Darsliklar yoki o‘quv qo‘llanmalar"

    def __str__(self):
        return f"{self.user.username}"


# 2. PhD yoki DSc dissertatsiyani himoya qilish
class DissertationHimoya(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Foydalanuvchiga bog'langan
    maqola = models.FileField(
        upload_to='dissertatsiya_himoya_files/',
        verbose_name="PhD yoki DSc dissertatsiyani himoya qilish"
    )
    link = models.URLField(verbose_name="Maqolaga havola")
    score = models.DecimalField(null=True, blank=True, verbose_name="Baholash",max_digits=4,decimal_places=1,validators=[MaxValueValidator(100.00)])  # Superuser reytingi
    izoh = models.TextField()

    class Meta:
        verbose_name = "Dissertatsiyani himoya qilish"
        verbose_name_plural = "Dissertatsiyalar himoyalari"

    def __str__(self):
        return f"{self.user.username}"


# 3. Ilmiy rahbarlik
class IlmiyRahbarlik(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Foydalanuvchiga bog'langan
    maqola = models.FileField(
        upload_to='ilmiy_rahbarlik_files/',
        verbose_name="Ilmiy rahbarlik"
    )
    link = models.URLField(verbose_name="Maqolaga havola")
    score = models.DecimalField(null=True, blank=True, verbose_name="Baholash",max_digits=4,decimal_places=1,validators=[MaxValueValidator(100.00)])  # Superuser reytingi
    izoh = models.TextField()

    class Meta:
        verbose_name = "Ilmiy rahbarlik"
        verbose_name_plural = "Ilmiy rahbarliklar"

    def __str__(self):
        return f"{self.user.username}"


# 4. Xorijda malaka oshirish yoki stajirovka
class HorijdaMalakaOshirish(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Foydalanuvchiga bog'langan
    maqola = models.FileField(
        upload_to='xorijda_malaka_oshirish_files/',
        verbose_name="Xorijda malaka oshirish yoki stajirovka"
    )
    link = models.URLField(verbose_name="Maqolaga havola")
    score = models.DecimalField(null=True, blank=True, verbose_name="Baholash",max_digits=4,decimal_places=1,validators=[MaxValueValidator(100.00)])  # Superuser reytingi
    izoh = models.TextField()

    class Meta:
        verbose_name = "Xorijda malaka oshirish"
        verbose_name_plural = "Xorijda malaka oshirishlar"

    def __str__(self):
        return f"{self.user.username}"
 


@receiver(post_save, sender=User)
def create_oquv_yili_fanlar(sender, instance, created, **kwargs):
    if created:
        # Check if OquvYiliFanlar for this user already exists
        OquvYiliFanlar.objects.get_or_create(user=instance)
        MustaqilTalimTopshiriqlari.objects.get_or_create(user=instance )
        OqitishSifati.objects.get_or_create(user=instance)
        FaolInterfaolMetodlar.objects.get_or_create(user=instance)
        AxborotMurobbiylikSoat.objects.get_or_create(user=instance)
