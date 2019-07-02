from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth import logout
from social_django.middleware import SocialAuthExceptionMiddleware
from social_core.exceptions import AuthAlreadyAssociated


class WeiBoAuthAlreadyAssociatedMiddleware(SocialAuthExceptionMiddleware):
    """Redirect users to desired-url when AuthAlreadyAssociated exception occurs."""
    def process_exception(self, request, exception):
        if isinstance(exception, AuthAlreadyAssociated):
            if request.backend.name == "weibo":
                message = "This account is already in use."
                print(str(exception))
                if message in str(exception):
                    # Add logic if required

                    # User is redirected to any url you want
                    # in this case to "app_name:url_name"
                    return redirect(settings.SOCIAL_AUTH_LOGIN_REDIRECT_URL)


def social_user(backend, uid, user=None, *args, **kwargs):
    '''OVERRIDED: It will logout the current user
    instead of raise an exception .
    and then you can login in a new user'''

    provider = backend.name
    social = backend.strategy.storage.user.get_social_auth(provider, uid)
    if social:
        if user and social.user != user:
            logout(backend.strategy.request)
            #msg = 'This {0} account is already in use.'.format(provider)
            #raise AuthAlreadyAssociated(backend, msg)
        elif not user:
            user = social.user
    return {'social': social,
            'user': user,
            'is_new': user is None,
            'new_association': False}