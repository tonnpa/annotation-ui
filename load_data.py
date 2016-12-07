import pandas as pd

from annotator.models import Annotation, Drug, Person


def load_drugs():
    drug_df = pd.read_excel('data/drugs.xlsx')

    column_to_index = dict([(c, i+1) for i, c in enumerate(drug_df.columns)])

    annotator = Person.objects.get(last_name='Amelie', first_name='Amazing')
    for record in drug_df.itertuples():
        drug = Drug(
            key=record[column_to_index['Drug Key (Unique ID)']],
            name=record[column_to_index['Drug Name']],
            overview=record[column_to_index['Overview']],
            cl_phase_1=record[column_to_index['Key Clinical - Phase I']],
            cl_phase_2=record[column_to_index['Key Clinical - Phase II']],
            cl_phase_3=record[column_to_index['Key Clinical - Phase III']],
            annotator=annotator,
        )
        drug.save()
    print("Loaded {} drugs".format(len(drug_df)))


def load_annotations():
    annotation_df = pd.read_excel('data/clinical.xlsx')

    column_to_index = dict([(c, i+1) for i, c in enumerate(annotation_df.columns)])

    for record in annotation_df.itertuples():
        annotation = Annotation(
            key=Drug.objects.get(key=record[column_to_index['Drug.Key..Unique.ID.']]),
            cui=record[column_to_index['cui']],
            mdr1=record[column_to_index['mdr1']],
        )
        annotation.save()
    print("Loaded {} annotations".format(len(annotation_df)))
