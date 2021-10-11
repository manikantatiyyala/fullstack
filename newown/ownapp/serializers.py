from rest_framework import serializers
from .models import Papers

class PaperSerializer(serializers.ModelSerializer):
    class Meta:
        model=Papers
        fields=('Creator','PaperId','PaperName','DateOfCreating','saved_file')