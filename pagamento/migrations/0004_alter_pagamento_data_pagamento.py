# Generated by Django 4.1 on 2023-06-10 12:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagamento', '0003_alter_pagamento_data_pagamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagamento',
            name='data_pagamento',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 10, 14, 12, 57, 843984)),
        ),
    ]