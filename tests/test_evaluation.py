from topn.evaluation.evaluator import RecommenderEvaluator
from topn.model.recommender import RecommenderSystem


# Unit tests for Evaluator class
def test_evaluator(sample_data, mock_gold_data):
    rec_sys = RecommenderSystem(sample_data)
    evaluator = RecommenderEvaluator(rec_sys, mock_gold_data)
    evaluation_results = evaluator.evaluate()

    assert evaluation_results["F1_score"] == 0.80
    assert evaluation_results["Accuracy"] == 0.67
