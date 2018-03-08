# Generated by Django 2.0.2 on 2018-03-08 00:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='None', max_length=100, verbose_name='Award Name')),
            ],
        ),
        migrations.CreateModel(
            name='Certifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='None', max_length=70, verbose_name='Certifications')),
            ],
        ),
        migrations.CreateModel(
            name='Clearance',
            fields=[
                ('ClearanceLevel', models.CharField(default='None', max_length=30, primary_key=True, serialize=False, verbose_name='Clearance Level')),
            ],
        ),
        migrations.CreateModel(
            name='Clubs_Hobbies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='None', max_length=100, verbose_name='Club and Hobby Name')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='None', max_length=100, verbose_name='Company Name')),
            ],
        ),
        migrations.CreateModel(
            name='Coursework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, verbose_name='Coursework')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to='documents/%Y%m%d')),
                ('type', models.CharField(max_length=128)),
                ('uploaduser', models.CharField(max_length=128)),
                ('wordstr', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LanguageSpoken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Language', models.CharField(default='None', max_length=20, verbose_name='Language')),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='None', max_length=50, verbose_name='Major')),
                ('Dept', models.CharField(default='None', max_length=50, verbose_name='Department')),
                ('MajorMinor', models.CharField(choices=[('Major', 'Major'), ('Minor', 'Minor')], default='Major', max_length=50, verbose_name='Major/Minor')),
            ],
        ),
        migrations.CreateModel(
            name='OCR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Resume', models.FileField(upload_to='PreOCR')),
                ('CreationDate', models.DateTimeField(verbose_name='Creation')),
                ('CreatedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='None', max_length=50, verbose_name='Name')),
                ('Email', models.CharField(blank=True, default='Not Parsed', max_length=50, null=True, verbose_name='Email')),
                ('Address', models.CharField(blank=True, default='Not Parsed', max_length=50, null=True, verbose_name='Address')),
                ('ZipCode', models.IntegerField(blank=True, default=0, verbose_name='Zip Code')),
                ('State', models.CharField(blank=True, default='Not Parsed', max_length=25, verbose_name='State')),
                ('PhoneNumber', models.CharField(blank=True, default='Not Parsed', max_length=50, null=True, verbose_name='Phone')),
                ('CreationDate', models.DateTimeField(auto_now_add=True, verbose_name='Created On')),
                ('LastUpdated', models.DateTimeField(auto_now=True, null=True, verbose_name='Last Updated')),
                ('Linkedin', models.CharField(blank=True, default='Not Parsed', max_length=70, null=True, verbose_name='LinkedIn')),
                ('GitHub', models.CharField(blank=True, default='Not Parsed', max_length=70, null=True, verbose_name='GitHub')),
                ('TypeResume', models.CharField(choices=[('Employee', 'Employee'), ('Intern', 'Intern'), ('Prospective Employee', 'Prospective Employee'), ('Prospective Intern', 'Prospective Intern')], default='Current Employee', max_length=50, verbose_name='Type')),
                ('WorkAuthorization', models.CharField(choices=[('Citizenship', 'Citizenship'), ('Permanent Resident', 'Permanent Resident'), ('Visa', 'Visa')], default='Citizenship', max_length=20, verbose_name='Work Authorization')),
                ('Comments', models.CharField(default='Add Comment...', max_length=500)),
                ('CreatedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('Resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Document')),
            ],
        ),
        migrations.CreateModel(
            name='PersonToAwards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Desc', models.CharField(default='None', max_length=1000, verbose_name='Award Description')),
                ('AwardID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Awards')),
                ('PersonID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Person')),
            ],
        ),
        migrations.CreateModel(
            name='PersonToCert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Interest', models.CharField(choices=[('Interested', 'Interested'), ('In Progess', 'In Progess'), ('Completed', 'Completed')], default='Interested', max_length=50, verbose_name='Interest')),
                ('Start_date', models.DateTimeField(blank=True, null=True, verbose_name='Start Date')),
                ('Completion_date', models.DateTimeField(blank=True, null=True, verbose_name='Completion Date')),
                ('CertID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Certifications')),
                ('PersonID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Person')),
            ],
        ),
        migrations.CreateModel(
            name='PersonToClearance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClearanceLevel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Clearance')),
                ('PersonID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Person')),
            ],
        ),
        migrations.CreateModel(
            name='PersonToClubs_Hobbies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Desc', models.CharField(default='None', max_length=100, verbose_name='Club and Hobby Description')),
                ('CHID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persontoclubshobbies_set', to='RSR.Clubs_Hobbies')),
                ('PersonID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persontoclubshobbies_set', to='RSR.Person')),
            ],
        ),
        migrations.CreateModel(
            name='PersonToCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(default='None', max_length=100, verbose_name='Title')),
                ('ExperienceOnJob', models.CharField(default='None', max_length=1000, verbose_name='Experience on Job')),
                ('StartDate', models.DateField(blank=True, null=True, verbose_name='Start Date')),
                ('EndDate', models.DateField(blank=True, null=True, verbose_name='End Date')),
                ('Desc', models.CharField(default='None', max_length=1000, verbose_name='Company Description')),
                ('CompanyID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Company')),
                ('PersonID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Person')),
            ],
        ),
        migrations.CreateModel(
            name='PersonToCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Desc', models.CharField(default='None', max_length=50, verbose_name='Coursework Description')),
                ('CourseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Coursework')),
                ('PersonID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Person')),
            ],
        ),
        migrations.CreateModel(
            name='PersonToLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LangID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.LanguageSpoken')),
                ('PersonID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Person')),
            ],
        ),
        migrations.CreateModel(
            name='PersonToProfessionalDevelopment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Desc', models.CharField(default='None', max_length=30, verbose_name='Professional Development Description')),
                ('PersonID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Person')),
            ],
        ),
        migrations.CreateModel(
            name='PersonToSchool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GradDate', models.CharField(default='None', max_length=20, verbose_name='Graduation Date')),
                ('GPA', models.FloatField(default='None', max_length=20, verbose_name='GPA')),
                ('MajorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Major')),
                ('PersonID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Person')),
            ],
        ),
        migrations.CreateModel(
            name='PersonToSide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Desc', models.CharField(default='None', max_length=50, verbose_name='Project Description')),
                ('PersonID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Person')),
            ],
        ),
        migrations.CreateModel(
            name='PersonToSkills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('YearsOfExperience', models.CharField(default=1, max_length=3, verbose_name='Years Of Experience')),
                ('Level', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '1'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=50, verbose_name='Level')),
                ('PersonID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Person')),
            ],
        ),
        migrations.CreateModel(
            name='PersonToTraining',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Interest', models.CharField(choices=[('Interested', 'Interested'), ('In Progess', 'In Progess'), ('Completed', 'Completed')], default='Interested', max_length=50, verbose_name='Interest')),
                ('Start_date', models.DateTimeField(blank=True, null=True, verbose_name='Start Date')),
                ('Completion_date', models.DateTimeField(blank=True, null=True, verbose_name='Completion Date')),
                ('PersonID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Person')),
            ],
        ),
        migrations.CreateModel(
            name='PersonToVolunteering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Desc', models.CharField(default='None', max_length=1000, verbose_name='Volunteering Description')),
                ('PersonID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Person')),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionalDevelopment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='None', max_length=20, verbose_name='Professional Development')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='None', max_length=150, verbose_name='School')),
                ('DegreeLevel', models.CharField(choices=[('Undergraduate', 'Undergraduate'), ('Graduate', 'Graduate')], default='Undergraduate', max_length=50, verbose_name='Degree Level')),
            ],
        ),
        migrations.CreateModel(
            name='SideProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='None', max_length=20, verbose_name='Project')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='None', max_length=100, verbose_name='Skills')),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='None', max_length=70, verbose_name='Title')),
            ],
        ),
        migrations.CreateModel(
            name='TitleToCert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CertID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Certifications')),
                ('TitleID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Title')),
            ],
        ),
        migrations.CreateModel(
            name='TitleToTrain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TitleID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Title')),
            ],
        ),
        migrations.CreateModel(
            name='Trainings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='None', max_length=70, verbose_name='Training')),
            ],
        ),
        migrations.CreateModel(
            name='Volunteering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='None', max_length=100, verbose_name='Volunteering Name')),
            ],
        ),
        migrations.AddField(
            model_name='titletotrain',
            name='TrainID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Trainings'),
        ),
        migrations.AddField(
            model_name='persontovolunteering',
            name='VolunID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Volunteering'),
        ),
        migrations.AddField(
            model_name='persontotraining',
            name='TrainID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Trainings'),
        ),
        migrations.AddField(
            model_name='persontoskills',
            name='SkillsID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Skills'),
        ),
        migrations.AddField(
            model_name='persontoside',
            name='SideID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.SideProject'),
        ),
        migrations.AddField(
            model_name='persontoschool',
            name='SchoolID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.School'),
        ),
        migrations.AddField(
            model_name='persontoprofessionaldevelopment',
            name='ProfID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.ProfessionalDevelopment'),
        ),
        migrations.AddField(
            model_name='ocr',
            name='NewPath',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RSR.Person'),
        ),
    ]
