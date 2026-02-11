import { IceCream } from "lucide-react";

export interface Message {
  id: string;
  text: string;
  sender: "user" | "bot";
  timestamp: Date;
}

interface ChatMessageProps {
  message: Message;
}

const ChatMessage = ({ message }: ChatMessageProps) => {
  const isUser = message.sender === "user";

  return (
    <div
      className={`flex items-end gap-2 animate-fade-in-up ${
        isUser ? "justify-end" : "justify-start"
      }`}
    >
      {!isUser && (
        <div className="w-8 h-8 rounded-full bg-secondary flex items-center justify-center flex-shrink-0 shadow-soft">
          <IceCream className="w-4 h-4 text-secondary-foreground" />
        </div>
      )}
      <div
        className={`max-w-[75%] px-4 py-2.5 text-sm leading-relaxed shadow-soft ${
          isUser ? "chat-bubble-user" : "chat-bubble-bot"
        }`}
      >
        {message.text}
      </div>
    </div>
  );
};

export default ChatMessage;
