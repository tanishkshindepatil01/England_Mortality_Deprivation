"""Tests target suppressed values, invalid joins and reported evidence."""
import importlib.util
import tempfile
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('analysis',ROOT/'scripts/analyze.py')
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)

class AnalysisTests(unittest.TestCase):
    def test_missing_and_zero_are_distinct(self):
        for value in ['', 'nan', 'NaN', None]: self.assertIsNone(a.number(value))
        self.assertEqual(a.number('0'),0)
        self.assertIsNone(a.percentage_change(0,4))
        with self.assertRaises(ValueError): a.number('inf')

    def test_quintile_means_do_not_impute_missing_rates(self):
        rows=[{'IndicatorID':'92196','DerivedLADeprivationQuintile':'Q1 Least deprived','Value':v}
              for v in ['2','4','']]
        rows.append({'IndicatorID':'92196','DerivedLADeprivationQuintile':'nan','Value':'99'})
        q=a.quintile_summary(rows)[0]
        self.assertEqual(q['MeanRatePer1000'],3)
        self.assertEqual(q['AssignedAuthorities'],3)
        self.assertEqual(q['AvailableRates'],2)

    def test_rejects_duplicate_analytical_key(self):
        d=ROOT/'data/processed'
        t=a.load_csv(d/'mortality_trends.csv');l=a.load_csv(d/'local_authority_comparison.csv')
        q=a.load_csv(d/'deprivation_inequality.csv');defs=a.load_csv(d/'indicator_definitions.csv')
        with self.assertRaisesRegex(ValueError,'Duplicate national'):
            a.validate(t+[t[0]],l,q,defs)
        q[0]['Value']='999'
        with self.assertRaisesRegex(ValueError,'changed a mortality value'):
            a.validate(t,l,q,defs)

    def test_snapshot_reproduces_presented_findings(self):
        with tempfile.TemporaryDirectory() as output:
            result=a.run(ROOT/'data/processed',Path(output))
            self.assertEqual(sum(r['MissingRates'] for r in result['local_coverage']),45)
            self.assertEqual(result['quintile_coverage']['available_and_assigned'],241)
            infant=next(r for r in result['national'] if r['IndicatorID']=='92196')
            self.assertAlmostEqual(infant['FullPeriodChangePct'],-22.22823447896719)
            self.assertAlmostEqual(result['infant_quintiles'][0]['MeanRatePer1000'],3.373902,places=5)
            self.assertTrue((Path(output)/'findings.md').is_file())

if __name__=='__main__': unittest.main()
