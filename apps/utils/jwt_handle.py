from datetime import datetime

from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework_jwt.views import JSONWebTokenAPIView, jwt_response_payload_handler,\
    api_settings, JSONWebTokenSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomizeJSONWebTokenAPIView(JSONWebTokenAPIView):
    """
    重写JSONWebTokenAPIView，　实现返回值添加ｕｓｅｒ信息，而不仅仅返回ｔｏｋｅｎ信息
    """
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        username = request.data.get("username")

        if not username:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.filter(username=username)[0]
        except serializers.ValidationError as e:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            if not user.is_active:
                return Response({"err_code": "0"}, status=status.HTTP_200_OK)

        if serializer.is_valid():
            user = serializer.object.get('user') or request.user

            token = serializer.object.get('token')
            response_data = jwt_response_payload_handler(token, user, request)
            response_data.update({"user_id": user.id, "user_name": user.username, "err_code": "1"})
            response = Response(response_data)
            if api_settings.JWT_AUTH_COOKIE:
                expiration = (datetime.utcnow() +
                              api_settings.JWT_EXPIRATION_DELTA)
                response.set_cookie(api_settings.JWT_AUTH_COOKIE,
                                    token,
                                    expires=expiration,
                                    httponly=True)
            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomizeJObtainJSONWebToken(CustomizeJSONWebTokenAPIView):
    """
    API View that receives a POST with a user's username and password.

    Returns a JSON Web Token that can be used for authenticated requests.
    """
    serializer_class = JSONWebTokenSerializer