import uuid
from backend.src.app.database.session import Session
from backend.src.app.models.db_models import Evaluation
from backend.src.app.eval.rag_eval import evaluate_rag

def run_evaluation(message_id:uuid.UUID,question:str,answer:str,contexts:list[str]):
    db=Session()
    try:
        scores=evaluate_rag(
            questions=[question],
            answers=[str(answer)],
            contexts=[contexts],
            ground_truth=[""]

        )
        score_dict=scores
        evaluation=Evaluation(
            message_id=message_id,
            faithfulness=float(score_dict["faithfulness"][0]),
            answer_relevancy=float(score_dict["answer_relevancy"][0]),
            context_precision=float(score_dict["context_precision"][0]),
            context_recall=float(score_dict["context_recall"][0])
        )
        db.add(evaluation)
        db.commit()
    finally:
        db.close()
    