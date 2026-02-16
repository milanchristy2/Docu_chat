from ragas import evaluate
# from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM,OllamaEmbeddings
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from typing import Any
from ragas.metrics import faithfulness,answer_relevancy,context_precision,context_recall
from datasets import Dataset

def evaluate_rag(questions,answers,contexts,ground_truth)->Any:
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
        metrics=[
            faithfulness,
            answer_relevancy,
            context_precision,
            context_recall
        ],
        llm=evaluator_llm,
        embeddings=eval_embeddings
    )

    return res

    