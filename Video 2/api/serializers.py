from rest_framework import serializers
from .models import Barang, Pesanan, Pembelian


class BarangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barang
        fields = [
            'nama', 'harga', 'stock',
        ]

        # validasi harga barang
        def validate_harga(self, value):
            if value <= 0:
                raise serializers.ValidationError(
                    'Harga barang tidak boleh kosong'
                )
            return value
