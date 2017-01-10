# annotation-ui

Activate Python environment with Django installed

~~~bash
source activate annotation_ui
~~~

Dump database content

~~~bash
python manage.py dumpdata annotator >> snapshot_20170109.json
cp db.sqlite3 /cbss-tsb/pnguye01/pharmaprojects_vs_genetics/20161121_ceased_drugs_processing/backup_database_files/db_20170109.sqlite3
~~~

Wipe database content

~~~bash
rm db.sqlite3
# delete migration files
rm annotator/migrations/000*.py
rm annotator/migrations/__pycache__/000*.pyc
python manage.py makemigrations
python manage.py migrate
~~~

Start server and create superuser

~~~bash
sudo /usr/local/bin/anaconda3/envs/annotation_ui/bin/python manage.py runserver 0.0.0.0:4039
python manage.py createsuperuser
~~~

Go to http://10.242.7.215:4039/admin/, log in as superuser and add annotators

Load data

~~~bash
python manage.py shell
> import load_data
> load_data.load_drugs(load_data.Ani)
> load_data.load_drugs(load_data.Luke)
> load_data.load_drugs(load_data.Aimee)
> load_data.load_annotations(load_data.Ani)
> load_data.load_annotations(load_data.Luke)
> load_data.load_annotations(load_data.Aimee)
> exit

python manage.py dumpdata > backup.json
# To load backup data, run:
# python manage.py loaddata backup

~~~

To manage database:

~~~bash
python manage.py dbshell
> UPDATE annotator_annotation SET annotation = NULL;
> DELETE FROM annotator_annotation;
> DELETE FROM annotator_drug;
~~~

To update codes via git

~~~bash
git status
git add <file>
git commit -m "<write message here>"
git push origin master
~~~


