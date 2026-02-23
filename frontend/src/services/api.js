const BASE_URL="http://localhost:8000";

export async function uploadDocument(file){
    const formData = new FormData();
    formData.append('file',file);

    const response=await fetch(
        `${BASE_URL}/documents/upload/`,{
            method:'POST',
            body:formData
        }
    );

    return response.json();
}

export async function queryDocument(chatId,question,documentId){
    const response=await fetch(
        `${BASE_URL}/query/`,{
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify({
                chat_id:chatId,
                content:question,
                document_id:documentId
            }),
        }
    );
    return response.json();
}