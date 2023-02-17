from django import forms
class FirstForm(forms.Form):
	full_name = forms.CharField(label='الإسم بالكامل', max_length=100)
	National_Id = forms.CharField(label='الرقم الوطني', max_length=100)
	phone= forms.CharField(label='رقم التلفون', max_length=15)
	
class SecondForm(forms.Form):
	password = forms.CharField(label='كلمة السر', max_length=100,widget=forms.PasswordInput)
	confirm_password = forms.CharField(label='تأكيد كلمة السر', max_length=100,widget=forms.PasswordInput)
	email= forms.EmailField(label=' الإيميل', max_length=100,widget=forms.EmailInput)
	class Meta:
	    fields=('password','email','confirm_password')
	def clean(self):
	    cleaned_data = super(SecondForm, self).clean()
	    password = cleaned_data.get("password")
	    confirm_password = cleaned_data.get("confirm_password")
	    if password != confirm_password:
		    raise forms.ValidationError(
                "كلمة المرور وتأكيد كلمة المرور غير متطابقة"
            )
	    
class ThirdForm(forms.Form):
	SecretsPassword = forms.CharField(label='أكتب كلمة الأمان', max_length=100)
	boolfield = forms.TypedChoiceField(
		          label='هل الهاتف جديد غير مستخدم من قبل؟',
                   coerce=lambda x: x == 'نعم',
                   choices=( (True, 'نعم'),(False, 'لا'),),
                   widget=forms.RadioSelect
                )
class FourForm(forms.Form):
	boolfield = forms.TypedChoiceField(
		          label='هل توافق علي جميع الشروط والصلاحيات في متابعة هاتفك في حالة الفقدان ومعرفة موقعة في الخريطة؟',
                   coerce=lambda x: x == 'نعم',
                   choices=( (True, 'نعم'),(False, 'لا'),),
                   widget=forms.RadioSelect
                )
    # isOwner = forms.CharField(label='الرقم الوطني', max_length=100)
