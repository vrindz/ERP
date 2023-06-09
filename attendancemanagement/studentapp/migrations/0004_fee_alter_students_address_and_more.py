# Generated by Django 4.2.1 on 2023-06-21 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0003_remove_students_phone_students_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('installment_count', models.PositiveIntegerField(default=2)),
            ],
        ),
        migrations.AlterField(
            model_name='students',
            name='Address',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='students',
            name='Alternative_Address',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Alternative Address'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_option', models.CharField(choices=[('full', 'Full Amount'), ('installment', 'Two-Time Installment')], max_length=20)),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentapp.students')),
            ],
        ),
    ]
