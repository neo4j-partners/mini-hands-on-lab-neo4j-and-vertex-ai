from typing import Iterable, Callable, Dict, Tuple
import pandas as pd
import numpy as np
from graphdatascience import GraphDataScience
from numpy.typing import ArrayLike


def rename_col_dict(name_keys: pd.Index, rename_fun: Callable) -> Dict[str, str]:
    name_values = [rename_fun(s) for s in name_keys]
    return dict(zip(name_keys, name_values))


def rename_cols(df: pd.DataFrame, rename_fun: Callable) -> pd.DataFrame:
    col_map = rename_col_dict(df.columns, rename_fun)
    return df.rename(columns=col_map)


def lower_first_and_remove_underscores(s: str) -> str:
    r = s[0].lower() + s[1:]
    return r.replace('_', '')


def lower_first_rename_cols(df):
    return rename_cols(df, lower_first_and_remove_underscores)


def make_beneficiary_df(data_dir: str = 'data/') -> pd.DataFrame:
    beneficiary_df = lower_first_rename_cols(pd.read_csv(f'{data_dir}Train_Beneficiarydata-1542865627584.csv'))

    # 2 is False for chronic conditions....lets make indicators
    for col in beneficiary_df.columns:
        if 'chronicCond' in col: 
            beneficiary_df.loc[beneficiary_df[col] == 2, col] = 0

    beneficiary_df['dOB'] = pd.to_datetime(beneficiary_df['dOB'], format="%Y-%m-%d")
    beneficiary_df['dOD'] = pd.to_datetime(beneficiary_df['dOD'], format="%Y-%m-%d")
    beneficiary_df['dobYear'] = beneficiary_df['dOB'].dt.year
    beneficiary_df['isDeceased'] = beneficiary_df['dOD'].apply(lambda val: 0 if val != val else 1)
    max_date = beneficiary_df[['dOB', 'dOD']].max().max()

    beneficiary_df['maxDate'] = beneficiary_df['dOD']
    beneficiary_df['maxDate'].fillna(value=max_date, inplace=True)
    beneficiary_df['approxAge'] = round((beneficiary_df['maxDate'] - beneficiary_df['dOB']).dt.days / 365, 1)
    beneficiary_df.drop(columns=['maxDate'])

    beneficiary_df['renalDiseaseIndicator'] = np.array(beneficiary_df['renalDiseaseIndicator'] == 'Y').astype(int)

    return beneficiary_df


def make_in_out_df(data_dir: str = 'data/') -> pd.DataFrame:
    inpatient_df = lower_first_rename_cols(pd.read_csv(f'{data_dir}Train_Inpatientdata-1542865627584.csv'))
    outpatient_df = lower_first_rename_cols(pd.read_csv(f'{data_dir}Train_Outpatientdata-1542865627584.csv'))
    inpatient_df['inpatient'] = 1
    outpatient_df['inpatient'] = 0
    return pd.concat([inpatient_df, outpatient_df])


def make_claim_df(data_dir: str = 'data/') -> pd.DataFrame:
    beneficiary_df = make_beneficiary_df(data_dir)
    claim_df = make_in_out_df(data_dir)
    claim_df['claimStartDt'] = pd.to_datetime(claim_df['claimStartDt'], format="%Y-%m-%d")
    claim_df['claimEndDt'] = pd.to_datetime(claim_df['claimEndDt'], format="%Y-%m-%d")
    claim_df['claimDuration'] = (claim_df['claimEndDt'] - claim_df['claimStartDt']).dt.days

    claim_df['admissionDt'] = pd.to_datetime(claim_df['admissionDt'], format="%Y-%m-%d")
    claim_df['dischargeDt'] = pd.to_datetime(claim_df['dischargeDt'], format="%Y-%m-%d")
    claim_df['admittedDuration'] = (claim_df['dischargeDt'] - claim_df['admissionDt']).dt.days.fillna(value=0)

    claim_df['oprPhysicianInd'] = claim_df['operatingPhysician'].notna().astype(int)
    claim_df['attPhysicianInd'] = claim_df['attendingPhysician'].notna().astype(int)
    claim_df['otherPhysicianInd'] = claim_df['otherPhysician'].notna().astype(int)
    return claim_df.merge(beneficiary_df, on='beneID')


def root_mean(x):
    return x.mean() ** (1 / 2)


def make_provider_df(data_dir: str = 'data/') -> pd.DataFrame:
    provider_df = lower_first_rename_cols(pd.read_csv(f'{data_dir}/Train-1542865627584.csv'))
    provider_df['potentialFraudInd'] = np.array(provider_df.potentialFraud == 'Yes').astype(int)
    return provider_df


def chunks(xs, n=50_000):
    n = max(1, n)
    return [xs[i:i + n] for i in range(0, len(xs), n)]


def load_nodes_from_keys(gds: GraphDataScience, node_keys: ArrayLike, node_key_name: str, node_label: str):
    print(f'======  loading {node_label} nodes  ======')
    total = len(node_keys)
    print(f'staging {total:,} records')

    cumulative_count = 0
    for nks in chunks(node_keys):
        res = gds.run_cypher(f'''
            UNWIND $nodeKeys AS nodeKey
            MERGE(n:{node_label} {{{node_key_name}: nodeKey}})
            RETURN count(n) AS nodeLoadedCount
        ''', params={'nodeKeys': list(nks)})
        cumulative_count += res.iloc[0, 0]
        print(f'Loaded {cumulative_count:,} of {total:,} nodes')



def min_max_scaler(s: ArrayLike) -> ArrayLike:
    mn = s.min()
    den = s.max() - mn
    return (s - mn) / den


def log_min_max_scaler(s: ArrayLike) -> ArrayLike:
    return min_max_scaler(np.log(s + 1.0))
