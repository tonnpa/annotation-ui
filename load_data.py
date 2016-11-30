import pandas as pd

from annotator.models import Annotation, Drug


def load_drugs():
    drug_df = pd.read_excel('data/drugs.xslx')

    column_to_index = dict([(c, i) for i, c in enumerate(drug_df.columns)])

    for record in drug_df.itertuples():
        drug = Drug(
            key=record[column_to_index['Drug Key (Unique ID)']],
            name=record[column_to_index['Drug Name']],
            overview=record[column_to_index['Overview']],
            cl_phase_1=record[column_to_index['Key Clinical - Phase I']],
            cl_phase_2=record[column_to_index['Key Clinical - Phase II']],
            cl_phase_3=record[column_to_index['Key Clinical - Phase III']],
        )
        drug.save()


def load_annotations():
    annotation_df = pd.read_excel('data/clinical.xlsx')
    