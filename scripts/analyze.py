#!/usr/bin/env python3
"""Reproduce descriptive summaries from supplied processed CSVs, without dependencies.

This is a new reproducibility script. It does not recreate upstream extraction,
IMD weighting, boundary handling, quintile assignment or the Tableau workbook.
"""
from __future__ import annotations
import argparse
import csv
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
QUINTILES = ['Q1 Least deprived', 'Q2', 'Q3', 'Q4', 'Q5 Most deprived']


def number(value):
    """Map empty/NaN fields to None, retaining true zeros and rejecting infinities."""
    if value is None or str(value).strip().lower() in ('', 'nan', 'null', 'none'):
        return None
    result = float(value)
    if not math.isfinite(result):
        raise ValueError(f'Non-finite numeric field: {value!r}')
    return result


def percentage_change(first, latest):
    return None if first in (None, 0) or latest is None else 100 * (latest / first - 1)


def load_csv(path):
    with Path(path).open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


def duplicate_keys(rows, fields):
    return len(rows) - len({tuple(r[k] for k in fields) for r in rows})


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate(trends, local, deprivation, definitions):
    require(trends and local and deprivation and definitions, 'An input dataset is empty.')
    require(duplicate_keys(trends, ('IndicatorID', 'TimePeriod')) == 0,
            'Duplicate national indicator-period key.')
    require(duplicate_keys(local, ('IndicatorID', 'AreaCode')) == 0,
            'Duplicate local indicator-area key.')
    require(duplicate_keys(deprivation, ('IndicatorID', 'AreaCode')) == 0,
            'Duplicate deprivation indicator-area key.')
    require({(r['IndicatorID'], r['AreaCode']) for r in local} ==
            {(r['IndicatorID'], r['AreaCode']) for r in deprivation},
            'Local and deprivation keys do not match.')
    lookup = {(r['IndicatorID'], r['AreaCode']): r for r in local}
    for row in deprivation:
        require(number(row['Value']) == number(lookup[(row['IndicatorID'], row['AreaCode'])]['Value']),
                'Deprivation join changed a mortality value.')
    for row in trends + local:
        value, low, high = [number(row[k]) for k in ('Value', 'LowerCI95', 'UpperCI95')]
        if all(v is not None for v in (value, low, high)):
            require(low <= value <= high, 'Invalid confidence-interval bounds.')
    latest = {}
    for row in sorted(trends, key=lambda r: number(r['TimePeriodSortable'])):
        latest[row['IndicatorID']] = row
    for row in definitions:
        require(row['IndicatorID'] in latest, 'Definition missing from national trends.')
        require(math.isclose(number(row['LatestEnglandValue']),
                             number(latest[row['IndicatorID']]['Value']), rel_tol=1e-10),
                'Latest definition value differs from national trend.')
    return {'national_duplicate_keys': 0, 'local_duplicate_keys': 0,
            'deprivation_duplicate_keys': 0, 'local_deprivation_keys_match': True,
            'local_deprivation_mortality_values_match': True,
            'reported_interval_bounds_valid': True, 'latest_definitions_match': True}


def national_summary(rows):
    groups = defaultdict(list)
    for row in rows:
        groups[row['IndicatorID']].append(row)
    out = []
    for indicator, group in sorted(groups.items()):
        group.sort(key=lambda r: number(r['TimePeriodSortable']))
        available = [r for r in group if number(r['Value']) is not None]
        require(available, f'No available national rates for {indicator}')
        first, latest = available[0], available[-1]
        low = min(available, key=lambda r: number(r['Value']))
        a, b, c = (number(r['Value']) for r in (first, latest, low))
        out.append({'IndicatorID': indicator, 'IndicatorName': first['IndicatorName'],
                    'RateUnit': first['RateUnit'], 'PeriodCount': len(group),
                    'EarliestPeriod': first['TimePeriod'], 'EarliestValue': a,
                    'LatestPeriod': latest['TimePeriod'], 'LatestValue': b,
                    'AbsoluteChange': b-a, 'FullPeriodChangePct': percentage_change(a,b),
                    'LowestPeriod': low['TimePeriod'], 'LowestValue': c,
                    'ChangeFromLowPct': percentage_change(c,b)})
    return out


def local_summary(rows):
    groups = defaultdict(list)
    for row in rows:
        groups[row['IndicatorID']].append(row)
    out = []
    for indicator, group in sorted(groups.items()):
        categories = Counter(r['ComparedToEngland'] for r in group)
        out.append({'IndicatorID': indicator, 'IndicatorName': group[0]['IndicatorName'],
                    'Authorities': len({r['AreaCode'] for r in group}),
                    'AvailableRates': sum(number(r['Value']) is not None for r in group),
                    'MissingRates': sum(number(r['Value']) is None for r in group),
                    **{k: categories[k] for k in ['Similar','Better','Worse','Not compared']}})
    return out


