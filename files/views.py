import os
from rest_framework import (
    status, generics, 
    mixins, exceptions,
) 
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from django.conf import settings
from .models import Invoice
from .serializers import InvoiceSerializer

from .algorithms.pdf_to_csv import process_file

User = get_user_model();

class InvoiceView(generics.CreateAPIView, ):
    permission_classes = (IsAuthenticated, )
    serializer_class = InvoiceSerializer

    def post(self, request, *args, **kwargs):
        user = request.user

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        file = request.data.get('file')

        # creating invoice
        invoice_obj = Invoice.objects.create(user=user, file=file)
        
        file_loc = os.path.join(settings.MEDIA_ROOT, str(invoice_obj.file))
        
        process_file(file_loc)        
        
        return Response({'detail': 'Invoice has been successfully created'}, 
                        status=status.HTTP_201_CREATED)

