from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

ENGINES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)
DRIVES = (
    ('I', 'Inboard'),
    ('J', 'Jet Drive'),
    ('10A', 'IPS10-A'),
    ('15A', 'IPS15-A'),
    ('15B', 'IPS15-B'),
    ('15C', 'IPS15-C'),
    ('20D', 'IPS20-D'),
    ('20E', 'IPS20-E'),
    ('2A', 'IPS2-A'),
    ('2B', 'IPS2-B'),
    ('2C', 'IPS2-C'),
    ('30D', 'IPS30-D'),
    ('30E', 'IPS30-E'),
    ('3A', 'IPS3-A'),
    ('3C', 'IPS3-C'),
    ('A', 'IPS-A'),
    ('B', 'IPS-B'),
    ('C', 'IPS-D'),
    ('E', 'IPS-E'),
    ('F', 'IPS-F'),
    ('DA', 'DPH-A'),
    ('DC', 'DPH-C'),
    ('DD', 'DPH-D'),
    ('DD1', 'DPH-D1'),
    ('DE', 'DPH-E'),
)

PARTS = (
    ('3809721', '3809721 Volvo 3809721 Fuel Filter'),
    ('A026K278', 'A026K278 Onan A026K278 Fuel Filter'),
    ('E1C', 'E1C Camp E1C Engine Anode'),
    ('2040N-30', '2040N-30 Racor 2040N-30 Fuel Filter'),
    ('2010PM-OR', '2010PM-OR Racor 2010PM-OR Fuel Filter'),
    ('838929', '838929 Engine Anode'),
    ('10077K-SHW', '10077K-SHW Sherwood Impeller Kit'),
    ('21707132', '21707132 Volvo 21707132 Oil Filter'),
    ('0185-5835', '0185-5835 Cummins 0185-5835 Oil Filter'),
    ('93132', '93132 Star Brite 93132 Diesel Additive(32oz)'),
    ('3556610', '3556610 West Marine 3556610 - 60 Antifreeze(1 Gallon)'),
    ('23219274', '23219274 Volvo 23219274 Diesel Engine Oil(1 Gallon) 15w-40'),
    ('23005191', '23005191 Volvo 23005191 IPS Oil Filter'),
    ('949656', '949656 Volvo 949656 O Ring'),
    ('3593981', '3593981 Volvo 3593981 Anode Kit'),
    ('1141680', '1141680 Volvo 1141680 Synthetic Gear Oil: 75W-90 (1 Gallon)'),
    ('22030852', '22030852 Volvo 22030852 Oil Filter'),
    ('22030848', '22030848 Volvo 22030848 Oil Filter'),
    ('21718912', '21718912 Volvo 21718912 Fuel Filter'),
    ('3584145', '3584145 Volvo 3584145 CCV Filter'),
    ('21702999', '21702999 Volvo 21702999 Air Filter Insert'),
)

class Boat(models.Model):
    name = models.CharField(max_length=40)
    brand = models.CharField(max_length=40)
    engine = models.CharField(max_length=40)
    drive_type = models.CharField(max_length=40)
    length = models.IntegerField()
    generator = models.CharField(max_length=40)
    year = models.IntegerField()


# class Boat:
#     def __init__(self, name, brand, num_engines, engine, drive_type, length, generator, year):
#         self.name = name
#         self.brand = brand
#         self.num_engines = num_engines
#         self.engine = engine
#         self.drive_type = drive_type
#         self.length = length
#         self.generator = generator
#         self.year = year

# boats = [
#     Boat('relax', 'riviera', 'd8', 'ips', 45, 'onan', 2019),
#     Boat('relax', 'riviera', 'd8', 'ips', 41, 'onan', 2012),
#     Boat('relax', 'riviera', 'd8', 'ips', 44, 'onan', 2015)
# ]