import unittest
import mock
import os
from unittest.mock import patch
from airflow.models import Variable
from airflow.models import DagBag

class TestDagIntegrity(unittest.TestCase):
    LOAD_SECOND_THRESHOLD = 1
    
    def setUp(self):
       self.dagbag = DagBag(dag_folder=".", include_examples=False)
    
    def test_import_Dags(self):
       print("Importing DAGs")
       self.assertFalse(
       len(self.dagbag.import_errors),
       'DAG import failures. Errors: {}'.format(self.dagbag.import_errors))
       if(len(self.dagbag.import_errors) == 0):
          print("DAG Import passed")
          print("unit tests completed")
           
print("Started unit testing ....")
suite = unittest.TestLoader().loadTestsFromTestCase(TestDagIntegrity)
unittest.TextTestRunner(verbosity=1).run(suite)
