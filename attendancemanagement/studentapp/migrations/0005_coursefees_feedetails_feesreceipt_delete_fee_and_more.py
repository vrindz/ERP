# Generated by Django 4.2.1 on 2023-06-22 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0003_delete_master'),
        ('studentapp', '0004_fee_alter_students_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseFees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fees_type', models.CharField(choices=[('one_time', 'One Time'), ('two_time', 'Two Time'), ('three_time', 'Three Time'), ('registration', 'Registration')], max_length=12, null=True)),
                ('amount', models.IntegerField(null=True)),
                ('installment_period', models.IntegerField(null=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courseapp.course')),
            ],
            options={
                'verbose_name_plural': 'CourseFees',
            },
        ),
        migrations.CreateModel(
            name='FeeDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selection_type', models.CharField(choices=[('one_times', 'One Time'), ('two_times', 'Two Times'), ('three_times', 'Three Times')], max_length=20, null=True)),
                ('first_pay', models.DateField(blank=True, null=True)),
                ('first_pay_amount', models.IntegerField(blank=True, null=True)),
                ('second_pay', models.DateField(blank=True, null=True)),
                ('second_pay_amount', models.IntegerField(blank=True, null=True)),
                ('third_pay', models.DateField(blank=True, null=True)),
                ('third_pay_amount', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'FeeDetails',
            },
        ),
        migrations.CreateModel(
            name='FeesReceipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField()),
                ('receipt_number', models.CharField(max_length=50)),
                ('balance_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('collected_to_account', models.CharField(choices=[('oneteam ac 1', 'Oneteam ac 1'), ('oneteam ac 2', 'Oneteam ac 2'), ('oneteam ac 3', 'Oneteam ac 3')], max_length=100)),
                ('tax_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('payment_mode', models.CharField(choices=[('cash', 'Cash'), ('credit_card', 'Credit Card'), ('debit_card', 'Debit Card'), ('bank_transfer', 'Bank Transfer'), ('cheque', 'Cheque')], max_length=50)),
                ('description', models.TextField()),
                ('receipt_image', models.ImageField(upload_to='receipts/')),
            ],
        ),
        migrations.DeleteModel(
            name='Fee',
        ),
        migrations.AlterField(
            model_name='students',
            name='City',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='students',
            name='Collegename',
            field=models.CharField(max_length=100, null=True, verbose_name='College Name'),
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.AddField(
            model_name='feesreceipt',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='studentapp.students'),
        ),
        migrations.AddField(
            model_name='feedetails',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='studentapp.students'),
        ),
    ]
