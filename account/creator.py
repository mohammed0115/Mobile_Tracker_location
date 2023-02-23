from account.models import User
from markers.models import Marker
from django.contrib.auth import login
def createMarkers(data):
    marker=Marker.objects.create(**data)

def createUser(data,request):
    # user=User()
    """
    {'full_name': 'Mohammed kamal Mohammed', 'National_Id': '11980419545', 'phone': None, 'password': '123',
      'confirm_password': '123', 'SecretsPassword': 'thank', 'c': 'True', 'boolfield1': 'True'}
    
    """
    user_dict={
       'email':data['email'],
       'full_name':data['full_name'],
       'National_number':data['National_Id'],
       'phone_number':data['phone'],
       'password':data['password'],
       'SecretsPassword':data['SecretsPassword'],
        'boolfield1':data['boolfield1'],
        'boolfield' :data['boolfield']
     }
    if User.objects.filter(email=user_dict['email']).exists():
        user =User.objects.get(email=user_dict['email'])
        
    else:
        user, created=User.objects.get_or_create(**user_dict)
        user.is_staff=True
        user.set_password(data['password'])
        user.save()
    login(request, user)    
    return user