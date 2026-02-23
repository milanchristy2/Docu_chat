import uuid
from typing import cast,Any,Dict
from backend.src.app.database.session import Session
from backend.src.app.models.db_models import Evaluation
from backend.src.app.eval.rag_eval import evaluate_rag

def run_evaluation(message_id:uuid.UUID,question:str,answer:str,contexts:list[str]):
    db=Session()
    try:
        result=evaluate_rag(
            questions=[question],
            answers=[answer],
            contexts=[contexts],
            ground_truth=[""],
            metrics=["faithfulness","answer_relevancy"]
        )
        exec_fn = getattr(result, "execute", None)
        scores = exec_fn() if callable(exec_fn) else result
        scores = cast(Dict[str, Any], scores)
        evaluation=Evaluation(
            message_id=message_id,
            faithfulness=float(scores["faithfulness"][0]),
            answer_relevancy=float(scores["answer_relevancy"][0]),
            context_precision=None,
            context_recall=None
        )
        db.add(evaluation)
        db.commit()
    finally:
        db.close()
    