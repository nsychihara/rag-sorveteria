import { useState, useRef, useEffect, useCallback } from "react";
import ChatMessage, { type Message } from "./ChatMessage";
import ChatInput from "./ChatInput";
import TypingIndicator from "./TypingIndicator";
import QuickReplies from "./QuickReplies";
import { getBotResponse } from "@/lib/chatbot";
import { sendMessageToRAG } from "@/lib/api";

const welcomeMessage: Message = {
  id: "welcome",
  text: "Olá! Bem-vindo(a) à Sorvelinux Chat!\n\nSou seu assistente virtual. Posso te ajudar com sabores, preços, promoções, horários e muito mais. O que você gostaria de saber?",
  sender: "bot",
  timestamp: new Date(),
};

const initialSuggestions = ["Sabores", "Preços", "Promoções", "Horário"];

const ChatContainer = () => {
  const [messages, setMessages] = useState<Message[]>([welcomeMessage]);
  const [isTyping, setIsTyping] = useState(false);
  const [suggestions, setSuggestions] = useState<string[]>(initialSuggestions);
  const bottomRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = useCallback(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, []);

  useEffect(() => {
    scrollToBottom();
  }, [messages, isTyping, scrollToBottom]);

  const handleSend = useCallback(async (text: string) => {
    const userMsg: Message = {
      id: Date.now().toString(),
      text,
      sender: "user",
      timestamp: new Date(),
    };

    setMessages((prev) => [...prev, userMsg]);
    setSuggestions([]);
    setIsTyping(true);

    try {
      // Tenta usar a API RAG primeiro
      const response = await sendMessageToRAG(text);

      const botMsg: Message = {
        id: (Date.now() + 1).toString(),
        text: response.response,
        sender: "bot",
        timestamp: new Date(),
      };

      setMessages((prev) => [...prev, botMsg]);

      // Sugestões podem vir dos produtos relacionados ou usar as padrões
      if (response.produtos_relacionados && response.produtos_relacionados.length > 0) {
        setSuggestions(["Mais sabores", "Preços", "Horário"]);
      } else {
        setSuggestions(["Sabores", "Preços", "Promoções"]);
      }

      setIsTyping(false);
    } catch (error) {
      // Fallback para respostas locais se a API falhar
      console.warn('API indisponível, usando respostas locais:', error);

      const delay = 800 + Math.random() * 700;
      setTimeout(() => {
        const response = getBotResponse(text);
        const botMsg: Message = {
          id: (Date.now() + 1).toString(),
          text: response.text,
          sender: "bot",
          timestamp: new Date(),
        };
        setMessages((prev) => [...prev, botMsg]);
        setSuggestions(response.suggestions || []);
        setIsTyping(false);
      }, delay);
    }
  }, []);

  return (
    <div className="flex flex-col flex-1 min-h-0">
      <div className="flex-1 overflow-y-auto scrollbar-thin px-4 py-4 space-y-3">
        {messages.map((msg) => (
          <ChatMessage key={msg.id} message={msg} />
        ))}
        {isTyping && <TypingIndicator />}
        <div ref={bottomRef} />
      </div>
      <ChatInput onSend={handleSend} disabled={isTyping} />
    </div>
  );
};

export default ChatContainer;