def quintile_summary(rows):
    infant = [r for r in rows if r['IndicatorID'] == '92196']
    result=[]
    for label in QUINTILES:
        subset=[r for r in infant if r['DerivedLADeprivationQuintile']==label]
        vals=[number(r['Value']) for r in subset if number(r['Value']) is not None]
        result.append({'Quintile':label,'AssignedAuthorities':len(subset),
                       'AvailableRates':len(vals), 'MeanRatePer1000':mean(vals) if vals else None})
    return result


def write_csv(path, rows):
    require(bool(rows), f'No rows to write to {path}')
    with Path(path).open('w',encoding='utf-8',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)


def run(data_dir=ROOT/'data/processed', output_dir=ROOT/'reports'):
    data_dir, output_dir=Path(data_dir),Path(output_dir)
    data={name:load_csv(data_dir/(name+'.csv')) for name in
          ['mortality_trends','local_authority_comparison','deprivation_inequality',
           'indicator_definitions','data_quality_summary']}
    checks=validate(data['mortality_trends'],data['local_authority_comparison'],
                    data['deprivation_inequality'],data['indicator_definitions'])
    national=national_summary(data['mortality_trends'])
    local=local_summary(data['local_authority_comparison'])
    quintiles=quintile_summary(data['deprivation_inequality'])
    infant=[r for r in data['deprivation_inequality'] if r['IndicatorID']=='92196']
    top=sorted([r for r in infant if number(r['Value']) is not None],
               key=lambda r: (-number(r['Value']),r['AreaCode']))[:15]
    top=[{k:r[k] for k in ['AreaCode','AreaName','TimePeriod','Value','LowerCI95',
                           'UpperCI95','ComparedToEngland','DifferenceFromEngland']} for r in top]
    q1,q5=quintiles[0]['MeanRatePer1000'],quintiles[-1]['MeanRatePer1000']
    assigned=sum(r['AssignedAuthorities'] for r in quintiles)
    covered=sum(r['AvailableRates'] for r in quintiles)
    summary={'input_rows':{k:len(v) for k,v in data.items()},'validation':checks,
             'national':national,'local_coverage':local,'infant_quintiles':quintiles,
             'quintile_coverage':{'total_infant_authorities':len(infant),'assigned':assigned,
                                  'unassigned':len(infant)-assigned,'available_and_assigned':covered},
             'quintile_gap':{'Q5MinusQ1Per1000':q5-q1 if q1 is not None and q5 is not None else None,
                              'Q5OverQ1':q5/q1 if q1 and q5 is not None else None},
             'interpretation':'Unweighted authority means. Ecological association, not causation.',
             'source_discrepancy':'Supplied S2/dashboard KPI image shows CI 4.08–4.27. CSV CI rounds to 4.07–4.26.'}
    output_dir.mkdir(parents=True,exist_ok=True)
    for name,rows in [('national_summary',national),('local_coverage',local),
                      ('infant_quintile_summary',quintiles),('infant_top15',top)]:
        write_csv(output_dir/(name+'.csv'),rows)
    (output_dir/'analysis_summary.json').write_text(json.dumps(summary,indent=2,allow_nan=False)+'\n',encoding='utf-8')
    inf=next(r for r in national if r['IndicatorID']=='92196')
    lines=['# Reproduced findings','',
           'Generated by `python scripts/analyze.py` from the supplied processed extracts.','',
           f"- Infant mortality: {inf['EarliestValue']:.2f} to {inf['LatestValue']:.2f} per 1,000 ({inf['FullPeriodChangePct']:.1f}%).",
           f"- Latest infant rate is {inf['ChangeFromLowPct']:.1f}% above the {inf['LowestPeriod']} low.",
           f'- Infant quintile analysis: {covered} available rates with assigned quintiles.',
           f'- {len(infant)-assigned} of {len(infant)} infant authorities have no assigned quintile.',
           f'- Q1 mean {q1:.3f}, Q5 mean {q5:.3f} per 1,000. Ratio {q5/q1:.2f}.','',
           'The script validates analytical keys, unchanged mortality values after the deprivation join, confidence-interval bounds, and latest definition values. It does not independently rerun source-level checks from unavailable raw data.','',
           summary['source_discrepancy'],'',
           'Quintiles are supplied labels. The original assignment code was not supplied, so this script does not infer or recreate it.']
    (output_dir/'findings.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    return summary


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data-dir',type=Path,default=ROOT/'data/processed')
    parser.add_argument('--output-dir',type=Path,default=ROOT/'reports')
    args=parser.parse_args()
    result=run(args.data_dir,args.output_dir)
    print(json.dumps({'status':'passed','input_rows':result['input_rows'],
                      'reports':str(args.output_dir.resolve())},indent=2))


if __name__=='__main__':
    main()
