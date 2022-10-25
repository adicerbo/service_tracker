# from wsgiref.validate import validator
from unicodedata import name
from django.db import models
from multiselectfield import MultiSelectField
# from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.contrib.auth.models import User

ENGINES_NUM = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

ENGINES = (
    ('1','D1-13'),
    ('2','D2-40'),
    ('3','D2-50'),
    ('4','D2-55'),
    ('5','D2-60'),
    ('6','D2-75'),
    ('7','D3-50'),
    ('8','D3-110'),
    ('9','D3-120'),
    ('10','D3-130'),
    ('11','D3-210'),
    ('12','D3-220'),
    ('13','D4-180'),
    ('14','D4-225'),
    ('15','D4-270'),
    ('16','D4-300'),
    ('17','D4-320'),
    ('19','D6-280'),
    ('20','D6-350'),
    ('21','D6-435'),
    ('22','D6-480'),
    ('23','D8A1'),
    ('24','D8A2'),
    ('25','D8A6'),
    ('26','D9A2'),
    ('27','D11A'),
    ('28','D11B'),
    ('29','D11C'),
    ('30','D13A'),
    ('31','D13B'),
    ('32','D13C')
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


class Part(models.Model):
    PARTS = (
        ('1', '3809721 Volvo 3809721 Fuel Filter'),
        ('2', 'A026K278 Onan A026K278 Fuel Filter'),
        ('3', 'E1C Camp E1C Engine Anode'),
        ('4', '2040N-30 Racor 2040N-30 Fuel Filter'),
        ('5', '2010PM-OR Racor 2010PM-OR Fuel Filter'),
        ('6', '838929 Engine Anode'),
        ('7', '10077K-SHW Sherwood Impeller Kit'),
        ('8', '21707132 Volvo 21707132 Oil Filter'),
        ('9', '0185-5835 Cummins 0185-5835 Oil Filter'),
        ('10', '93132 Star Brite 93132 Diesel Additive(32oz)'),
        ('11', '3556610 West Marine 3556610 - 60 Antifreeze(1 Gallon)'),
        ('12', '23219274 Volvo 23219274 Diesel Engine Oil(1 Gallon) 15w-40'),
        ('13', '23005191 Volvo 23005191 IPS Oil Filter'),
        ('14', '949656 Volvo 949656 O Ring'),
        ('15', '3593981 Volvo 3593981 Anode Kit'),
        ('16', '1141680 Volvo 1141680 Synthetic Gear Oil: 75W-90 (1 Gallon)'),
        ('17', '22030852 Volvo 22030852 Oil Filter'),
        ('18', '22030848 Volvo 22030848 Oil Filter'),
        ('19', '21718912 Volvo 21718912 Fuel Filter'),
        ('20', '3584145 Volvo 3584145 CCV Filter'),
        ('21', '21702999 Volvo 21702999 Air Filter Insert'),
    )
    parts = MultiSelectField(choices=PARTS, max_length=1000)

    # def __str__(self):
    #     return f"{self._get_part_display()}"

    def get_absolute_url(self):
        return reverse('parts_detail', kwargs={'pk': self.id})

class Boat(models.Model):
    name = models.CharField(max_length=40)
    brand = models.CharField(max_length=40)
    num_engines = models.CharField(
        max_length = 1,
        choices=ENGINES_NUM,
        default=ENGINES_NUM[0][0]
    )
    engine = models.CharField(
        max_length=40,
        choices=ENGINES,
        default=ENGINES[0][0]
        )
    drive_type = models.CharField(
        max_length=40,
        choices=DRIVES,
        default=DRIVES[0][0]
        )
    length = models.IntegerField()
    generator = models.CharField(max_length=40)
    year = models.IntegerField()
    hours = models.IntegerField()
    parts = models.ManyToManyField(Part)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'boat_id': self.id})

class Service(models.Model):
    date = models.DateField('Service Date')
    hours = models.IntegerField('Hours When Serviced')
    SERVICES = (
        ('1', 'Engine Oil'),
        ('2', 'Drive Oil'),
        ('3', 'Fuel Filters'),
        ('4', 'Air Filters'),
        ('5', 'Impellers'),
        ('6', 'Engine Anodes'),
        ('7', 'Drive Anodes'),
        ('8', 'Hull Anodes'),
        ('9', 'Air Coolers'),
        ('10', 'Heat Exchangers'),
        ('11', 'Oil Samples'),
        ('12', 'Coolant Test'),
        ('13', 'Coolant Swap'),
    )
    services = MultiSelectField(choices=SERVICES, max_length=13)
    
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE)

    def __str__(self): 
        return f"{self.get_service_display()} on {self.date}"

    class Meta:
        ordering = ['hours']
