const API_BASE_URL = 'http://127.0.0.1:8000';

export interface ChatResponse {
  response: string;
}

export async function sendMessageToRAG(
  message: string
): Promise<ChatResponse> {
  const response = await fetch(`${API_BASE_URL}/api/chatbot/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ message }),
  });

  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }

  return await response.json();
}
