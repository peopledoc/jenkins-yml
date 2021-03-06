from unittest import TestCase


class TestContains(TestCase):
    def test_paramaters(self):
        from jenkins_yml import Job

        current_job = Job('freestyle', config=dict(
            parameters=dict(
                TOTO='tata',
            ),
        ))

        new_job = Job('freestyle', config=dict(
            parameters=dict(
                TOTO='tata', TITI='tata',
            ),
        ))

        assert not current_job.contains(new_job)

        merged_job = current_job.merge(new_job)

        assert merged_job.contains(current_job)
        assert merged_job.contains(new_job)

    def test_axis(self):
        from jenkins_yml import Job

        current_job = Job('matrix', config=dict(
            axis=dict(
                TOTO=['tata'],
            ),
        ))

        new_job = Job('freestyle', config=dict(
            axis=dict(
                TOTO=['tata'], TITI=['tata'],
            ),
        ))

        assert not current_job.contains(new_job)

        merged_job = current_job.merge(new_job)

        assert merged_job.contains(current_job)
        assert merged_job.contains(new_job)

    def test_axis_values(self):
        from jenkins_yml import Job

        current_job = Job('matrix', config=dict(
            axis=dict(TOTO=['tata']),
        ))

        new_job = Job('freestyle', config=dict(
            axis=dict(TOTO=['tata', 'titi']),
        ))

        assert not current_job.contains(new_job)

        merged_job = current_job.merge(new_job)

        assert merged_job.contains(current_job)
        assert merged_job.contains(new_job)

    def test_freestyle_nodes(self):
        from jenkins_yml import Job

        current_job = Job('freestyle', config=dict(node='slave1'))
        new_job = Job('freestyle', config=dict(node='slave2'))

        assert current_job.contains(new_job)

    def test_matrix_nodes(self):
        from jenkins_yml import Job

        current_job = Job('matrix', config=dict(
            node='slave1', axis=dict(A=['0']),
        ))

        new_job = Job('matrix', config=dict(
            node='slave2', axis=dict(A=[0]),
        ))

        assert not current_job.contains(new_job)

        merged_job = current_job.merge(new_job)

        assert merged_job.contains(current_job)
        assert merged_job.contains(new_job)

    def test_features(self):
        from jenkins_yml import Job

        current_job = Job('job', features={'feat1'})
        new_job = Job('job', features={'feat1', 'feat2'})

        assert not current_job.contains(new_job)

        merged_job = current_job.merge(new_job)

        assert merged_job.contains(current_job)
        assert merged_job.contains(new_job)
