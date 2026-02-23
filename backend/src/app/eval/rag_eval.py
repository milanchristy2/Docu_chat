from ragas import evaluate
# from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM,OllamaEmbeddings
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from typing import Any,cast
from ragas.metrics import faithfulness,answer_relevancy
from datasets import Dataset
METRIC_MAP={
    'faithfulness':faithfulness,
    'answer_relevancy':answer_relevancy
}
def evaluate_rag(questions,answers,contexts,ground_truth,metrics=None):
    if metrics is None:
        metrics=['faithfulness','answer_relevancy']
    selected_metrics=[METRIC_MAP[m] for m in metrics]
    data={
        "question":questions,
        "answer":answers,
        "contexts":contexts,
        "ground_truth":ground_truth
    }
    dataset=Dataset.from_dict(data)
    llm=OllamaLLM(model="llama3.2-vision:latest")
    evaluator_llm=LangchainLLMWrapper(llm)
    embeddings=OllamaEmbeddings(model="mxbai-embed-large")
    eval_embeddings=LangchainEmbeddingsWrapper(embeddings)
    res=evaluate(
        dataset,
        metrics=selected_metrics,
        llm=evaluator_llm,
        embeddings=eval_embeddings
    )
    if hasattr(res,"result"):
        res=cast(Any,res).result()

    return res

    