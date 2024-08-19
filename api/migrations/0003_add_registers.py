from django.db import migrations
from datetime import datetime, timezone

def add_new_registers(apps, schema_editor):
    Register = apps.get_model('api', 'Register')
    
    user_id = 1

    registers = [
        Register(user_id_id=user_id, created_at=datetime(2024, 8, 1, 12, 0, tzinfo=timezone.utc), amount=10.0),
        Register(user_id_id=user_id, created_at=datetime(2024, 8, 1, 14, 0, tzinfo=timezone.utc), amount=20.0),
        Register(user_id_id=user_id, created_at=datetime(2024, 8, 13, 16, 0, tzinfo=timezone.utc), amount=30.0),
    ]

    Register.objects.bulk_create(registers)

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_register'),
    ]

    operations = [
        migrations.RunPython(add_new_registers),
    ]