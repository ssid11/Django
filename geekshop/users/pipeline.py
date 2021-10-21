import datetime
from collections import OrderedDict
from urllib.parse import urlunparse, urlencode
import requests
from django.utils import timezone
from social_core.exceptions import AuthForbidden

from users.models import  UserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return
    api_url = urlunparse(('http','api.vk.com', 'method/users.get',None,
                          urlencode(OrderedDict(fields=','.join(('bdate', 'sex', 'about')),
                                          access_token=response['access_token'], v=5.131)), None))
    resp = requests.get(api_url)
    if resp.status_code != 200:
        return

    data = resp.json()['response'][0]
    if data['sex']:
        user.userprofile.gender = UserProfile.MALE if data['sex'] == 2 else UserProfile.FEMALE

    if data['about']:
        user.userprofile.about = data['about']

    if data['bdate']:
        bdate = datetime.datetime.strptime(data['bdate'], '%d.%m.%Y').date()

        user.age = timezone.now().date().year - bdate.year
        if user.age > 100:
            user.delete()
            raise AuthForbidden('social_core.backends.vk.VKOAuth2')

        # user.save()

