from django import forms
from .models import *
from django.core.exceptions import ValidationError

class FanVideoKontentForm(forms.ModelForm):
    class Meta:
        model = FanVideoKontent
        fields = ['link','score', 'izoh']  # Superuserlar uchun barcha maydonlar
        widgets = {
            'link': forms.URLInput(attrs={'class': 'form-control', 'id': 'linkInput1', 'placeholder': 'Linkni kiriting'}),
            'izoh': forms.Textarea(attrs={'class': 'form-control', 'id': 'commentInput1', 'rows': 3, 'placeholder': 'Izoh kiriting'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'id': 'scoreInput1', 'placeholder': 'Baholash'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Foydalanuvchini olish
        super(FanVideoKontentForm, self).__init__(*args, **kwargs)
        
        # Agar foydalanuvchi superuser bo'lmasa, 'score' maydonini olib tashlang
        if user and not user.is_superuser:
            self.fields.pop('score')
class NashrEtilganDarsliklarForm(forms.ModelForm):
    class Meta:
        model = NashrEtilganDarsliklar
        fields = ['maqola', 'score', 'izoh']  # Superuserlar uchun barcha maydonlar
        widgets = {
            'maqola': forms.FileInput(attrs={'class': 'form-control', 'id': 'maqolaInput1', 'placeholder': 'Maqolani yuklang'}),
            'izoh': forms.Textarea(attrs={'class': 'form-control', 'id': 'commentInput1', 'rows': 3, 'placeholder': 'Izoh kiriting'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'id': 'scoreInput1', 'placeholder': 'Baholash'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Foydalanuvchini olish
        super(NashrEtilganDarsliklarForm, self).__init__(*args, **kwargs)
        
        # Agar foydalanuvchi superuser bo'lmasa, 'score' maydonini olib tashlang
        if user and not user.is_superuser:
            self.fields.pop('score')

###########################################################################
class ScopusWebOfScienceForm(forms.ModelForm):
    class Meta:
        model = ScopusWebOfScience
        fields = ['maqola','link', 'izoh', 'score']
        widgets = {
            'maqola': forms.FileInput(attrs={'class': 'form-control', 'id': 'maqolaInput1', 'placeholder': 'Maqolani yuklang'}),
            'link': forms.URLInput(attrs={'class': 'form-control', 'id': 'linkInput1', 'placeholder': 'Linkni kiriting'}),
            'izoh': forms.Textarea(attrs={'class': 'form-control', 'id': 'commentInput1', 'rows': 3, 'placeholder': 'Izoh kiriting'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'id': 'scoreInput1', 'placeholder': 'Baholashni kiriting'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Foydalanuvchini olish
        super(ScopusWebOfScienceForm, self).__init__(*args, **kwargs)
        
        # Agar foydalanuvchi superuser bo'lmasa, 'score' maydoni olib tashlanadi
        if user and not user.is_superuser:
            self.fields.pop('score')

class OAKJurnaliMaqolaForm(forms.ModelForm):
    class Meta:
        model = OAKJurnaliMaqola
        fields = ['maqola','link', 'izoh', 'score']
        widgets = {
            'maqola': forms.FileInput(attrs={'class': 'form-control', 'id': 'maqolaInput1', 'placeholder': 'Maqolani yuklang'}),
            'link': forms.URLInput(attrs={'class': 'form-control', 'id': 'linkInput1', 'placeholder': 'Linkni kiriting'}),
            'izoh': forms.Textarea(attrs={'class': 'form-control', 'id': 'commentInput1', 'rows': 3, 'placeholder': 'Izoh kiriting'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'id': 'scoreInput1', 'placeholder': 'Baholashni kiriting'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Foydalanuvchini olish
        super(OAKJurnaliMaqolaForm, self).__init__(*args, **kwargs)
        
        # Agar foydalanuvchi superuser bo'lmasa, 'score' maydoni olib tashlanadi
        if user and not user.is_superuser:
            self.fields.pop('score')


class HIndexForm(forms.ModelForm):
    class Meta:
        model = HIndex
        fields = ['maqola','link', 'izoh', 'score']
        widgets = {
            'maqola': forms.FileInput(attrs={'class': 'form-control', 'id': 'maqolaInput1', 'placeholder': 'Maqolani yuklang'}),
            'link': forms.URLInput(attrs={'class': 'form-control', 'id': 'linkInput1', 'placeholder': 'Linkni kiriting'}),
            'izoh': forms.Textarea(attrs={'class': 'form-control', 'id': 'commentInput1', 'rows': 3, 'placeholder': 'Izoh kiriting'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'id': 'scoreInput1', 'placeholder': 'Baholashni kiriting'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Foydalanuvchini olish
        super(HIndexForm, self).__init__(*args, **kwargs)
        
        # Agar foydalanuvchi superuser bo'lmasa, 'score' maydoni olib tashlanadi
        if user and not user.is_superuser:
            self.fields.pop('score')


class KonferensiyaMaqolaForm(forms.ModelForm):
    class Meta:
        model = KonferensiyaMaqola
        fields = ['maqola','link', 'izoh', 'score']
        widgets = {
            'maqola': forms.FileInput(attrs={'class': 'form-control', 'id': 'maqolaInput1', 'placeholder': 'Maqolani yuklang'}),
            'link': forms.URLInput(attrs={'class': 'form-control', 'id': 'linkInput1', 'placeholder': 'Linkni kiriting'}),
            'izoh': forms.Textarea(attrs={'class': 'form-control', 'id': 'commentInput1', 'rows': 3, 'placeholder': 'Izoh kiriting'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'id': 'scoreInput1', 'placeholder': 'Baholashni kiriting'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Foydalanuvchini olish
        super(KonferensiyaMaqolaForm, self).__init__(*args, **kwargs)
        
        # Agar foydalanuvchi superuser bo'lmasa, 'score' maydoni olib tashlanadi
        if user and not user.is_superuser:
            self.fields.pop('score')

class LoyihalarTayyorlashForm(forms.ModelForm):
    class Meta:
        model = LoyihalarTayyorlash
        fields = ['maqola','izoh', 'score']
        widgets = {
            'maqola': forms.FileInput(attrs={'class': 'form-control', 'id': 'maqolaInput1', 'placeholder': 'Maqolani yuklang'}),
            'izoh': forms.Textarea(attrs={'class': 'form-control', 'id': 'commentInput1', 'rows': 3, 'placeholder': 'Izoh kiriting'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'id': 'scoreInput1', 'placeholder': 'Baholashni kiriting'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Foydalanuvchini olish
        super(LoyihalarTayyorlashForm, self).__init__(*args, **kwargs)
        
        # Agar foydalanuvchi superuser bo'lmasa, 'score' maydoni olib tashlanadi
        if user and not user.is_superuser:
            self.fields.pop('score')



class LoyihaMoliyaForm(forms.ModelForm):
    class Meta:
        model = LoyihaMoliya
        fields = ['maqola','izoh', 'score']
        widgets = {
            'maqola': forms.FileInput(attrs={'class': 'form-control', 'id': 'maqolaInput1', 'placeholder': 'Maqolani yuklang'}),
            'izoh': forms.Textarea(attrs={'class': 'form-control', 'id': 'commentInput1', 'rows': 3, 'placeholder': 'Izoh kiriting'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'id': 'scoreInput1', 'placeholder': 'Baholashni kiriting'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Foydalanuvchini olish
        super(LoyihaMoliyaForm, self).__init__(*args, **kwargs)
        
        # Agar foydalanuvchi superuser bo'lmasa, 'score' maydoni olib tashlanadi
        if user and not user.is_superuser:
            self.fields.pop('score')


class AKTDasturlarForm(forms.ModelForm):
    class Meta:
        model = AKTDasturlar
        fields = ['maqola','izoh', 'score']
        widgets = {
            'maqola': forms.FileInput(attrs={'class': 'form-control', 'id': 'maqolaInput1', 'placeholder': 'Maqolani yuklang'}),
            'izoh': forms.Textarea(attrs={'class': 'form-control', 'id': 'commentInput1', 'rows': 3, 'placeholder': 'Izoh kiriting'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'id': 'scoreInput1', 'placeholder': 'Baholashni kiriting'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Foydalanuvchini olish
        super(AKTDasturlarForm, self).__init__(*args, **kwargs)
        
        # Agar foydalanuvchi superuser bo'lmasa, 'score' maydoni olib tashlanadi
        if user and not user.is_superuser:
            self.fields.pop('score')



class TalabaIlmiyFaoliyatiForm(forms.ModelForm):
    class Meta:
        model = TalabaIlmiyFaoliyati
        fields = ['maqola','izoh', 'score']
        widgets = {
            'maqola': forms.FileInput(attrs={'class': 'form-control', 'id': 'maqolaInput1', 'placeholder': 'Maqolani yuklang'}),
            'izoh': forms.Textarea(attrs={'class': 'form-control', 'id': 'commentInput1', 'rows': 3, 'placeholder': 'Izoh kiriting'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'id': 'scoreInput1', 'placeholder': 'Baholashni kiriting'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Foydalanuvchini olish
        super(TalabaIlmiyFaoliyatiForm, self).__init__(*args, **kwargs)
        
        # Agar foydalanuvchi superuser bo'lmasa, 'score' maydoni olib tashlanadi
        if user and not user.is_superuser:
            self.fields.pop('score')


class TarbiyaTadbirlarForm(forms.ModelForm):
    class Meta:
        model = TarbiyaTadbirlar
        fields = ['maqola','izoh', 'score']
        widgets = {
            'maqola': forms.FileInput(attrs={'class': 'form-control', 'id': 'maqolaInput1', 'placeholder': 'Maqolani yuklang'}),
            'izoh': forms.Textarea(attrs={'class': 'form-control', 'id': 'commentInput1', 'rows': 3, 'placeholder': 'Izoh kiriting'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'id': 'scoreInput1', 'placeholder': 'Baholashni kiriting'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Foydalanuvchini olish
        super(TarbiyaTadbirlarForm, self).__init__(*args, **kwargs)
        
        # Agar foydalanuvchi superuser bo'lmasa, 'score' maydoni olib tashlanadi
        if user and not user.is_superuser:
            self.fields.pop('score')


class DarstanTashqariTadbirlarForm(forms.ModelForm):
    class Meta:
        model = DarstanTashqariTadbirlar
        fields = ['maqola','izoh', 'score']
        widgets = {
            'maqola': forms.FileInput(attrs={'class': 'form-control', 'id': 'maqolaInput1', 'placeholder': 'Maqolani yuklang'}),
            'izoh': forms.Textarea(attrs={'class': 'form-control', 'id': 'commentInput1', 'rows': 3, 'placeholder': 'Izoh kiriting'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'id': 'scoreInput1', 'placeholder': 'Baholashni kiriting'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Foydalanuvchini olish
        super(DarstanTashqariTadbirlarForm, self).__init__(*args, **kwargs)
        
        # Agar foydalanuvchi superuser bo'lmasa, 'score' maydoni olib tashlanadi
        if user and not user.is_superuser:
            self.fields.pop('score')

class TalabalarTurarJoyTadbirlarForm(forms.ModelForm):
    class Meta:
        model = TalabalarTurarJoyTadbirlar
        fields = ['maqola','izoh', 'score']
        widgets = {
            'maqola': forms.FileInput(attrs={'class': 'form-control', 'id': 'maqolaInput1', 'placeholder': 'Maqolani yuklang'}),
            'izoh': forms.Textarea(attrs={'class': 'form-control', 'id': 'commentInput1', 'rows': 3, 'placeholder': 'Izoh kiriting'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'id': 'scoreInput1', 'placeholder': 'Baholashni kiriting'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Foydalanuvchini olish
        super(TalabalarTurarJoyTadbirlarForm, self).__init__(*args, **kwargs)
        
        # Agar foydalanuvchi superuser bo'lmasa, 'score' maydoni olib tashlanadi
        if user and not user.is_superuser:
            self.fields.pop('score')

class OtaOnalarIshlashForm(forms.ModelForm):
    class Meta:
        model = OtaOnalarIshlash
        fields = ['maqola','izoh', 'score']
        widgets = {
            'maqola': forms.FileInput(attrs={'class': 'form-control', 'id': 'maqolaInput1', 'placeholder': 'Maqolani yuklang'}),
            'izoh': forms.Textarea(attrs={'class': 'form-control', 'id': 'commentInput1', 'rows': 3, 'placeholder': 'Izoh kiriting'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'id': 'scoreInput1', 'placeholder': 'Baholashni kiriting'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Foydalanuvchini olish
        super(OtaOnalarIshlashForm, self).__init__(*args, **kwargs)
        
        # Agar foydalanuvchi superuser bo'lmasa, 'score' maydoni olib tashlanadi
        if user and not user.is_superuser:
            self.fields.pop('score')

class AxborotMurobbiylikSoatForm(forms.ModelForm):
    class Meta:
        model = AxborotMurobbiylikSoat
        fields = ['izoh', 'score']
        widgets = {
            'izoh': forms.Textarea(attrs={'class': 'form-control', 'id': 'commentInput1', 'rows': 3, 'placeholder': 'Izoh kiriting'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'id': 'scoreInput1', 'placeholder': 'Baholashni kiriting'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Foydalanuvchini olish
        super(AxborotMurobbiylikSoatForm, self).__init__(*args, **kwargs)
        
        # Agar foydalanuvchi superuser bo'lmasa, 'score' maydoni olib tashlanadi
        if user and not user.is_superuser:
            self.fields.pop('score')

class MuhimTashabbuslarIshlariForm(forms.ModelForm):
    class Meta:
        model = MuhimTashabbuslarIshlari
        fields = ['maqola','izoh', 'score']
        widgets = {
            'maqola': forms.FileInput(attrs={'class': 'form-control', 'id': 'maqolaInput1', 'placeholder': 'Maqolani yuklang'}),
            'izoh': forms.Textarea(attrs={'class': 'form-control', 'id': 'commentInput1', 'rows': 3, 'placeholder': 'Izoh kiriting'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'id': 'scoreInput1', 'placeholder': 'Baholashni kiriting'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Foydalanuvchini olish
        super(MuhimTashabbuslarIshlariForm, self).__init__(*args, **kwargs)
        
        # Agar foydalanuvchi superuser bo'lmasa, 'score' maydoni olib tashlanadi
        if user and not user.is_superuser:
            self.fields.pop('score')

class BirZiyoliBirMahallaForm(forms.ModelForm):
    class Meta:
        model = BirZiyoliBirMahalla
        fields = ['maqola','izoh', 'score']
        widgets = {
            'maqola': forms.FileInput(attrs={'class': 'form-control', 'id': 'maqolaInput1', 'placeholder': 'Maqolani yuklang'}),
            'izoh': forms.Textarea(attrs={'class': 'form-control', 'id': 'commentInput1', 'rows': 3, 'placeholder': 'Izoh kiriting'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'id': 'scoreInput1', 'placeholder': 'Baholashni kiriting'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Foydalanuvchini olish
        super(BirZiyoliBirMahallaForm, self).__init__(*args, **kwargs)
        
        # Agar foydalanuvchi superuser bo'lmasa, 'score' maydoni olib tashlanadi
        if user and not user.is_superuser:
            self.fields.pop('score')
########################
class DarslikYokiQollanmaForm(forms.ModelForm):
    class Meta:
        model = DarslikYokiQollanma
        fields = ['maqola','izoh', 'score']
        widgets = {
            'maqola': forms.FileInput(attrs={'class': 'form-control', 'id': 'maqolaInput1', 'placeholder': 'Maqolani yuklang'}),
            'izoh': forms.Textarea(attrs={'class': 'form-control', 'id': 'commentInput1', 'rows': 3, 'placeholder': 'Izoh kiriting'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'id': 'scoreInput1', 'placeholder': 'Baholashni kiriting'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Foydalanuvchini olish
        super(DarslikYokiQollanmaForm, self).__init__(*args, **kwargs)
        
        # Agar foydalanuvchi superuser bo'lmasa, 'score' maydoni olib tashlanadi
        if user and not user.is_superuser:
            self.fields.pop('score')


class DissertationHimoyaForm(forms.ModelForm):
    class Meta:
        model = DissertationHimoya
        fields = ['maqola','izoh', 'score']
        widgets = {
            'maqola': forms.FileInput(attrs={'class': 'form-control', 'id': 'maqolaInput1', 'placeholder': 'Maqolani yuklang'}),
            'izoh': forms.Textarea(attrs={'class': 'form-control', 'id': 'commentInput1', 'rows': 3, 'placeholder': 'Izoh kiriting'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'id': 'scoreInput1', 'placeholder': 'Baholashni kiriting'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Foydalanuvchini olish
        super(DissertationHimoyaForm, self).__init__(*args, **kwargs)
        
        # Agar foydalanuvchi superuser bo'lmasa, 'score' maydoni olib tashlanadi
        if user and not user.is_superuser:
            self.fields.pop('score')

class IlmiyRahbarlikForm(forms.ModelForm):
    class Meta:
        model = IlmiyRahbarlik
        fields = ['maqola','izoh', 'score','link']
        widgets = {
            'link': forms.URLInput(attrs={'class': 'form-control', 'id': 'linkInput1', 'placeholder': 'Linkni kiriting'}),
            'maqola': forms.FileInput(attrs={'class': 'form-control', 'id': 'maqolaInput1', 'placeholder': 'Maqolani yuklang'}),
            'izoh': forms.Textarea(attrs={'class': 'form-control', 'id': 'commentInput1', 'rows': 3, 'placeholder': 'Izoh kiriting'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'id': 'scoreInput1', 'placeholder': 'Baholashni kiriting'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Foydalanuvchini olish
        super(IlmiyRahbarlikForm, self).__init__(*args, **kwargs)
        
        # Agar foydalanuvchi superuser bo'lmasa, 'score' maydoni olib tashlanadi
        if user and not user.is_superuser:
            self.fields.pop('score')
    
class HorijdaMalakaOshirishForm(forms.ModelForm):
    class Meta:
        model = HorijdaMalakaOshirish
        fields = ['maqola','izoh', 'score']
        widgets = {
            'maqola': forms.FileInput(attrs={'class': 'form-control', 'id': 'maqolaInput1', 'placeholder': 'Maqolani yuklang'}),
            'izoh': forms.Textarea(attrs={'class': 'form-control', 'id': 'commentInput1', 'rows': 3, 'placeholder': 'Izoh kiriting'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'id': 'scoreInput1', 'placeholder': 'Baholashni kiriting'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Foydalanuvchini olish
        super(HorijdaMalakaOshirishForm, self).__init__(*args, **kwargs)
        
        # Agar foydalanuvchi superuser bo'lmasa, 'score' maydoni olib tashlanadi
        if user and not user.is_superuser:
            self.fields.pop('score')