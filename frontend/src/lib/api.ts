const API_BASE_URL = 'http://localhost:8000';
const DEFAULT_TIMEOUT = 30000;

export interface ChatRequest {
  message: string;
}

export interface Produto {
  nome: string;
  descricao: string;
  score: number;
}

export interface ChatResponse {
  response: string;
  produtos_relacionados: Produto[];
}

export async function sendMessageToRAG(message: string): Promise<ChatResponse> {
  try {
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

    const data: ChatResponse = await response.json();
    return data;
  } catch (error) {
    console.error('Erro ao chamar API do chatbot:', error);
    throw error;
  }
}

export async function sendMessageWithTimeout(
  message: string,
  timeoutMs: number = DEFAULT_TIMEOUT
): Promise<ChatResponse> {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), timeoutMs);

  try {
    const response = await fetch(`${API_BASE_URL}/api/chatbot/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message }),
      signal: controller.signal,
    });

    clearTimeout(timeoutId);

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    return await response.json();
  } catch (error) {
    clearTimeout(timeoutId);
    if (error instanceof Error && error.name === 'AbortError') {
      throw new Error('Timeout: A requisição demorou muito');
    }
    throw error;
  }
}
