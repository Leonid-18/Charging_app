from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import views, generics, status
from .models import Rate
from .serializers import RateSerializer


class RateView(views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = RateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True) and request.user.is_staff:
            serializer.save()
        else:
            return Response({"status": status.HTTP_403_FORBIDDEN,
                             "message": 'Access Denied'})
        return Response({
            'status': 200,
            'message': 'Successfully saved'
        })


class RetrieveRatesView(views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request):
        rates = Rate.objects.all()
        serializer = RateSerializer(rates, many=True)
        return JsonResponse(serializer.data, safe=False)
