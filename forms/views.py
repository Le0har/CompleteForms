from rest_framework import viewsets
from rest_framework.response import Response
from forms.models import Form
from forms.serializers import FormSerializer
from rest_framework.decorators import action


class FormsAPIView(viewsets.ModelViewSet):
    queryset = Form.objects.all() 
    serializer_class = FormSerializer

    @action(detail=False, methods=['post'])
    def get_form(self, request):
        data_in = request.data
        serializer = FormSerializer(data=data_in)
        serializer.is_valid(raise_exception=True)
        keys_data_in = list(data_in.keys())
        short_form = ['email', 'phone']
        middle_form = ['email', 'phone', 'data']
        long_form = ['email', 'phone', 'data', 'text']
        if set(long_form).issubset(keys_data_in):
            return Response({'form_name': 'LongForm'})
        if set(middle_form).issubset(keys_data_in):
            return Response({'form_name': 'MiddleForm'})
        if set(short_form).issubset(keys_data_in):
            return Response({'form_name': 'ShortForm'})
        return Response({'form_name': 'Unknown'})
        