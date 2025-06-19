import random
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from api.models import User, Barang, Pesanan, Pembelian


class Command(BaseCommand):
    help = 'Membuat data dummy aplikasi'

    def handle(self, *args, **kwargs):
        # dapatkan atau buat superuser
        user = User.objects.filter(username='admin').first()
        if not user:
            user = User.objects.create_superuser(
                username='admin', password='test')

        # buat produk - nama, deskripsi, harga, stok, gambar
        products = [
            Barang(nama="Macbook Pro 16", deskripsi=lorem_ipsum.paragraph(
            ), harga=Decimal('9999.9'), stock=4),
            Barang(nama="Mesin Kopi", deskripsi=lorem_ipsum.paragraph(
            ), harga=Decimal('200.1'), stock=6),
            Barang(nama="Speaker Simbada", deskripsi=lorem_ipsum.paragraph(
            ), harga=Decimal('15.99'), stock=11),
            Barang(nama="Iphone 16 Pro Max",
                   deskripsi=lorem_ipsum.paragraph(), harga=Decimal('1250.0'), stock=2),
            Barang(nama="Kamera Digital", deskripsi=lorem_ipsum.paragraph(
            ), harga=Decimal('350.99'), stock=4),
            Barang(nama="Apple Watch", deskripsi=lorem_ipsum.paragraph(),
                   harga=Decimal('500.05'), stock=0),
        ]

        # buat Barang & ambil ulang dari DB
        Barang.objects.bulk_create(products)
        products = Barang.objects.all()

        # buat beberapa perintah tiruan yang terikat pada superuser
        for _ in range(3):
            # buat Pesanan dengan 2 item pesanan
            order = Pesanan.objects.create(user=user)
            for product in random.sample(list(products), 2):
                Pembelian.objects.create(
                    pesans=order, barangs=product, quantity=random.randint(
                        1, 3)
                )
